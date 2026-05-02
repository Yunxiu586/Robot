# Function Template

A **function template** is a blueprint for generating functions. It allows you to write one generic function that works with different data types.

Instead of writing separate functions for `int`, `double`, `std::string`, and other types, you can write a single template function.

[toc]

##### Basic Syntax

```cpp
template <typename T>
T functionName(T parameter) {
    // function body
}
```

You can also use `class` instead of `typename`:

```cpp
template <class T>
T functionName(T parameter) {
    // function body
}
```

In function templates, `typename` and `class` are usually equivalent.

##### Template Type Parameter

A template type parameter represents a type that will be determined later.

```cpp
template <typename T>
void printValue(T value) {
    std::cout << value << std::endl;
}
```

```cpp
printValue(10);        // T is int
printValue(3.14);      // T is double
printValue("hello");   // T is const char*
```

The compiler automatically deduces the type of `T` from the argument.



Usually, the compiler deduces the template type automatically.

```cpp
printValue(100); // T is deduced as int
```

You can also specify the type explicitly.

```cpp
printValue<int>(100);
printValue<double>(100);
```

In the second call, `100` is converted to `double`.



A function template can have more than one template parameter.

```cpp
template <typename T, typename U>
void printPair(T first, U second) {
    std::cout << first << " " << second << std::endl;
}
```

`T` and `U` are template types, which are automatically deduced by the compiler based on the arguments you pass in. The type of the parameter `first` is `T`, and the type of the parameter `second` is `U`.

```cpp
printPair(1, 3.14);          // T is int, U is double
printPair("age", 20);        // T is const char*, U is int
```



##### Return Type with Multiple Types

When parameters have different types, the return type may need special handling.

Using `auto`

```cpp
template <typename T, typename U>
auto add(T a, U b) {
    return a + b;
}
```

```cpp
auto result = add(10, 2.5); // result is double
```

The compiler deduces the return type from the expression `a + b`.

##### Function Template Overloading

Function templates can be overloaded, just like normal functions.

```cpp
template <typename T>
void print(T value) {
    std::cout << "Generic: " << value << std::endl;
}

void print(int value) {
    std::cout << "Integer: " << value << std::endl;
}
```

```cpp
print(10);      // calls non-template function
print(3.14);    // calls template function
```

When both a normal function and a function template match, the normal function is usually preferred.

##### Template Specialization

Template specialization allows you to provide a specific implementation for a specific type.

```cpp
template <typename T>
void display(T value) {
    std::cout << "Generic value: " << value << std::endl;
}

template <>
void display<const char*>(const char* value) {
    std::cout << "C-string: " << value << std::endl;
}
```

```cpp
display(42);
display("hello");
```

Output

```text
Generic value: 42
C-string: hello
```

Specialization is useful when a certain type needs different behavior.