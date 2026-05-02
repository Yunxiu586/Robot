# Basic syntax

[toc]

##### Variables and Data Types

```cpp
int age = 20;
float pi = 3.14;
double price = 19.99;
char grade = 'A';
bool passed = true;

#include <string>
string name = "Alice";
```

Implicit Conversion

```cpp
int a = 10;
double b = a;  // int is converted to double automatically
```

Explicit Conversion

```cpp
double x = 3.8;
int y = static_cast<int>(x);  // y = 3
```

##### auto

`auto` lets the compiler infer the variable type.

```cpp
auto x = 10;        // int
auto y = 3.14;      // double
auto s = "hello";   // const char*
```

Useful when iterating over STL containers:

```cpp
map<string, int> mp;

for (auto item : mp) {
    cout << item.first << " " << item.second << endl;
}
```

Use references to avoid copying:

```cpp
for (const auto& item : mp) {
    cout << item.first << " " << item.second << endl;
}
```

##### Arrays

An array stores multiple values of the same type.

```cpp
int nums[5] = {1, 2, 3, 4, 5};

cout << nums[0] << endl;  // first element
cout << nums[4] << endl;  // last element
```

Traversing an Array

```cpp
int nums[5] = {1, 2, 3, 4, 5};

for (int i = 0; i < 5; i++) {
    cout << nums[i] << endl;
}
```

Range-based for Loop

```cpp
for (int x : nums) {
    cout << x << endl;
}
```

##### Constants

Constants cannot be changed after initialization.

```cpp
const double PI = 3.1415926;
```

A modern alternative is `constexpr` when the value is known at compile time.

```cpp
constexpr int MAX_SIZE = 100;
```

##### Input and Output

C++ uses `cin` for input and `cout` for output.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;

    cout << "You entered: " << x << endl;
    return 0;
}
```

##### Operators

Arithmetic Operators

```cpp
int a = 10, b = 3;

cout << a + b << endl;  // addition
cout << a - b << endl;  // subtraction
cout << a * b << endl;  // multiplication
cout << a / b << endl;  // integer division
cout << a % b << endl;  // remainder
```

Assignment Operators

```cpp
int x = 10;
x += 5;   // x = x + 5
x -= 2;   // x = x - 2
x *= 3;   // x = x * 3
x /= 2;   // x = x / 2
x %= 4;   // x = x % 4
```

Comparison Operators

```cpp
a == b;   // equal
a != b;   // not equal
a > b;    // greater than
a < b;    // less than
a >= b;   // greater than or equal
a <= b;   // less than or equal
```

Logical Operators

```cpp
bool p = true;
bool q = false;

p && q;   // logical AND
p || q;   // logical OR
!p;       // logical NOT
```

##### Conditional Statements

if Statement

```cpp
int score = 85;

if (score >= 60) {
    cout << "Pass" << endl;
}
```

if-else Statement

```cpp
if (score >= 60) {
    cout << "Pass" << endl;
} else {
    cout << "Fail" << endl;
}
```

if-else if-else Statement

```cpp
if (score >= 90) {
    cout << "A" << endl;
} else if (score >= 80) {
    cout << "B" << endl;
} else if (score >= 70) {
    cout << "C" << endl;
} else {
    cout << "D" << endl;
}
```

switch Statement

```cpp
int day = 3;

switch (day) {
    case 1:
        cout << "Monday" << endl;
        break;
    case 2:
        cout << "Tuesday" << endl;
        break;
    case 3:
        cout << "Wednesday" << endl;
        break;
    default:
        cout << "Other day" << endl;
        break;
}
```

`break` prevents the program from continuing into the next case.

##### Loops

for Loop

```cpp
for (int i = 0; i < 5; i++) {
    cout << i << endl;
}
```

while Loop

```cpp
int i = 0;

while (i < 5) {
    cout << i << endl;
    i++;
}
```

do-while Loop

```cpp
int i = 0;

do {
    cout << i << endl;
    i++;
} while (i < 5);
```

break and continue

```cpp
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;      // stop the loop
    }

    if (i % 2 == 0) {
        continue;   // skip this iteration
    }

    cout << i << endl;
}
```

##### Functions

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    cout << result << endl;
    return 0;
}
```

Void Function

```cpp
void printHello() {
    cout << "Hello" << endl;
}
```

Function Declaration

```cpp
int add(int a, int b);

int main() {
    cout << add(1, 2) << endl;
    return 0;
}

int add(int a, int b) {
    return a + b;
}
```

##### Pass by Value and Pass by Reference

Pass by Value

The function receives a copy.

```cpp
void change(int x) {
    x = 100;
}

int main() {
    int a = 10;
    change(a);
    cout << a << endl;  // still 10
}
```

Pass by Reference

The function can modify the original variable.

```cpp
void change(int& x) {
    x = 100;
}

int main() {
    int a = 10;
    change(a);
    cout << a << endl;  // 100
}
```

Pass by Const Reference

Useful for avoiding copying while preventing modification.

```cpp
void printString(const string& s) {
    cout << s << endl;
}
```

##### Pointers

A pointer stores the address of a variable.

```cpp
int x = 10;
int* p = &x;

cout << p << endl;   // address of x
cout << *p << endl;  // value of x
```

Modify Value Through Pointer

```cpp
int x = 10;
int* p = &x;

*p = 20;
cout << x << endl;  // 20
```

Null Pointer

```cpp
int* p = nullptr;
```

##### References

A reference is another name for an existing variable.

```cpp
int x = 10;
int& ref = x;

ref = 20;
cout << x << endl;  // 20
```

References must be initialized when declared.

##### Dynamic Memory

Dynamic memory is allocated at runtime.

```cpp
int* p = new int;
*p = 10;

cout << *p << endl;

delete p;
p = nullptr;
```

Dynamic Array

```cpp
int n = 5;
int* arr = new int[n];

for (int i = 0; i < n; i++) {
    arr[i] = i;
}

delete[] arr;
arr = nullptr;
```

In modern C++, prefer `vector`, `string`, and smart pointers instead of manual `new` and `delete`.

##### Struct

A `struct` groups related data together.

```cpp
struct Point {
    double x;
    double y;
};

int main() {
    Point p;
    p.x = 1.0;
    p.y = 2.0;

    cout << p.x << ", " << p.y << endl;
    return 0;
}
```

Struct with Constructor

```cpp
struct Point {
    double x;
    double y;

    Point(double x_, double y_) {
        x = x_;
        y = y_;
    }
};
```

##### Class

A `class` combines data and functions.

```cpp
#include <iostream>
using namespace std;

class Robot {
private:
    double x;
    double y;

public:
    // Constructor
    Robot(double x_, double y_) {
        x = x_;
        y = y_;
    }

    void move(double dx, double dy) {
        x += dx;
        y += dy;
    }

    void printPosition() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Robot robot(0.0, 0.0);
    robot.move(1.0, 2.0);
    robot.printPosition();

    return 0;
}
```

Access Specifiers

| Keyword     | Meaning                                              |
| ----------- | ---------------------------------------------------- |
| `public`    | Can be accessed from outside the class               |
| `private`   | Can only be accessed inside the class                |
| `protected` | Can be accessed inside the class and derived classes |

##### Constructor and Destructor

A constructor is called when an object is created.

```cpp
class Student {
public:
    Student() {
        cout << "Student created" << endl;
    }
};
```

A destructor is called when an object is destroyed.

```cpp
class Student {
public:
    ~Student() {
        cout << "Student destroyed" << endl;
    }
};
```

##### Header Files and Source Files

A larger C++ project is usually split into `.h` and `.cpp` files.

`math_utils.h`

```cpp
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

int add(int a, int b);

#endif
```

`math_utils.cpp`

```cpp
#include "math_utils.h"

int add(int a, int b) {
    return a + b;
}
```

`main.cpp`

```cpp
#include <iostream>
#include "math_utils.h"
using namespace std;

int main() {
    cout << add(1, 2) << endl;
    return 0;
}
```

##### `inline`

C++ normally allows only one definition of a non-inline function across the entire program.

This rule is called the **One Definition Rule**, often abbreviated as **ODR**.

If the function is marked as `inline`, it can be defined in a header file safely.

```cpp
// math_utils.hpp
inline int add(int a, int b) {
    return a + b;
}
```

Now multiple `.cpp` files can include this header without causing a multiple-definition linker error.



Member functions defined inside a class body are implicitly inline.

```cpp
class Vector3 {
public:
    double x, y, z;

    double normSquared() const {
        return x * x + y * y + z * z;
    }
};
```

The function `normSquared()` is implicitly inline because it is defined inside the class definition. This is equivalent in spirit to

```cpp
class Vector3 {
public:
    double x, y, z;

    inline double normSquared() const {
        return x * x + y * y + z * z;
    }
};
```

However, when a member function is defined outside the class body but still inside a header file, it should usually be marked `inline`.

```cpp
// vector3.hpp
class Vector3 {
public:
    double x, y, z;

    double normSquared() const;
};

inline double Vector3::normSquared() const {
    return x * x + y * y + z * z;
}
```

This avoids multiple-definition problems when the header is included by multiple `.cpp` files.

Use `inline` when

+ Define a small function in a header file.
+ Define a class member function outside the class body but inside a header file.
+ Write header-only utility code.

##### Namespace

A namespace avoids naming conflicts.

```cpp
namespace math_utils {
    int add(int a, int b) {
        return a + b;
    }
}

int main() {
    cout << math_utils::add(1, 2) << endl;
    return 0;
}
```

In the examples, `using namespace std;` is common.

```cpp
std::cout << "Hello" << std::endl;
```

`::` is the **scope resolution operator** and used to access a name from a specific scope. It tells the compiler which namespace, class, or scope a name belongs to.

##### Enumerations

An `enum` defines a set of named values.

```cpp
enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT
};

Direction dir = UP;
```

Modern C++ prefers `enum class`.

```cpp
enum class Direction {
    Up,
    Down,
    Left,
    Right
};

Direction dir = Direction::Up;
```

##### Basic File Input and Output

Write to a File

```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream fout("output.txt");

    fout << "Hello file" << endl;

    fout.close();
    return 0;
}
```

Read from a File

```cpp
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream fin("input.txt");
    string line;

    while (getline(fin, line)) {
        cout << line << endl;
    }

    fin.close();
    return 0;
}
```

##### Exception Handling

Exceptions handle runtime errors.

```cpp
#include <iostream>
using namespace std;

int divide(int a, int b) {
    if (b == 0) {
        throw runtime_error("division by zero");
    }

    return a / b;
}

int main() {
    try {
        cout << divide(10, 0) << endl;
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}
```

##### Lambda Expressions

A lambda is an anonymous function.

```cpp
auto add = [](int a, int b) {
    return a + b;
};

cout << add(1, 2) << endl;
```

Stores the lambda function in a variable named `add`.

```cpp
auto add
```

Defines the lambda parameter list.  This lambda takes two `int` parameters: `a` and `b`.

```cpp
[](int a, int b)
```

Defines the function body.

```cpp
{
    return a + b;
}
```

Lambda in Sorting

```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v = {3, 1, 2};

sort(v.begin(), v.end(), [](int a, int b) {
    return a > b;
});
```

```cpp
sort(v.begin(), v.end(), ...);
```

means sorting the elements from the beginning to the end of `v`.

```cpp
sort(v.begin(), v.end());
```

means sorting in ascending order.

The lambda function used as the custom comparison rule. Put `a` before `b` if `a` is greater than `b`.

```cpp
[](int a, int b) {
    return a > b;
}
```
