# Functions and Memory

[toc]

##### Functions

A function has a return type, name, parameter list, and body.

```cpp
int add(int a, int b) {
    return a + b;
}

void printHello() {
    std::cout << "Hello\n";
}
```

Declare a function before it is called.

```cpp
int add(int a, int b);   // declaration

int main() {
    return add(1, 2);
}

int add(int a, int b) {  // definition
    return a + b;
}
```

Default arguments are normally written in the declaration.

```cpp
void printValue(int value, int width = 4);
```

##### Header and Source Files

A header file usually contains function declarations that form an interface. A source file contains the corresponding definitions. Each source file that uses the function includes the header.

```cpp
// math_utils.hpp
#pragma once

int add(int a, int b);
```

```cpp
// math_utils.cpp
#include "math_utils.hpp"

int add(int a, int b) {
    return a + b;
}
```

```cpp
// main.cpp
#include "math_utils.hpp"

#include <iostream>

int main() {
    std::cout << add(2, 3) << '\n';
    return 0;
}
```

Each `.cpp` file is compiled separately. Including the same header in both files keeps the declaration consistent with the definition. 

Do not include a `.cpp` file; compile and link it instead. Ordinary non-`inline` functions should normally have one definition in the program. Header-defined `inline` functions and templates are covered in their dedicated sections.

##### Function Parameters

A **parameter** is a named input in a function declaration or definition. An **argument** is the concrete value or expression supplied by the caller.

```cpp
int add(int a, int b) {  // a and b are parameters
    return a + b;
}

int result = add(2, 3);  // 2 and 3 are arguments
```

By default, arguments are passed by value. The parameter receives a copy, so modifying it does not change the original argument.

```cpp
void increment(int value) {
    ++value;
}

int number = 5;
increment(number);

std::cout << number << '\n';  // 5
```

Pass by reference can modify the caller's object.

```cpp
void increment(int& value) {
    ++value;
}
```

Pass by const reference avoids copying and prevents modification.

```cpp
void printName(const std::string& name) {
    std::cout << name << '\n';
}
```

Use a pointer parameter when `nullptr` is a meaningful state or pointer arithmetic is required.

```cpp
void reset(int* value) {
    if (value != nullptr) {
        *value = 0;
    }
}
```

Practical rule:

| Need | Preferred Parameter |
| --- | --- |
| Small independent value | `T value` |
| Read a large object | `const T& value` |
| Modify a required object | `T& value` |
| Optional object | `T* value` |

##### Function Features

Returning by value is normally efficient because compilers apply copy elision and move semantics.

```cpp
std::string makeGreeting() {
    return "Hello";
}
```

A function defined inside a class body is implicitly `inline`. `inline` also allows identical definitions in multiple translation units, which is useful for small header-defined functions.

```cpp
inline int square(int x) {
    return x * x;
}
```

Recursion requires a base case.

```cpp
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

A lambda is an unnamed function.

```cpp
auto add = [](int a, int b) {
    return a + b;
};
```

Capture surrounding variables with `[]`.

```cpp
int scale = 3;

auto multiply = [scale](int x) {
    return scale * x;
};

auto modifyScale = [&scale]() {
    ++scale;
};
```

| Capture | Meaning |
| --- | --- |
| `[]` | Capture nothing |
| `[x]` | Capture `x` by value |
| `[&x]` | Capture `x` by reference |
| `[=]` | Capture used local variables by value |
| `[&]` | Capture used local variables by reference |

Avoid returning a lambda that holds references to local variables that have already been destroyed.

##### Math and Randomness

Use `<cmath>` for mathematical functions.

```cpp
#include <cmath>

 double x = 9.0;
 double root = std::sqrt(x);
 double power = std::pow(2.0, 3.0);
 double angle = std::sin(3.1415926 / 2.0);
 double rounded = std::round(3.6);
 double lower = std::floor(3.6);
 double upper = std::ceil(3.2);
 double absolute = std::abs(-5.0);
```

Floating-point values are approximate. Do not usually compare them with exact equality.

```cpp
bool almostEqual(double a, double b, double epsilon = 1e-9) {
    return std::abs(a - b) < epsilon;
}
```

Use `<random>` instead of `rand()` for modern random-number generation.

```cpp
#include <random>

std::mt19937 engine{std::random_device{}()};
std::uniform_int_distribution<int> distribution(1, 6);
int dice = distribution(engine);
```

##### Arrays

An array is a sequence of objects of the **same type** that occupy a **contiguous area** of memory.

A built-in array has fixed size.

```cpp
int values[5] = {1, 2, 3, 4, 5};
// int values[] = {1, 2, 3, 4, 5};

std::cout << values[0] << '\n';	// 1
std::cout << values[4] << '\n';	// 5
```

For a one-dimensional built-in array, `sizeof` gives the total storage occupied by the array. The element count and the address of the first element can also be obtained while the array type is preserved.

```cpp
int values[] = {10, 20, 30, 40, 50};

// std::size_t is an unsigned integer type 
// used to represent object sizes and array indices
std::size_t byte_size = sizeof(values);
std::size_t length = sizeof(values) / sizeof(values[0]);
int* first_address = values;

std::cout << byte_size << '\n';
std::cout << length << '\n';
std::cout << static_cast<const void*>(first_address) << '\n';
```

In most expressions, the array name is converted to a pointer to its first element, so `values` and `&values[0]` identify the same address. The `sizeof` expressions above work only before the array has decayed to a pointer.

C++ does not automatically check built-in array bounds.

```cpp
for (std::size_t i = 0; i < 5; ++i) {
    std::cout << values[i] << '\n';
}
```

When passed to a function, a built-in array usually decays to a pointer and loses its size.

```cpp
void printValues(const int* values, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << values[i] << '\n';
    }
}
```

**Bubble sort** repeatedly compares adjacent elements and swaps them when they are in the wrong order. After each pass, the largest unsorted element moves to the end of the unsorted range. If a pass performs no swaps, the array is already sorted.

```cpp
#include <cstddef>
#include <iostream>

// Sorts the array in ascending order using bubble sort
void bubbleSort(int values[], std::size_t size) {
    // Shrinks the unsorted range after each pass
    for (std::size_t end = size; end > 1; --end) {
        // Tracks whether this pass made any swaps
        bool swapped = false;

        // Compares each adjacent pair in the unsorted range
        for (std::size_t i = 0; i + 1 < end; ++i) {
            if (values[i] > values[i + 1]) {
                int temp = values[i];
                values[i] = values[i + 1];
                values[i + 1] = temp;

                swapped = true;
            }
        }

        // No swaps means the array is already sorted
        if (!swapped) {
            break;
        }
    }
}

int main() {
    int values[] = {5, 1, 4, 2, 8};
    const std::size_t size = sizeof(values) / sizeof(values[0]);

    bubbleSort(values, size);

    for (const int value : values) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}
```

Multidimensional array:

```cpp
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

```cpp
int matrix[][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

```cpp
int matrix[2][3] = {
    1, 2, 3,
    4, 5, 6
};
```

```cpp
int matrix[][3] = {
    1, 2, 3,
    4, 5, 6
};
```

```cpp
int matrix[2][3]{};

matrix[0][0] = 1;
matrix[0][1] = 2;
matrix[0][2] = 3;
matrix[1][0] = 4;
matrix[1][1] = 5;
matrix[1][2] = 6;
```

For a two-dimensional built-in array, `sizeof` can be used to obtain the row count and column count while the array type is preserved.

```cpp
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// Gets the number of rows
std::size_t rows = sizeof(matrix) / sizeof(matrix[0]);
// Gets the number of columns
std::size_t columns = sizeof(matrix[0]) / sizeof(matrix[0][0]);

// Points to the first row
int (*first_row_address)[3] = matrix;
// Points to the first element
int* first_element_address = &matrix[0][0];

std::cout << rows << '\n';
std::cout << columns << '\n';

// Prints the address of the first row
std::cout << static_cast<const void*>(first_row_address) << '\n';
// Prints the address of the first element
std::cout << static_cast<const void*>(first_element_address) << '\n';
```

In most expressions, `matrix` is converted to a pointer to its first row. `&matrix[0][0]` is the address of the first `int` element. Both addresses have the same numeric location but different pointer types.

##### Strings

A C-style string is a null-terminated character array. Its storage is an array whose capacity must be managed explicitly.

```cpp
#include <cstring>

char c_text[] = "hello";   // {'h','e','l','l','o','\0'}
std::size_t length = std::strlen(c_text);
```

A C++ string is represented by `std::string`, which manages its character storage automatically.

```cpp
#include <string>

std::string cpp_text = "hello";
```

| C-style string | `std::string` |
| --- | --- |
| Null-terminated character array | Standard-library class |
| Fixed array capacity | Resizable managed storage |
| Operations use functions such as those in `<cstring>` | Operations use member functions and operators |
| Buffer size and termination require explicit care | Storage and termination are managed automatically |

Prefer `std::string` for ordinary string handling. Its operations, conversions, and string streams are covered in `Standard Library.md`.

##### Pointers

A pointer stores an address.

```cpp
int value = 10;
int* pointer = &value;

std::cout << pointer << '\n';   // address
std::cout << *pointer << '\n';  // pointed-to value

*pointer = 20;
```

Use `nullptr` for a null pointer.

```cpp
int* pointer = nullptr;

if (pointer != nullptr) {
    std::cout << *pointer << '\n';
}
```

Pointer constness:

```cpp
int a = 1;
int b = 2;

const int* p1 = &a;       // pointer to const int
int* const p2 = &a;       // const pointer to int
const int* const p3 = &a; // const pointer to const int
```

Object member access:

```cpp
struct Point {
    double x;
    double y;
};

Point point{1.0, 2.0};
Point* point_ptr = &point;

point_ptr->x = 3.0;       // equivalent to (*point_ptr).x
```

Pointer arithmetic is mainly appropriate for contiguous arrays. Do not dereference null, dangling, or out-of-range pointers.

##### References

A reference is an alias for an existing object and must be initialized.

```cpp
int value = 10;
int& reference = value;

reference = 20;
std::cout << value << '\n';
```

A const reference can bind to temporary values.

```cpp
const std::string& text = std::string{"hello"};
```

| Reference | Main Use |
| --- | --- |
| `T&` | Modify an existing object |
| `const T&` | Read without copying |
| `T&&` | Bind to temporary objects and support move semantics |

For basic review, understand `T&&` as an rvalue reference used by move-aware code. Most direct uses appear in library or generic code.

##### Dynamic Memory and RAII

Manual allocation:

```cpp
int* value = new int{10};
delete value;
value = nullptr;
```

Dynamic array:

```cpp
std::size_t size = 5;
int* values = new int[size]{};

delete[] values;
values = nullptr;
```

Common errors include memory leaks, double deletion, use-after-free, and mismatching `new[]` with `delete`.

Modern C++ uses Resource Acquisition Is Initialization (RAII): a resource is owned by an object and released automatically by its destructor. Prefer standard containers for dynamic sequences and the ownership types described in `Standard Library.md` instead of manual `new` and `delete`.

##### Structs, Enums, and Unions

A `struct` groups related data.

```cpp
struct Point {
    double x{};
    double y{};

    double squaredNorm() const {
        return x * x + y * y;
    }
};

Point point{1.0, 2.0};
```

Access defaults and constructor initialization are covered with classes in `OOP and Advanced C++.md`.

Prefer scoped enumerations.

```cpp
enum class State {
    Idle,
    Running,
    Failed
};

State state = State::Running;
```

A union stores different members in the same memory. Only one member is normally active at a time.

```cpp
union Number {
    int integer;
    float decimal;
};
```

For type-safe alternatives, prefer `std::variant` when available.

##### Date and Time

C-style time utilities are provided by `<ctime>`.

```cpp
#include <ctime>

std::time_t now = std::time(nullptr);
std::cout << std::ctime(&now);
```

Modern duration measurement uses `<chrono>`.

```cpp
#include <chrono>

const auto start = std::chrono::steady_clock::now();
// work
const auto end = std::chrono::steady_clock::now();

const auto milliseconds =
    std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

std::cout << milliseconds.count() << " ms\n";
```

Use `steady_clock` for elapsed time because it is monotonic.
