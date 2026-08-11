# Object-Oriented Programming

[toc]

### Friends

Friend declarations give a function or class permission to name private and protected members. A friend is not a member; friendship is not inherited or transitive.

Friendship grants selected access without making the members public.

##### Friend Functions

A non-member function may be declared as a friend.

```cpp
class Screen {
private:
	std::string contents_{"hello"};

	friend void clear(Screen& screen);
};

void clear(Screen& screen) {
	screen.contents_.clear();
}
```

##### Friend Classes

Every member of a friend class can access the granting class's private and protected members.

```cpp
class WindowManager;

class Screen {
private:
	std::string contents_{"hello"};

	friend class WindowManager;
};

class WindowManager {
public:
	void clear(Screen& screen) const;
};

void WindowManager::clear(Screen& screen) const {
	screen.contents_.clear();
}
```

##### Friend Member Functions

A selected member function of another class can be declared as a friend. The member function must be declared before the friend declaration. In this example, it is defined after the granting class is complete because its definition accesses the granting class's members.

```cpp
class Screen;

class WindowManager {
public:
	void clear(Screen& screen) const;
};

class Screen {
private:
	std::string contents_{"hello"};

	friend void WindowManager::clear(Screen& screen) const;
};

void WindowManager::clear(Screen& screen) const {
	screen.contents_.clear();
}
```

The member function is declared before the friend declaration. Its definition follows `Screen` because it accesses `Screen::contents_`.

### Operators

##### Operator Functions

Built-in operators already have language-defined meanings for fundamental types. Operator overloading gives an existing operator a meaning for class or enumeration operands; it does not change the operator's behavior for expressions containing only built-in types.

An overloaded operator is a function with a special name such as `operator+`. It can be selected by overload resolution like other overloaded functions.

A binary operator can usually be written as a non-static member function with one explicit parameter or as a non-member function with two parameters. For example, `left + right` can call either `left.operator+(right)` or `operator+(left, right)`.

##### Common Operators

The following example uses `Vector2` for arithmetic, stream output, increment, assignment, and equality.

```cpp
#include <iostream>

class Vector2 {
public:
	Vector2(int x, int y)
		: x_{x}, y_{y} {}

	Vector2 operator+(const Vector2& other) const {
		return {x_ + other.x_, y_ + other.y_};
	}

	Vector2& operator++() {
		++x_;
		++y_;
		return *this;					// Return the same object for chained prefix operations
	}

	Vector2 operator++(int) {			// The int parameter distinguishes postfix ++
		Vector2 old{*this};				// Save the value before modification
		++(*this);
		return old;						// Postfix returns the previous value by value
	}

	// Vector2& operator=(const Vector2&) is implicitly declared for copy assignment
    Vector2& operator=(const Vector2& other) {
        x_ = other.x_;
        y_ = other.y_;
        return *this;					// Return this object by reference for chained assignment
    }
    

	friend std::ostream& operator<<(std::ostream& out, const Vector2& value);
	friend bool operator==(const Vector2& left, const Vector2& right);

private:
	int x_{};
	int y_{};
};

std::ostream& operator<<(std::ostream& out, const Vector2& value) {
	out << '(' << value.x_ << ", " << value.y_ << ')';
	return out;							// Return the stream for chained output
}

bool operator==(const Vector2& left, const Vector2& right) {
	return left.x_ == right.x_ && left.y_ == right.y_;
}
```

```cpp
Vector2 first{1, 2};
Vector2 second{3, 4};
Vector2 third{5, 6};

Vector2 sum = first + second;			// Calls first.operator+(second)
std::cout << first << ' ' << sum;		// Non-member operator<< supports chained output

++(++first);							// Prefix ++ returns Vector2&
Vector2 old = first++;

first = second;							// Calls first.operator=(second)
first = second = third;					// Chained assignment

bool equal = first == third;			// Calls non-member operator==
```

For `operator<<`, a non-member overload is natural because the left operand is `std::ostream`. Declaring it as a friend allows direct access to private data without making that data public.

Prefix `operator++()` conventionally returns a reference to the modified object. Postfix `operator++(int)` uses the `int` parameter only to distinguish the postfix form and normally returns the old value by value.

`operator=` is a member operator, so `left = right` is interpreted as `left.operator=(right)` for a class left operand. 

If a class has no user-declared copy assignment operator, one is normally declared implicitly. Its generated definition performs member-wise assignment of base subobjects and non-static data members and returns the assigned object by reference. Define `operator=` yourself only when different assignment behavior is required.

##### Function Call

A class that defines `operator()` can be called with function-call syntax and is commonly called a function object or functor. `operator()` itself can also be overloaded.

```cpp
class VectorPrinter {
public:
	void operator()(const Vector2& value) const {
		std::cout << value;
	}

	void operator()(const Vector2& value, std::ostream& out) const {
		out << value;
	}
};

VectorPrinter printer;
printer(sum);							// Equivalent to printer.operator()(sum)
printer(sum, std::cout);				// Selects another operator() overload
VectorPrinter{}(sum);					// Temporary unnamed function object, then operator()
```

`VectorPrinter{}(sum)` first creates a temporary object with no variable name, then applies function-call syntax to that object, which invokes its `operator()`.

##### Operator Rules

An operator function must involve at least one class or enumeration operand. Overloading cannot change an operator's precedence, grouping, or number of operands.

The operators `.`, `.*`, `::`, and `?:` cannot be overloaded. `sizeof` is not an overloadable operator-function name.

### Inheritance

##### Base and Derived Classes

Inheritance lets a derived class reuse and extend common data and behavior from a base class, reducing repeated code when the types have an inheritance relationship. 

The standard terms are **base class** and **derived class**; parent and child are informal terms.

```cpp
class Person {
public:
	void setName(const std::string& name) {
		name_ = name;
	}

	const std::string& name() const {
		return name_;
	}

private:
	std::string name_{};
};

class Student : public Person {			// Derived : access Base
public:
	void printName() const {
		std::cout << name() << '\n';	// Reuse the base-class interface
	}
};

Student student;
student.setName("Alice");
student.printName();
```

A base-specifier has the form `class Derived : access-specifier Base`. If the access specifier is omitted, a `class` uses private inheritance and a `struct` uses public inheritance.

Public inheritance normally models an **is-a** relationship: a `Student` is a `Person`.

##### Inheritance Access

The inheritance access specifier changes the accessibility of inherited public and protected members.

| Inheritance | Public Base Members | Protected Base Members | Private Base Members |
| --- | --- | --- | --- |
| `public` | `public` | `protected` | Inaccessible directly |
| `protected` | `protected` | `protected` | Inaccessible directly |
| `private` | `private` | `private` | Inaccessible directly |

```cpp
class Base {
public:
	int public_value{};

protected:
	int protected_value{};

private:
	int private_value{};
};

class PublicDerived : public Base {
	void update() {
		public_value = 1;				// Remains public
		protected_value = 2;			// Remains protected
		// private_value = 3;			// Error: private in Base
	}
};

class ProtectedDerived : protected Base {
	void update() {
		public_value = 1;				// Becomes protected
		protected_value = 2;			// Remains protected
	}
};

class PrivateDerived : private Base {
	void update() {
		public_value = 1;				// Becomes private
		protected_value = 2;			// Becomes private
	}
};
```

Inheritance access affects accessibility, not whether the base-class subobject exists.

##### Object Model

A derived object contains a base-class subobject. That base subobject contains the base class's non-static data members, including private members.

```cpp
class Base {
public:
	int value() const {
		return value_;					// Base can access its own private member
	}

private:
	int value_{10};
};

class Derived : public Base {
private:
	int extra_{20};
};

Derived object;
int value = object.value();				// Access through the Base public interface
// object.value_ = 30;					// Error: Base::value_ is private
```

A representative MSVC layout for the example above, in `/d1reportSingleClassLayoutDerived` format:

```text
class Derived size(8):
	+---
	| +--- (base class Base)
 0	| | value_
	| +---
 4	| extra_
	+---
```

Static data members are not part of each object. Exact size, padding, and base-subobject offsets are implementation-dependent.

##### Construction and Destruction

For simple inheritance, the base class is constructed before the derived class. Destruction occurs in the reverse order.

For a most-derived object, initialization order is: virtual bases, direct bases in base-specifier order, non-static data members in declaration order, then the constructor body. Destruction reverses this order.

##### Hidden Members

A declaration in a derived class can hide a base-class member with the same name. Unqualified access finds the derived member; qualify with `Base::` to select the hidden base member explicitly.

```cpp
class Base {
public:
	int value{1};
	inline static int count{10};

	void print() const {
		std::cout << "Base\n";
	}

	static void reset() {
		count = 0;
	}
};

class Derived : public Base {
public:
	int value{2};						// Hides Base::value
	inline static int count{20};		// Hides Base::count

	void print() const {				// Hides Base::print
		std::cout << "Derived\n";
	}

	static void reset() {				// Hides Base::reset
		count = 0;
	}
};

Derived object;

int derived_value = object.value;		// Derived::value
int base_value = object.Base::value;	// Base::value
object.print();							// Derived::print
object.Base::print();					// Base::print

int object_count = object.count;		// Derived::count through an object
int base_object_count = object.Base::count;
int class_count = Derived::count;		// Derived::count through the class name
int base_class_count = Base::count;		// Base::count through the class name

object.reset();							// Derived::reset through an object
object.Base::reset();					// Base::reset through an object
Derived::reset();						// Derived::reset through the class name
Base::reset();							// Base::reset through the class name
```

Name hiding is a lookup rule; it is separate from virtual-function overriding.

##### Multiple Inheritance

A class can have more than one direct base class. Base classes are separated by commas.

```cpp
class Scanner {
public:
	void status() const {
		std::cout << "Scanner ready\n";
	}
};

class Printer {
public:
	void status() const {
		std::cout << "Printer ready\n";
	}
};

class OfficeMachine : public Scanner, public Printer {
public:
	void check() const {
		Scanner::status();		// Qualify an ambiguous base member
		Printer::status();
	}
};

OfficeMachine machine;
// machine.status();			// Error: ambiguous
machine.Scanner::status();
machine.Printer::status();
```

An `OfficeMachine` object contains both direct base-class subobjects. A representative MSVC layout for this empty-base example is:

```text
class OfficeMachine size(2):
	+---
 0	| +--- (base class Scanner)
	| +---
 1	| +--- (base class Printer)
	| +---
	+---
```

The exact size and base-subobject offsets are implementation-dependent.

Direct base classes are initialized in the order written in the base-specifier list, regardless of the order used in a constructor's member-initializer list.

##### Diamond Inheritance

Diamond inheritance occurs when two intermediate classes derive from the same base and another class derives from both intermediate classes.

```text
        Device
       /      \
   Scanner   Printer
       \      /
     OfficeMachine
```

With non-virtual inheritance, the most-derived object contains two distinct `Device` base subobjects, so an unqualified `Device` member can be ambiguous.

```cpp
class Device {
public:
	int id{};
};

class Scanner : public Device {};
class Printer : public Device {};
class OfficeMachine : public Scanner, public Printer {};

OfficeMachine machine;
// machine.id = 1;			// Error: two Device subobjects
machine.Scanner::id = 1;
machine.Printer::id = 2;
```

Virtual inheritance makes the common base a virtual base. The most-derived object then contains one shared subobject for each distinct virtual base type.

```cpp
class Device {
public:
	int id{};
};

class Scanner : virtual public Device {};
class Printer : virtual public Device {};
class OfficeMachine : public Scanner, public Printer {};

OfficeMachine machine;
machine.id = 1;			// One shared Device virtual base subobject
```

A representative MSVC x64 layout for the virtual-inheritance example is:

```text
class OfficeMachine size(24):
	+---
	| +--- (base class Scanner)
 0	| | {vbptr}
	| +---
	| +--- (base class Printer)
 8	| | {vbptr}
	| +---
	+---
	+--- (virtual base Device)
16	| id
	| <alignment member> (size=4)
	+---

OfficeMachine::$vbtable@Scanner@:
 0	| 0
 1	| 16

OfficeMachine::$vbtable@Printer@:
 0	| 0
 1	| 8
```

The object layout can be viewed more directly as:

```text
0                       8                      16          20      24
+-----------------------+----------------------+-----------+-------+
| Scanner vbptr         | Printer vbptr        | Device::id|padding|
+-----------------------+----------------------+-----------+-------+
       8 bytes                  8 bytes           4 bytes   4 bytes
```

`Scanner::vbptr` reaches the shared `Device` virtual base with a displacement of `16` bytes:

```text
Scanner::vbptr
OfficeMachine + 0
        |
        | +16
        v
OfficeMachine + 16
Device
```

`Printer::vbptr` starts at offset `8`, so it reaches the same shared `Device` with a displacement of `8` bytes:

```text
Printer::vbptr
OfficeMachine + 8
        |
        | +8
        v
OfficeMachine + 16
Device
```

The most-derived class is responsible for initializing a virtual base. Virtual bases are initialized before non-virtual direct bases.

`vbptr` and `vbtable` are implementation details. In Microsoft Visual C++, a hidden virtual-base pointer (`vbptr`) can refer to a virtual-base displacement table (`vbtable`); the displacement is used to locate the shared virtual-base subobject.

The presence, position, size, and table format are ABI/compiler-specific.


### Polymorphism

##### Static Polymorphism

**Static polymorphism** is resolved at compile time, so it is also called **compile-time polymorphism** or **early binding**. Function overloading and operator overloading are common examples.

```cpp
#include <iostream>

class Dog {};
class Cat {};

void print(const Dog&) {
	std::cout << "Dog\n";
}

void print(const Cat&) {
	std::cout << "Cat\n";
}

int main() {
	Dog dog;
	Cat cat;

	print(dog);		// Selects print(const Dog&) at compile time
	print(cat);		// Selects print(const Cat&) at compile time
}
```

The selected overload depends on the **static type**, the type known from the declaration or expression at compile time.

##### Dynamic Polymorphism

**Dynamic polymorphism** uses inheritance and virtual functions. A call through a base-class pointer or reference is selected from the object's **dynamic type**, the actual derived type at runtime. This runtime selection is **virtual dispatch**, also called **late binding**.

```cpp
#include <iostream>

class Animal {
public:
	virtual ~Animal() = default;

	virtual void print() const {
		std::cout << "Animal\n";
	}
};

class Dog : public Animal {
public:
	void print() const override {
		std::cout << "Dog\n";
	}
};

class Cat : public Animal {
public:
	void print() const override {
		std::cout << "Cat\n";
	}
};

void printAnimal(const Animal& animal) {
	animal.print();		// Virtual dispatch through the base reference
}

int main() {
	Dog dog;
	Cat cat;

	printAnimal(dog);	// Dog
	printAnimal(cat);	// Cat
}
```

| | Static Polymorphism | Dynamic Polymorphism |
| --- | --- | --- |
| Binding | Compile time | Runtime |
| Selection | Static type | Dynamic type |
| Common mechanism | Function/operator overloading | Virtual functions and overriding |
| Inheritance | Not required | Required |

An **overriding function** in a derived class provides the implementation used for a base-class virtual function. Its name, parameter-type list, and relevant qualifiers such as `const` must match the base virtual function.

`override` is not required for overriding itself. When written after the function declaration, it asks the compiler to verify that the function actually overrides a base virtual function. 

`final` can be applied to a virtual function to prevent further overriding, or to a class to prevent further derivation.

```cpp
class Base {
public:
	virtual void print() const {}
};

class Derived : public Base {
public:
	void print() const override final {}	
    // Overrides Base::print() and prevents further overriding
	// void print() override {}
	// Error: missing const, so it does not override Base::print()
};

class FurtherDerived : public Derived {
public:
	// void print() const override {}	// Error: Derived::print() is final
};
```

Runtime polymorphism normally requires an inheritance relationship, a virtual function in the base class, an overriding function in a derived class, and a call through a base pointer or reference.

A derived object can be implicitly converted to an accessible, unambiguous base pointer or reference. The reverse conversion is not implicit.

```cpp
Dog dog;
Animal* animal = &dog;			// Implicit derived-to-base conversion
animal->print();				// Dog

// Dog* dog_pointer = animal;	// Error: no implicit base-to-derived conversion
```

Copying a derived object into a concrete base object keeps only the base-class subobject. This is **object slicing**; base pointers and references preserve the dynamic type.

```cpp
Dog dog;
Animal& reference = dog;
Animal sliced = dog;

reference.print();		// Dog
sliced.print();			// Animal
```

A stable base interface lets new derived implementations be added without changing code that uses the interface. This supports the **open-closed principle**: open for extension, closed for modification. It also improves structure, readability, extensibility, and maintenance.

##### Virtual Layout

Virtual dispatch is a language feature; `vfptr` and `vftable` are compiler/ABI implementation details. In Microsoft Visual C++, virtual-function pointers refer to virtual-function tables used to bind virtual calls.

```cpp
#include <iostream>

class Base {
public:
	virtual void print() const {
		std::cout << "Base\n";
	}
};

class Derived : public Base {
public:
	void print() const override {
		std::cout << "Derived\n";
	}
};

int main() {
	Derived object;
	Base* base = &object;
	base->print();	// Derived
}
```

A simplified MSVC `/d1reportSingleClassLayout`-style representation on a 64-bit target is:

```text
class Base size(8):
	+---
 0	| {vfptr}
	+---

Base::$vftable@:
 0	| &Base::print

class Derived size(8):
	+---
	| +--- (base class Base)
 0	| | {vfptr}
	| +---
	+---

Derived::$vftable@:
 0	| &Derived::print
```

The `Base` table still contains `Base::print`. The derived object's virtual-function table has the corresponding entry for `Derived::print`; overriding does not modify the base class's table. Exact object layout, pointer placement, table contents, and table format are implementation-dependent.

##### Pure Virtual Functions

A pure virtual function is declared with `= 0`. A class with an unimplemented pure virtual function is abstract and cannot be instantiated. A derived class remains abstract until it provides a non-pure override for every inherited pure virtual function.

```cpp
#include <iostream>

class Device {
public:
	virtual ~Device() = default;
	virtual void run() const = 0;		// Pure virtual function
};

class IncompleteDevice : public Device {
	// run() is not overridden, so this class is still abstract
};

class Printer : public Device {
public:
	void run() const override {
		std::cout << "Printing\n";
	}
};

int main() {
	// Device device;					// Error: abstract class
	// IncompleteDevice incomplete;		// Error: abstract class
	Printer printer;					// Concrete class
	printer.run();
}
```

##### Virtual Destructors

Deleting an object of derived type through a base pointer requires an appropriate virtual destructor. If the base destructor is non-virtual, deleting through that base pointer has undefined behavior.

A virtual destructor may be defined or defaulted in the class. A pure virtual destructor also makes the class abstract, but it still requires a definition because the base destructor is called when a derived object is destroyed.

```cpp
#include <iostream>

class Resource {
public:
	virtual ~Resource() {
		std::cout << "Destroy Resource\n";
	}
};

class Buffer : public Resource {
public:
	Buffer()
		: data_{new int[1024]{}} {}

	~Buffer() override {
		delete[] data_;		// Release the derived-class resource
		std::cout << "Destroy Buffer\n";
	}

private:
	int* data_{};
};

int main() {
	Resource* resource = new Buffer;	// Base pointer refers to a derived object
	delete resource;		// Calls Buffer::~Buffer(), then Resource::~Resource()
}
```

Pure virtual destructor syntax:

```cpp
class Interface {
public:
	virtual ~Interface() = 0;
};

Interface::~Interface() = default;	// A pure virtual destructor still needs a definition
```

The need for a virtual destructor depends on polymorphic deletion, not on whether the derived class directly owns heap memory.

##### Example

The example combines abstract interfaces, overriding, overload resolution, derived-to-base conversion, and runtime dispatch.

```cpp
#include <iostream>

class CPU {
public:
	virtual ~CPU() = 0;		// Pure virtual destructor; CPU is abstract
	virtual void calculate() const = 0;
};

CPU::~CPU() = default;		// A pure virtual destructor still needs a definition

class GPU {
public:
	virtual ~GPU() = default;
	virtual void display() const = 0;
};

class Memory {
public:
	virtual ~Memory() = default;
	virtual void store() const = 0;
};

class IntelCPU final : public CPU {
public:
	void calculate() const override {
		std::cout << "Intel CPU\n";
	}
};

class AmdCPU final : public CPU {
public:
	void calculate() const override {
		std::cout << "AMD CPU\n";
	}
};

class NvidiaGPU final : public GPU {
public:
	void display() const override {
		std::cout << "NVIDIA GPU\n";
	}
};

class IntelGPU final : public GPU {
public:
	void display() const override {
		std::cout << "Intel GPU\n";
	}
};

class AmdMemory final : public Memory {
public:
	void store() const override {
		std::cout << "AMD memory\n";
	}
};

class NvidiaMemory final : public Memory {
public:
	void store() const override {
		std::cout << "NVIDIA memory\n";
	}
};

void runPart(const CPU& cpu) {
	cpu.calculate();		// Virtual dispatch through the CPU interface
}

void runPart(const GPU& gpu) {
	gpu.display();			// Overload selected from the static type
}

void runPart(const Memory& memory) {
	memory.store();			// Virtual dispatch through the Memory interface
}

class Computer {
public:
	Computer(CPU* cpu, GPU* gpu, Memory* memory)
		: cpu_{cpu}, gpu_{gpu}, memory_{memory} {}

	void run() const {
		runPart(*cpu_);
		runPart(*gpu_);
		runPart(*memory_);
	}

private:
	CPU* cpu_{};			// Base pointer to a CPU implementation
	GPU* gpu_{};			// Base pointer to a GPU implementation
	Memory* memory_{};		// Base pointer to a Memory implementation
};

int main() {
	IntelCPU intel_cpu;
	NvidiaGPU nvidia_gpu;
	AmdMemory amd_memory;

	AmdCPU amd_cpu;
	IntelGPU intel_gpu;
	NvidiaMemory nvidia_memory;

	Computer first{&intel_cpu, &nvidia_gpu, &amd_memory};		
    // Derived-to-base pointer conversions
	Computer second{&amd_cpu, &intel_gpu, &nvidia_memory};

	first.run();
	// Intel CPU
	// NVIDIA GPU
	// AMD memory

	second.run();
	// AMD CPU
	// Intel GPU
	// NVIDIA memory
}
```

`Computer` depends only on the abstract `CPU`, `GPU`, and `Memory` interfaces. Different derived implementations can be substituted without changing `Computer`.
