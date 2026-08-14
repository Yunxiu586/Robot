# Basic Syntax

[toc]

### Program Basics

##### Program Structure

A C++ program starts from `main()`.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, C++\n";
    return 0;
}
```

| Part | Purpose |
| --- | --- |
| `#include <iostream>` | Imports declarations for stream input and output |
| `int main()` | Program entry point |
| `{ ... }` | Defines a scope |
| `;` | Ends most statements |
| `return 0` | Reports successful termination |

C++ is case-sensitive. `value`, `Value`, and `VALUE` are different names.
##### Comments

```cpp
// Single-line comment

/*
   Multi-line comment
*/
```

##### Identifiers and Keywords

An identifier may contain letters, digits, and underscores, but it cannot start with a digit or use a reserved keyword.

```cpp
int item_count = 3;    // valid
int index = 0;         // valid
// int 2items = 2;     // invalid
// int class = 1;      // invalid: class is a keyword
```

Prefer descriptive names and a consistent style.
### Types and Variables

##### Fundamental Types

```cpp
bool ready = true;
char grade = 'A';					// single char
char str1[] = "Hello World!";		// C-string array, ends with '\0', size = len+1
short small_value = 10;
int count = 100;
long long large_value = 1'000'000'000LL;	// LL specifies long long literal type
unsigned int non_negative = 42U;	// U specifies unsigned literal type
float ratio = 0.5F;					// F specifies float literal, otherwise double
double distance = 3.14;				// double by default
long double precise_value = 3.14L;	// L specifies long double literal
double a = 1.5e3;   				// 1500
double b = 2E-4;    				// 0.0002
```

| Category | Common Types | Notes |
| --- | --- | --- |
| Boolean | `bool` | `true` or `false` |
| Character | `char` | Stores a character or small integer |
| Integer | `short`, `int`, `long`, `long long` | Exact width is implementation-dependent |
| Unsigned integer | `unsigned int`, etc. | Cannot represent negative values |
| Floating point | `float`, `double`, `long double` | `double` is the usual default |
| No value | `void` | Used for functions with no return value |

Use `sizeof` to inspect storage size.

```cpp
std::cout << sizeof(bool) << '\n';			// 1
std::cout << sizeof(char) << '\n';			// 1
std::cout << sizeof(short) << '\n';     	// 2
std::cout << sizeof(int) << '\n';       	// 4
std::cout << sizeof(long) << '\n';      	// 4 on Windows, 8 on 64-bit Linux
std::cout << sizeof(long long) << '\n'; 	// 8
std::cout << sizeof(float) << '\n';     	// 4
std::cout << sizeof(double) << '\n';    	// 8
std::cout << sizeof(long double) << '\n';	// 8 on Windows， 16 on Linux
```

For fixed-width integers, use `<cstdint>`.

```cpp
#include <cstdint>

std::int32_t id = 100;
std::uint64_t timestamp = 0;
```
##### Escape Sequences

Escape sequences represent special characters inside character and string literals. Each escape sequence begins with a backslash (`\`).

| escape sequence | meaning               |
| --------------- | --------------------- |
| `\n`            | newline               |
| `\t`            | horizontal tab        |
| `\r`            | carriage return       |
| `\\`            | backslash             |
| `\'`            | single quotation mark |
| `\"`            | double quotation mark |
| `\0`            | null character        |

```cpp
std::cout << "Name:\tAlice\n";
std::cout << "Path: C:\\Users\\Alice\n";
std::cout << "She said, \"Hello.\"\n";
```

A backslash must itself be escaped as `\\`. Similarly, quotation marks must be escaped when they would otherwise terminate the surrounding literal.
##### Initialization

Prefer initialization when a variable is declared.

```cpp
int a = 10;
int b(20);
int c{30};            // list initialization
int zero{};           // initialized to 0
```

Brace initialization prevents many narrowing conversions.

```cpp
double x = 3.8;
int y = static_cast<int>(x);   // explicit conversion, y == 3
// int z{x};                   // error: narrowing conversion
```

##### Type Deduction and Aliases

`auto` asks the compiler to infer the type.

```cpp
auto count = 10;          // int
auto length = 2.5;        // double
auto name = std::string{"Alice"};
```

Use `auto` when the type is obvious or unnecessarily long, not when it hides important meaning.

```cpp
using Index = std::size_t;
typedef unsigned long OldStyleId;
```

`using` is the preferred modern syntax for type aliases.
##### Scope and Lifetime

A name is visible only within its scope.

```cpp
int global_value = 1;     // global scope

void update() {
    int local_value = 2;  // block scope

    if (local_value > 0) {
        int temporary = 3;
    }
    // temporary is no longer visible here
}
```

Avoid global mutable variables. Pass data through parameters or store it inside objects.

A local `static` variable is initialized once and keeps its value between calls.

```cpp
int nextId() {
    static int id = 0;
    return ++id;
}
```

An `extern` declaration can refer to an entity defined elsewhere in the program. A declaration with `extern` and no initializer or function body is not a definition.

```cpp
// config.cpp
int max_iterations = 100;

// main.cpp
extern int max_iterations;
```

`register` is obsolete in modern C++ and should not be used.
##### Declaration Specifiers and Qualifiers

Common modern C++ declaration specifiers and declarator qualifiers are summarized below.

| Syntax | Category | Common Use |
| --- | --- | --- |
| `const` | cv-qualifier | Prevents modification through the const-qualified type; after a non-static member function, makes the implicit object const-qualified |
| `volatile` | cv-qualifier | Marks accesses that may be affected by implementation-external conditions; mainly used for low-level hardware access |
| `constexpr` | declaration specifier | Declares a variable or function usable in constant evaluation when its requirements are satisfied |
| `consteval` | declaration specifier | Declares an immediate function whose potentially evaluated calls must produce constant expressions |
| `constinit` | declaration specifier | Requires static or thread storage duration variables to have static initialization; does not make them const |
| `static` | storage-class specifier | Gives static storage duration to local variables; also declares class-wide static members or namespace-scope internal linkage depending on context |
| `thread_local` | storage-class specifier | Gives a variable thread storage duration, with a separate object for each thread |
| `extern` | storage-class specifier | Declares an entity that can be defined elsewhere; commonly used for declarations with external linkage |
| `mutable` | storage-class specifier | Allows a non-static data member to be modified even through a const-qualified object |
| `inline` | declaration specifier | Permits an inline function or variable to have identical definitions in multiple translation units |
| `virtual` | function specifier | Declares a non-static member function for virtual dispatch |
| `explicit` | function specifier | Prevents constructors and conversion functions from participating in unwanted implicit conversions |
| `friend` | declaration specifier | Grants a function or class access to private and protected members |
| `noexcept` | exception specification | Declares whether a function is non-throwing |
| `&` / `&&` | ref-qualifier | Restricts a non-static member function to lvalue or rvalue objects |
| `override` | virt-specifier | Requires a virtual member function to override a base-class virtual function |
| `final` | virt-specifier | Prevents further overriding of a virtual function, or further derivation from a class |
| `= default` | function definition form | Requests a compiler-generated definition for an eligible function |
| `= delete` | deleted function definition | Declares a function as deleted so it cannot be used |
| `= 0` | pure-specifier | Declares a virtual function as pure virtual |

`override` and `final` are identifiers with special meaning rather than ordinary keywords. `&`, `&&`, `= default`, `= delete`, and `= 0` are included because they commonly appear in modern declarations.

```cpp
const double pi = 3.1415926;
constexpr int max_size = 100;
constinit static int startup_count = 0;
thread_local int thread_count = 0;

constexpr int square(int x) {
    return x * x;
}

constexpr int area = square(5);
```

`volatile` does not provide atomicity or thread synchronization.
### Expressions and Control Flow

##### Operators

Arithmetic operators:

```cpp
int a = 10;
int b = 3;

int sum = a + b;
int difference = a - b;
int product = a * b;
int quotient = a / b;    // 3: integer division
int remainder = a % b;   // 1
```

Assignment and increment operators:

```cpp
int x = 5;
x += 2;
x -= 1;
x *= 3;
x /= 2;
x %= 2;
++x;       // increment first
x++;       // use old value, then increment
```

Comparison and logical operators:

```cpp
bool equal = (a == b);
bool different = (a != b);
bool inside = (a >= 0 && a < 100);	// AND
bool valid = ready || count > 0;	// OR
bool stopped = !ready;				// NOT
```

Bitwise operators work on integer bits.

```cpp
unsigned int flags = 0b0011U;
flags |= 0b0100U;       // set bits, flags = 0b0111
flags &= ~0b0010U;      // clear bits, flags = 0b0101
bool enabled = (flags & 0b0001U) != 0U;
```

Conditional operator:

```cpp
int absolute = x >= 0 ? x : -x;
```

Member and scope operators:

| Operator | Meaning |
| --- | --- |
| `.` | Access a member through an object |
| `->` | Access a member through a pointer |
| `::` | Access a namespace, class, or global scope |
| `&` | Address-of operator or reference declaration |
| `*` | Dereference operator or pointer declaration |

Use parentheses when operator precedence is not immediately clear.
##### Conditional Statements

```cpp
int score = 85;

if (score >= 90) {
    std::cout << "A\n";
} else if (score >= 80) {
    std::cout << "B\n";
} else {
    std::cout << "C or below\n";
}
```

`switch` is useful for discrete integral or enumeration values.

```cpp
int choice = 2;

switch (choice) {
    case 1:
        std::cout << "Start\n";
        break;
    case 2:
        std::cout << "Settings\n";
        break;
    case 3:
        std::cout << "Exit\n";
        break;
    default:
        std::cout << "Invalid choice\n";
        break;
}
```

A missing `break` causes execution to continue into the next case. Use `[[fallthrough]]` when that behavior is intentional.
##### Loops

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << '\n';
}
```

Nested loops can be used for two-dimensional iteration. The following example prints a 9 × 9 multiplication table.

```cpp
for (int i = 1; i <= 9; ++i) {
    for (int j = 1; j <= i; ++j) {
        std::cout << j << " * " << i << " = " << i * j << '\t';
    }
    std::cout << '\n';
}
```

```cpp
int i = 0;
while (i < 5) {
    ++i;
}
```

```cpp
int input = 0;
do {
    std::cin >> input;
} while (input < 0);
```

Range-based loops are preferred for containers and arrays.

```cpp
int values[] = {1, 2, 3};

for (int value : values) {
    std::cout << value << '\n';
}
```

Use references to modify elements or avoid copies.

```cpp
for (int& value : values) {
    value *= 2;
}

for (const int& value : values) {
    std::cout << value << '\n';
}
```

`break` exits the nearest loop. `continue` skips the rest of the current iteration. `goto` transfers control to a labeled statement and should be used sparingly.

```cpp
for (int row = 1; row <= 3; ++row) {
    for (int column = 1; column <= 5; ++column) {
        if (column == 2) {
            continue;		// Skip the current iteration.
        }

        if (column == 5) {
            break;     		// Exit the inner loop.
        }

        if (row == 3 && column == 4) {
            goto finished;  // Exit both loops.
        }

        std::cout << row << ", " << column << '\n';
    }
}

finished:
std::cout << "Finished\n";
```
### Error Handling

##### Exceptions

Exception handling transfers control from a point where an exception is thrown to a matching handler. Use `try` for code that may throw, `throw` to signal an error, and `catch` to handle it.

```cpp
#include <iostream>
#include <stdexcept>

int divide(int dividend, int divisor) {
    if (divisor == 0) {
        throw std::invalid_argument{"division by zero"};
    }

    return dividend / divisor;
}

int main() {
    try {
        std::cout << divide(10, 0) << '\n';
    } catch (const std::invalid_argument& error) {
        std::cerr << error.what() << '\n';
    }
}
```

Throw exception objects by value and catch them by `const` reference. Standard exception types derive from `std::exception`.

When an exception propagates out of a block, automatic objects already constructed in that block are destroyed during stack unwinding.
### Input and Output

##### Standard Streams

`<iostream>` provides the standard character streams. `operator<<` performs formatted output, `operator>>` performs formatted input, and `std::getline` reads a complete line.

| Stream | Purpose |
| --- | --- |
| `std::cin` | Standard input |
| `std::cout` | Standard output |
| `std::cerr` | Error output |
| `std::clog` | Log output |

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    int age{};

    std::getline(std::cin, name);
    std::cin >> age;

    std::cout << name << " is " << age << " years old\n";
}
```

`'\n'` inserts a newline. `std::endl` inserts a newline and then flushes the output stream, so prefer `'\n'` for ordinary line breaks.

##### File Streams

`<fstream>` provides the standard file stream types.

| Type | Purpose | Default mode |
| --- | --- | --- |
| `std::ifstream` | File input | `std::ios::in` |
| `std::ofstream` | File output | `std::ios::out` |
| `std::fstream` | File input and output | `std::ios::in | std::ios::out` |

File open modes are bitmask flags and can be combined with `|`.

| Mode | Effect |
| --- | --- |
| `std::ios::in` | Open for input |
| `std::ios::out` | Open for output |
| `std::ios::ate` | Seek to the end immediately after opening |
| `std::ios::app` | Seek to the end before each write |
| `std::ios::trunc` | Discard existing contents when opening |
| `std::ios::binary` | Open in binary mode |

Without `std::ios::binary`, the file is opened in text mode. With its default mode, `std::ofstream` truncates an existing file. Use `std::ios::app` when new output should be appended.

Write a text file with `operator<<`:

```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream output{"scores.txt"};

    if (!output) {
        std::cerr << "cannot open file\n";
        return 1;
    }

    output << "Alice " << 95 << '\n';
}
```

Constructing a file stream with a filename opens it immediately. Use `open()` when construction and opening need to be separate.

```cpp
std::ofstream output;
output.open("scores.txt", std::ios::out | std::ios::app);
```

Read formatted values with `operator>>`, or read complete lines with `std::getline`.

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream input{"scores.txt"};

    if (!input) {
        std::cerr << "cannot open file\n";
        return 1;
    }

    std::string name;
    int score{};

    while (input >> name >> score) {
        std::cout << name << ' ' << score << '\n';
    }
}
```

```cpp
std::string line;
while (std::getline(input, line)) {
    std::cout << line << '\n';
}
```

`close()` closes the associated file. File streams also close their files when destroyed, so an explicit `close()` is normally needed only when the file must be closed before the stream leaves scope or the stream will be reused.

```cpp
output.close();
```

##### Binary I/O

Use `std::ios::binary` with `read()` and `write()` when exact byte-oriented I/O is required.

```cpp
#include <cstdint>
#include <fstream>
#include <iostream>

int main() {
    const std::uint32_t written{42};

    {
        std::ofstream output{"data.bin", std::ios::binary};
        if (!output) {
            return 1;
        }

        output.write(reinterpret_cast<const char*>(&written), sizeof written);
    }

    std::uint32_t read{};
    std::ifstream input{"data.bin", std::ios::binary};

    if (!input) {
        return 1;
    }

    input.read(reinterpret_cast<char*>(&read), sizeof read);

    if (input) {
        std::cout << read << '\n';		// 42
    }
}
```

This binary example stores the native object representation. Portable file formats should define byte order and field representation explicitly instead of dumping pointers, `std::string`, or arbitrary class objects directly.
