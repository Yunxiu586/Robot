# OOP and Advanced C++

[toc]

##### Classes and Objects

A class combines state and behavior.

```cpp
class Rectangle {
private:
    double width_{};
    double height_{};

public:
    void setSize(double width, double height) {
        width_ = width;
        height_ = height;
    }

    double area() const {
        return width_ * height_;
    }
};

Rectangle rectangle;
rectangle.setSize(4.0, 3.0);
```

Access control:

| Keyword | Access |
| --- | --- |
| `public` | Accessible through the class interface |
| `private` | Accessible only inside the class and friends |
| `protected` | Accessible inside the class, friends, and derived classes |

A `class` uses private access by default. A `struct` uses public access by default; otherwise, both support member functions, constructors, and the same access specifiers.

##### Object Lifecycle

A constructor establishes a valid object state.

```cpp
class Rectangle {
public:
    Rectangle(double width, double height)
        : width_{width}, height_{height} {}

private:
    double width_;
    double height_;
};
```

Use member initialization lists. Members are initialized in declaration order, not list order.

```cpp
class Book {
public:
    Book() = default;
    explicit Book(std::string title) : title_{std::move(title)} {}

private:
    std::string title_;
};
```

`explicit` prevents unintended single-argument conversions.

A destructor releases owned resources.

```cpp
class FileHandle {
public:
    ~FileHandle() {
        // release resource
    }
};
```

Prefer library RAII types instead of manually writing resource-management destructors.

Special member functions:

```cpp
class Data {
public:
    // Default constructor:
    // Creates a Data object using compiler-generated default initialization.
    Data() = default;

    // Copy constructor:
    // Creates a new Data object by copying an existing Data object.
    Data(const Data&) = default;

    // Copy assignment operator:
    // Copies the contents of an existing Data object into an already existing object.
    Data& operator=(const Data&) = default;

    // Move constructor:
    // Creates a new Data object by transferring resources from another Data object.
    // noexcept indicates that this operation does not throw exceptions.
    Data(Data&&) noexcept = default;

    // Move assignment operator:
    // Transfers resources from another Data object into an already existing object.
    Data& operator=(Data&&) noexcept = default;

    // Destructor:
    // Destroys the Data object and releases resources owned by its members.
    ~Data() = default;
};
```

Rule of Zero: when members manage themselves, define none of these manually.

```cpp
class Data {
private:
    std::vector<int> values_;
};
```

`std::move` does not move an object by itself. It converts its argument to an rvalue expression so that a move constructor or move assignment operator can be selected.

```cpp
std::string source = "Hello";
std::string destination = std::move(source);
```

After a move, the source object remains valid, but its value is generally unspecified; it may still be assigned to or destroyed.

##### Class Members

`this` points to the current object.

```cpp
class Counter {
public:
    Counter& increment() {
        ++value_;
        return *this;
    }

    int value() const {
        return value_;
    }

private:
    int value_{};
};
```

A `const` member function promises not to modify ordinary data members.

Static members belong to the class rather than each object.

```cpp
class Student {
public:
    Student() {
        ++count_;
    }

    static int count() {
        return count_;
    }

private:
    inline static int count_ = 0;
};
```

A friend can access private members, but it weakens encapsulation and should be used sparingly.

```cpp
class Point {
public:
    Point(double x, double y)
        : x_{x}, y_{y} {}

private:
    double x_{};
    double y_{};

    friend Point operator+(const Point& a, const Point& b);
};
```

The friend function is declared inside the class and defined outside the class:

```cpp
Point operator+(const Point& a, const Point& b) {
    return Point{
        a.x_ + b.x_,
        a.y_ + b.y_
    };
}
```

`operator+` is a non-member friend function that can access the private members of `Point` and defines how two `Point` objects are added.

##### Encapsulation and Abstraction

Encapsulation hides representation behind a controlled interface.

```cpp
class Temperature {
public:
    explicit Temperature(double celsius) {
        setCelsius(celsius);
    }

    void setCelsius(double value) {
        if (value < -273.15) {
            throw std::invalid_argument{"invalid temperature"};
        }
        celsius_ = value;
    }

    double celsius() const {
        return celsius_;
    }

private:
    double celsius_{};
};
```

```cpp
Temperature t{20.0};

// t.celsius_ = -500.0;  // Compilation error
t.setCelsius(25.0);
double value = t.celsius();
```

Abstraction exposes what an object does while hiding how it does it. A good class maintains its invariants after every public operation.

##### Inheritance

Inheritance models an “is-a” relationship.

```cpp
class Person {
public:
    void setName(const std::string& name) {
        name_ = name;
    }

protected:
    std::string name_;
};

class Student : public Person {
public:
    void printName() const {
        std::cout << name_ << '\n';
    }
};
```

```cpp
Person person;
person.setName("Alice");
// person.name_ = "Bob";  // Compilation error
```

```cpp
Student student;

student.setName("Alice");
student.printName();
```

Inheritance access:

| Form | Public Base Members | Protected Base Members |
| --- | --- | --- |
| `public` inheritance | remain public | remain protected |
| `protected` inheritance | become protected | remain protected |
| `private` inheritance | become private | become private |

Public inheritance is the normal choice for polymorphic interfaces. Prefer composition when the relationship is “has-a” rather than “is-a”.

Construction runs from base to derived. Destruction runs from derived to base.

##### Overloading

Function overloading uses the same name for related operations with different parameter lists.

```cpp
void print(int value);
void print(double value);
void print(const std::string& value);
```

```cpp
print(10);               // Calls print(int)
print(3.14);             // Calls print(double)
print(std::string{"A"}); // Calls print(const std::string&)
```

Operator overloading gives user-defined types natural syntax.

```cpp
struct Point {
    double x{};
    double y{};
};

Point operator+(const Point& a, const Point& b) {
    return {a.x + b.x, a.y + b.y};
}

bool operator==(const Point& a, const Point& b) {
    return a.x == b.x && a.y == b.y;
}
```

Do not overload an operator with surprising meaning. Some operators, including `.`, `::`, `?:`, and `sizeof`, cannot be overloaded.

##### Polymorphism

Runtime polymorphism uses virtual functions through base references or pointers.

```cpp
class Animal {
public:
    virtual ~Animal() = default;

    virtual void makeSound() const {
        std::cout << "Animal sound\n";
    }
};

class Dog : public Animal {
public:
    void makeSound() const override {
        std::cout << "Woof\n";
    }
};

class Cat : public Animal {
public:
    void makeSound() const override {
        std::cout << "Meow\n";
    }
};

void playSound(const Animal& animal) {
    animal.makeSound();
}
```

The function calls the overridden version according to the actual object type.

```cpp
Dog dog;
Cat cat;

playSound(dog);  // Woof
playSound(cat);  // Meow
```

Important rules:

- Use `override` on overriding functions.
- Give a polymorphic base class a virtual destructor.
- Pass polymorphic objects by pointer or reference to avoid object slicing.
- Use `final` when further overriding or inheritance must be prohibited.

```cpp
class FixedAnimal final : public Animal {
public:
    void makeSound() const override final {
        std::cout << "Fixed sound\n";
    }
};
```

##### Abstract Classes and Interfaces

A pure virtual function makes a class abstract.

```cpp
class Animal {
public:
    virtual ~Animal() = default;
    virtual void makeSound() const = 0;
};
```

```cpp
//Animal animal;	// Compilation error
```

```cpp
class Dog : public Animal {
public:
    void makeSound() const override {
        std::cout << "Woof\n";
    }
};

class Cat : public Animal {
};

Dog dog;
dog.makeSound();  // Woof
//Cat cat;  // Compilation error
```

An abstract class cannot be instantiated. A derived class must implement all required pure virtual functions before it becomes concrete.

Prefer small interfaces focused on one responsibility.

##### Class Files and Namespaces

The general header/source compilation model is covered in `Functions and Memory.md`. For a class, place its declaration in a header and define non-inline member functions in a source file.

Typical class declaration:

```cpp
// student.hpp
#pragma once

#include <string>

namespace school {

class Student {
public:
    Student(const std::string& name, int age);

    void setAge(int age);
    void printInfo() const;

private:
    std::string name_;
    int age_;
};

}  // namespace school
```

Class member functions are defined in the source file:

```cpp
// student.cpp
#include "student.hpp"

#include <iostream>

namespace school {

Student::Student(const std::string& name, int age)
    : name_{name}, age_{age} {}

void Student::setAge(int age) {
    age_ = age;
}

void Student::printInfo() const {
    std::cout << name_ << ", " << age_ << '\n';
}

}  // namespace school
```

The class can be used in another source file:

```cpp
// main.cpp
#include "student.hpp"

int main() {
    school::Student student{"Alice", 20};

    student.setAge(21);
    student.printInfo();

    return 0;
}
```

Use `#include <...>` for standard library or installed headers:

```cpp
#include <iostream>
#include <string>
#include <vector>
```

Use `#include "..."` for local headers:

```cpp
#include "student.hpp"
```

A classic include guard provides the same basic protection as `#pragma once`:

```cpp
#ifndef SCHOOL_STUDENT_HPP
#define SCHOOL_STUDENT_HPP

#include <string>

namespace school {

class Student {
public:
    Student(const std::string& name, int age);

private:
    std::string name_;
    int age_;
};

}  // namespace school

#endif
```

Namespaces prevent name collisions between classes or functions with the same name.

```cpp
namespace school {
    class Student {};
}

namespace university {
    class Student {};
}

school::Student school_student;
university::Student university_student;
```

Avoid `using namespace std;` in header files because it introduces all names from `std` into every source file that includes the header.

In source files, limited `using` declarations are safer:

```cpp
using std::cout;
using std::string;

string name = "Alice";
cout << name << '\n';
```

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
