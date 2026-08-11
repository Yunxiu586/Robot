# Containers

[toc]

### Overview

##### Categories

The standard library provides containers for storing collections of objects. This note covers the containers used most often in basic STL study.

| Category | Types |
| --- | --- |
| Character sequence | `std::string` |
| Sequence containers | `std::vector`, `std::deque`, `std::list` |
| Container adaptors | `std::stack`, `std::queue` |
| Associative containers | `std::set`, `std::map` |

`vector`, `deque`, `list`, `set`, and `map` expose iterators. `stack` and `queue` provide restricted interfaces and do not expose iterators.

##### Iterators

A half-open range `[first, last)` includes `first` and excludes `last`.

```cpp
#include <iostream>
#include <vector>

std::vector<int> values{10, 20, 30};

for (auto iterator = values.begin(); iterator != values.end(); ++iterator) {
    std::cout << *iterator << '\n';
}
```

Use `cbegin()` and `cend()` when the elements must not be modified through the iterator.

```cpp
for (auto iterator = values.cbegin(); iterator != values.cend(); ++iterator) {
    std::cout << *iterator << '\n';
}
```

### Sequences

##### `std::string`

`std::string` stores a dynamically sized sequence of `char` elements.

```cpp
#include <string>

std::string first{"Hello"};
std::string second{first};
std::string repeated(3, 'a');   // "aaa"
```

Assignment and concatenation:

```cpp
std::string text;
text = "Hello";
text += " World";
text.append("!");
```

Size and access:

```cpp
bool empty = text.empty();
std::size_t size = text.size();

char first_char = text[0];      // no bounds check
char second_char = text.at(1);  // bounds-checked
```

Search and replace:

```cpp
std::size_t position = text.find("World");

if (position != std::string::npos) {
    text.replace(position, 5, "C++");
}
```

Insertion, erasure, and substring:

```cpp
std::string text{"Hello World"};

text.insert(5, ",");
text.erase(5, 1);

std::string word = text.substr(6, 5);  // "World"
```

Comparison is lexicographical.

```cpp
std::string first{"apple"};
std::string second{"banana"};

int result = first.compare(second);  // negative, zero, or positive
```

##### `std::vector`

`std::vector<T>` is a dynamically sized contiguous sequence container with random access.

```cpp
#include <vector>

std::vector<int> first{1, 2, 3};
std::vector<int> second(3, 10);  // 10, 10, 10
std::vector<int> copy{first};
```

Size and capacity:

```cpp
std::vector<int> values{1, 2, 3};

std::size_t size = values.size();
std::size_t capacity = values.capacity();
bool empty = values.empty();

values.reserve(100);  // changes capacity, not size
values.resize(5);     // changes the number of elements
```

Insertion and erasure:

```cpp
values.push_back(4);
values.emplace_back(5);
values.pop_back();

values.insert(values.begin() + 1, 10);
values.erase(values.begin() + 1);
values.clear();
```

Element access:

```cpp
int first = values.front();
int last = values.back();
int value = values[1];      // no bounds check
int checked = values.at(1); // bounds-checked
```

Reallocation can invalidate all pointers, references, and iterators to the elements. Use `reserve()` before many insertions when an approximate final size is known.

| Operation | Complexity |
| --- | --- |
| Random access | `O(1)` |
| Insert/erase at end | Amortized `O(1)` |
| Insert/erase in the middle | `O(n)` |

##### `std::deque`

`std::deque<T>` supports random access and efficient insertion and removal at both ends. Its elements are not required to be contiguous.

```cpp
#include <deque>

std::deque<int> values{2, 3};

values.push_front(1);
values.push_back(4);
values.pop_front();
values.pop_back();
```

Size, access, insertion, and erasure:

```cpp
std::deque<int> values{1, 2, 3};

bool empty = values.empty();
std::size_t size = values.size();

int first = values.front();
int last = values.back();
int value = values.at(1);

values.insert(values.begin() + 1, 10);
values.erase(values.begin() + 1);
values.clear();
```

| Operation | Complexity |
| --- | --- |
| Random access | `O(1)` |
| Insert/erase at either end | `O(1)` |
| Insert/erase in the middle | `O(n)` |

##### `std::list`

`std::list<T>` is a doubly linked sequence container. It provides bidirectional iteration but no random access.

```cpp
#include <list>

std::list<int> values{2, 3};

values.push_front(1);
values.push_back(4);
values.pop_front();
values.pop_back();
```

Insertion and erasure are constant time after the position is known.

```cpp
#include <iterator>

std::list<int> values{1, 2, 3};
auto iterator = values.begin();
std::advance(iterator, 1);

values.insert(iterator, 10);
values.erase(iterator);
```

List-specific operations:

```cpp
std::list<int> values{3, 1, 2, 2};

values.sort();
values.unique();  // removes adjacent equivalent elements
values.remove(1);
values.reverse();
```

Insertion does not invalidate iterators or references to existing elements. Erasure invalidates only iterators and references to the erased elements.

### Adaptors

##### `std::stack`

`std::stack<T>` is a container adaptor that provides LIFO access.

```cpp
#include <stack>

std::stack<int> values;
values.push(1);
values.push(2);
values.emplace(3);

int top = values.top();
values.pop();

bool empty = values.empty();
std::size_t size = values.size();
```

`pop()` removes the top element and returns no value. Call `top()` before `pop()` when the element is needed.

##### `std::queue`

`std::queue<T>` is a container adaptor that provides FIFO access.

```cpp
#include <queue>

std::queue<int> values;
values.push(1);
values.push(2);
values.emplace(3);

int first = values.front();
int last = values.back();
values.pop();

bool empty = values.empty();
std::size_t size = values.size();
```

`pop()` removes the front element and returns no value.

### Associative

##### `std::set`

`std::set<Key>` stores unique keys in sorted order according to its comparison object.

```cpp
#include <set>

std::set<int> values{3, 1, 2, 2};  // 1, 2, 3

auto [iterator, inserted] = values.insert(4);
values.erase(1);
```

Lookup:

```cpp
auto iterator = values.find(3);

if (iterator != values.end()) {
    // found
}

std::size_t count = values.count(3);  // 0 or 1 for std::set
auto lower = values.lower_bound(2);   // first element not less than 2
auto upper = values.upper_bound(2);   // first element greater than 2
```

Elements are treated as keys, so they cannot be modified through a `set` iterator. Use `std::multiset` when equivalent keys are intentionally required.

##### `std::map`

`std::map<Key, T>` stores key-value pairs ordered by unique keys.

```cpp
#include <map>
#include <string>

std::map<std::string, int> scores;

scores["Alice"] = 90;
scores.insert({"Bob", 85});
scores.emplace("Carol", 92);
```

Lookup and access:

```cpp
int alice = scores.at("Alice");

auto iterator = scores.find("Bob");
if (iterator != scores.end()) {
    int score = iterator->second;
}
```

`operator[]` inserts a value-initialized mapped value when the key does not exist. Use `find()` or `at()` when insertion is not wanted.

```cpp
for (const auto& [name, score] : scores) {
    // name is the key, score is the mapped value
}
```

Erasure and bounds:

```cpp
scores.erase("Bob");

auto lower = scores.lower_bound("B");
auto upper = scores.upper_bound("D");
```

A map element has type similar to `std::pair<const Key, T>`: the key is not modifiable through the element, while the mapped value is.

### Selection

##### Common Choices

| Requirement | Container |
| --- | --- |
| Text | `string` |
| General dynamic sequence | `vector` |
| Efficient operations at both ends | `deque` |
| Frequent insertion/erasure at known positions | `list` |
| LIFO access | `stack` |
| FIFO access | `queue` |
| Ordered unique keys | `set` |
| Ordered key-value pairs | `map` |

For a general dynamic sequence, start with `vector` unless another container provides behavior the program specifically needs.
