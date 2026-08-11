# Functions and Arrays

[toc]

### Functions

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

##### Parameters

A **parameter** is an input declared in a function declaration or definition. An **argument** is the concrete value or expression supplied by the caller.

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

int number = 5;
increment(number);

std::cout << number << '\n';	// 6
```

Pass by const reference avoids copying and prevents modification.

```cpp
void printName(const std::string& name) {
    std::cout << name << '\n';
}
```

| Need | Preferred Parameter |
| --- | --- |
| Small independent value | `T value` |
| Optional object | `T* value` |
| Modify a required object | `T& value` |
| Read a large object | `const T& value` |

A **default argument** is used when a trailing argument is omitted. After a parameter has a default argument, each following parameter must also have one.

With separate declaration and definition, place default arguments in the declaration and do not repeat them in the definition.

```cpp
void printValue(int value, int width = 4, char fill = ' ');

void printValue(int value, int width, char fill) {
    std::cout << fill << value << ' ' << width << '\n';
}

printValue(10);
printValue(10, 6);
printValue(10, 6, '0');

// void invalid(int value = 0, int width);  // Error
```

A parameter name may be omitted when the function does not use it. The argument is still required unless the unnamed parameter has a default argument.

```cpp
void printMessage(const std::string& message, int = 0);

void printMessage(const std::string& message, int) {
    std::cout << message << '\n';
}

printMessage("Hello");
printMessage("Hello", 1);
```
##### Overloading

Function overloading reuses one function name for related operations. Overloads are declared in the same scope and differ in parameter count, type, or order. Return type alone cannot distinguish overloads.

```cpp
void func(int value);
void func(double value);
void func(int value, int count);
void func(int value, double scale);
void func(double scale, int value);

// double func(int value);  // Error: differs only by return type
```

Reference types can distinguish overloads.

```cpp
void show(int& value) {
    std::cout << "modifiable: " << value << '\n';
}

void show(const int& value) {
    std::cout << "read-only: " << value << '\n';
}

int value = 10;
const int limit = 20;

show(value);  // modifiable: 10
show(limit);  // read-only: 20
show(30);     // read-only: 30
```

Default arguments can make an overloaded call ambiguous. Avoid such overload sets.

```cpp
void display(int value);
void display(int value, int width = 4);

// display(10);  // Error: ambiguous call
```
##### Return Values

Returning by value is normally efficient because compilers apply copy elision and move semantics.

```cpp
std::string makeGreeting() {
    return "Hello";
}
```
##### Recursion

Recursion requires a base case.

```cpp
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```
##### Lambdas

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
### Arrays

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
### Program Structure

##### Preprocessor

Preprocessor directives begin with `#` and are processed before normal compilation. Common uses are file inclusion, macro definition, and conditional compilation.

`#include` inserts the contents of another file. Angle brackets are normally used for standard headers; quotes are normally used for project headers.

```cpp
#include <iostream>
#include "math_utils.hpp"
```

Macros perform token replacement. Prefer constants, functions, and templates when normal C++ language features can express the same operation.

```cpp
#define SQUARE_BAD(x) x * x

constexpr int square(int value) {
    return value * value;
}

int first = SQUARE_BAD(1 + 2);  // Expands to 1 + 2 * 1 + 2
int second = square(1 + 2);     // 9
```

Conditional directives include or exclude source text according to a preprocessing condition.

```cpp
#ifdef DEBUG
std::cout << "debug information\n";
#endif
```

`#ifndef`, `#define`, and `#endif` are also commonly used to form include guards.
##### Headers and Sources

A header file usually contains declarations that form an interface. A source file contains the corresponding definitions. Do not include a `.cpp` file; compile and link it instead.

A header may be included more than once through direct or indirect inclusion. Use an include guard to prevent repeated inclusion.

```cpp
// math_utils.hpp
#ifndef MATH_UTILS_HPP
#define MATH_UTILS_HPP

namespace math_utils {

int add(int a, int b);

}  // namespace math_utils

#endif  // MATH_UTILS_HPP
```

An include guard uses conditional preprocessing so that the declarations are seen only once in a translation unit. Use a distinct macro name for each header.

In project code, place declarations in a named namespace in the header and their definitions in the same namespace in the source file. The source file should include its matching header first. 

Do not write `using namespace ...;` in a header. Names used only within one source file may be placed in an unnamed namespace in that `.cpp` file.

```cpp
// math_utils.cpp
#include "math_utils.hpp"

namespace math_utils {

int add(int a, int b) {
    return a + b;
}

}  // namespace math_utils
```

```cpp
// main.cpp
#include "math_utils.hpp"

#include <iostream>

int main() {
    std::cout << math_utils::add(2, 3) << '\n';
    return 0;
}
```

Each `.cpp` file is compiled separately. Including the same header in the source file and its users keeps the declaration consistent with the definition.

##### Inline Functions

An `inline` function may have identical definitions in multiple translation units. This allows a small function definition to be placed in a header included by several source files.

```cpp
// math_utils.hpp
#ifndef MATH_UTILS_HPP
#define MATH_UTILS_HPP

namespace math_utils {

inline int square(int value) {
	return value * value;
}

}  // namespace math_utils

#endif  // MATH_UTILS_HPP
```

```cpp
// area.cpp
#include "math_utils.hpp"

int squareArea(int side) {
	return math_utils::square(side);
}
```

```cpp
// main.cpp
#include "math_utils.hpp"

#include <iostream>

int main() {
	std::cout << math_utils::square(5) << '\n';
	return 0;
}
```

Both source files include the header, so the definition of `square` appears in both translation units. `inline` permits these identical definitions; without it, defining a non-`inline` function in the header would cause a multiple-definition error when the program is linked.

A member function defined inside a class body is implicitly `inline`. The keyword does not require the compiler to expand the function call; inlining as an optimization is decided by the compiler.

### Utilities

##### Math and Randomness

Use `<cmath>` for mathematical functions.

```cpp
#include <cmath>

 double x = 9.0;
 double root = std::sqrt(x);        // 3.0
 double power = std::pow(2.0, 3.0); // 8.0
 double angle = std::sin(3.1415926 / 2.0);
 double rounded = std::round(3.6);  // 4.0
 double lower = std::floor(3.6);    // 3.0
 double upper = std::ceil(3.2);     // 4.0
 double absolute = std::abs(-5.0);	// 5.0
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
