# Standard Template Library

[toc]

### Sequence Containers

##### `vector`

`std::vector<T>` is a sequence container that supports **random access**. Except for the `bool` specialization, its elements are stored **contiguously**. Its storage is managed automatically and can grow **dynamically**.

When additional storage is required, a `vector` may allocate a larger contiguous block and move or copy its elements into the new storage. The growth factor is not specified by the standard.

**Data Structure**

Conceptually, `vector` manages a dynamically allocated array containing constructed elements followed by reserved storage:

```text
[ element ][ element ][ element ][ reserved storage ... ]
^                              ^                        ^
begin                          end              end of storage
```

The exact object representation and growth strategy are implementation-defined.

**Construction and Assignment**

Common construction and assignment forms include:

```cpp
using size_type = std::vector<T>::size_type;

std::vector<T>();
explicit std::vector<T>(size_type count);
std::vector<T>(size_type count, const T& value);
template<class InputIt>
std::vector<T>(InputIt first, InputIt last);
std::vector<T>(const std::vector<T>& other);	// Copy constructor
std::vector<T>(std::initializer_list<T> init);	// Initializer-list constructor

std::vector<T>& operator=(const std::vector<T>& other);
std::vector<T>& operator=(std::initializer_list<T> init);

void assign(size_type count, const T& value);
template<class InputIt>
void assign(InputIt first, InputIt last);
void assign(std::initializer_list<T> init);
```

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> source{10, 20, 30};
	std::vector<int> range(source.begin(), source.end());
	std::vector<int> repeated(3, 7);	// 7 7 7
	std::vector<int> copy(source);
	std::vector<int> init_list{3, 7};	// 3 7

	std::cout << range[1] << '\n';		// 20
	std::cout << repeated[0] << '\n';	// 7
	std::cout << copy.back() << '\n';	// 30

	std::vector<int> assigned;
	assigned = source;
	std::cout << assigned.back() << '\n';	// 30

	assigned = {1, 2, 3};
	std::cout << assigned.front() << '\n';	// 1

	copy.assign(2, 5);
	std::cout << copy.size() << '\n';	// 2
	std::cout << copy.front() << '\n';	// 5

	copy.assign(source.begin() + 1, source.end());
	std::cout << copy.front() << '\n';		// 20

	copy.assign({40, 50});
	std::cout << copy.back() << '\n';		// 50
}
```

**Size and Capacity**

- `size()` returns the number of elements
- `empty()` tests whether the vector contains no elements
- `capacity()` returns the number of elements that can be stored without reallocation
- `reserve()` requests capacity for at least the specified number of elements without changing `size()`
- `resize()` changes the number of elements
- `shrink_to_fit()` requests reducing `capacity()` to `size()`; the request is non-binding

```cpp
bool empty() const noexcept;
size_type size() const noexcept;
size_type capacity() const noexcept;

void reserve(size_type new_capacity);
void resize(size_type count);
void resize(size_type count, const T& value);
void shrink_to_fit();
```

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values;

	values.reserve(100);
	std::cout << values.size() << '\n';					// 0
	std::cout << (values.capacity() >= 100) << '\n';	// 1

	values.resize(3, 7);
	std::cout << values.size() << '\n';		// 3
	std::cout << values[2] << '\n';			// 7

	values.resize(2);
	std::cout << values.size() << '\n';		// 2

	values.shrink_to_fit();					// Request to reduce capacity
	std::cout << (values.capacity() >= values.size()) << '\n';	// 1
}
```

Use `reserve()` when an approximate final size is known and repeated reallocations should be avoided.

**Access**

- `operator[]` provides unchecked random access
- `at()` provides checked random access and throws `std::out_of_range` for an invalid position
- `front()` and `back()` access the first and last element of a non-empty vector
- `data()` returns a pointer to the contiguous element storage

```cpp
T& operator[](size_type pos);
const T& operator[](size_type pos) const;
T& at(size_type pos);
const T& at(size_type pos) const;
T& front();
const T& front() const;
T& back();
const T& back() const;
T* data() noexcept;
const T* data() const noexcept;
```

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values{10, 20, 30};

	std::cout << values[1] << '\n';			// 20
	std::cout << values.at(2) << '\n';		// 30
	std::cout << values.front() << '\n';	// 10
	std::cout << values.back() << '\n';		// 30
	std::cout << *values.data() << '\n';	// 10
}
```

**Iterators**

- `begin()` and `end()` delimit the forward range
- `rbegin()` and `rend()` delimit the reverse range
- `cbegin()` / `cend()` and `crbegin()` / `crend()` return const iterators

```cpp
iterator begin() noexcept;
const_iterator begin() const noexcept;
const_iterator cbegin() const noexcept;

iterator end() noexcept;
const_iterator end() const noexcept;
const_iterator cend() const noexcept;

reverse_iterator rbegin() noexcept;
const_reverse_iterator rbegin() const noexcept;
const_reverse_iterator crbegin() const noexcept;

reverse_iterator rend() noexcept;
const_reverse_iterator rend() const noexcept;
const_reverse_iterator crend() const noexcept;
```

`iterator` permits modification of an element when the container is non-const. `const_iterator` refers to elements as const: the iterator itself can still be incremented or otherwise moved, but the element cannot be modified through it.

- `cbegin()` and `cend()` always return `const_iterator`
- `begin()` and `end()` on a const container also return `const_iterator`
- an `iterator` can be converted to the corresponding `const_iterator`

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values{10, 20, 30};

	std::vector<int>::iterator it = values.begin();
	*it = 100;

	std::vector<int>::const_iterator cit = values.cbegin();
	std::cout << *cit << '\n';	// 100
	++cit;
	std::cout << *cit << '\n';	// 20
	// *cit = 200;	// Error: cannot modify an element through const_iterator

	std::vector<int>::const_iterator converted = values.begin();
	std::cout << *converted << '\n';	// 100

	const std::vector<int> constants{40, 50};
	auto const_it = constants.begin();
	std::cout << *const_it << '\n';	// 40

	for (auto rit = values.rbegin(); rit != values.rend(); ++rit) {
		std::cout << *rit << ' ';
	}
	std::cout << '\n';	// 30 20 100
}
```

**Traversal Forms**

Range-based `for` traverses the range delimited by `begin()` and `end()`:

- `for (auto value : values)` copies each element
- `for (const auto& value : values)` reads elements without copying
- `for (auto& value : values)` refers to the original elements and permits modification
- an explicit iterator loop exposes the iterator itself; `*it` accesses the current element

```cpp
std::vector<int> values{10, 20, 30};

for (auto value : values) {
	value += 1;					// Modifies only the copy
}

for (auto& value : values) {
	value += 1;					// Modifies the element
}

for (const auto& value : values) {
	std::cout << value << ' ';	// Read-only access, no copy
}
std::cout << '\n';				// 11 21 31

for (auto it = values.begin(); it != values.end(); ++it) {
	*it += 1;					// Access through iterator
}
```

Use a range-based `for` when only the elements are needed. Use an explicit iterator when the iterator or its position is needed, such as for iterator-based container operations.

**Modification**

- `push_back()` add an element at the end
- `pop_back()` removes the last element
- `insert()` inserts elements before a position
- `erase()` removes an element or range
- `clear()` removes all elements
- `swap()` exchanges the contents and capacity of two vectors

```cpp
void push_back(const T& value);
void push_back(T&& value);
void pop_back();

iterator insert(const_iterator pos, const T& value);
iterator insert(const_iterator pos, T&& value);
iterator insert(const_iterator pos, size_type count, const T& value);
template<class InputIt>
iterator insert(const_iterator pos, InputIt first, InputIt last);

iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);

void clear() noexcept;
void swap(std::vector<T>& other);
```

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values{10, 40};
	std::vector<int> extra{50, 60};

	values.push_back(70);
	values.insert(values.begin() + 1, 20);
	values.insert(values.begin() + 2, 2, 30);
	values.insert(values.end() - 1, extra.begin(), extra.end());

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30 30 40 50 60 70

	values.erase(values.begin() + 2);
	values.erase(values.begin() + 4, values.end() - 1);

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30 40 70

	values.pop_back();
	values.clear();
	std::cout << values.empty() << '\n';	// 1
    
	values.reserve(100);
	values.resize(3, 10);
	std::cout << values.size() << ' ' << values.capacity() << '\n';	// 3 >=100(128)

	std::vector<int>().swap(values);		// Replace with an empty vector
	std::cout << values.empty() << '\n';	// 1
}
```

`clear()` changes the size to zero but does not require the implementation to reduce `capacity()`.

**Iterator Invalidation**

A reallocation invalidates all iterators, pointers, and references to `vector` elements.

Without reallocation:

- insertion invalidates iterators, pointers, and references at or after the insertion point
- erasure invalidates iterators and references at or after the erased position

Do not keep an iterator across an operation that may invalidate it.

##### `deque`

`std::deque<T>` is a sequence container with **random-access iterators**. It supports constant-time insertion and removal at both ends; insertion and removal in the middle are linear.

Its storage is managed automatically but its elements are **not stored contiguously**. Prefer `vector` when contiguous storage is required.

**Data Structure**

A typical implementation uses a **control structure** that stores pointers to separately allocated blocks.

```text
	                     	  control structure
                +--------+--------+--------+--------+--------+
                | unused |   *    |   *    |   *    | unused |
                +--------+---|----+---|----+---|----+--------+
                             |        |        |
                             v        v        v
                         +------+ +------+ +------+
                         | T... | | T... | | T... |
                         +------+ +------+ +------+
                          block    block    block

                          ^                      ^
                        start                  finish
```

`start` and `finish` identify the active range across these blocks. The block layout and control structure are implementation details rather than a required object layout.

**Construction and Assignment**

Common construction and assignment forms include:

```cpp
using size_type = std::deque<T>::size_type;

std::deque<T>();
explicit std::deque<T>(size_type count);
std::deque<T>(size_type count, const T& value);
template<class InputIt>
std::deque<T>(InputIt first, InputIt last);
std::deque<T>(const std::deque<T>& other);
std::deque<T>(std::initializer_list<T> init);

std::deque<T>& operator=(const std::deque<T>& other);
std::deque<T>& operator=(std::initializer_list<T> init);

void assign(size_type count, const T& value);
template<class InputIt>
void assign(InputIt first, InputIt last);
void assign(std::initializer_list<T> init);
```

```cpp
#include <deque>
#include <iostream>

int main() {
	std::deque<int> source{10, 20, 30};
	std::deque<int> range(source.begin(), source.end());
	std::deque<int> repeated(3, 7);			// 7 7 7
	std::deque<int> copy(source);

	std::cout << range[1] << '\n';			// 20
	std::cout << repeated.front() << '\n';	// 7

	std::deque<int> assigned;
	assigned = source;
	std::cout << assigned.back() << '\n';	// 30

	assigned = {1, 2, 3};
	std::cout << assigned.front() << '\n';	// 1

	copy.assign(3, 7);
	std::cout << copy.size() << '\n';		// 3
	std::cout << copy.front() << '\n';		// 7

	copy.assign(source.begin() + 1, source.end());
	std::cout << copy.front() << '\n';		// 20

	copy.assign({40, 50});
	std::cout << copy.back() << '\n';		// 50
	std::cout << range[1] << '\n';			// 20
}
```

**Size and Access**

- `size()` returns the number of elements
- `empty()` tests whether the deque contains no elements
- `resize()` changes the number of elements
- `operator[]` provides unchecked random access
- `at()` provides checked random access
- `front()` and `back()` access the first and last element of a non-empty deque

```cpp
bool empty() const noexcept;
size_type size() const noexcept;
void resize(size_type count);
void resize(size_type count, const T& value);

T& operator[](size_type pos);
const T& operator[](size_type pos) const;
T& at(size_type pos);
const T& at(size_type pos) const;
T& front();
const T& front() const;
T& back();
const T& back() const;
```

```cpp
#include <deque>
#include <iostream>

int main() {
	std::deque<int> values{10, 20, 30};

	values.resize(5, 40);

	std::cout << values.size() << '\n';		// 5
	std::cout << values.front() << '\n';	// 10
	std::cout << values.at(2) << '\n';		// 30
	std::cout << values[3] << '\n';			// 40
	std::cout << values.back() << '\n';		// 40

	values.resize(3);
	std::cout << values.size() << '\n';		// 3
}
```

**Iterators**

- `begin()` and `end()` delimit the forward range
- `rbegin()` and `rend()` delimit the reverse range
- deque iterators support random access

```cpp
iterator begin() noexcept;
const_iterator begin() const noexcept;
iterator end() noexcept;
const_iterator end() const noexcept;

reverse_iterator rbegin() noexcept;
const_reverse_iterator rbegin() const noexcept;
reverse_iterator rend() noexcept;
const_reverse_iterator rend() const noexcept;
```

```cpp
#include <deque>
#include <iostream>

int main() {
	std::deque<int> values{10, 20, 30};

	for (auto it = values.begin(); it != values.end(); ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';	// 10 20 30

	for (auto it = values.rbegin(); it != values.rend(); ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';	// 30 20 10
}
```

**Modification**

- `push_front()` / `push_back()` add elements at either end
- `pop_front()` / `pop_back()` remove elements at either end
- `insert()` inserts one element, repeated copies, or an iterator range before a position
- `erase()` removes one element or an iterator range
- `clear()` removes all elements
- `swap()` exchanges two deques

```cpp
void push_front(const T& value);
void push_front(T&& value);
void push_back(const T& value);
void push_back(T&& value);

void pop_front();
void pop_back();

iterator insert(const_iterator pos, const T& value);
iterator insert(const_iterator pos, T&& value);
iterator insert(const_iterator pos, size_type count, const T& value);
template<class InputIt>
iterator insert(const_iterator pos, InputIt first, InputIt last);

iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);

void clear() noexcept;
void swap(std::deque<T>& other);
```

```cpp
#include <deque>
#include <iostream>

int main() {
	std::deque<int> values{20, 50};
	std::deque<int> extra{60, 70};

	values.push_front(10);
	values.push_back(80);
	values.insert(values.begin() + 2, 30);
	values.insert(values.begin() + 3, 2, 40);
	values.insert(values.end() - 1, extra.begin(), extra.end());

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30 40 40 50 60 70 80

	values.erase(values.begin() + 2);
	values.erase(values.begin() + 2, values.begin() + 4);

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 50 60 70 80

	values.pop_front();
	values.pop_back();
	std::cout << values.front() << '\n';	// 20
	std::cout << values.back() << '\n';		// 70

	values.clear();
	std::cout << values.empty() << '\n';	// 1
}
```

Because `deque` has random-access iterators, algorithms such as `std::sort()` can operate on it.

```cpp
#include <algorithm>
#include <deque>
#include <iostream>

int main() {
	std::deque<int> values{30, 10, 20};

	std::sort(values.begin(), values.end());

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30
}
```

##### `list`

`std::list<T>` is a **doubly linked sequence container**. It supports bidirectional traversal and constant-time insertion or erasure at a known position.

It does not provide random access.

**Data Structure**

`list` is typically represented as a chain of **nodes**. Each node stores an element together with links to its neighboring nodes:

```text
... <-> [ prev | value | next ] <-> [ prev | value | next ] <-> ...
```

Insertion or erasure at a known node changes links between neighboring nodes instead of shifting later elements.

**Construction and Assignment**

Common construction and assignment forms include:

```cpp
using size_type = std::list<T>::size_type;

std::list<T>();
explicit std::list<T>(size_type count);
std::list<T>(size_type count, const T& value);
template<class InputIt>
std::list<T>(InputIt first, InputIt last);
std::list<T>(const std::list<T>& other);
std::list<T>(std::initializer_list<T> init);

std::list<T>& operator=(const std::list<T>& other);
std::list<T>& operator=(std::initializer_list<T> init);

void assign(size_type count, const T& value);
template<class InputIt>
void assign(InputIt first, InputIt last);
void assign(std::initializer_list<T> init);
```

```cpp
#include <iostream>
#include <list>

int main() {
	std::list<int> source{10, 20, 30};
	std::list<int> range(source.begin(), source.end());
	std::list<int> repeated(3, 7);			// 7 7 7
	std::list<int> copy(source);

	std::cout << range.front() << '\n';		// 10
	std::cout << repeated.front() << '\n';	// 7

	std::list<int> assigned;
	assigned = source;
	std::cout << assigned.back() << '\n';	// 30

	assigned = {1, 2, 3};
	std::cout << assigned.front() << '\n';	// 1

	copy.assign(3, 7);
	std::cout << copy.size() << '\n';		// 3
	std::cout << copy.front() << '\n';		// 7

	auto first = source.begin();
	++first;
	copy.assign(first, source.end());
	std::cout << copy.front() << '\n';		// 20

	copy.assign({40, 50});
	std::cout << copy.back() << '\n';		// 50
	std::cout << range.front() << '\n';		// 10
}
```

**Size and Access**

- `size()` returns the number of elements
- `empty()` tests whether the list contains no elements
- `resize()` changes the number of elements
- `front()` and `back()` access the first and last element of a non-empty list
- `list` does not provide `operator[]` or `at()`

```cpp
bool empty() const noexcept;
size_type size() const noexcept;
void resize(size_type count);
void resize(size_type count, const T& value);

T& front();
const T& front() const;
T& back();
const T& back() const;
```

```cpp
#include <iostream>
#include <list>

int main() {
	std::list<int> values{10, 20};

	values.resize(4, 30);

	std::cout << values.size() << '\n';		// 4
	std::cout << values.front() << '\n';	// 10
	std::cout << values.back() << '\n';		// 30

	values.resize(2);
	std::cout << values.size() << '\n';		// 2
}
```

**Iterators**

- `begin()` and `end()` delimit the forward range
- `rbegin()` and `rend()` delimit the reverse range
- list iterators are bidirectional, not random-access

```cpp
iterator begin() noexcept;
const_iterator begin() const noexcept;
iterator end() noexcept;
const_iterator end() const noexcept;

reverse_iterator rbegin() noexcept;
const_reverse_iterator rbegin() const noexcept;
reverse_iterator rend() noexcept;
const_reverse_iterator rend() const noexcept;
```

```cpp
#include <iostream>
#include <list>

int main() {
	std::list<int> values{10, 20, 30};
    
    auto it = values.begin();
    ++it;
    std::cout << *it << '\n';	// 20
    --it;
    std::cout << *it << '\n';	// 10
    // auto next = it + 1;		// Error: list iterators do not support random access

	for (auto it = values.begin(); it != values.end(); ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';	// 10 20 30

	for (auto it = values.rbegin(); it != values.rend(); ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';	// 30 20 10
}
```

**Modification**

- `push_front()` / `push_back()` add elements at either end
- `pop_front()` / `pop_back()` remove elements at either end
- `insert()` inserts one element, repeated copies, or an iterator range before a position
- `erase()` removes one element or an iterator range
- `remove()` erases all elements equal to a specified value
- `clear()` removes all elements
- `swap()` exchanges two lists

```cpp
void push_front(const T& value);
void push_front(T&& value);
void push_back(const T& value);
void push_back(T&& value);
void pop_front();
void pop_back();

iterator insert(const_iterator pos, const T& value);
iterator insert(const_iterator pos, T&& value);
iterator insert(const_iterator pos, size_type count, const T& value);
template<class InputIt>
iterator insert(const_iterator pos, InputIt first, InputIt last);

iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);
size_type remove(const T& value);

void clear() noexcept;
void swap(std::list<T>& other);
```

```cpp
#include <iostream>
#include <list>

int main() {
	std::list<int> values{20, 50, 50};
	std::list<int> extra{60, 70};

	auto print_values = [&values]() {
		for (int value : values) {
			std::cout << value << ' ';
		}
		std::cout << '\n';
	};

	values.push_front(10);
	values.push_back(80);
	print_values();	// 10 20 50 50 80

	auto position = values.begin();
	++position;							// Refers to 20
	values.insert(position, 15);
	values.insert(position, 2, 18);
	values.insert(values.end(), extra.begin(), extra.end());
	print_values();						// 10 15 18 18 20 50 50 80 60 70
	std::cout << *position << '\n';		// 20: insertion keeps position valid

	values.erase(position);				// position is invalid after erasing 20
	print_values();						// 10 15 18 18 50 50 80 60 70

	auto first = values.begin();
	++first;
	++first;							// Refers to the first 18
	auto last = first;
	++last;
	++last;								// Refers to the first 50
	values.erase(first, last);
	print_values();						// 10 15 50 50 80 60 70
	std::cout << *last << '\n';			// 50: last was not erased and remains valid

	values.remove(50);					// last is invalid because its element is removed
	print_values();						// 10 15 80 60 70

	values.pop_front();
	values.pop_back();
	print_values();						// 15 80 60

	values.clear();
	std::cout << values.empty() << '\n';	// 1
}
```

- `list`: insertion does not invalidate existing iterators or references; erasure invalidates only those referring to erased elements
- `vector`: reallocation invalidates all iterators and references; otherwise insertion or erasure invalidates those at or after the affected position

**List Operations**

- `reverse()` reverses the element order
- `sort()` sorts the list

```cpp
void reverse() noexcept;

void sort();
template<class Compare>
void sort(Compare comp);
```

`std::sort()` requires random-access iterators, so use `list::sort()` for a `std::list`.

```cpp
#include <iostream>
#include <list>

int main() {
	std::list<int> values{3, 1, 2};

	values.sort();
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 1 2 3

	values.sort([](int lhs, int rhs) { return lhs > rhs; });
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 3 2 1

	values.reverse();
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 1 2 3
}
```

**Example**

Custom type sorting can define multiple comparison levels. The following example sorts by `age` in ascending order, then by `height` in descending order when ages are equal.

```cpp
#include <iostream>
#include <list>
#include <string>

struct Person {
	std::string name;
	int age;
	int height;
};

struct PersonCompare {
	bool operator()(const Person& lhs, const Person& rhs) const {
		if (lhs.age != rhs.age) {
			return lhs.age < rhs.age;
		}
		return lhs.height > rhs.height;
	}
};

bool comparePerson(const Person& lhs, const Person& rhs) {
	if (lhs.age != rhs.age) {
		return lhs.age < rhs.age;
	}
	return lhs.height > rhs.height;
}

void printPeople(const std::list<Person>& people) {
	for (const auto& person : people) {
		std::cout << person.name << ' '
				  << person.age << ' '
				  << person.height << '\n';
	}
}

int main() {
	std::list<Person> people{
		{"Alice", 20, 165},
		{"Bob", 18, 175},
		{"Charlie", 20, 180},
		{"David", 18, 170}
	};

	auto people_by_functor = people;
	people_by_functor.sort(PersonCompare{});
	printPeople(people_by_functor);
	// Bob     18 175
	// David   18 170
	// Charlie 20 180
	// Alice   20 165

	std::cout << '\n';

	auto people_by_callback = people;
	people_by_callback.sort(comparePerson);
	printPeople(people_by_callback);
	// Bob     18 175
	// David   18 170
	// Charlie 20 180
	// Alice   20 165
}
```

