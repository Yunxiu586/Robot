# Basic Syntax

[toc]

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

##### Comments, Identifiers, and Keywords

```cpp
// Single-line comment

/*
   Multi-line comment
*/
```

An identifier may contain letters, digits, and underscores, but it cannot start with a digit or use a reserved keyword.

```cpp
int item_count = 3;    // valid
int index = 0;         // valid
// int 2items = 2;     // invalid
// int class = 1;      // invalid: class is a keyword
```

Prefer descriptive names and a consistent style.

##### Variables and Fundamental Types

```cpp
bool ready = true;
char grade = 'A';					// single char
char str1[] = "Hello World!"		// C-string array, ends with '\0', size = len+1
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

##### Initialization and Aliases

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

`extern` declares a variable or function whose definition is provided elsewhere in the program.

```cpp
// config.cpp
int max_iterations = 100;

// main.cpp
extern int max_iterations;
```

`register` is obsolete in modern C++ and should not be used.

##### Constants and Qualifiers

```cpp
const double pi = 3.1415926;          // cannot be modified
constexpr int max_size = 100;         // compile-time constant
volatile bool hardware_flag = false;  // value may change outside normal code flow
```

Use `const` whenever an object should not be modified. Use `constexpr` when the value or function can be evaluated at compile time.

```cpp
constexpr int square(int x) {
    return x * x;
}

constexpr int area = square(5);
```

`volatile` is mainly for low-level hardware access. It does not make code thread-safe.

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

##### Input and Output

```cpp
#include <iostream>
#include <string>

int main() {
    int age{};
    std::string name;

    std::cout << "Name: ";
    std::getline(std::cin, name);

    std::cout << "Age: ";
    std::cin >> age;

    std::cout << name << " is " << age << " years old\n";
}
```

| Stream | Purpose |
| --- | --- |
| `std::cin` | Standard input |
| `std::cout` | Normal output |
| `std::cerr` | Error output, usually unbuffered |
| `std::clog` | Log output, usually buffered |

`'\n'` is a newline character. Inserting it writes the newline character to the output sequence but does not itself request a flush.

`std::endl` is a standard output-stream manipulator. For an output stream `os`, its effect is equivalent to

```cpp
os.put(os.widen('\n'));
os.flush();
```

Therefore, the two forms differ as follows:

```cpp
std::cout << '\n';          // inserts a newline
std::cout << std::endl;     // inserts a newline, then flushes the stream
```

Use `'\n'` for ordinary line breaks. Use `std::endl` when a newline followed by an immediate flush is specifically required. A stream can also be flushed without inserting a newline by using `std::flush`.

When `std::getline` follows `operator>>`, consume the remaining newline first.

```cpp
#include <limits>

std::cin >> age;
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
std::getline(std::cin, name);
```

##### Quick Review

```cpp
#include <iostream>
#include <string>

int main() {
    constexpr int pass_score = 60;
    std::string name;
    int score{};

    std::getline(std::cin, name);
    std::cin >> score;

    const bool passed = score >= pass_score;
    std::cout << name << (passed ? " passed\n" : " failed\n");

    return 0;
}
```
