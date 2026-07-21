# Basic Syntax and Control Flow

[toc]

##### Program Structure and Compilation

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
int robot_count = 3;   // valid
int _index = 0;        // valid, but leading underscores are best avoided
// int 2robots = 2;    // invalid
// int class = 1;      // invalid: class is a keyword
```

Prefer descriptive names and a consistent style.

##### Variables and Fundamental Types

```cpp
bool ready = true;
char grade = 'A';
short small_value = 10;
int count = 100;
long long large_value = 1'000'000'000LL;
unsigned int non_negative = 42U;
float ratio = 0.5F;
double distance = 3.14;
long double precise_value = 3.14L;
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
std::cout << sizeof(int) << '\n';
std::cout << sizeof(double) << '\n';
```

For fixed-width integers, use `<cstdint>`.

```cpp
#include <cstdint>

std::int32_t id = 100;
std::uint64_t timestamp = 0;
```

##### Initialization, `auto`, and Type Aliases

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
auto name = std::string{"robot"};
```

Use `auto` when the type is obvious or unnecessarily long, not when it hides important meaning.

```cpp
using Index = std::size_t;
typedef unsigned long OldStyleId;
```

`using` is the preferred modern syntax for type aliases.

##### Scope, Lifetime, and Storage Duration

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

`extern` declares a variable or function defined in another translation unit.

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
++x;       // increment first
x++;       // use old value, then increment
```

Comparison and logical operators:

```cpp
bool equal = (a == b);
bool different = (a != b);
bool inside = (a >= 0 && a < 100);
bool valid = ready || count > 0;
bool stopped = !ready;
```

Bitwise operators work on integer bits.

```cpp
unsigned int flags = 0b0011;
flags |= 0b0100;       // set bits
flags &= ~0b0010;      // clear bits
bool enabled = (flags & 0b0001) != 0;
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
enum class Mode { Idle, Run, Walk };
Mode mode = Mode::Run;

switch (mode) {
    case Mode::Idle:
        break;
    case Mode::Run:
        std::cout << "Run\n";
        break;
    case Mode::Walk:
        std::cout << "Walk\n";
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

`break` exits the nearest loop. `continue` skips the rest of the current iteration.

```cpp
for (int i = 0; i < 10; ++i) {
    if (i == 8) {
        break;
    }
    if (i % 2 == 0) {
        continue;
    }
    std::cout << i << '\n';
}
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

`'\n'` only inserts a newline. `std::endl` inserts a newline and flushes the stream, so avoid unnecessary `std::endl` in performance-sensitive loops.

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
