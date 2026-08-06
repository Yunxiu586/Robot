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

An operator function gives an operator meaning for class or enumeration operands.

A compound-assignment operator commonly modifies its left operand and returns it by reference. The corresponding binary operator can reuse it and return a new value.

```cpp
class Vector2 {
public:
	Vector2(int x, int y)
		: x_{x}, y_{y} {}

	Vector2& operator+=(const Vector2& other) {
		x_ += other.x_;
		y_ += other.y_;
		return *this;
	}

	friend bool operator==(const Vector2& left, const Vector2& right);

private:
	int x_{};
	int y_{};
};

Vector2 operator+(Vector2 left, const Vector2& right) {
	return left += right;
}

bool operator==(const Vector2& left, const Vector2& right) {
	return left.x_ == right.x_ && left.y_ == right.y_;
}
```

```cpp
Vector2 first{1, 2};
Vector2 second{3, 4};

Vector2 sum = first + second;
first += second;

bool equal = first == sum;
```

##### Operator Rules

An operator function must have at least one class or enumeration operand. Overloading cannot change an operator's precedence, grouping, or number of operands.

Operators including `.`, `.*`, `::`, `?:`, and `sizeof` cannot be overloaded.

### Inheritance

##### Base and Derived Classes

Inheritance creates a derived class from a base class. Public inheritance normally represents an “is-a” relationship.

```cpp
class Person {
public:
	void setName(const std::string& name) {
		name_ = name;
	}

protected:
	std::string name_{};
};

class Student : public Person {
public:
	void printName() const {
		std::cout << name_ << '\n';
	}
};

Student student;
student.setName("Alice");
student.printName();
```

A derived class cannot directly access private base members. It uses the base class's public or protected interface. Protected data exposes representation to derived classes, so private data with protected operations is usually safer when invariants matter.

##### Inheritance Access

The inheritance specifier changes the accessibility of inherited public and protected members.

| Inheritance | Public Base Members | Protected Base Members |
| --- | --- | --- |
| `public` | Remain `public` | Remain `protected` |
| `protected` | Become `protected` | Remain `protected` |
| `private` | Become `private` | Become `private` |

Private base members remain inaccessible directly from the derived class under every inheritance form.

##### Lifetime and Composition

For a most-derived object, construction initializes virtual base classes in depth-first left-to-right order, direct base classes in base-specifier order, and data members in declaration order, followed by the constructor body. Destruction occurs in the reverse order.

Use inheritance for an “is-a” relationship. Prefer composition when one type merely contains or uses another type, which represents a “has-a” relationship.

### Polymorphism

##### Virtual Dispatch

Runtime polymorphism uses virtual functions through a base reference or pointer. The function selected depends on the object's dynamic type.

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

```cpp
Dog dog;
Cat cat;

playSound(dog);					// Woof
playSound(cat);					// Meow
```

##### Object Slicing

Copying a derived object into a concrete base object keeps only the base subobject. This is object slicing.

```cpp
Dog dog;
Animal& reference = dog;			// Preserves the dynamic type
Animal sliced = dog;				// Discards the Dog part

reference.makeSound();			// Woof
sliced.makeSound();				// Animal sound
```

Prefer base references or pointers for runtime polymorphism.

##### Abstract Classes

A pure virtual function uses `= 0`. A class is abstract if at least one virtual function has a pure virtual final overrider, and an abstract class cannot be instantiated.

```cpp
class Animal {
public:
	virtual ~Animal() = default;
	virtual void makeSound() const = 0;
};

class Dog final : public Animal {
public:
	void makeSound() const override {
		std::cout << "Woof\n";
	}
};

// Animal animal;				// Error: abstract class
Dog dog;
```

A derived class remains abstract while any final overrider is pure virtual.

##### Safe Base Interfaces

Use `override` on overriding functions so the compiler checks the intended override. Use `final` when further inheritance or overriding must be prohibited.

A polymorphic base class should normally have either a public virtual destructor or a protected non-virtual destructor. Use a public virtual destructor when objects may be destroyed through a base pointer. Pass polymorphic objects by reference or pointer to preserve their dynamic type.
