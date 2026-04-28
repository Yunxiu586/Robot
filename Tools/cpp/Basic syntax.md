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

##### Standard Template Library

The Standard Template Library, usually called STL, provides commonly used containers and algorithms.

|                  | Header            | Ordered                          | Duplicate Elements | Common Use                            |
| ---------------- | ----------------- | -------------------------------- | ------------------ | ------------------------------------- |
| `vector`         | `<vector>`        | Keep insertion order             | Yes                | Store a list of elements              |
| `string`         | `<string>`        | Keep character order             | Yes                | Store and process text                |
| `pair`           | `<utility>`       | Not a container                  | -                  | Store coordinate, key-value-like data |
| `map`            | `<map>`           | Sorted by key                    | Keys are unique    | Ordered dictionary                    |
| `unordered_map`  | `<unordered_map>` | No                               | Keys are unique    | Fast average lookup                   |
| `set`            | `<set>`           | Sorted                           | No                 | Store sorted unique values            |
| `unordered_set`  | `<unordered_set>` | No                               | No                 | Fast average existence check          |
| `queue`          | `<queue>`         | By insertion order               | Yes                | BFS                                   |
| `stack`          | `<stack>`         | By insertion order               | Yes                | DFS, simulation                       |
| `priority_queue` | `<queue>`         | Top element has highest priority | Yes                | Dijkstra, greedy algorithms           |
| `sort`           | `<algorithm>`     | Result depends on comparator     | Yes                | Sort arrays or vectors                |
| `find`           | `<algorithm>`     | -                                | -                  | Find an element in a range            |

##### vector

`vector` is a dynamic array.

```cpp
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> nums;

    nums.push_back(10);
    nums.push_back(20);
    nums.push_back(30);

    cout << nums.size() << endl;
    cout << nums[0] << endl;

    for (int x : nums) {
        cout << x << endl;
    }

    return 0;
}
```

Common vector Operations

```cpp
vector<int> v = {1, 2, 3};

v.push_back(4);     // add element at the end
v.pop_back();       // remove last element
v.size();           // number of elements
v.empty();          // whether vector is empty
v.clear();          // remove all elements
v.front();          // first element
v.back();           // last element
```

##### strings

A `string` stores text.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hello";

    cout << s.length() << endl;
    cout << s[0] << endl;

    s += " world";
    cout << s << endl;

    return 0;
}
```

Common String Operations

```cpp
string s = "algorithm";

cout << s.size() << endl;        // length
cout << s[0] << endl;            // first character
cout << s.substr(0, 4) << endl;  // "algo"
cout << s.find("go") << endl;    // position of substring
```

Reading a Full Line

```cpp
string line;
getline(cin, line);
```

If `getline()` is used after `cin >>`, you may need to clear the leftover newline:

```cpp
cin.ignore();
getline(cin, line);
```

##### pair

`pair` stores two values.

```cpp
#include <utility>
#include <iostream>
using namespace std;

int main() {
    pair<int, string> p = {1, "Alice"};

    cout << p.first << endl;
    cout << p.second << endl;

    return 0;
}
```

##### map

`map` stores key-value pairs in sorted order by key.

```cpp
#include <map>
#include <iostream>
using namespace std;

int main() {
    map<string, int> score;

    score["Alice"] = 90;
    score["Bob"] = 85;

    cout << score["Alice"] << endl;

    for (auto item : score) {
        cout << item.first << " " << item.second << endl;
    }

    return 0;
}
```

##### unordered_map

`unordered_map` stores key-value pairs using a hash table.

```cpp
#include <unordered_map>
#include <iostream>
using namespace std;

int main() {
    unordered_map<string, int> score;

    score["Alice"] = 90;
    score["Bob"] = 85;

    cout << score["Bob"] << endl;

    return 0;
}
```

`unordered_map` usually has faster average lookup, but its elements are not sorted.

| Feature            | `map`                       | `unordered_map`              |
| ------------------ | --------------------------- | ---------------------------- |
| Internal structure | Balanced binary search tree | Hash table                   |
| Element form       | Key-value pairs             | Key-value pairs              |
| Key order          | Sorted by key               | Unordered                    |
| Duplicate keys     | Not allowed                 | Not allowed                  |
| Search complexity  | `O(log n)`                  | Average `O(1)`               |
| Insert complexity  | `O(log n)`                  | Average `O(1)`               |
| Delete complexity  | `O(log n)`                  | Average `O(1)`               |
| Header file        | `<map>`                     | `<unordered_map>`            |
| Common use         | Need sorted keys            | Need fast key lookup         |
| Example            | Store scores sorted by name | Count word frequency quickly |

##### set

`set` stores unique elements in sorted order.

```cpp
#include <set>
#include <iostream>
using namespace std;

int main() {
    set<int> s;

    s.insert(3);
    s.insert(1);
    s.insert(3);

    for (int x : s) {
        cout << x << endl;  // 1 3
    }

    return 0;
}
```

##### unordered_set

`unordered_set` stores unique elements using a hash table.

Unlike `set`, an `unordered_set` does not keep elements sorted. Its average insertion, deletion, and lookup complexity is `O(1)`.

```cpp
#include <unordered_set>
#include <iostream>
using namespace std;

int main() {
    unordered_set<int> s;

    s.insert(3);
    s.insert(1);
    s.insert(3);  // duplicate element, ignored

    cout << s.count(3) << endl;  // 1, means 3 exists
    cout << s.count(5) << endl;  // 0, means 5 does not exist

    for (int x : s) {
        cout << x << endl;
    }

    return 0;
}
```

Common unordered_set Operations

```cpp
unordered_set<int> s;

s.insert(x);       // insert x
s.erase(x);        // remove x
s.count(x);        // return 1 if x exists, otherwise 0
s.find(x);         // return iterator to x if found
s.empty();         // whether the set is empty
s.size();          // number of elements
s.clear();         // remove all elements
```

Check Whether an Element Exists

```cpp
if (s.find(x) != s.end()) {
    cout << "Found" << endl;
}
```

or:

```cpp
if (s.count(x)) {
    cout << "Found" << endl;
}
```

| Feature            | `set`                       | `unordered_set`                   |
| ------------------ | --------------------------- | --------------------------------- |
| Internal structure | Balanced binary search tree | Hash table                        |
| Element form       | Single values               | Single values                     |
| Element order      | Sorted                      | Unordered                         |
| Duplicate elements | Not allowed                 | Not allowed                       |
| Search complexity  | `O(log n)`                  | Average `O(1)`                    |
| Insert complexity  | `O(log n)`                  | Average `O(1)`                    |
| Delete complexity  | `O(log n)`                  | Average `O(1)`                    |
| Header file        | `<set>`                     | `<unordered_set>`                 |
| Common use         | Need sorted unique elements | Need fast existence check         |
| Example            | Store sorted student IDs    | Check whether a word has appeared |

Use `set` when you need sorted order. Use `unordered_set` when you only need to check whether an element exists quickly.

##### stack

`stack` is a last-in-first-out data structure.

```cpp
#include <stack>
#include <iostream>
using namespace std;

int main() {
    stack<int> st;

    st.push(1);
    st.push(2);

    cout << st.top() << endl;
    st.pop();

    return 0;
}
```

Common stack Operations

```cpp
st.push(x);
st.pop();
st.top();
st.empty();
st.size();
```

##### queue

`queue` is a first-in-first-out data structure.

```cpp
#include <queue>
#include <iostream>
using namespace std;

int main() {
    queue<int> q;

    q.push(1);
    q.push(2);

    cout << q.front() << endl;
    q.pop();

    return 0;
}
```

Common queue Operations

```cpp
q.push(x);
q.pop();
q.front();
q.back();
q.empty();
q.size();
```

##### priority_queue

`priority_queue` is a heap-based data structure.

Max Heap by Default

```cpp
#include <queue>
#include <iostream>
using namespace std;

int main() {
    priority_queue<int> pq;

    pq.push(3);
    pq.push(1);
    pq.push(5);

    cout << pq.top() << endl;  // 5

    return 0;
}
```

Min Heap

```cpp
#include <queue>
#include <vector>
#include <functional>
using namespace std;

priority_queue<int, vector<int>, greater<int>> pq;
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

In small examples, `using namespace std;` is common. In larger projects, prefer explicit names such as:

```cpp
std::cout << "Hello" << std::endl;
```

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

##### Sorting

Use `sort()` from `<algorithm>`.

```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v = {3, 1, 2};

sort(v.begin(), v.end());  // ascending order
```

Descending Order

```cpp
sort(v.begin(), v.end(), greater<int>());
```

Custom Sorting

```cpp
vector<pair<int, int>> points = {{1, 2}, {1, 1}, {2, 0}};

sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
    if (a.first != b.first) {
        return a.first < b.first;
    }
    return a.second < b.second;
});
```

##### Basic Algorithm Functions

Common functions from `<algorithm>`:

```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v = {1, 2, 3, 4, 5};

reverse(v.begin(), v.end());

int maxValue = *max_element(v.begin(), v.end());
int minValue = *min_element(v.begin(), v.end());

auto it = find(v.begin(), v.end(), 3);

if (it != v.end()) {
    cout << "Found" << endl;
}
```

##### Iterator

An iterator is similar to a pointer and is used to access container elements.

```cpp
vector<int> v = {1, 2, 3};

for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
    cout << *it << endl;
}
```

With `auto`:

```cpp
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << endl;
}
```

### 