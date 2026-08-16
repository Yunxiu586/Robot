# Standard Template Library

[toc]

### Function Objects

##### Custom Function Objects

A function object is an object for which function-call syntax is defined, commonly by overloading `operator()`.

- it can be called with arguments and return a value
- it can store state in data members
- it can be passed to algorithms or other functions as a callable object

```cpp
#include <iostream>

class Accumulator {
public:
	int operator()(int value) {
		total_ += value;
		++calls_;
		return total_;
	}

	int total() const {
		return total_;
	}

	int calls() const {
		return calls_;
	}

private:
	int total_{};
	int calls_{};
};

void apply(Accumulator& accumulator, int value) {
	accumulator(value);
}

int main() {
	Accumulator accumulator;

	std::cout << accumulator(10) << '\n';		// 10
	apply(accumulator, 20);

	std::cout << accumulator.total() << '\n';	// 30
	std::cout << accumulator.calls() << '\n';	// 2
}
```

##### Predicates

A predicate is a callable whose result is used as a Boolean condition.

- a unary predicate is called with one argument
- a binary predicate is called with two arguments

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

class GreaterThan {
public:
	explicit GreaterThan(int limit)
		: limit_{limit} {}

	bool operator()(int value) const {
		return value > limit_;
	}

private:
	int limit_{};
};

int main() {
	std::vector<int> values{10, 40, 20, 30};

	auto found = std::find_if(values.begin(), values.end(), GreaterThan{25});
	if (found != values.end()) {
		std::cout << *found << '\n';	// 40
	}

	// A lambda can be used directly as a short local predicate
	auto small = std::find_if(values.begin(), values.end(), [](int value) {
		return value < 20;
	});
	if (small != values.end()) {
		std::cout << *small << '\n';	// 10
	}

	std::sort(values.begin(), values.end(), [](int lhs, int rhs) {
		return lhs > rhs;
	});
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';					// 40 30 20 10
}
```

##### Standard Function Objects

Header `<functional>` provides function objects for common operators.

**Arithmetic**

- `std::plus<>`
- `std::minus<>`
- `std::multiplies<>`
- `std::divides<>`
- `std::modulus<>`
- `std::negate<>`

**Comparison**

- `std::equal_to<>`
- `std::not_equal_to<>`
- `std::greater<>`
- `std::greater_equal<>`
- `std::less<>`
- `std::less_equal<>`

**Logical**

- `std::logical_and<>`
- `std::logical_or<>`
- `std::logical_not<>`

The empty template argument form uses the `void` specialization and performs transparent calls.

```cpp
#include <functional>
#include <iostream>

int main() {
	std::cout << std::plus<>{}(10, 20) << '\n';				// 30
	std::cout << std::negate<>{}(10) << '\n';				// -10
	std::cout << std::greater<>{}(20, 10) << '\n';			// 1
	std::cout << std::logical_and<>{}(true, false) << '\n';	// 0
	std::cout << std::logical_not<>{}(false) << '\n';		// 1
}
```

### Algorithms

The algorithms below primarily use `<algorithm>`. `std::accumulate()` is declared in `<numeric>`, and standard function objects are declared in `<functional>`.

##### Traversal Algorithms

- `for_each()` applies a callable to every element in a range
- `transform()` applies an operation and writes each result to a destination range
- the callable can be a function, function object, or lambda expression

Common overloads used here:

```cpp
template<class InputIt, class UnaryFunc>
UnaryFunc for_each(InputIt first, InputIt last, UnaryFunc function);

template<class InputIt, class OutputIt, class UnaryOp>
OutputIt transform(InputIt first, InputIt last, OutputIt destination, UnaryOp operation);
```

The destination supplied to `transform()` must contain enough writable positions when a normal iterator is used.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

void printValue(int value) {
	std::cout << value << ' ';
}

int main() {
	const std::vector<int> values{1, 2, 3, 4};
	std::vector<int> squares(values.size());

	std::for_each(values.begin(), values.end(), printValue);
	std::cout << '\n';			// 1 2 3 4

	std::transform(values.begin(), values.end(), squares.begin(), [](int value) {
		return value * value;
	});
	std::for_each(squares.begin(), squares.end(), printValue);
	std::cout << '\n';			// 1 4 9 16
}
```

##### Search and Count Algorithms

- `find()` searches for a value
- `find_if()` searches for the first element satisfying a predicate
- `adjacent_find()` searches for adjacent equivalent elements
- `binary_search()` tests whether a value is present in an appropriately partitioned range; a normally sorted range satisfies this requirement
- `count()` counts elements equal to a value
- `count_if()` counts elements satisfying a predicate
- for program-defined types, `find()` and `count()` use equality comparison; `find_if()` and `count_if()` use the supplied predicate

Common overloads used here:

```cpp
template<class InputIt, class T>
InputIt find(InputIt first, InputIt last, const T& value);

template<class InputIt, class Predicate>
InputIt find_if(InputIt first, InputIt last, Predicate predicate);

template<class ForwardIt>
ForwardIt adjacent_find(ForwardIt first, ForwardIt last);

template<class ForwardIt, class T>
bool binary_search(ForwardIt first, ForwardIt last, const T& value);

template<class InputIt, class T>
typename std::iterator_traits<InputIt>::difference_type
count(InputIt first, InputIt last, const T& value);

template<class InputIt, class Predicate>
typename std::iterator_traits<InputIt>::difference_type
count_if(InputIt first, InputIt last, Predicate predicate);
```

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Person {
	std::string name;
	int age;
};

bool operator==(const Person& lhs, const Person& rhs) {
	return lhs.name == rhs.name && lhs.age == rhs.age;
}

int main() {
	const std::vector<int> values{10, 20, 20, 30, 40};

	auto found = std::find(values.begin(), values.end(), 30);
	auto adjacent = std::adjacent_find(values.begin(), values.end());

	if (found != values.end()) {
		std::cout << *found << '\n';		// 30
	}
	if (adjacent != values.end()) {
		std::cout << *adjacent << '\n';		// 20
	}

	std::cout << std::boolalpha
			  << std::binary_search(values.begin(), values.end(), 40) << '\n';	// true
	std::cout << std::count(values.begin(), values.end(), 20) << '\n';		// 2

	const std::vector<Person> people{
		{"Alice", 20},
		{"Bob", 30},
		{"Bob", 30}
	};

	auto bob = std::find(people.begin(), people.end(), Person{"Bob", 30});
	auto older = std::find_if(people.begin(), people.end(), [](const Person& person) {
		return person.age > 20;
	});

	if (bob != people.end()) {
		std::cout << bob->name << '\n';		// Bob
	}
	if (older != people.end()) {
		std::cout << older->name << '\n';	// Bob
	}

	std::cout << std::count(people.begin(), people.end(), Person{"Bob", 30}) << '\n';	// 2
	std::cout << std::count_if(people.begin(), people.end(), [](const Person& person) {
		return person.age > 20;
	}) << '\n';	// 2
}
```

##### Sorting and Reordering Algorithms

- `sort()` orders a random-access range; a comparison object can define a different ordering
- `shuffle()` randomly rearranges a random-access range using a supplied random number generator
- `merge()` combines two sorted ranges into one sorted destination range
- `reverse()` reverses a bidirectional range

`std::random_shuffle()` was removed from the standard library. Use `std::shuffle()` instead.

Common overloads used here:

```cpp
template<class RandomIt>
void sort(RandomIt first, RandomIt last);

template<class RandomIt, class Compare>
void sort(RandomIt first, RandomIt last, Compare compare);

template<class RandomIt, class URBG>
void shuffle(RandomIt first, RandomIt last, URBG&& generator);

template<class InputIt1, class InputIt2, class OutputIt>
OutputIt merge(InputIt1 first1, InputIt1 last1,
               InputIt2 first2, InputIt2 last2,
               OutputIt destination);

template<class BidirectionalIt>
void reverse(BidirectionalIt first, BidirectionalIt last);
```

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <random>
#include <vector>

int main() {
	std::vector<int> values{30, 10, 40, 20};

	std::sort(values.begin(), values.end());
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30 40

	std::sort(values.begin(), values.end(), std::greater<>{});
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 40 30 20 10

	std::reverse(values.begin(), values.end());
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 10 20 30 40

	std::mt19937 generator{42};
	std::shuffle(values.begin(), values.end(), generator);
}
```

`merge()` requires both input ranges to be sorted according to the same ordering relation.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
	const std::vector<int> first{1, 3, 5};
	const std::vector<int> second{2, 4, 6};
	std::vector<int> result(first.size() + second.size());

	auto end = std::merge(
		first.begin(), first.end(),
		second.begin(), second.end(),
		result.begin()
	);

	for (auto it = result.begin(); it != end; ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';	// 1 2 3 4 5 6
}
```

##### Copy and Replace Algorithms

- `copy()` copies a range to a destination range
- `replace()` replaces elements equal to a specified value
- `replace_if()` replaces elements satisfying a predicate
- `swap()` exchanges two objects of the same type

Common overloads used here:

```cpp
template<class InputIt, class OutputIt>
OutputIt copy(InputIt first, InputIt last, OutputIt destination);

template<class ForwardIt, class T>
void replace(ForwardIt first, ForwardIt last, const T& old_value, const T& new_value);

template<class ForwardIt, class Predicate, class T>
void replace_if(ForwardIt first, ForwardIt last, Predicate predicate, const T& new_value);

template<class T>
void swap(T& first, T& second);
```

```cpp
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

int main() {
	const std::vector<int> source{1, 2, 3, 2, 4};
	std::vector<int> values(source.size());

	std::copy(source.begin(), source.end(), values.begin());
	std::cout << values.front() << ' ' << values.back() << '\n';	// 1 4

	std::replace(values.begin(), values.end(), 2, 20);
	std::replace_if(values.begin(), values.end(), [](int value) {
		return value > 10;
	}, 99);

	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';	// 1 99 3 99 4

	std::vector<int> other{7, 8};
	std::swap(values, other);

	std::cout << values.size() << '\n';		// 2
	std::cout << values.front() << '\n';	// 7
	std::cout << other.size() << '\n';		// 5
	std::cout << other.front() << '\n';		// 1
}
```

##### Accumulation and Fill

- `accumulate()` combines the elements of a range with an initial value
- `fill()` assigns a value to every element in a range

Common overloads used here:

```cpp
template<class InputIt, class T>
T accumulate(InputIt first, InputIt last, T initial);

template<class ForwardIt, class T>
void fill(ForwardIt first, ForwardIt last, const T& value);
```

`accumulate()` is declared in `<numeric>`. The type of its initial value determines the accumulator type.

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
	std::vector<int> values{1, 2, 3, 4, 5};

	const int sum = std::accumulate(values.begin(), values.end(), 100);
	std::cout << sum << '\n';	// 115

	std::fill(values.begin() + 1, values.end() - 1, 0);
	for (int value : values) {
		std::cout << value << ' ';
	}
	std::cout << '\n';			// 1 0 0 0 5
}
```

##### Set Operations on Sorted Ranges

- `set_intersection()` writes the intersection of two sorted ranges
- `set_union()` writes the union of two sorted ranges
- `set_difference()` writes the elements of the first sorted range that are not matched by the second

Both input ranges must be sorted according to the same ordering relation.

Common overloads used here:

```cpp
template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_intersection(InputIt1 first1, InputIt1 last1,
                          InputIt2 first2, InputIt2 last2,
                          OutputIt destination);

template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_union(InputIt1 first1, InputIt1 last1,
                   InputIt2 first2, InputIt2 last2,
                   OutputIt destination);

template<class InputIt1, class InputIt2, class OutputIt>
OutputIt set_difference(InputIt1 first1, InputIt1 last1,
                        InputIt2 first2, InputIt2 last2,
                        OutputIt destination);
```

Each algorithm returns the end of the output range that it produced.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

template<class InputIt>
void printRange(InputIt first, InputIt last) {
	for (auto it = first; it != last; ++it) {
		std::cout << *it << ' ';
	}
	std::cout << '\n';
}

int main() {
	const std::vector<int> first{1, 2, 3, 4};
	const std::vector<int> second{3, 4, 5};

	std::vector<int> intersection(std::min(first.size(), second.size()));
	auto intersection_end = std::set_intersection(
		first.begin(), first.end(),
		second.begin(), second.end(),
		intersection.begin()
	);
	printRange(intersection.begin(), intersection_end);	// 3 4

	std::vector<int> union_values(first.size() + second.size());
	auto union_end = std::set_union(
		first.begin(), first.end(),
		second.begin(), second.end(),
		union_values.begin()
	);
	printRange(union_values.begin(), union_end);		// 1 2 3 4 5

	std::vector<int> difference(first.size());
	auto difference_end = std::set_difference(
		first.begin(), first.end(),
		second.begin(), second.end(),
		difference.begin()
	);
	printRange(difference.begin(), difference_end);		// 1 2
}
```
