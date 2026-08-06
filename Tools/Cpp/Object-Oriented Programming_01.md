# Object-Oriented Programming

[toc]

`OOP` stands for `Object-Oriented Programming`. A class defines a user-defined type, and an object is an instance of that class.

The three core OOP features are encapsulation, inheritance, and polymorphism.

### Encapsulation

##### Classes and Objects

A class combines state and behavior. Data members store state, while member functions define operations on that state. An object uses `.`, while a pointer to an object uses `->` to access members.

```cpp
class Student {
public:
	std::string name{};
	int age{};

	void setAge(int value) {
		age = value;
	}
};

Student student;
student.name = "Alice";		// Data member through an object
student.setAge(20);			// Member function through an object

Student* student_ptr = &student;
student_ptr->name = "Bob";	// Data member through a pointer
student_ptr->setAge(21);	// Member function through a pointer
```

`pointer->member` is equivalent to `(*pointer).member`; the parentheses are required.

C++ does not prescribe one naming style. Engineering projects should use one convention consistently. 

The examples use `PascalCase` for types, `lowerCamelCase` for functions, `lower_snake_case` for local variables and parameters, and `lower_snake_case_` for private data members.

##### Access Control

Access specifiers control where class members can be named.

| Specifier | Accessible From |
| --- | --- |
| `public` | Any code that can access the object |
| `protected` | The class, friends, and derived classes |
| `private` | The class and friends |

The usual class interface is `public`; implementation details are normally `private` or `protected`.

##### Controlled Interface

Private data prevents unrestricted modification. Setters and getters can provide read-write, read-only, or write-only access and validate new values.

```cpp
#include <iostream>
#include <string>

class Student {
public:
	void setName(const std::string& name) {
		name_ = name;
	}

    // First const: the returned reference cannot modify name_
    // Second const: this function cannot modify the Student object
	const std::string& name() const {
		return name_;
	}

	bool setAge(int age) {
		if (age < 0 || age > 150) {
			return false;
		}

		age_ = age;
		return true;
	}

	int age() const {
		return age_;
	}

	int studentId() const {
		return student_id_;		// Read-only access
	}

	void setPassword(const std::string& password) {
		password_ = password;	// Write-only access
	}

private:
	std::string name_{};
	std::string password_{};
	int age_{};
	int student_id_{1001};
};

int main() {
	Student student;

	student.setName("Alice");
	student.setPassword("secret123");
	if (!student.setAge(20)) {
		std::cout << "Invalid age\n";
	}
	std::cout << "Student ID: " << student.studentId() << '\n';

	// student.age_ = -1;			// Error: age_ is private
	// student.name() = "Bob";		// Error: name() returns const std::string&

	return 0;
}
```

##### Class and Struct

`class` and `struct` support the same members, constructors, inheritance, and access specifiers. Their default access differs.

| Type | Default Member Access | Default Base Access |
| --- | --- | --- |
| `class` | `private` | `private` |
| `struct` | `public` | `public` |

A `struct` is commonly used for a simple value whose members form its public representation. A `class` is commonly used when an invariant is maintained through a controlled interface.

##### Member and Free Functions

An implicit-object non-static member function has an implicit object and can access private members of its class. A free function has no implicit object and normally uses the public interface.

```cpp
class Student {
public:
	const std::string& name() const {
		return name_;
	}

	void print() const {
		std::cout << name_ << '\n';			// Direct private access
	}

private:
	std::string name_{"Alice"};
};

void printStudent(const Student& student) {
	std::cout << student.name() << '\n';	// Public interface
}
```

##### Inline Member Functions

A member function defined inside its class definition in the global module is implicitly `inline`; writing the specifier is unnecessary. A member function defined outside the class is not implicitly `inline` merely because it is a member function.

```cpp
// student.hpp
#ifndef STUDENT_HPP
#define STUDENT_HPP

#include <string>

class Student {
public:
	Student() = default;				// Implicitly inline

	const std::string& name() const {
		return name_;					// Implicitly inline
	}

	void setName(const std::string& name);

private:
	std::string name_{};
};

inline void Student::setName(const std::string& name) {
	name_ = name;						// Explicitly inline
}

void printStudent(const Student& student);

#endif  // STUDENT_HPP
```

```cpp
// student.cpp
#include "student.hpp"

#include <iostream>

void printStudent(const Student& student) {
	std::cout << student.name() << '\n';
}
```

```cpp
// main.cpp
#include "student.hpp"

int main() {
	Student student;
	student.setName("Alice");
	printStudent(student);
	return 0;
}
```

`student.cpp` and `main.cpp` are separate translation units. Both contain the same inline member definitions from the header, which is permitted.

Constructors, destructors, and static member functions defined inside the class follow the same rule. A function explicitly defaulted on its first declaration is also implicitly `inline`.

`inline` permits identical definitions in multiple translation units; it does not require call expansion.

### Object Lifecycle

##### Constructors and Destructors

A constructor initializes an object. It has the class name and no return type. 

A destructor performs cleanup when the object's lifetime ends; it has the class name prefixed by `~`, no return type, and no parameters.

```cpp
class Student {
public:
	Student() = default;		// Default constructor

	explicit Student(int age)
		: age_{age} {}			// Parameterized constructor

	Student(const Student& other)
		: age_{other.age_} {}	// Copy constructor

	~Student() = default;		// Destructor

private:
	int age_{};
};
```

Each object is constructed once when its lifetime begins and destroyed once when its lifetime ends. A constructor may take no arguments or parameters; a destructor cannot take parameters.

##### Initialization Forms

A default constructor can be selected by default-initialization or empty-brace value-initialization. `Student student();` is a function declaration, not an object definition.

```cpp
Student first;					// Default initialization
Student second{};				// Calls the default constructor

// Student third();				// Declares a function

Student fourth(20);				// Direct initialization
Student fifth(fourth);			// Direct copy construction

Student sixth = Student{21};		// Uses the parameterized constructor
Student seventh = Student{fourth};	// Uses the copy constructor
```

A temporary object whose lifetime is not extended is destroyed at the end of its full-expression.

```cpp
Student{22};					// Destroyed at the end of this statement
Student{fourth};				// Temporary copy

// Student(fourth);				// Can be parsed as a declaration; avoid
```

A non-`explicit` single-argument constructor can be used for an implicit conversion. In engineering code, such constructors are normally `explicit` unless the conversion is intentional.

```cpp
class Score {
public:
	Score(int value)
		: value_{value} {}

private:
	int value_{};
};

void printScore(const Score& score);

Score score = 90;					// Implicit conversion
printScore(100);					// Implicit temporary object
```

##### Copy Construction

A copy constructor initializes a new object from an existing object of the same type. Passing an lvalue object by value also initializes the parameter by copying it.

```cpp
void inspect(Student student) {
	std::cout << "inspect\n";
}

Student original{20};
Student copied{original};			// New object from an existing object

inspect(original);					// Copy into the value parameter
```

##### Generated Functions

The compiler can implicitly declare special member functions. Generated constructors and destructors still initialize and destroy base-class and member subobjects.

| User Declarations | Default Constructor | Copy Constructor | Destructor |
| --- | --- | --- | --- |
| No constructor or destructor | Implicitly declared | Implicitly declared | Implicitly declared |
| Parameterized constructor | Not implicitly declared | Still implicitly declared | Implicitly declared |
| Copy constructor | Not implicitly declared | User-declared version | Implicitly declared |

An implicitly declared function can be defined as deleted when a base or member cannot perform the required operation.

```cpp
class Data {
public:
	Data() = default;
	Data(const Data&) = default;
	Data& operator=(const Data&) = default;
	~Data() = default;
};
```

##### Copy Depth

A member-wise copy of a raw pointer copies only the address. Two objects then refer to the same allocation, which can cause repeated deletion.

```cpp
class ShallowBox {
public:
	explicit ShallowBox(int value)
		: value_{new int{value}} {}	// Member initializer list

	~ShallowBox() {
		delete value_;
	}

private:
	int* value_{};
};

ShallowBox first{10};
// ShallowBox second{first};		// Unsafe: both objects would own the same address
```

A deep copy gives each object separate storage and copies the pointed-to value. A class that owns a raw resource must also handle copy assignment and destruction consistently.

```cpp
class Box {
public:
	explicit Box(int value)
		: value_{new int{value}} {}

	Box(const Box& other)	// Deep copy
		: value_{new int{*other.value_}} {}

	Box& operator=(const Box& other) {
		if (this != &other) {
			*value_ = *other.value_;
		}

		return *this;
	}

	~Box() {
		delete value_;
	}

	int value() const {
		return *value_;
	}

private:
	int* value_{};
};
```

The raw pointer above is used only to demonstrate deep copy. Modern C++ normally prefers RAII types such as `std::string` and `std::vector`; their members manage resources and usually make compiler-generated copy operations correct. This is the **Rule of Zero**.

##### Initializers and Object Members

A member initializer list initializes members before the constructor body runs. Members are initialized in their declaration order, not the textual order of the initializer list.

```cpp
class Engine {
public:
	explicit Engine(int power)
		: power_{power} {}

private:
	int power_{};
};

class Car {
public:
	Car(const std::string& model, int power)
		: model_{model}, engine_{power} {}

private:
	std::string model_{};
	Engine engine_;
};
```

For an object member, the member object is constructed before the containing object's constructor body. During destruction, the containing destructor body runs first, then member objects are destroyed in reverse declaration order.

##### Static Members

A static data member is not part of any object. A non-`thread_local` static data member is shared by all objects of the class and has static storage duration. A `thread_local` static data member has one copy per thread and thread storage duration.

The declaration of a non-inline static data member inside the class is not a definition. If the member is odr-used, it requires a definition at namespace scope, even when it is private.

A static member function belongs to the class rather than to a particular object. It has no `this` pointer and cannot access a non-static member without an object.

```cpp
class Student {
public:
	Student() {
		++count_;
	}

	Student(const Student&) {
		++count_;
	}

	~Student() {
		--count_;
	}

	static int school_code;

	static int count() {
		return count_;
	}

private:
	int student_id_{};
	static int count_;

	static void resetCount() {
		count_ = 0;
		// student_id_ = 0;		// Error: no object
	}
};

int Student::school_code = 1001;
int Student::count_ = 0;
```

Static data members and static member functions can be named through an object or through the class name. Class-name access is clearer because no object is required. Static members follow the same access rules as other class members.

```cpp
Student first;
Student second;

int first_code = first.school_code;		// Valid
int second_code = Student::school_code;	// Preferred

first.school_code = 2001;
int shared_code = second.school_code;	// 2001: shared value

int first_count = first.count();		// Valid
int second_count = Student::count();	// Preferred

// int count = Student::count_;			// Error: private static data member
// Student::resetCount();				// Error: private static member function
```

Since C++17, an `inline static` data member can be defined and initialized inside the class.

```cpp
class Counter {
private:
	inline static int value_{};
};
```

### Object Model

##### Object Representation

Every object of class type has one member subobject for each direct non-static data member. A static data member is not part of the class subobjects.

```cpp
class Counter {
public:
	void increment();
	static int total();

private:
	int value_{};				// One value_ in each object
	inline static int total_{};	// One total_ shared by all objects
};

void Counter::increment() {
	++value_;
	++total_;
}

int Counter::total() {
	return total_;
}
```

Member functions are not stored in each object. Objects of the same type call the same function definition; `this` identifies the current object of an implicit-object non-static call.

##### The this Pointer

`this` names a pointer to the object for which an implicit-object member function is invoked. The expression `this` is not permitted in a static or explicit-object member function.

```cpp
class Counter {
public:
	Counter& setValue(int value_) {
		this->value_ = value_;		// Distinguish the member from the parameter
		return *this;
	}

	Counter& add(int value) {
		value_ += value;
		return *this;
	}

	Counter copy() const {
		return *this;
	}

	int value() const {
		return value_;
	}

private:
	int value_{};
};

Counter counter;
counter.setValue(1).add(2).add(3);	// Chained calls modify the same object

Counter copied = counter.copy();	// A separate result object
copied.add(4);						// Does not modify counter
```

Returning `*this` by reference returns the same object and supports chained calls. Returning by value produces a separate result object.

##### Null Object Pointers

A non-static member function requires an object. Calling a non-static member function through a null pointer has undefined behavior.

```cpp
Counter* counter = nullptr;
// counter->value();			// Undefined behavior
```

##### Const Members and Objects

In a const-qualified non-static member function, `this` has pointer-to-const class type. Non-mutable data members cannot be modified.

```cpp
class Counter {
public:
	void increment() {
		++value_;
	}

	int value() const {
		++read_count_;			// mutable may be modified
		return value_;
	}

private:
	int value_{};
	mutable int read_count_{};
};

const Counter counter;
int value = counter.value();	// Calls a const member function
// counter.increment();			// Error: non-const member function
```

For non-static member functions, a const object can call only const-qualified overloads. A `mutable` member can be modified even when the complete object is const.
