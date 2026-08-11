# Algorithms

[toc]

### Basics

##### Iterator Ranges

Standard library algorithms operate on iterator ranges, usually written as `[first, last)`.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> values{3, 1, 2};
std::sort(values.begin(), values.end());
```

The algorithm does not need to know the concrete container type. It only requires iterators that satisfy the algorithm's requirements.

### Callables

##### Function Objects

A function object is an object that can be called with function-call syntax. A class becomes callable by defining `operator()`.

```cpp
class Square {
public:
    int operator()(int value) const {
        return value * value;
    }
};

Square square;
int result = square(5);  // 25
```

Function objects can store state.

```cpp
class Add {
public:
    explicit Add(int offset)
        : offset_{offset} {}

    int operator()(int value) const {
        return value + offset_;
    }

private:
    int offset_{};
};
```

##### Predicates

A predicate is a callable whose result is used as a Boolean condition.

Unary predicate:

```cpp
class IsEven {
public:
    bool operator()(int value) const {
        return value % 2 == 0;
    }
};
```

Binary predicate:

```cpp
class Descending {
public:
    bool operator()(int left, int right) const {
        return left > right;
    }
};
```

Lambdas are often the shortest way to provide a local predicate.

```cpp
auto is_even = [](int value) {
    return value % 2 == 0;
};
```

##### Standard Function Objects

The `<functional>` header provides reusable function objects.

```cpp
#include <functional>

std::plus<int> add;
std::greater<int> greater;
std::logical_not<bool> logical_not;

int sum = add(2, 3);          // 5
bool result = greater(5, 3);  // true
bool value = logical_not(false);
```

| Category | Examples |
| --- | --- |
| Arithmetic | `plus`, `minus`, `multiplies`, `divides`, `modulus`, `negate` |
| Comparison | `equal_to`, `not_equal_to`, `greater`, `less`, `greater_equal`, `less_equal` |
| Logical | `logical_and`, `logical_or`, `logical_not` |

### Traversal

##### `std::for_each`

`std::for_each` invokes a callable for each element in a range.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> values{1, 2, 3};

std::for_each(values.begin(), values.end(), [](int value) {
    std::cout << value << '\n';
});
```

Use a reference parameter when the callable should modify the elements.

```cpp
std::for_each(values.begin(), values.end(), [](int& value) {
    value *= 2;
});
```

##### `std::transform`

Unary transformation:

```cpp
#include <algorithm>
#include <vector>

std::vector<int> source{1, 2, 3};
std::vector<int> result(source.size());

std::transform(source.begin(), source.end(), result.begin(), [](int value) {
    return value * 2;
});
```

Binary transformation:

```cpp
std::vector<int> left{1, 2, 3};
std::vector<int> right{10, 20, 30};
std::vector<int> result(left.size());

std::transform(
    left.begin(), left.end(), right.begin(), result.begin(), std::plus<int>{}
);
```

The destination range must provide enough writable elements unless an insertion iterator is used.

### Search

##### `std::find` and `std::find_if`

```cpp
#include <algorithm>
#include <vector>

std::vector<int> values{1, 3, 4, 6};

auto value_iterator = std::find(values.begin(), values.end(), 4);
auto predicate_iterator = std::find_if(values.begin(), values.end(), [](int value) {
    return value % 2 == 0;
});
```

A failed search returns the supplied `last` iterator.

```cpp
if (value_iterator != values.end()) {
    // found
}
```

##### `std::adjacent_find`

`std::adjacent_find` finds the first pair of adjacent equivalent elements.

```cpp
std::vector<int> values{1, 2, 2, 3};
auto iterator = std::adjacent_find(values.begin(), values.end());
```

A binary predicate can define the matching relation.

```cpp
auto iterator = std::adjacent_find(
    values.begin(), values.end(), [](int left, int right) {
        return right == left + 1;
    }
);
```

##### `std::binary_search`

`std::binary_search` checks whether an element occurs in a partitioned range. With the default comparison, the range is normally sorted in ascending order.

```cpp
std::vector<int> values{1, 2, 3, 4, 5};
bool found = std::binary_search(values.begin(), values.end(), 3);
```

When a custom ordering is used, the range and the search must use compatible ordering.

##### `std::count` and `std::count_if`

```cpp
std::vector<int> values{1, 2, 2, 3, 4};

auto twos = std::count(values.begin(), values.end(), 2);
auto even = std::count_if(values.begin(), values.end(), [](int value) {
    return value % 2 == 0;
});
```

### Ordering

##### `std::sort`

`std::sort` orders a random-access range.

```cpp
#include <algorithm>
#include <functional>
#include <vector>

std::vector<int> values{4, 1, 3, 2};

std::sort(values.begin(), values.end());
std::sort(values.begin(), values.end(), std::greater<int>{});
```

The comparison must define a strict weak ordering.

##### `std::shuffle`

`std::shuffle` randomly permutes a range using a supplied uniform random bit generator.

```cpp
#include <algorithm>
#include <random>
#include <vector>

std::vector<int> values{1, 2, 3, 4, 5};
std::mt19937 engine{std::random_device{}()};

std::shuffle(values.begin(), values.end(), engine);
```

##### `std::merge`

`std::merge` combines two sorted ranges into one sorted output range.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> first{1, 3, 5};
std::vector<int> second{2, 4, 6};
std::vector<int> result(first.size() + second.size());

std::merge(
    first.begin(), first.end(),
    second.begin(), second.end(),
    result.begin()
);
```

The input ranges must be sorted with an ordering compatible with the merge operation.

##### `std::reverse`

```cpp
std::vector<int> values{1, 2, 3, 4};
std::reverse(values.begin(), values.end());
```

### Copy and Replace

##### `std::copy`

`std::copy` copies a range to an output range.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> source{1, 2, 3};
std::vector<int> destination(source.size());

std::copy(source.begin(), source.end(), destination.begin());
```

An insertion iterator can grow a destination container.

```cpp
#include <iterator>

std::vector<int> destination;
std::copy(source.begin(), source.end(), std::back_inserter(destination));
```

##### `std::replace` and `std::replace_if`

```cpp
std::vector<int> values{1, 2, 2, 3, 4};

std::replace(values.begin(), values.end(), 2, 0);

std::replace_if(values.begin(), values.end(), [](int value) {
    return value < 0;
}, 0);
```

##### `std::swap`

`std::swap` exchanges two objects.

```cpp
#include <utility>

int first = 10;
int second = 20;
std::swap(first, second);
```

Containers also provide `swap()` member functions.

### Numeric

##### `std::accumulate`

`std::accumulate` combines the elements of a range with an initial value.

```cpp
#include <numeric>
#include <vector>

std::vector<int> values{1, 2, 3, 4};
int sum = std::accumulate(values.begin(), values.end(), 0);  // 10
```

A custom binary operation can replace addition.

```cpp
int product = std::accumulate(
    values.begin(), values.end(), 1, std::multiplies<int>{}
);
```

##### `std::fill`

`std::fill` assigns the same value to each element in a range.

```cpp
#include <algorithm>
#include <vector>

std::vector<int> values(5);
std::fill(values.begin(), values.end(), 10);
```

##### `std::iota`

`std::iota` assigns successive values beginning with an initial value.

```cpp
#include <numeric>
#include <vector>

std::vector<int> values(5);
std::iota(values.begin(), values.end(), 10);  // 10, 11, 12, 13, 14
```

### Sets

Set algorithms operate on sorted input ranges. If a custom comparison is used, all input ranges and the algorithm must use compatible ordering.

##### `std::set_intersection`

```cpp
#include <algorithm>
#include <iterator>
#include <vector>

std::vector<int> first{1, 2, 3, 4};
std::vector<int> second{3, 4, 5};
std::vector<int> result;

std::set_intersection(
    first.begin(), first.end(),
    second.begin(), second.end(),
    std::back_inserter(result)
);  // 3, 4
```

##### `std::set_union`

```cpp
std::vector<int> result;

std::set_union(
    first.begin(), first.end(),
    second.begin(), second.end(),
    std::back_inserter(result)
);  // 1, 2, 3, 4, 5
```

##### `std::set_difference`

```cpp
std::vector<int> result;

std::set_difference(
    first.begin(), first.end(),
    second.begin(), second.end(),
    std::back_inserter(result)
);  // 1, 2
```
