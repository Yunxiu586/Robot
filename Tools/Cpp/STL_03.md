# Standard Template Library

[toc]

### Associative Containers

Associative containers organize elements according to a comparison object. `set`, `multiset`, `map`, and `multimap` provide bidirectional iterators and logarithmic key-based search and insertion.

##### `pair`

`std::pair<T1, T2>` stores two values as one object. The members are named `first` and `second`.

Common construction forms include brace initialization and `std::make_pair()`:

```cpp
std::pair<T1, T2> value{first, second};
auto value = std::make_pair(first, second);
```

```cpp
#include <iostream>
#include <string>
#include <utility>

int main() {
	std::pair<std::string, int> first{"Alice", 90};
	auto second = std::make_pair(std::string{"Bob"}, 85);

	std::cout << first.first << ' ' << first.second << '\n';		// Alice 90
	std::cout << second.first << ' ' << second.second << '\n';	// Bob 85
}
```

Map-like containers store elements as pairs whose first member is the key and second member is the mapped value.

##### `set` and `multiset`

- `std::set<Key>` stores unique keys
- `std::multiset<Key>` permits equivalent keys
- elements are ordered by the comparison object
- elements cannot be modified through iterators because modifying a key could break the ordering

**Construction and Assignment**

Common forms include:

```cpp
std::set<Key, Compare>();
std::set<Key, Compare>(const std::set<Key, Compare>& other);
std::set<Key, Compare>(std::initializer_list<Key> init);

template<class InputIt>
std::set<Key, Compare>(InputIt first, InputIt last);

std::set<Key, Compare>& operator=(const std::set<Key, Compare>& other);
std::set<Key, Compare>& operator=(std::initializer_list<Key> init);
```

`multiset` provides corresponding construction and assignment forms.

```cpp
#include <iostream>
#include <set>

int main() {
	std::set<int> values{30, 10, 20, 20};	// Duplicate key is ignored
	std::set<int> copy{values};
	std::set<int> assigned;
	assigned = values;

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';				// 10 20 30
	std::cout << copy.size() << '\n';		// 3

	std::set<int> other{100};
	assigned.swap(other);
	std::cout << *assigned.begin() << '\n';	// 100
	std::cout << other.size() << '\n';		// 3
}
```

**Size and Iteration**

- `empty()` tests whether the container contains no elements
- `size()` returns the number of elements
- `begin()` and `end()` delimit the ordered range
- `swap()` exchanges two containers of the same type

```cpp
bool empty() const noexcept;
size_type size() const noexcept;

iterator begin() noexcept;
const_iterator begin() const noexcept;
iterator end() noexcept;
const_iterator end() const noexcept;

void swap(std::set& other);
```

`multiset` provides corresponding operations.

**Insertion and Erasure**

- `set::insert()` reports whether a new key was inserted
- `multiset::insert()` inserts an element even when an equivalent key already exists
- `erase()` removes an element, range, or all elements equivalent to a key
- `clear()` removes all elements

```cpp
std::pair<iterator, bool> insert(const value_type& value);
iterator insert(const_iterator hint, const value_type& value);

template<class InputIt>
void insert(InputIt first, InputIt last);

iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);
size_type erase(const key_type& key);
void clear() noexcept;
```

For `multiset`, insertion of one value returns an `iterator` rather than `std::pair<iterator, bool>`.

```cpp
#include <iostream>
#include <set>

int main() {
	std::set<int> values{10, 20, 30};

	auto [first, inserted] = values.insert(40);
	auto [second, duplicate] = values.insert(20);

	std::cout << *first << ' ' << inserted << '\n';		// 40 1
	std::cout << *second << ' ' << duplicate << '\n';	// 20 0

	values.erase(10);
	std::cout << values.size() << '\n';				// 3

	std::multiset<int> repeated{10, 20, 20, 30};
	repeated.insert(20);
	std::cout << repeated.count(20) << '\n';			// 3

	values.clear();
	std::cout << values.empty() << '\n';				// 1
}
```

**Lookup**

- `find(key)` returns an iterator to a matching element or `end()`
- `count(key)` returns the number of elements equivalent to the key
- for `set`, `count()` returns either `0` or `1`
- for `multiset`, `count()` may return more than `1`

```cpp
iterator find(const key_type& key);
const_iterator find(const key_type& key) const;
size_type count(const key_type& key) const;
```

```cpp
#include <iostream>
#include <set>

int main() {
	const std::multiset<int> values{10, 20, 20, 30};

	auto found = values.find(20);
	if (found != values.end()) {
		std::cout << *found << '\n';		// 20
	}

	std::cout << values.count(20) << '\n';	// 2
	std::cout << values.count(40) << '\n';	// 0
}
```

**Ordering**

The comparison object determines the ordering and must define a strict weak ordering.

```cpp
#include <functional>
#include <iostream>
#include <set>
#include <string>

struct Person {
	std::string name;
	int age;
};

struct ComparePerson {
	bool operator()(const Person& lhs, const Person& rhs) const {
		if (lhs.age != rhs.age) {
			return lhs.age < rhs.age;
		}
		return lhs.name < rhs.name;
	}
};

int main() {
	std::set<int, std::greater<>> descending{10, 30, 20};

	for (int value : descending) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 30 20 10

	std::set<Person, ComparePerson> people{
		{"Alice", 20},
		{"Bob", 18},
		{"Carol", 20}
	};

	for (const Person& person : people) {
		std::cout << person.name << ':' << person.age << ' ';
	}
	std::cout << '\n';	// Bob:18 Alice:20 Carol:20
}
```

##### `map` and `multimap`

- `std::map<Key, T>` stores ordered key/value pairs with unique keys
- `std::multimap<Key, T>` permits equivalent keys
- each element has type `std::pair<const Key, T>`
- the key cannot be modified through an iterator

**Construction and Assignment**

Common forms include:

```cpp
std::map<Key, T, Compare>();
std::map<Key, T, Compare>(const std::map<Key, T, Compare>& other);
std::map<Key, T, Compare>(std::initializer_list<value_type> init);

template<class InputIt>
std::map<Key, T, Compare>(InputIt first, InputIt last);

std::map<Key, T, Compare>& operator=(const std::map<Key, T, Compare>& other);
std::map<Key, T, Compare>& operator=(std::initializer_list<value_type> init);
```

`multimap` provides corresponding construction and assignment forms.

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
	std::map<std::string, int> scores{
		{"Alice", 90},
		{"Bob", 85}
	};
	std::map<std::string, int> copy{scores};
	std::map<std::string, int> assigned;
	assigned = scores;

	std::cout << copy.at("Alice") << '\n';		// 90

	std::map<std::string, int> other{{"Carol", 95}};
	assigned.swap(other);
	std::cout << assigned.at("Carol") << '\n';	// 95
	std::cout << other.size() << '\n';			// 2
}
```

**Size and Iteration**

- `empty()` tests whether the container contains no elements
- `size()` returns the number of elements
- `begin()` and `end()` delimit the key-ordered range
- `swap()` exchanges two containers of the same type

```cpp
bool empty() const noexcept;
size_type size() const noexcept;

iterator begin() noexcept;
const_iterator begin() const noexcept;
iterator end() noexcept;
const_iterator end() const noexcept;

void swap(std::map& other);
```

`multimap` provides corresponding operations.

**Element Access**

- `operator[]` returns the mapped value for a key; if the key is absent, a new element is inserted with a value-initialized mapped value
- `at()` accesses an existing mapped value without inserting and throws `std::out_of_range` when the key is absent
- `multimap` does not provide `operator[]` or `at()`

```cpp
T& operator[](const key_type& key);
T& operator[](key_type&& key);

T& at(const key_type& key);
const T& at(const key_type& key) const;
```

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
	std::map<std::string, int> scores{
		{"Alice", 90},
		{"Bob", 85}
	};

	scores["Alice"] = 92;
	std::cout << scores.at("Alice") << '\n';	// 92

	// operator[] inserts a missing key
	std::cout << scores["Carol"] << '\n';		// 0
	std::cout << scores.size() << '\n';			// 3
}
```

**Insertion and Erasure**

- `map::insert()` inserts only when an equivalent key is absent and reports whether insertion occurred
- `multimap::insert()` permits equivalent keys
- `erase()` removes an element, range, or all elements equivalent to a key
- `clear()` removes all elements

```cpp
std::pair<iterator, bool> insert(const value_type& value);
iterator insert(const_iterator hint, const value_type& value);

template<class InputIt>
void insert(InputIt first, InputIt last);

iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);
size_type erase(const key_type& key);
void clear() noexcept;
```

For `multimap`, insertion of one value returns an `iterator` rather than `std::pair<iterator, bool>`.

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
	std::map<std::string, int> scores;

	auto [alice, inserted] = scores.insert({"Alice", 90});
	auto [same, duplicate] = scores.insert({"Alice", 100});
	scores.insert({"Bob", 85});

	std::cout << alice->second << ' ' << inserted << '\n';		// 90 1
	std::cout << same->second << ' ' << duplicate << '\n';		// 90 0

	scores.erase("Bob");
	std::cout << scores.size() << '\n';						// 1

	std::multimap<std::string, int> attempts{
		{"Alice", 90},
		{"Alice", 95}
	};
	std::cout << attempts.count("Alice") << '\n';			// 2

	scores.clear();
	std::cout << scores.empty() << '\n';					// 1
}
```

**Lookup**

- `find(key)` returns an iterator to a matching element or `end()`
- `count(key)` returns the number of elements with an equivalent key
- for `map`, `count()` returns either `0` or `1`
- for `multimap`, `count()` may return more than `1`

```cpp
iterator find(const key_type& key);
const_iterator find(const key_type& key) const;
size_type count(const key_type& key) const;
```

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
	const std::map<std::string, int> scores{
		{"Alice", 90},
		{"Bob", 85}
	};

	auto found = scores.find("Bob");
	if (found != scores.end()) {
		std::cout << found->first << ' ' << found->second << '\n';	// Bob 85
	}

	std::cout << scores.count("Alice") << '\n';					// 1
	std::cout << scores.count("Carol") << '\n';					// 0
}
```

**Ordering**

The comparison object orders elements by key.

```cpp
#include <functional>
#include <iostream>
#include <map>
#include <string>

int main() {
	std::map<int, std::string, std::greater<>> values{
		{1, "one"},
		{3, "three"},
		{2, "two"}
	};

	for (const auto& [key, value] : values) {
		std::cout << key << ':' << value << ' ';
	}
	std::cout << '\n';	// 3:three 2:two 1:one
}
```

### Unordered Associative Containers

Unordered associative containers organize elements into buckets using a hash function and an equivalent-key relation. They provide forward iterators and average constant-time key lookup; worst-case lookup can be linear.

##### `unordered_set` and `unordered_multiset`

- `std::unordered_set<Key>` stores unique keys
- `std::unordered_multiset<Key>` permits equivalent keys
- iteration order is not specified
- insertion may trigger rehashing

**Construction and Assignment**

Common forms include:

```cpp
std::unordered_set<Key>();
std::unordered_set<Key>(const std::unordered_set<Key>& other);
std::unordered_set<Key>(std::initializer_list<Key> init);

std::unordered_set<Key>& operator=(const std::unordered_set<Key>& other);
std::unordered_set<Key>& operator=(std::initializer_list<Key> init);
```

`unordered_multiset` provides corresponding forms.

**Size, Modification, and Lookup**

- `empty()` and `size()` query the number of elements
- `insert()` inserts elements
- `erase()` removes an element, range, or matching key
- `clear()` removes all elements
- `find()` returns a matching element or `end()`
- `count()` returns the number of equivalent keys

```cpp
bool empty() const noexcept;
size_type size() const noexcept;

std::pair<iterator, bool> insert(const value_type& value);
iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);
size_type erase(const key_type& key);
void clear() noexcept;

iterator find(const key_type& key);
const_iterator find(const key_type& key) const;
size_type count(const key_type& key) const;
```

For `unordered_multiset`, insertion of one value returns an `iterator` rather than `std::pair<iterator, bool>`.

```cpp
#include <iostream>
#include <unordered_set>

int main() {
	std::unordered_set<int> values{30, 10, 20, 20};

	auto [first, inserted] = values.insert(40);
	auto [second, duplicate] = values.insert(20);

	std::cout << *first << ' ' << inserted << '\n';		// 40 1
	std::cout << *second << ' ' << duplicate << '\n';	// 20 0
	std::cout << values.size() << '\n';				// 4

	auto found = values.find(30);
	std::cout << (found != values.end()) << '\n';		// 1

	std::unordered_multiset<int> repeated{10, 20, 20, 30};
	repeated.insert(20);
	std::cout << repeated.count(20) << '\n';			// 3
}
```

##### `unordered_map` and `unordered_multimap`

- `std::unordered_map<Key, T>` stores unique key/value pairs
- `std::unordered_multimap<Key, T>` permits equivalent keys
- `unordered_map` provides `operator[]` and `at()`
- `unordered_multimap` does not provide `operator[]` or `at()`

**Construction and Assignment**

Common forms include:

```cpp
std::unordered_map<Key, T>();
std::unordered_map<Key, T>(const std::unordered_map<Key, T>& other);
std::unordered_map<Key, T>(std::initializer_list<value_type> init);

std::unordered_map<Key, T>& operator=(const std::unordered_map<Key, T>& other);
std::unordered_map<Key, T>& operator=(std::initializer_list<value_type> init);
```

`unordered_multimap` provides corresponding forms.

**Element Access, Modification, and Lookup**

```cpp
T& operator[](const key_type& key);
T& operator[](key_type&& key);
T& at(const key_type& key);
const T& at(const key_type& key) const;

std::pair<iterator, bool> insert(const value_type& value);
iterator erase(const_iterator pos);
iterator erase(const_iterator first, const_iterator last);
size_type erase(const key_type& key);
void clear() noexcept;

iterator find(const key_type& key);
const_iterator find(const key_type& key) const;
size_type count(const key_type& key) const;
```

For `unordered_multimap`, insertion of one value returns an `iterator` rather than `std::pair<iterator, bool>`.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
	std::unordered_map<std::string, int> counts;

	++counts["apple"];
	++counts["banana"];
	++counts["apple"];

	std::cout << counts.at("apple") << '\n';		// 2
	std::cout << counts.at("banana") << '\n';	// 1

	auto found = counts.find("apple");
	std::cout << (found != counts.end()) << '\n';	// 1

	std::unordered_multimap<std::string, int> values{
		{"apple", 1},
		{"apple", 2}
	};
	std::cout << values.count("apple") << '\n';	// 2
}
```

##### Hash Policy

- `bucket_count()` returns the current number of buckets
- `load_factor()` returns the average number of elements per bucket
- `max_load_factor()` gets or sets the load-factor threshold used for automatic rehashing
- `reserve()` prepares for at least an expected number of elements
- `rehash()` requests at least a specified number of buckets subject to the load-factor requirement

```cpp
size_type bucket_count() const noexcept;
float load_factor() const noexcept;
float max_load_factor() const noexcept;
void max_load_factor(float value);

void reserve(size_type count);
void rehash(size_type count);
```

Rehashing invalidates iterators but does not invalidate references or pointers to elements.

```cpp
#include <iostream>
#include <unordered_map>

int main() {
	std::unordered_map<int, int> values;

	values.reserve(100);
	std::cout << values.size() << '\n';					// 0

	values.emplace(1, 10);
	values.emplace(2, 20);
	std::cout << (values.load_factor() <= values.max_load_factor()) << '\n';	// 1

	values.rehash(200);
	std::cout << (values.bucket_count() >= 200) << '\n';			// 1
}
```
