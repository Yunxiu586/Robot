# Standard Template Library

[toc]

### Sequence Containers

##### `vector`

`std::vector<T>` is a sequence container that supports random access. Except for the `bool` specialization, its elements are stored contiguously. Its storage is managed automatically and can grow dynamically.

When additional storage is required, a `vector` may allocate a larger contiguous block and move or copy its elements into the new storage. The growth factor is not specified by the standard.

**Construction and Assignment**

Common construction and assignment forms include:

```cpp
using size_type = std::vector<T>::size_type;

std::vector<T>();
explicit std::vector<T>(size_type count);
std::vector<T>(size_type count, const T& value);
template<class InputIt>
std::vector<T>(InputIt first, InputIt last);
std::vector<T>(const std::vector<T>& other);
std::vector<T>(std::initializer_list<T> init);

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
	std::vector<int> repeated(3, 7);
	std::vector<int> copy{source};

	std::cout << range[1] << '\n';		// 20
	std::cout << repeated[0] << '\n';	// 7
	std::cout << copy.back() << '\n';	// 30

	copy.assign(2, 5);
	std::cout << copy.size() << '\n';	// 2
	std::cout << copy.front() << '\n';	// 5

	copy.assign(source.begin() + 1, source.end());
	std::cout << copy.front() << '\n';	// 20

	copy.assign({40, 50});
	std::cout << copy.back() << '\n';	// 50
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
	std::cout << values[0] << '\n';			// 7

	values.resize(2);
	std::cout << values.size() << '\n';		// 2

	values.shrink_to_fit();
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

```cpp
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values{10, 20, 30};

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

- `push_back()` and `emplace_back()` add an element at the end
- `pop_back()` removes the last element
- `insert()` inserts elements before a position
- `erase()` removes an element or range
- `clear()` removes all elements
- `swap()` exchanges the contents and capacity of two vectors

```cpp
void push_back(const T& value);
void push_back(T&& value);
template<class... Args>
T& emplace_back(Args&&... args);
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

`std::deque<T>` is a sequence container with random-access iterators. It supports constant-time insertion and removal at both ends; insertion and removal in the middle are linear.

Its storage is managed automatically but is not required to form one contiguous block. Prefer `vector` when contiguous storage is required.

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
	std::deque<int> copy{source};

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

	values.resize(4, 40);

	std::cout << values.size() << '\n';	// 4
	std::cout << values[1] << '\n';		// 20
	std::cout << values.at(2) << '\n';	// 30
	std::cout << values.back() << '\n';	// 40
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
- `emplace_front()` / `emplace_back()` construct elements at either end
- `insert()` and `erase()` modify a specified position or range
- `clear()` removes all elements
- `swap()` exchanges two deques

```cpp
void push_front(const T& value);
void push_front(T&& value);
void push_back(const T& value);
void push_back(T&& value);

template<class... Args>
T& emplace_front(Args&&... args);
template<class... Args>
T& emplace_back(Args&&... args);

void pop_front();
void pop_back();

iterator insert(const_iterator pos, const T& value);
iterator insert(const_iterator pos, T&& value);
iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);

void clear() noexcept;
void swap(std::deque<T>& other);
```

```cpp
#include <deque>
#include <iostream>

int main() {
	std::deque<int> values{20, 30};

	values.push_front(10);
	values.push_back(40);
	values.insert(values.begin() + 2, 25);
	values.erase(values.begin() + 2);

	std::cout << values.front() << '\n';	// 10
	std::cout << values.back() << '\n';		// 40

	values.pop_front();
	values.pop_back();

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 20 30

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

`std::list<T>` is a doubly linked sequence container. It supports bidirectional traversal and constant-time insertion or erasure at a known position.

It does not provide random access.

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
	std::list<int> copy{source};

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
- `insert()` and `erase()` modify a known position or range
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
	std::list<int> values{20, 30, 30};

	values.push_front(10);
	values.push_back(40);

	auto position = values.begin();
	++position;
	values.insert(position, 15);
	values.erase(position);
	values.remove(30);

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 15 40

	values.pop_front();
	values.pop_back();
	std::cout << values.front() << '\n';	// 15

	values.clear();
	std::cout << values.empty() << '\n';	// 1
}
```

Insertion does not invalidate existing iterators or references. Erasing an element invalidates only iterators and references to the erased element.

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
	values.reverse();

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 3 2 1
}
```

### Container Adaptors

Container adaptors expose a restricted interface over an underlying container. They do not expose iterators.

##### `stack`

`std::stack<T>` provides last-in, first-out access. Its default underlying container is `std::deque<T>`.

**Construction and Assignment**

```cpp
std::stack<T>();
explicit std::stack<T>(const Container& cont);
std::stack<T>(const std::stack<T>& other);

std::stack<T>& operator=(const std::stack<T>& other);
```

```cpp
#include <deque>
#include <iostream>
#include <stack>

int main() {
	std::deque<int> source{10, 20, 30};
	std::stack<int> values(source);
	std::stack<int> copy{values};

	std::cout << copy.top() << '\n';	// 30
}
```

**Access and Modification**

- `top()` accesses the top element
- `push()` and `emplace()` add an element to the top
- `pop()` removes the top element
- `empty()` and `size()` query the adaptor
- `swap()` exchanges two stacks

```cpp
bool empty() const;
size_type size() const;

T& top();
const T& top() const;

void push(const T& value);
void push(T&& value);
template<class... Args>
decltype(auto) emplace(Args&&... args);

void pop();
void swap(std::stack<T>& other);
```

```cpp
#include <iostream>
#include <stack>

int main() {
	std::stack<int> values;

	values.push(10);
	values.push(20);
	values.emplace(30);

	std::cout << values.size() << '\n';		// 3
	std::cout << values.top() << '\n';		// 30

	values.pop();
	std::cout << values.top() << '\n';		// 20

	values.pop();
	values.pop();
	std::cout << values.empty() << '\n';	// 1
}
```

`pop()` removes an element and does not return it. Read `top()` before `pop()` when the value is needed.

##### `queue`

`std::queue<T>` provides first-in, first-out access. Its default underlying container is `std::deque<T>`.

**Construction and Assignment**

```cpp
std::queue<T>();
explicit std::queue<T>(const Container& cont);
std::queue<T>(const std::queue<T>& other);

std::queue<T>& operator=(const std::queue<T>& other);
```

```cpp
#include <deque>
#include <iostream>
#include <queue>

int main() {
	std::deque<int> source{10, 20, 30};
	std::queue<int> values(source);
	std::queue<int> copy{values};

	std::cout << copy.front() << '\n';	// 10
}
```

**Access and Modification**

- `front()` accesses the first element
- `back()` accesses the last element
- `push()` and `emplace()` add an element at the back
- `pop()` removes the first element
- `empty()` and `size()` query the adaptor
- `swap()` exchanges two queues

```cpp
bool empty() const;
size_type size() const;

T& front();
const T& front() const;
T& back();
const T& back() const;

void push(const T& value);
void push(T&& value);
template<class... Args>
decltype(auto) emplace(Args&&... args);

void pop();
void swap(std::queue<T>& other);
```

```cpp
#include <iostream>
#include <queue>

int main() {
	std::queue<int> values;

	values.push(10);
	values.push(20);
	values.emplace(30);

	std::cout << values.size() << '\n';		// 3
	std::cout << values.front() << '\n';	// 10
	std::cout << values.back() << '\n';		// 30

	values.pop();
	std::cout << values.front() << '\n';	// 20

	values.pop();
	values.pop();
	std::cout << values.empty() << '\n';	// 1
}
```
