# Pointers and Memory

[toc]

##### Pointers

A pointer stores an address. The unary address-of operator (`&`) obtains the address of an object, and the unary indirection operator (`*`) accesses the object at that address.

```cpp
int value = 10;
int* pointer = &value;	// Gets the address of value

std::cout << pointer << '\n';   // Stored address
std::cout << *pointer << '\n';  // Pointed-to value

*pointer = 20;			// Modifies value
```

In a declaration, `*` declares a pointer; in an expression, it dereferences a pointer.

```cpp
int* pointer = nullptr;		// Pointer declaration
// int value = *pointer; 	// Pointer dereference
```

`nullptr` is a null pointer constant convertible to any pointer type. Use it when a pointer does not refer to an object. A null pointer points to no object or function, and dereferencing it has undefined behavior.

```cpp
int* pointer = nullptr;

if (pointer != nullptr) {
    std::cout << *pointer << '\n';
}
```

An uninitialized pointer has an indeterminate value. An invalid pointer does not point to a valid object, and a dangling pointer refers to an object whose lifetime has ended. Dereferencing any of them has undefined behavior.

```cpp
int* uninitialized;  // Indeterminate value

int* dangling = nullptr;
{
    int value = 10;
    dangling = &value;
}
// *dangling is invalid here
```

| Declaration | Meaning | Modify the object | Change the address |
| --- | --- | --- | --- |
| `const int* p` | Pointer to const `int` | No | Yes |
| `int* const p` | Const pointer to `int` | Yes | No |
| `const int* const p` | Const pointer to const `int` | No | No |

```cpp
int a = 1;
int b = 2;

const int* p1 = &a;
p1 = &b;
// *p1 = 3;  // Error

int* const p2 = &a;
*p2 = 3;
// p2 = &b;  // Error

const int* const p3 = &a;
// *p3 = 4;  // Error
// p3 = &b;  // Error
```

Pointer arguments are also passed by value. The pointer parameter receives a copy of the address. Dereferencing it can modify the caller's object, but changing the parameter itself does not change the caller's pointer.

```cpp
void setByValue(int value) {
    value = 0;		// Changes only the parameter
}

void setByAddress(int* value) {
    if (value != nullptr) {
        *value = 0;	// Changes the caller's object
    }
}

int number = 10;

setByValue(number);
std::cout << number << '\n';  // 10

setByAddress(&number);
std::cout << number << '\n';  // 0
```

An array is converted to a pointer to its first element. In a function parameter, `int values[]` is adjusted to `int* values`; both forms receive the first-element address. The following version uses explicit pointer syntax and dereferencing.

```cpp
#include <cstddef>
#include <iostream>

void printValues(const int* values, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << *(values + i) << ' ';
    }
    std::cout << '\n';
}

void bubbleSort(int* values, std::size_t size) {
    for (std::size_t end = size; end > 1; --end) {
        bool swapped = false;

        for (std::size_t i = 0; i + 1 < end; ++i) {
            if (*(values + i) > *(values + i + 1)) {
                int temp = *(values + i);
                *(values + i) = *(values + i + 1);
                *(values + i + 1) = temp;
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }
}

int main() {
    int values[] = {5, 1, 4, 2, 8};
    const std::size_t size = sizeof(values) / sizeof(values[0]);

    bubbleSort(values, size);
    printValues(values, size);
}
```

Pointer arithmetic is valid only within the same array and one position past its end. Do not dereference null, invalid, dangling, out-of-range, or one-past-the-end pointers.

##### Value Categories

Every expression has a value category. The fundamental categories are `lvalue`, `xvalue`, and `prvalue`; `glvalue` and `rvalue` group these categories. Value categories affect language rules such as reference binding.

- `glvalue` (generalized lvalue): an expression whose evaluation determines the **identity** of an object or function. Identity means which specific object or function is being referred to, so it can be distinguished from others; this is commonly associated with a stable object location. A glvalue is either an `lvalue` or an `xvalue`.
- `rvalue`: an expression that is either a `prvalue` or an `xvalue`. It represents a value that can be used for initialization or computation, or an object whose resources can be reused. An rvalue does not necessarily lack identity because an `xvalue` is also a glvalue.
- `lvalue`: a glvalue that is not an xvalue. It normally refers to an object or function with an established identity. A named variable is typically an lvalue, but having a name is not the definition; for example, `*pointer` is also an lvalue.
- `prvalue` (pure rvalue): an expression whose evaluation initializes an object or computes a value. Literals and most arithmetic results are common prvalues.
- `xvalue` (expiring value): a glvalue that denotes an object or bit-field whose resources can be reused, usually because the object is near the end of its lifetime. A cast to an rvalue reference type can produce an xvalue.

```cpp
int value = 10;
int* pointer = &value;

value;                      // lvalue: refers to the specific object value
*pointer;                   // lvalue: refers to the object pointed to by pointer
10;                         // prvalue: computes the value 10
value + 1;                  // prvalue: computes a new value
static_cast<int&&>(value);  // xvalue: still refers to value, but resources may be reused
```

##### References

A reference is an alias for an existing object. It must be initialized, and it cannot later be changed to refer to another object. Assignment through a reference modifies the referred-to object.

```cpp
int value = 10;
int another = 20;

// int& reference;       // Error: no initializer
int& reference = value;

reference = another;     // Assigns 20 to value; does not rebind reference
std::cout << value << '\n';  // 20
```

A const reference provides read-only access through the reference. It is commonly used for function parameters that should not copy or modify an argument.

```cpp
void printText(const std::string& text) {
    std::cout << text << '\n';
    // text += "!";  // Error: text is read-only
}
```

A non-const lvalue reference cannot bind to a temporary. A const lvalue reference and an rvalue reference can bind to a temporary. The lifetime of a temporary bound to a reference can be extended to the lifetime of the reference, subject to specific exceptions such as reference parameters in function calls.

```cpp
int value = 10;

int& lvalue_reference = value;       // Binds to a modifiable lvalue
// int& invalid = 10;                // Error: cannot bind to a temporary

const int& const_reference = 10;     // Binds to a read-only temporary
int&& rvalue_reference = 10;         // Binds to a modifiable temporary
// int&& invalid = value;            // Error: cannot bind to an lvalue

lvalue_reference = 20;
rvalue_reference = 30;
// const_reference = 20;             // Error: read-only
```

A function may return a reference to an existing object whose lifetime continues after the call. A call to a function returning `T&` is an lvalue, so it can appear on the left side of an assignment.

```cpp
int& larger(int& first, int& second) {
    return first > second ? first : second;
}

int first = 10;
int second = 20;

larger(first, second) = 0;  // Modifies second
```

Do not return a reference to a local automatic variable because the object is destroyed when the function returns.

```cpp
int& invalidReference() {
    int value = 10;
    return value;  // Wrong: returns a dangling reference
}
```

```cpp
int& validReference() {
    static int value = 10;
    return value;  // Correct: value has static storage duration
}
```

For understanding, a reference has non-reseatable behavior similar to a const pointer.

```cpp
int value = 10;

int& reference = value;
int* const pointer = &value;

reference = 20;  // Modifies value directly
*pointer = 30;   // Requires explicit dereferencing
```

References provide alias syntax without explicit dereferencing. They are commonly used to modify caller-owned objects, avoid copies with `const T&`, and return existing objects.

##### Move Semantics

Move semantics allow resources to be transferred from an object that can be treated as an rvalue instead of copying those resources.

`std::move` is defined in `<utility>`. It does not move an object by itself; it casts its argument to an xvalue so that move-aware overloads can be selected.

```cpp
#include <iostream>
#include <string>
#include <utility>

int main() {
	std::string source{"example"};
	std::string copied{source};				// Deep copy
	std::string moved{std::move(source)};	// Move

	std::cout << copied << '\n';	// example
	std::cout << moved << '\n';		// example

	source = "reset";				// Assign before relying on its value again
    
    std::cout << copied << '\n';	// example
	std::cout << moved << '\n';		// example
}
```

For standard-library types, an object moved from remains valid, but its value is generally unspecified unless the type documents a stronger guarantee.

A named rvalue-reference variable is an lvalue expression. Use `std::move` when its resources should be transferred again.

```cpp
#include <string>
#include <utility>

void consume(std::string&& text) {
	std::string local{std::move(text)};
}
```

Use `std::move` when ownership or resources should explicitly move to another scope. Do not add it to a local return value solely to force a move.

```cpp
std::string makeName() {
	std::string name{"Alice"};
	return name;	// Do not write: return std::move(name);
}
```

##### Structs, Enums, and Unions

A `struct` defines a user-defined type that groups related members. Its members are public by default.

A named structure type can be defined first and used to create objects later. In C++, the `struct` keyword does not need to be repeated when declaring objects.

```cpp
struct Student {
    std::string name;
    int age{};
};

Student alice{"Alice", 20};
```

Use the member access operator (`.`) to access or modify a member of a structure object.

```cpp
Student student{"Alice", 20};
student.age = 21;
student.name = "Bob";
```

Objects can also be declared with the structure definition.

```cpp
struct Point {
    double x{};
    double y{};
} origin{}, target{3.0, 4.0};
```

An unnamed structure can create objects, but its type cannot later be named and reused.

```cpp
struct {
    std::string title;
    int pages{};
} book{"C++ Basics", 200};
```

A structure array stores structure objects of the same type. Access an element with `[]`, then access one of its members with `.`.

```cpp
Student students[3] = {
    {"Alice", 20},
    {"Bob", 21},
    {"Carol", 19}
};

students[0].age = 21;
students[1] = Student{"David", 22};

for (const Student& current : students) {
    std::cout << current.name << ' '
              << current.age << '\n';
}
```

A pointer can point to a structure object. For a structure pointer, `pointer->member` is equivalent to `(*pointer).member`.

```cpp
Student student{"Alice", 20};
Student* pointer = &student;

std::cout << pointer->name << '\n';	// Alice
pointer->age = 21;
(*pointer).name = "Bob";
```

A structure can contain an object of another structure type as a member.

```cpp
struct Address {
    std::string city;
    int postal_code{};
};

struct Employee {
    std::string name;
    Address address;
};

Employee employee{"Alice", {"Nanjing", 210000}};

std::cout << employee.address.city << '\n';
employee.address.city = "Shanghai";
```

A structure can also contain member functions.

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
##### Memory Model and RAII

C++ specifies storage duration and object lifetime rather than a fixed physical memory layout. The following four-region model is a common implementation; exact sections depend on the compiler and operating system.

After compilation, a typical executable contains code and data-related sections. The loader maps them into process memory when the program starts.

| Region | Common Contents | Characteristics |
| --- | --- | --- |
| Code area | Compiled machine instructions | Commonly read-only and may be shared by processes running the same program |
| Global area | Global variables, static variables, string literals, and namespace-scope `const` objects | Static storage duration; exists for the program lifetime |

```cpp
int global_value = 10;
const int global_limit = 100;
const char* message = "hello";

void countCalls() {
    static int calls = 0;
    ++calls;
}
```

`global_value`, `global_limit`, `message`, and `calls` have static storage duration. Their storage remains available until program termination; the operating system reclaims the process memory afterward.

During execution, automatic and dynamic storage are commonly represented by the stack and heap.

| Region | Common Contents | Characteristics |
| --- | --- | --- |
| Stack area | Function parameters and local automatic variables | Storage is created and released automatically as blocks and function calls begin and end |
| Heap or free store | Objects and arrays created with `new` | Storage remains allocated until released with `delete` or `delete[]` |

```cpp
void printNext(int parameter) {
    int local_value = parameter + 1;
    std::cout << local_value << '\n';
}
```

`parameter` and `local_value` have automatic storage duration. 

Do not return a pointer or reference to a local automatic variable because its lifetime ends when the function returns.

```cpp
int* invalidAddress() {
    int value = 10;
    return &value;  // Wrong: value no longer exists after return
}
```

Use `new` to create a single object in dynamic storage and `delete` to release it.

```cpp
int* value = new int{10};

std::cout << *value << '\n';

delete value;
value = nullptr;
```

Use `new[]` to create a dynamic array and `delete[]` to release it.

```cpp
int* values = new int[3]{1, 2, 3};

for (int i = 0; i < 3; ++i) {
    std::cout << values[i] << ' ';
}

delete[] values;
values = nullptr;
```

Match `new` with `delete` and `new[]` with `delete[]`. 

Failing to release dynamic storage causes a memory leak while the program runs. The operating system normally reclaims process memory at termination, but it does not replace correct resource management.

Modern C++ uses Resource Acquisition Is Initialization (RAII): an object owns a resource and releases it in its destructor. Prefer standard containers and smart pointers for ownership instead of manual `new` and `delete`.

##### Smart Pointers

Smart pointers are RAII types defined in `<memory>`. They represent ownership and automatically release the owned object.

Prefer `std::unique_ptr` for exclusive ownership; use `std::shared_ptr` when ownership must be shared. Raw pointers and references normally represent non-owning access.

| Type | Ownership | Copyable | Movable |
| --- | --- | --- | --- |
| `std::unique_ptr<T>` | Exclusive | No | Yes |
| `std::shared_ptr<T>` | Shared | Yes | Yes |
| `std::weak_ptr<T>` | Non-owning observer of shared ownership | Yes | Yes |

**`std::unique_ptr`**

`std::unique_ptr` owns one object and destroys it when the pointer is destroyed or reset.

**Creation**

- `make_unique<T>(args...)` creates a `T` and returns a `unique_ptr<T>`
- `make_unique<T[]>(size)` creates a dynamically allocated array
- Prefer `make_unique` to an explicit `new` when creating an owned object

```cpp
template<class T, class... Args>
std::unique_ptr<T> make_unique(Args&&... args);

template<class T>
std::unique_ptr<T> make_unique(std::size_t size);  // T is U[]
```

```cpp
#include <memory>
#include <string>

int main() {
	auto number = std::make_unique<int>(42);
	auto text = std::make_unique<std::string>("hello");
	auto values = std::make_unique<int[]>(3);

	values[0] = 10;
	values[1] = 20;
	values[2] = 30;
}
```

**Access and Modification**

- `operator*` and `operator->` access the owned object
- `operator[]` accesses an element of `unique_ptr<T[]>`
- `get()` returns the stored pointer without releasing ownership
- `operator bool()` tests whether a pointer is stored
- `release()` returns the stored pointer and releases ownership
- `reset()` replaces the owned object or makes the `unique_ptr` empty
- `swap()` exchanges the stored pointers

```cpp
using pointer = typename std::unique_ptr<T>::pointer;

T& operator*() const;
pointer operator->() const noexcept;
pointer get() const noexcept;
explicit operator bool() const noexcept;

pointer release() noexcept;
void reset(pointer p = pointer{}) noexcept;
void swap(std::unique_ptr& other) noexcept;

// std::unique_ptr<T[]>
T& operator[](std::size_t index) const;
```

```cpp
#include <iostream>
#include <memory>
#include <utility>

int main() {
	auto first = std::make_unique<int>(10);
	auto second = std::make_unique<int>(20);

	std::cout << *first << '\n';					// 10
	std::cout << *first.get() << '\n';				// 10
	std::cout << static_cast<bool>(first) << '\n';	// 1

	first.swap(second);
	std::cout << *first << '\n';					// 20

	std::unique_ptr<int> third{first.release()};
	std::cout << (first == nullptr) << '\n';		// 1
	std::cout << *third << '\n';					// 20

	third.reset();
	std::cout << (third == nullptr) << '\n';		// 1

	auto values = std::make_unique<int[]>(3);
	values[1] = 42;
	std::cout << values[1] << '\n';					// 42
}
```

`release()` transfers responsibility for the returned raw pointer. Use it only when ownership must be transferred through a raw-pointer interface.

**`std::shared_ptr`**

`std::shared_ptr` implements shared ownership. The managed object is destroyed when the last owning `shared_ptr` releases it.

**Creation**

- `make_shared<T>(args...)` creates a `T` and returns a `shared_ptr<T>`
- `make_shared<T[]>(size)` creates a dynamically allocated array since C++20
- Copying a `shared_ptr` shares ownership; moving transfers one owner's handle

```cpp
template<class T, class... Args>
std::shared_ptr<T> make_shared(Args&&... args);

template<class T>
std::shared_ptr<T> make_shared(std::size_t size);  // T is U[], since C++20
```

```cpp
#include <memory>
#include <string>

int main() {
	auto first = std::make_shared<std::string>("hello");
	auto second = first;
	auto values = std::make_shared<int[]>(3);

	values[0] = 10;
	values[1] = 20;
	values[2] = 30;
}
```

**Access and Modification**

- `operator*` and `operator->` access the managed object
- `operator[]` accesses an element of `shared_ptr<T[]>`
- `get()` returns the stored pointer without changing ownership

```cpp
T& operator*() const noexcept;
T* operator->() const noexcept;
T* get() const noexcept;

// std::shared_ptr<T[]>
T& operator[](std::ptrdiff_t index) const;
```

**Observation and Modification**

- `use_count()` returns the number of `shared_ptr` owners
- `operator bool()` tests whether a pointer is stored
- `reset()` releases this owner's current ownership
- `swap()` exchanges the stored pointers and ownership state

```cpp
long use_count() const noexcept;
explicit operator bool() const noexcept;

void reset() noexcept;
template<class Y>
void reset(Y* p);
void swap(std::shared_ptr& other) noexcept;
```

```cpp
#include <iostream>
#include <memory>

int main() {
	auto first = std::make_shared<int>(10);
	auto second = first;

	std::cout << *first << '\n';					// 10
	std::cout << *first.get() << '\n';				// 10
	std::cout << first.use_count() << '\n';			// 2

	first.reset();
	std::cout << static_cast<bool>(first) << '\n';	// 0
	std::cout << second.use_count() << '\n';		// 1

	auto third = std::make_shared<int>(30);
	second.swap(third);
	std::cout << *second << '\n';					// 30
}
```

Prefer `make_shared` when creating a new shared object. The raw-pointer `reset(Y*)` overload is mainly useful when adopting an existing owning pointer.

**`std::weak_ptr`**

`std::weak_ptr` observes an object managed by `std::shared_ptr` without owning it. It cannot access the object directly; use `lock()` to obtain temporary shared ownership.

**Creation**

Common construction forms include:

```cpp
std::weak_ptr<T>();
std::weak_ptr<T>(const std::weak_ptr<T>& other);
std::weak_ptr<T>(std::weak_ptr<T>&& other) noexcept;

template<class Y>
std::weak_ptr<T>(const std::shared_ptr<Y>& owner) noexcept;
```

**Observation and Modification**

- `use_count()` returns the number of `shared_ptr` owners
- `expired()` tests whether the managed object has already been destroyed
- `lock()` returns a `shared_ptr`; it is empty if the object has expired
- `reset()` makes the `weak_ptr` empty
- `swap()` exchanges observed ownership states

```cpp
long use_count() const noexcept;
bool expired() const noexcept;
std::shared_ptr<T> lock() const noexcept;

void reset() noexcept;
void swap(std::weak_ptr& other) noexcept;
```

```cpp
#include <iostream>
#include <memory>

int main() {
	auto owner = std::make_shared<int>(42);
	std::weak_ptr<int> observer = owner;

	std::cout << observer.use_count() << '\n';		// 1
	std::cout << observer.expired() << '\n';		// 0

	if (auto current = observer.lock()) {
		std::cout << *current << '\n';				// 42
	}

	owner.reset();
	std::cout << observer.expired() << '\n';		// 1
	std::cout << static_cast<bool>(observer.lock()) << '\n';	// 0

	observer.reset();
}
```

A `weak_ptr` can be used to break cycles of shared ownership.

```cpp
struct Node {
	std::shared_ptr<Node> next;
	std::weak_ptr<Node> previous;	// Does not participate in ownership
};
```

Use `get()` only when an API needs the underlying raw pointer without taking ownership. Do not `delete` a pointer obtained from `get()`.
