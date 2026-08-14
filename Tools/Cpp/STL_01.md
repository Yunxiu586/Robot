# Standard Template Library

[toc]

### STL Overview

##### Components

The STL model is commonly described with six cooperating components:

| Component       | Purpose                                                     |
| --------------- | ----------------------------------------------------------- |
| Container       | Stores and organizes objects                                |
| Algorithm       | Performs operations on iterator ranges                      |
| Iterator        | Provides a uniform way to access elements                   |
| Function object | Supplies callable behavior to algorithms and containers     |
| Adaptor         | Exposes an existing component through a different interface |
| Allocator       | Provides storage allocation for allocator-aware containers  |

Containers and algorithms are intentionally separated. Algorithms operate on iterator ranges instead of depending on a specific container type.

##### Container

Standard containers are commonly grouped by organization and access model:

- **Sequence containers** organize elements in a strictly linear arrangement: `array`, `vector`, `deque`, `list`, `forward_list`
- **Associative containers** maintain elements in an order determined by a comparison object: `set`, `multiset`, `map`, `multimap`
- **Unordered associative containers** organize elements into buckets using a hash function and an equivalence relation: `unordered_set`, `unordered_multiset`, `unordered_map`, `unordered_multimap`
- **Container adaptors** provide restricted interfaces over another container: `stack`, `queue`, `priority_queue`

Traditional STL introductions often group containers as **sequence containers** and **associative containers**. The standard library specifies **unordered associative containers** separately because their organization and complexity guarantees differ.

`std::string` is a specialization of `std::basic_string` and is commonly studied with sequence-like containers.

##### Algorithm

The standard library groups the algorithms covered in these notes into categories including:

- **non-modifying sequence operations**
- **mutating sequence operations**
- **sorting and related operations**
- **generalized numeric operations**

##### Iterator

An iterator generalizes pointer-like traversal so that algorithms can operate on different data structures through the same interface.

The standard specifies six iterator categories according to the operations they support:

| Category      | Main capability                               | Common examples                                  |
| ------------- | --------------------------------------------- | ------------------------------------------------ |
| Input         | Read while moving forward                     | input streams                                    |
| Output        | Write while moving forward                    | output streams                                   |
| Forward       | Multi-pass forward traversal                  | `forward_list`, unordered associative containers |
| Bidirectional | Forward and backward traversal                | `list`, associative containers                   |
| Random access | Constant-time jumps and ordering operations   | `deque`                                          |
| Contiguous    | Random access with contiguous element storage | `array`, `vector`                                |

For traversal categories, the refinement order is input → forward → bidirectional → random access → contiguous. Output is a separate capability.

Container adaptors such as `stack`, `queue`, and `priority_queue` do not expose iterators.

##### Iterator Ranges

Classic STL algorithms usually operate on a half-open range:

```text
[first, last)
```

`first` refers to the first element. `last` refers to the position one past the final element and is not dereferenced.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values{10, 20, 30, 40};

	auto first = values.begin();
	auto last = values.end();
	auto found = std::find(first, last, 30);

	if (found != last) {
		std::cout << *found << '\n';	// 30
	}
}
```

##### Allocators

Allocator-aware containers use an allocator object to obtain and release storage. The standard allocator is suitable for ordinary use; custom allocators are an advanced customization point.

`std::array` contains its fixed-size storage directly and does not use an allocator template parameter.

### Strings

##### `string`

`std::string` is a specialization of `std::basic_string<char>`. It stores a variable-length contiguous sequence of characters and manages its storage automatically.

The declarations below show the common overloads used in these notes. Less common allocator-, iterator-, and range-based overloads are omitted.

**Construction and Assignment**

Common construction and assignment forms include:

```cpp
using size_type = std::string::size_type;

std::string();
std::string(const char* s);
std::string(const std::string& str);
std::string(size_type count, char ch);

std::string& operator=(const char* s);
std::string& operator=(const std::string& str);
std::string& operator=(char ch);

std::string& assign(const char* s);
std::string& assign(const char* s, size_type count);
std::string& assign(const std::string& str);
std::string& assign(size_type count, char ch);
```

```cpp
#include <iostream>
#include <string>

int main() {
	std::string text{"Hello"};
	std::string repeated(3, '!');
	std::string copy{text};

	copy.assign("C++");
	std::cout << copy << '\n';		// C++

	copy.assign("Hello", 3);
	std::cout << copy << '\n';		// Hel

	copy.assign(4, '*');
	std::cout << copy << '\n';		// ****

	std::cout << text << '\n';		// Hello
	std::cout << repeated << '\n';	// !!!
}
```

**Size and Access**

- `size()` and `length()` return the number of characters
- `empty()` tests whether the string contains no characters
- `operator[]` accesses without bounds checking
- `at()` checks the position and throws `std::out_of_range` when it is invalid
- `front()` and `back()` access the first and last character of a non-empty string

```cpp
size_type size() const noexcept;
size_type length() const noexcept;
bool empty() const noexcept;

char& operator[](size_type pos);
const char& operator[](size_type pos) const;
char& at(size_type pos);
const char& at(size_type pos) const;
char& front();
const char& front() const;
char& back();
const char& back() const;
```

```cpp
#include <iostream>
#include <string>

int main() {
	std::string text{"hello"};

	std::cout << text.size() << '\n';	// 5
	std::cout << text[0] << '\n';		// h
	std::cout << text.at(1) << '\n';	// e

	text.front() = 'H';
	text.back() = '!';

	std::cout << text << '\n';		// Hell!
}
```

**Modification**

Common modifying operations include:

- `+=` and `append()` append characters or strings
- `insert()` inserts characters
- `erase()` removes characters
- `replace()` replaces part of the sequence
- `clear()` removes all characters

```cpp
std::string& operator+=(const char* s);
std::string& operator+=(const std::string& str);
std::string& operator+=(char ch);

std::string& append(const char* s);
std::string& append(const char* s, size_type count);
std::string& append(const std::string& str);
std::string& append(const std::string& str, size_type pos, size_type count = npos);

std::string& insert(size_type pos, const char* s);
std::string& insert(size_type pos, const std::string& str);
std::string& insert(size_type pos, size_type count, char ch);

std::string& erase(size_type pos = 0, size_type count = npos);

std::string& replace(size_type pos, size_type count, const std::string& str);
std::string& replace(size_type pos, size_type count, const char* s);

void clear() noexcept;
```

```cpp
#include <iostream>
#include <string>

int main() {
	std::string text{"Hello"};

	text += " World";
	text.append("!");
	std::cout << text << '\n';	// Hello World!

	text.insert(5, ",");
	text.replace(7, 5, "C++");
	text.erase(5, 1);
	std::cout << text << '\n';	// Hello C++!

	text.clear();
	std::cout << text.empty() << '\n';	// 1
}
```

**Comparison**

Strings support lexicographical comparison. `compare()` returns a negative value, zero, or a positive value according to whether the string is less than, equal to, or greater than the compared sequence.

```cpp
int compare(const std::string& str) const noexcept;
int compare(const char* s) const;
```

```cpp
#include <iostream>
#include <string>

int main() {
	const std::string first{"apple"};
	const std::string second{"banana"};

	std::cout << std::boolalpha << (first < second) << '\n';	// true
	std::cout << first.compare("apple") << '\n';				// 0
}
```

**Search and Substrings**

- `find()` returns the first matching position or `std::string::npos`
- `rfind()` searches from the end
- `substr(pos, count)` returns a new string containing a subsequence

```cpp
static constexpr size_type npos = size_type(-1);

size_type find(const std::string& str, size_type pos = 0) const noexcept;
size_type find(const char* s, size_type pos = 0) const;
size_type find(const char* s, size_type pos, size_type count) const;
size_type find(char ch, size_type pos = 0) const noexcept;

size_type rfind(const std::string& str, size_type pos = npos) const noexcept;
size_type rfind(const char* s, size_type pos = npos) const;
size_type rfind(const char* s, size_type pos, size_type count) const;
size_type rfind(char ch, size_type pos = npos) const noexcept;

std::string substr(size_type pos = 0, size_type count = npos) const;
```

```cpp
#include <iostream>
#include <string>

int main() {
	const std::string text{"one two three"};

	const std::size_t first = text.find("two");
	const std::size_t from = text.find('o', 2);
	const std::size_t last = text.rfind('e');
	const std::size_t missing = text.find("four");

	std::cout << first << '\n';						// 4
	std::cout << from << '\n';						// 6
	std::cout << last << '\n';						// 12
	std::cout << (missing == std::string::npos) << '\n';	// 1
	std::cout << text.substr(4, 3) << '\n';			// two
}
```

**C-String Access**

`c_str()` returns a pointer to a null-terminated character sequence representing the current string. `data()` provides access to the contiguous character storage.

```cpp
const char* c_str() const noexcept;
const char* data() const noexcept;
char* data() noexcept;
```

```cpp
#include <cstdio>
#include <string>

int main() {
	const std::string text{"hello"};

	std::printf("%s\n", text.c_str());	// hello
}
```

References, pointers, and iterators to string elements may be invalidated by operations that modify the string.