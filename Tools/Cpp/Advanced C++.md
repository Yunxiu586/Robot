# Advanced C++

[toc]

##### Templates

A function template works with multiple types.

```cpp
template <typename T>
T maximum(const T& a, const T& b) {
    return a < b ? b : a;
}
```

```cpp
int integer_max = maximum(3, 5);
double double_max = maximum(2.5, 1.5);
```

A class template creates a family of types.

```cpp
template <typename T>
class Box {
public:
    explicit Box(T value) : value_{std::move(value)} {}

    const T& value() const {
        return value_;
    }

private:
    T value_;
};

Box<int> integer_box{10};
Box<std::string> string_box{"Hello"};
```

Template definitions are normally placed in header files because the compiler must see the full definition when instantiating them.

##### Exception Handling

Use exceptions for errors that cannot be handled locally and are not part of normal control flow.

```cpp
#include <stdexcept>

int divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument{"division by zero"};
    }
    return a / b;
}
```

```cpp
try {
    std::cout << divide(10, 0) << '\n';
} catch (const std::invalid_argument& error) {
    std::cerr << error.what() << '\n';
} catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
}
```

Catch exceptions by `const` reference. Throw objects by value.

Common standard exceptions:

| Exception | Typical Meaning |
| --- | --- |
| `std::invalid_argument` | Invalid function argument |
| `std::out_of_range` | Invalid index or key range |
| `std::runtime_error` | General runtime failure |
| `std::logic_error` | Programming-logic failure |
| `std::bad_alloc` | Dynamic allocation failed |

RAII ensures local resources are released during stack unwinding.

Use `noexcept` when a function is guaranteed not to throw.

```cpp
void reset() noexcept {
    // non-throwing operation
}
```

##### Files and Streams

Write a text file:

```cpp
#include <fstream>

std::ofstream output{"result.txt"};
if (!output) {
    throw std::runtime_error{"cannot open output file"};
}

output << "name score\n";
output << "Alice " << 95 << '\n';
```

Read a text file:

```cpp
#include <fstream>
#include <string>

std::ifstream input{"result.txt"};
if (!input) {
    throw std::runtime_error{"cannot open input file"};
}

std::string line;
while (std::getline(input, line)) {
    std::cout << line << '\n';
}
```

Open modes:

| Mode | Meaning |
| --- | --- |
| `std::ios::in` | Read |
| `std::ios::out` | Write |
| `std::ios::app` | Append |
| `std::ios::trunc` | Replace existing content |
| `std::ios::binary` | Binary mode |

Streams close automatically when their objects are destroyed. Explicit `close()` is only needed when the file must close earlier.

Binary I/O:

```cpp
int value = 42;
std::ofstream output{"value.bin", std::ios::binary};
output.write(reinterpret_cast<const char*>(&value), sizeof(value));
```

Raw binary serialization is not portable across different architectures, compilers, padding rules, or endianness. Define a stable file format for portable data exchange.

##### Preprocessor

The preprocessor runs before compilation.

```cpp
#include <iostream>
#define VERSION 2
```

Prefer `constexpr`, inline functions, and templates over function-like macros.

```cpp
#define SQUARE_BAD(x) x * x
constexpr int squareGood(int x) { return x * x; }
```

`SQUARE_BAD(1 + 2)` expands incorrectly. Macros also ignore normal scope and type checking.

Conditional compilation:

```cpp
#ifdef DEBUG
std::cout << "debug information\n";
#endif
```

```cpp
#if VERSION >= 2
// compiled when VERSION is at least 2
#endif
```

Useful predefined macros include `__FILE__`, `__LINE__`, `__DATE__`, and `__TIME__`.
