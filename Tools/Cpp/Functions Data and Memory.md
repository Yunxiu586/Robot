# Functions, Data, and Memory

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

Function overloading allows the same name with different parameter lists.

```cpp
int maxValue(int a, int b);
double maxValue(double a, double b);
```

The return type alone cannot distinguish overloads.

##### Value, Reference, and Pointer Parameters

Pass by value creates a copy.

```cpp
void increment(int value) {
    ++value;
}
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

##### Return Values, `inline`, Recursion, and Lambdas

Returning by value is normally efficient because compilers apply copy elision and move semantics.

```cpp
std::string makeName() {
    return "planner";
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

##### Numbers, Math, and Random Values

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

A built-in array has fixed size.

```cpp
int values[5] = {1, 2, 3, 4, 5};

std::cout << values[0] << '\n';
std::cout << values[4] << '\n';
```

C++ does not automatically check built-in array bounds.

```cpp
for (std::size_t i = 0; i < 5; ++i) {
    std::cout << values[i] << '\n';
}
```

Multidimensional array:

```cpp
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

int value = matrix[1][2];
```

When passed to a function, a built-in array usually decays to a pointer and loses its size.

```cpp
void printValues(const int* values, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << values[i] << '\n';
    }
}
```

Prefer `std::array` for fixed-size arrays and `std::vector` for dynamic arrays.

##### Strings

A C-style string is a null-terminated character array.

```cpp
char text[] = "robot";   // {'r','o','b','o','t','\0'}
```

Common C-string operations are in `<cstring>`, but they require careful buffer management.

```cpp
#include <cstring>

std::size_t length = std::strlen(text);
```

Prefer `std::string`.

```cpp
#include <string>

std::string first = "Fast";
std::string second = "Planner";
std::string name = first + "-" + second;

std::cout << name.size() << '\n';
std::cout << name[0] << '\n';
```

Common operations:

```cpp
std::string s = "trajectory";

s += " planner";
s.append(" test");
s.insert(0, "local ");
s.erase(0, 6);

std::size_t pos = s.find("planner");
std::string part = s.substr(0, 10);
bool empty = s.empty();
```

`operator[]` does not check bounds. `at()` throws `std::out_of_range` for invalid positions.

```cpp
char first_char = s.at(0);
```

Conversions:

```cpp
int number = std::stoi("42");
double value = std::stod("3.14");
std::string text_number = std::to_string(100);
```

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
const std::string& name = std::string{"robot"};
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

Modern C++ uses Resource Acquisition Is Initialization (RAII): a resource is owned by an object and released automatically by its destructor.

```cpp
#include <memory>

std::unique_ptr<int> value = std::make_unique<int>(10);
std::cout << *value << '\n';
```

Prefer:

| Requirement | Preferred Type |
| --- | --- |
| Dynamic sequence | `std::vector<T>` |
| Exclusive dynamic object | `std::unique_ptr<T>` |
| Shared ownership | `std::shared_ptr<T>` |
| Non-owning observation | Reference, raw pointer, or `std::weak_ptr<T>` |

Do not use `shared_ptr` merely to avoid deciding ownership.

##### Structures, Enumerations, and Unions

A `struct` groups related data. Its members are public by default.

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

Use constructor initialization lists when explicit construction logic is needed.

```cpp
struct Pose {
    double x;
    double y;

    Pose(double x_value, double y_value)
        : x{x_value}, y{y_value} {}
};
```

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

##### Basic `vector` and Data Structures

`std::vector` is the default dynamic sequence container.

```cpp
#include <vector>

std::vector<int> values{1, 2, 3};
values.push_back(4);
values.pop_back();

for (const int value : values) {
    std::cout << value << '\n';
}
```

Fundamental data-structure choices:

| Need | Typical Choice |
| --- | --- |
| Fixed contiguous data | Built-in array or `std::array` |
| Resizable contiguous data | `std::vector` |
| Key-value lookup | `std::map` or `std::unordered_map` |
| Unique values | `std::set` or `std::unordered_set` |
| Last-in, first-out | `std::stack` |
| First-in, first-out | `std::queue` |

The detailed container interfaces are summarized in the STL file.
