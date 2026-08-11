# Templates

[toc]

Templates support generic programming by defining functions and classes in terms of parameters. A template is instantiated with concrete template arguments when a corresponding function or type is needed.

### Function Templates

##### Basic Syntax

A function template defines a family of functions.

```cpp
template <typename T>
T maximum(const T& first, const T& second) {
    return first < second ? second : first;
}

int integer_max = maximum(3, 5);          // T is deduced as int
double double_max = maximum(2.5, 1.5);   // T is deduced as double
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

##### Deduction

For a function template, template arguments can often be deduced from the function arguments.

```cpp
template <typename T>
T maximum(T first, T second) {
    return first < second ? second : first;
}

int a = maximum(10, 20);             // maximum<int>
double b = maximum<double>(10, 2.5); // T is specified explicitly

// auto c = maximum(10, 2.5);        // Error: T cannot be deduced as both int and double
```

When a template argument is supplied explicitly, ordinary implicit conversions can still apply to the function arguments.

A function template may have more than one template parameter.

```cpp
template <typename T, typename U>
auto add(T first, U second) {
    return first + second;
}

auto result = add(2, 3.5);           // T is int, U is double
```

##### Overloading

Function templates can be overloaded with other templates or non-template functions. Normal overload resolution selects the best viable function; when otherwise indistinguishable, a non-template function is preferred over a function-template specialization.

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

##### Requirements

A template is valid only when the operations used by an instantiated specialization are valid for its template arguments.

```cpp
template <typename T>
const T& minimum(const T& first, const T& second) {
    return second < first ? second : first; // T must support comparison with <
}
```

For user-defined types, the required operation can be provided by the type itself.

```cpp
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


##### Specialization

An explicit specialization provides a definition for a specific set of template arguments.

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
Student second{1, "Bob"};
bool same = sameValue(first, second);
```

The primary template remains unchanged; the specialization is selected only for `Student`.

### Class Templates

##### Basic Syntax

A class template defines a family of classes.

```cpp
#include <string>

template <typename T>
class Box {
public:
    explicit Box(const T& value)
        : value_{value} {}

    const T& value() const {
        return value_;
    }

private:
    T value_;
};

Box<int> integer_box{10};
Box<std::string> string_box{"Hello"};
```

Each specialization is a distinct type.

```cpp
Box<int> first{10};
Box<double> second{3.14};

// first = second; // Error: Box<int> and Box<double> are different types
```

##### Parameters

A class template can have multiple template parameters and default template arguments.

```cpp
template <typename T, typename U = int>
class Pair {
public:
    Pair(T first, U second)
        : first_{first}, second_{second} {}

    T first() const {
        return first_;
    }

    U second() const {
        return second_;
    }

private:
    T first_;
    U second_;
};

Pair<double> first{3.14, 10};              // Pair<double, int>
Pair<int, double> second{1, 2.5};
```

A template parameter does not have to represent a type. A constant value can also be a template parameter.

```cpp
#include <cstddef>

template <typename T, std::size_t N>
class Buffer {
public:
    constexpr std::size_t size() const {
        return N;
    }

private:
    T data_[N]{};
};

Buffer<int, 8> buffer;
```

##### Member Functions

Member functions can be defined inside or outside a class template.

```cpp
template <typename T>
class Holder {
public:
    explicit Holder(T value);
    const T& value() const;

private:
    T value_;
};

template <typename T>
Holder<T>::Holder(T value)
    : value_{value} {}

template <typename T>
const T& Holder<T>::value() const {
    return value_;
}
```

When a member is defined outside the class template, both the template parameter list and the class specialization `Holder<T>` are required.

##### Instantiation

A class-template specialization is formed from concrete template arguments. Definitions of its non-deleted member functions are generally instantiated when they are needed.

```cpp
#include <iostream>

template <typename T>
class Printer {
public:
    explicit Printer(T value)
        : value_{value} {}

    void print() const {
        std::cout << value_ << '\n'; // Requires T to support stream insertion when used
    }

private:
    T value_;
};

Printer<int> printer{42};
printer.print();
```

This allows different members of a class template to impose different requirements on `T`.

##### Object Parameters

A function can accept one specific specialization of a class template.

```cpp
void printBox(const Box<int>& box) {
    std::cout << box.value() << '\n';
}
```

A function template can accept any `Box<T>` specialization.

```cpp
template <typename T>
void printBox(const Box<T>& box) {
    std::cout << box.value() << '\n';
}

Box<int> integer_box{10};
Box<double> double_box{2.5};

printBox(integer_box);
printBox(double_box);
```

A more general function template can accept any type that supports the operations used by the function body.

```cpp
template <typename BoxType>
void showValue(const BoxType& box) {
    std::cout << box.value() << '\n'; // BoxType must provide value()
}
```

##### Inheritance

When deriving from a class template, the base class must denote a concrete specialization or depend on the derived template parameters.

```cpp
template <typename T>
class Base {
protected:
    T value_{};
};

class IntegerBox : public Base<int> {
};

template <typename T>
class DerivedBox : public Base<T> {
};
```

##### Deduction

Class template arguments are commonly written explicitly. Since C++17, they can also be deduced from constructors when suitable deduction information is available.

```cpp
template <typename T, typename U>
class Entry {
public:
    Entry(T key, U value)
        : key_{key}, value_{value} {}

private:
    T key_;
    U value_;
};

Entry<int, double> first{1, 2.5};
Entry second{1, 2.5};              // C++17: Entry<int, double>
```

Class template argument deduction does not change the template itself; it determines the template arguments used to form a specialization.


##### Friends

A friend can be defined inside a class template when it needs access to private members. A common example is stream output.

```cpp
#include <iostream>

template <typename T>
class Value {
public:
    explicit Value(const T& value)
        : value_{value} {}

    friend std::ostream& operator<<(std::ostream& output, const Value& value) {
        return output << value.value_; // Accesses the private member
    }

private:
    T value_;
};

Value<int> value{42};
std::cout << value << '\n';
```

Defining the friend inside the class template keeps this common case concise and makes the corresponding function available for each specialization.

##### Organization

A template definition must normally be visible at the point where a specialization is instantiated. For this reason, template definitions are commonly placed in header files.

```cpp
// box.hpp
#ifndef BOX_HPP
#define BOX_HPP

template <typename T>
class Box {
public:
    explicit Box(T value)
        : value_{value} {}

    const T& value() const {
        return value_;
    }

private:
    T value_;
};

#endif
```

Explicit instantiation can be used when a template implementation should support only a known set of specializations, but the inclusion model is the usual choice for general-purpose templates.
