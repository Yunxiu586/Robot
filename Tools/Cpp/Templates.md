# Templates

[toc]

Templates are the basis for generic programming in C++. They allow functions and classes to be defined in terms of parameters so that the same definition can operate on different concrete types or values. A template is instantiated with concrete template arguments when a corresponding function or type is needed.

### Function Templates

##### Basic Syntax

A function template defines a family of functions.

```cpp
template <typename T>
T maximum(const T& first, const T& second) {
    return first < second ? second : first;
}

int integer_max = maximum(3, 5);		// T is deduced as int
double double_max = maximum(2.5, 1.5);	// T is deduced as double
```

`typename` and `class` are equivalent when declaring a type template parameter.

```cpp
template <class T>
void swapValues(T& first, T& second) {
    T temporary = first;
    first = second;
    second = temporary;
}
```

The same algorithm can be used with arrays whose elements have different types.

```cpp
template <typename T>
void selectionSort(T array[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        int minimum_index = i;

        for (int j = i + 1; j < size; ++j) {
            if (array[j] < array[minimum_index]) {
                minimum_index = j;
            }
        }

        T temporary = array[i];
        array[i] = array[minimum_index];
        array[minimum_index] = temporary;
    }
}

int integers[]{5, 2, 4, 1, 3};
char characters[]{'d', 'a', 'c', 'b'};

selectionSort(integers, 5);    // 1, 2, 3, 4, 5
selectionSort(characters, 4);  // 'a', 'b', 'c', 'd'
```

##### Deduction

For a function template, template arguments can often be deduced from the function arguments. During deduction, the parameter type and the corresponding argument type are compared; implicit conversions are not used to make different argument types deduce the same template parameter.

A non-template function can use implicit conversions to convert arguments to its parameter types.

```cpp
int maximum(int first, int second) {
    return first < second ? second : first;
}

int a = maximum('a', 'b'); // char arguments are converted to int
```

For a function template, `maximum('c', 'd')` is valid and deduces `T` as `char`; the arguments are not converted to `int`. If different arguments would deduce conflicting types for the same template parameter, deduction fails.

```cpp
template <typename T>
T maximum(T first, T second) {
    return first < second ? second : first;
}

int a = maximum(10, 20);       // T is deduced as int
char b = maximum('c', 'd');    // T is deduced as char

// auto c = maximum(10, 'd');  // Error: T cannot be deduced as both int and char
```

When a template argument is supplied explicitly, that template parameter does not participate in deduction, and implicit conversions can apply to the corresponding function arguments.

```cpp
int d = maximum<int>('c', 'd'); // T is int; char arguments are converted to int
```

A function template may have more than one template parameter.

```cpp
template <typename T, typename U>
auto add(T first, U second) {
    return first + second;
}

auto result = add(2, 3.5);			// T is int, U is double
```

##### Overloading

Function templates can be overloaded with other templates or non-template functions. 

Normal overload resolution selects the best viable function; when otherwise indistinguishable, a non-template function is preferred over a function-template specialization.

```cpp
#include <iostream>

void print(int value) {
    std::cout << "int: " << value << '\n';
}

template <typename T>
void print(const T& value) {
    std::cout << "value: " << value << '\n';
}

print(10);       // Calls print(int)
print(3.14);     // Calls print<double>(const double&)
print<>(10);     // Forces consideration of function templates named print
```

##### Custom Types

A template can be instantiated with a user-defined type when the operations used by the selected specialization are valid for that type. 

One approach is to provide the required operation for the user-defined type.

```cpp
template <typename T>
const T& minimum(const T& first, const T& second) {
    return second < first ? second : first; // T must support comparison with <
}

struct Student {
    int score{};
};

bool operator<(const Student& first, const Student& second) {
    return first.score < second.score;
}

Student first{85};
Student second{92};
const Student& lower = minimum(first, second);
```

When one exact set of template arguments requires different behavior from the primary template, an explicit **specialization** can provide a separate definition. An explicit specialization is introduced by `template <>`.

```cpp
#include <string>

template <typename T>
bool sameValue(const T& first, const T& second) {
    return first == second;
}

struct Student {
    int id{};
    std::string name;
};

template <>
bool sameValue<Student>(const Student& first, const Student& second) {
    return first.id == second.id; // Compare Student objects by ID
}

Student first{1, "Alice"};
Student second{2, "Bob"};
bool is_same = sameValue(first, second);
```

The primary template remains unchanged; the specialization is selected only for `Student`. For type-specific behavior that differs from the primary template, specialization directly expresses that separate definition.

### Class Templates

##### Basic Syntax

A class template defines a family of classes. A specialization is formed when template arguments are supplied for the template parameters.

```cpp
#include <utility>

template <typename T>
class Box {
public:
    explicit Box(T value)
    	: value_{std::move(value)} {}

    const T& value() const {
        return value_;
    }

private:
    T value_{};
};

Box<int> first{10};			// T is explicitly int
Box<double> second{3.14};	// T is explicitly double
// first = second;			// Error: Box<int> and Box<double> are different types
```

Different specializations are different types.

A class template can have multiple template parameters, default template arguments, and constant template parameters.

```cpp
#include <cstddef>

template <typename T, std::size_t N = 8>
class Buffer {
public:
    constexpr std::size_t size() const {
        return N;
    }

private:
    T data_[N]{};
};

Buffer<int> first;       // N uses the default value 8
Buffer<double, 16> second;
```

##### Deduction

Template arguments are commonly written explicitly when naming a class-template specialization.

Since C++17, class template argument deduction (CTAD) can deduce template arguments from initialization when deduction information is available. Therefore, a class template is not restricted to explicit template arguments.

```cpp
#include <utility>

template <typename T>
class Box {
public:
    explicit Box(T value)
        : value_{std::move(value)} {}

    const T& value() const {
        return value_;
    }

private:
    T value_{};
};

Box<int> first{10};            // Explicit: Box<int>
Box second{20};                // C++17 CTAD: Box<int>
Box third{2.5};                // C++17 CTAD: Box<double>
```

##### Members

Constructors and other member functions of a class template may be defined inside or outside the class definition.

```cpp
template <typename T>
class Holder {
public:
    explicit Holder(const T& value);
    const T& value() const;

private:
    T value_{};
};

template <typename T>
Holder<T>::Holder(const T& value)
    : value_{value} {}

template <typename T>
const T& Holder<T>::value() const {
    return value_;
}
```

For an out-of-class definition, repeat the template parameter list and qualify the member with the class-template specialization `Holder<T>`.

When a class-template specialization is implicitly instantiated, declarations of its non-deleted member functions are instantiated, but their definitions are not all instantiated immediately. 

A member-function definition is instantiated when it is needed in a context that requires the definition.

```cpp
#include <iostream>

struct Student {
    int id{};
};

template <typename T>
class Printer {
public:
    explicit Printer(const T& value)
        : value_{value} {}

    void print() const {
        std::cout << value_ << '\n';
    }

    int id() const {
        return value_.id;      // Valid only when T has an id member
    }

private:
    T value_{};
};

Printer<int> number{42};       // OK: id() definition is not needed here
number.print();                // 42
// number.id();                // Error when id() is instantiated for T = int

Printer<Student> student{{7}};
std::cout << student.id() << '\n'; // 7
```

This differs from an ordinary non-template class: there is no later template substitution that can defer checking of dependent expressions in its member-function definitions.

##### Object Parameters

Objects produced from a class template can be passed to functions in three common forms.

A function can accept one exact specialization.

```cpp
#include <utility>

template <typename T>
class Box {
public:
    explicit Box(T value)
        : value_{std::move(value)} {}

    const T& value() const {
        return value_;
    }

private:
    T value_{};
};

Box<int> integer_box{10};
Box<double> double_box{2.5};
```

```cpp
void print(const Box<int>& box) {
    std::cout << box.value() << '\n';
}
```

The element type can be a function-template parameter, allowing any `Box<T>` specialization.

```cpp
template <typename T>
void print(const Box<T>& box) {
    std::cout << box.value() << '\n';
}
```

The complete object type can also be a function-template parameter. This form is more general because the parameter is no longer restricted to `Box<T>`.

```cpp
template <typename ObjectType>
void print(const ObjectType& object) {
    std::cout << object.value() << '\n'; // ObjectType must provide value()
}
```

##### Inheritance

A base-specifier must denote a class type. When the base is a class template, the derived class must therefore name a specialization such as `Base<int>`, or make the specialization depend on its own template parameters.

```cpp
template <typename T>
class Base {
protected:
    T value_{};
};

class IntegerBox : public Base<int> {
public:
    void set(int value) {
        value_ = value;
    }
};

// class InvalidBox : public Base {};
// Error: Base names a template, not a base-class type
```

If the base type should remain configurable, make the derived class a template as well.

```cpp
template <typename T>
class DerivedBox : public Base<T> {
public:
    void set(const T& value) {
        this->value_ = value;   // value_ belongs to a dependent base class
    }
};

DerivedBox<int> integer_box;
DerivedBox<double> double_box;
```

The object layout includes a base-class subobject, so the base class used by a concrete derived type must ultimately be a concrete specialization.

##### Friends

A friend function may be defined directly inside a class template. It is a non-member function with access to private and protected members.

```cpp
#include <iostream>

template <typename T>
class Box {
public:
    explicit Box(const T& value)
        : value_{value} {}

    friend void print(const Box& box) {
        std::cout << box.value_ << '\n';
    }

private:
    T value_{};
};

Box<int> box{42};
print(box);			// 42
```

A friend defined this way is not called as a member function. The unqualified call can find the corresponding friend through argument-dependent lookup.

For an out-of-class definition, declare the class template and function template first, then befriend the matching function-template specialization.

```cpp
#include <iostream>

template <typename T>
class Box;						// Forward declaration

template <typename T>
void print(const Box<T>& box);	// Function template declaration

template <typename T>
class Box {
public:
    explicit Box(const T& value)
        : value_{value} {}

private:
    T value_{};

    friend void print<T>(const Box<T>& box);
};

template <typename T>
void print(const Box<T>& box) {
    std::cout << box.value_ << '\n';
}

Box<int> box{42};
print(box);			// 42
```

##### Organization

A template definition normally has to be reachable where the corresponding specialization is instantiated. This is why general-purpose class templates are usually implemented in headers instead of placing only their declarations in a header and compiling their definitions as an ordinary `.cpp` translation unit.

One inclusion model keeps declarations and definitions in separate files but includes the implementation file from the header.

```cpp
// Box.h
#ifndef BOX_H
#define BOX_H

template <typename T>
class Box {
public:
    explicit Box(const T& value);
    const T& value() const;

private:
    T value_{};
};

#include "Box.cpp"             // Makes template definitions visible

#endif
```

```cpp
// Box.cpp

template <typename T>
Box<T>::Box(const T& value)
    : value_{value} {}

template <typename T>
const T& Box<T>::value() const {
    return value_;
}
```

In this model, `Box.cpp` is included as template implementation text; it should not also be treated as an independent ordinary source file by the build.

For a small class template, keeping the declaration and definition together in one C++ header is usually simpler.

```cpp
// Box.hpp
#ifndef BOX_HPP
#define BOX_HPP

template <typename T>
class Box {
public:
    explicit Box(const T& value)
        : value_{value} {}

    const T& value() const {
        return value_;
    }

private:
    T value_{};
};

#endif
```

C++ does not assign different language semantics to `.h` and `.hpp`. They are filename conventions. In C++ projects, `.hpp` is often used to make a C++-only header explicit; `.h` is also valid. For template-only code, a single `.hpp` file is a clear and convenient organization.

Explicit instantiation is another option when only a fixed set of specializations should be provided, but the inclusion model is the usual choice for general-purpose templates.

##### Example

The following example places the class template in `Array.hpp` and uses it from `main.cpp`. The `Array` class provides fixed-capacity storage, deep copy, copy assignment, tail insertion/removal, indexed access, and size/capacity queries.

```cpp
// Array.hpp
#ifndef ARRAY_HPP
#define ARRAY_HPP

#include <cstddef>
#include <memory>

template <typename T>
class Array {
public:
	// Constructs an empty array with fixed capacity
	explicit Array(std::size_t capacity)
		: capacity_{capacity}, data_{new T[capacity]{}} {}

	// Copy constructor
	// Allocates independent storage and copies the elements
	Array(const Array& other)
		: capacity_{other.capacity_},
		  size_{other.size_} {
		auto new_data = std::make_unique<T[]>(capacity_);

		for (std::size_t i = 0; i < size_; ++i) {
			new_data[i] = other.data_[i];
		}

		data_ = new_data.release();
	}

	// Copy assignment operator
	// Allocates independent storage before replacing the current storage
	Array& operator=(const Array& other) {
		if (this != &other) {
			auto new_data = std::make_unique<T[]>(other.capacity_);

			for (std::size_t i = 0; i < other.size_; ++i) {
				new_data[i] = other.data_[i];
			}

			delete[] data_;

			data_ = new_data.release();
			capacity_ = other.capacity_;
			size_ = other.size_;
		}

		return *this;
	}

	// Releases the dynamically allocated array
	~Array() {
		delete[] data_;
	}

	// Appends an element at the end
	// Returns false when the array has reached its capacity
	bool pushBack(const T& value) {
		if (size_ == capacity_) {
			return false;
		}

		data_[size_] = value;
		++size_;
		return true;
	}

	// Removes the last logical element
	// Returns false when the array is empty
	// The underlying T object is not destroyed until the Array is destroyed
	bool popBack() {
		if (size_ == 0) {
			return false;
		}

		--size_;
		return true;
	}

	// Provides unchecked indexed access to an element
	T& operator[](std::size_t index) {
		return data_[index];
	}

	// Provides unchecked read-only indexed access for const objects
	const T& operator[](std::size_t index) const {
		return data_[index];
	}

	// Returns the number of logically stored elements
	std::size_t size() const {
		return size_;
	}

	// Returns the maximum number of elements that can be stored
	std::size_t capacity() const {
		return capacity_;
	}

private:
	std::size_t capacity_{};	// Allocated element capacity
	std::size_t size_{};		// Number of logically stored elements
	T* data_{};					// Dynamically allocated storage
};

#endif
```

The copy constructor and copy assignment operator allocate separate storage and copy the stored elements, so each `Array` object owns its own dynamic array.

```cpp
// main.cpp
#include <iostream>

#include "Array.hpp"

struct Student {
	int id{};
	int score{};
};

int main() {
	Array<int> scores{3};
	scores.pushBack(90);
	scores.pushBack(85);

	std::cout << scores[0] << '\n';			// 90
	std::cout << scores.size() << '\n';		// 2
	std::cout << scores.capacity() << '\n';	// 3

	Array<int> copied{scores};
	copied[0] = 100;
	std::cout << scores[0] << '\n';			// 90

	Array<int> assigned{1};
	assigned = scores;
	std::cout << assigned[1] << '\n';		// 85

	scores.popBack();
	std::cout << scores.size() << '\n';		// 1

	Array<Student> students{2};
	students.pushBack({1, 92});
	students.pushBack({2, 88});

	std::cout << students[0].id << '\n';	// 1
	std::cout << students[0].score << '\n';	// 92

	return 0;
}
```

Built-in types and user-defined types can use the same class template when they support the operations required by the selected member functions. `operator[]` performs unchecked access, and `new T[capacity]{}` requires `T` to be usable as an array element and assignable by the operations above.

