# Standard Library

[toc]

##### STL Overview

The Standard Template Library is built around containers, iterators, algorithms, and callable objects.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> values{3, 1, 2};
std::sort(values.begin(), values.end());
```

| Component | Role |
| --- | --- |
| Container | Stores objects |
| Iterator | Refers to a position in a container |
| Algorithm | Operates on an iterator range |
| Callable | Function, function object, or lambda used by an algorithm |

A half-open range `[first, last)` includes `first` but excludes `last`.

##### Iterators

```cpp
std::vector<int> values{10, 20, 30};

for (auto iterator = values.begin(); iterator != values.end(); ++iterator) {
    std::cout << *iterator << '\n';
}
```

Const iterators prevent element modification.

```cpp
for (auto iterator = values.cbegin(); iterator != values.cend(); ++iterator) {
    std::cout << *iterator << '\n';
}
```

Reverse iterators:

```cpp
for (auto iterator = values.rbegin(); iterator != values.rend(); ++iterator) {
    std::cout << *iterator << '\n';
}
```

Use an iterator when its position or iterator operations are needed; otherwise use the range-based loop form covered in `Basic Syntax.md`.

Iterator invalidation depends on the container. In particular, growing a `vector` may invalidate all pointers, references, and iterators to its elements.

##### `std::array`

`std::array<T, N>` is a fixed-size contiguous container.

```cpp
#include <array>

std::array<int, 4> values{1, 2, 3, 4};

std::cout << values.size() << '\n';
std::cout << values.front() << '\n';
std::cout << values.back() << '\n';
```

```cpp
values.fill(0);
values.at(2) = 5;      // bounds-checked
int raw = values[2];   // not bounds-checked
```

Use `std::array` when the size is known at compile time and you want container operations without dynamic allocation.

##### `std::vector`

`std::vector<T>` is a resizable contiguous array and the default sequence container.

```cpp
#include <vector>

std::vector<int> values{1, 2, 3};
values.push_back(4);
values.emplace_back(5);
values.pop_back();
```

Access and size:

```cpp
std::cout << values.size() << '\n';
std::cout << values.capacity() << '\n';
std::cout << values.front() << '\n';
std::cout << values.back() << '\n';
std::cout << values.at(1) << '\n';
```

Capacity management:

```cpp
std::vector<int> values;
values.reserve(100);   // changes capacity, not size
values.resize(20);     // changes number of elements
values.shrink_to_fit();
```

Insertion and erasure:

```cpp
values.insert(values.begin() + 1, 99);
values.erase(values.begin() + 1);
values.clear();
```

Complexity:

| Operation | Typical Complexity |
| --- | --- |
| Random access | `O(1)` |
| Add/remove at end | Amortized `O(1)` |
| Insert/erase in middle | `O(n)` |
| Search without ordering | `O(n)` |

Store objects directly when possible.

```cpp
std::vector<std::string> words;
words.emplace_back("hello");  // constructs the string directly in the vector
```

Use `reserve()` before many insertions when an approximate final size is known.

##### `std::deque` and `std::list`

`std::deque<T>` supports efficient insertion and removal at both ends and random access.

```cpp
#include <deque>

std::deque<int> values{2, 3};
values.push_front(1);
values.push_back(4);
values.pop_front();
values.pop_back();
```

`std::list<T>` is a doubly linked list.

```cpp
#include <iterator>
#include <list>

std::list<int> values{1, 2, 3};
values.push_front(0);
values.push_back(4);
```

List insertion or erasure is constant time only after the position is already known. Finding that position remains linear.

```cpp
auto iterator = values.begin();
std::advance(iterator, 2);
values.insert(iterator, 99);
values.erase(iterator);
```

Use container-specific list operations.

```cpp
values.sort();
values.unique();
values.remove(99);
values.reverse();
```

| Need | Better Choice |
| --- | --- |
| General dynamic sequence | `vector` |
| Efficient operations at both ends | `deque` |
| Stable iterators and frequent known-position insertion | `list` |

Do not choose `list` merely because insertion is theoretically `O(1)`; `vector` is often faster because of cache locality.

##### Container Adapters

These are container adaptors that expose restricted interfaces.

Last-in, first-out:

```cpp
#include <stack>

std::stack<int> values;
values.push(1);
values.push(2);

std::cout << values.top() << '\n';
values.pop();
```

First-in, first-out:

```cpp
#include <queue>

std::queue<int> values;
values.push(1);
values.push(2);

std::cout << values.front() << '\n';
values.pop();
```

Priority queue, largest value first by default:

```cpp
std::priority_queue<int> values;
values.push(3);
values.push(1);
values.push(5);

std::cout << values.top() << '\n';   // 5
```

Minimum-first priority queue:

```cpp
#include <functional>
#include <vector>

std::priority_queue<int, std::vector<int>, std::greater<int>> values;
```

Always call `top()` or `front()` before `pop()` because `pop()` returns no value.

##### Sets

`std::set<T>` stores unique ordered keys, usually in a balanced tree.

```cpp
#include <set>

std::set<int> ids{3, 1, 2, 2};
ids.insert(4);
ids.erase(1);

if (ids.find(3) != ids.end()) {
    std::cout << "found\n";
}
```

Useful operations:

```cpp
bool contains = ids.count(3) != 0;
auto lower = ids.lower_bound(2);  // first element not less than 2
auto upper = ids.upper_bound(2);  // first element greater than 2
```

`std::unordered_set<T>` stores unique keys in a hash table.

```cpp
#include <string>
#include <unordered_set>

std::unordered_set<std::string> colors{"red", "green"};
colors.insert("blue");
```

| Container | Order | Typical Lookup |
| --- | --- | --- |
| `set` | Sorted | `O(log n)` |
| `unordered_set` | Unspecified | Average `O(1)`, worst `O(n)` |

Use `multiset` only when duplicate keys are intentionally required.

##### Maps

`std::map<Key, Value>` stores ordered key-value pairs.

```cpp
#include <map>
#include <string>

std::map<std::string, int> scores;
scores["Alice"] = 90;
scores.insert({"Bob", 85});
scores.emplace("Carol", 92);
```

Access carefully:

```cpp
int alice = scores.at("Alice");

auto iterator = scores.find("Bob");
if (iterator != scores.end()) {
    std::cout << iterator->first << ' ' << iterator->second << '\n';
}
```

`operator[]` inserts a default value when the key does not exist. Use `find()`, `contains()` in C++20, or `at()` when insertion is not wanted.

```cpp
for (const auto& [name, score] : scores) {
    std::cout << name << ' ' << score << '\n';
}
```

`std::unordered_map<Key, Value>` uses hashing.

```cpp
#include <string>
#include <unordered_map>

std::unordered_map<int, std::string> number_names;
number_names.emplace(1, "one");
number_names.emplace(2, "two");
```

| Container | Order | Typical Lookup |
| --- | --- | --- |
| `map` | Sorted by key | `O(log n)` |
| `unordered_map` | Unspecified | Average `O(1)`, worst `O(n)` |

Use `map` when sorted traversal, range queries, or deterministic key order matters. Use `unordered_map` for fast average lookup when ordering is unnecessary and a hash exists.

##### Common Algorithms

Algorithms operate on iterator ranges.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> values{4, 1, 3, 2, 3};

std::sort(values.begin(), values.end());
std::reverse(values.begin(), values.end());
```

Searching and counting:

```cpp
auto iterator = std::find(values.begin(), values.end(), 3);
auto count = std::count(values.begin(), values.end(), 3);

bool any_negative = std::any_of(values.begin(), values.end(), [](int value) {
    return value < 0;
});
```

Minimum and maximum:

```cpp
auto minimum = std::min_element(values.begin(), values.end());
auto maximum = std::max_element(values.begin(), values.end());
```

Transform:

```cpp
std::transform(values.begin(), values.end(), values.begin(), [](int value) {
    return value * 2;
});
```

Remove-erase idiom:

```cpp
values.erase(
    std::remove(values.begin(), values.end(), 3),
    values.end()
);
```

`std::remove` moves the retained elements toward the beginning and returns the new logical end; it does not change the container size. Elements after the new logical end remain valid but have unspecified values. In C++20, `std::erase(values, 3)` is simpler for supported containers.

Unique adjacent duplicates:

```cpp
std::sort(values.begin(), values.end());
values.erase(std::unique(values.begin(), values.end()), values.end());
```

Custom sorting:

```cpp
std::sort(values.begin(), values.end(), std::greater<int>{});
```

##### Numeric Utilities

```cpp
#include <numeric>

std::vector<int> values{1, 2, 3, 4};

int sum = std::accumulate(values.begin(), values.end(), 0);
std::iota(values.begin(), values.end(), 10);  // 10, 11, 12, 13
```

`std::pair` stores two values.

```cpp
#include <string>
#include <utility>

std::pair<int, std::string> student{1, "Alice"};
std::cout << student.first << ' ' << student.second << '\n';

auto [id, name] = student;  // structured binding
```

##### Strings and Streams

`std::string` manages a resizable character sequence.

```cpp
#include <string>

std::string first = "Hello";
std::string second = "World";
std::string text = first + " " + second;
```

Common operations:

```cpp
bool empty = text.empty();
std::size_t size = text.size();

text += "!";
text.append(" Welcome.");
text.insert(0, "Message: ");
text.erase(0, 9);
text.replace(0, 5, "Hi");

std::size_t position = text.find("World");
std::string part = text.substr(0, 2);
```

`operator[]` does not check bounds. `at()` throws `std::out_of_range` for an invalid position.

```cpp
char first_character = text.at(0);
```

String-number conversions:

```cpp
int number = std::stoi("42");
double value = std::stod("3.14");
std::string number_text = std::to_string(100);
```

Parse formatted text with `std::istringstream`.

```cpp
#include <sstream>

std::istringstream input{"10 20 30"};
int a{}, b{}, c{};
input >> a >> b >> c;
```

Build a string with `std::ostringstream`.

```cpp
std::ostringstream output;
output << "Value: " << 42;
std::string result = output.str();
```

##### Stream Formatting

```cpp
#include <iomanip>
#include <iostream>

const double value = 3.1415926;

std::cout << std::fixed << std::setprecision(3) << value << '\n';
std::cout << std::setw(8) << std::setfill('0') << 42 << '\n';
std::cout << std::boolalpha << true << '\n';
std::cout << std::hex << 255 << '\n';
```

Formatting flags remain active until changed, except `std::setw`, which applies only to the next formatted field.

##### Smart Pointers

Smart pointers express dynamic-object ownership and release their objects automatically.

```cpp
#include <memory>

struct Resource {};
```

Exclusive ownership uses `std::unique_ptr`:

```cpp
auto first = std::make_unique<Resource>();
auto second = std::move(first);  // transfers ownership; first is empty
```

Shared ownership uses `std::shared_ptr`:

```cpp
auto shared_resource = std::make_shared<Resource>();
auto another_owner = shared_resource;
```

Use `std::weak_ptr` for non-owning observation of an object managed by `shared_ptr`, especially to break ownership cycles.

```cpp
std::weak_ptr<Resource> observer = shared_resource;

if (auto locked = observer.lock()) {
    // safely use locked
}
```

| Type | Ownership |
| --- | --- |
| `std::unique_ptr<T>` | Exactly one owner |
| `std::shared_ptr<T>` | Reference-counted shared ownership |
| `std::weak_ptr<T>` | Non-owning observation of a shared object |
| Raw pointer or reference | Usually non-owning access |

Prefer `std::make_unique` and `std::make_shared` rather than writing `new` directly.

```cpp
void useResource(const Resource& resource);              // required non-owning access
void maybeUseResource(const Resource* resource);         // optional non-owning access
void takeResource(std::unique_ptr<Resource> resource);   // ownership transfer
void shareResource(std::shared_ptr<Resource> resource);  // shared ownership
```

Do not use `shared_ptr` merely to avoid deciding ownership. A smart pointer communicates ownership; it is not a replacement syntax for every raw pointer.

##### Container Selection

| Requirement | Recommended Container |
| --- | --- |
| Fixed-size sequence | `array` |
| General dynamic sequence | `vector` |
| Push/pop at both ends | `deque` |
| Stable iterators with frequent known-position edits | `list` |
| LIFO access | `stack` |
| FIFO access | `queue` |
| Highest-priority access | `priority_queue` |
| Ordered unique keys | `set` |
| Fast average unique-key lookup | `unordered_set` |
| Ordered key-value pairs | `map` |
| Fast average key-value lookup | `unordered_map` |

Approximate complexity:

| Container | Random Access | Insert at End | Insert at Known Middle Position | Key Lookup |
| --- | --- | --- | --- | --- |
| `array` | `O(1)` | Not resizable | Not resizable | `O(n)` |
| `vector` | `O(1)` | Amortized `O(1)` | `O(n)` | `O(n)` |
| `deque` | `O(1)` | `O(1)` at either end | `O(n)` | `O(n)` |
| `list` | No indexed access | `O(1)` | `O(1)` after iterator is known | `O(n)` |
| `set` / `map` | No indexed access | — | `O(log n)` | `O(log n)` |
| `unordered_set` / `unordered_map` | No indexed access | — | Average `O(1)` | Average `O(1)` |

Start with `vector` unless another container's behavior is specifically required.

##### Common Mistakes

+ Accessing an empty container with `front()`, `back()`, or `top()`.
+ Using `operator[]` on a map when accidental insertion is unwanted.
+ Keeping a vector iterator after reallocation or erasure.
+ Assuming unordered containers preserve insertion order.
+ Calling `list` algorithms such as `std::sort` instead of `list::sort()`.
+ Forgetting that `std::remove` does not erase elements by itself.
+ Copying large elements in loops instead of using `const auto&`.
+ Choosing `list` without measuring whether its node allocation and poor cache locality are acceptable.
