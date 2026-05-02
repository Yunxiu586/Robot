# std

[toc]

##### Standard Template Library

The C++ standard library provides commonly used containers, algorithms, iterators, input/output utilities, and helper types.

STL usually refers to the container, iterator, and algorithm parts of the standard library.

|                  | Header            | Ordered                          | Duplicate Elements | Common Use                            |
| ---------------- | ----------------- | -------------------------------- | ------------------ | ------------------------------------- |
| `vector`         | `<vector>`        | Keep insertion order             | Yes                | Store a dynamic list of elements      |
| `array`          | `<array>`         | Keep fixed order                 | Yes                | Fixed-size array with STL interface   |
| `deque`          | `<deque>`         | Keep insertion order             | Yes                | Fast insertion/removal at both ends   |
| `list`           | `<list>`          | Keep insertion order             | Yes                | Frequent insertion/removal by iterator |
| `string`         | `<string>`        | Keep character order             | Yes                | Store and process text                |
| `pair`           | `<utility>`       | Not a container                  | -                  | Store coordinate, key-value-like data |
| `tuple`          | `<tuple>`         | Not a container                  | -                  | Store more than two related values    |
| `map`            | `<map>`           | Sorted by key                    | Keys are unique    | Ordered dictionary                    |
| `unordered_map`  | `<unordered_map>` | No                               | Keys are unique    | Fast average lookup                   |
| `set`            | `<set>`           | Sorted                           | No                 | Store sorted unique values            |
| `unordered_set`  | `<unordered_set>` | No                               | No                 | Fast average existence check          |
| `multiset`       | `<set>`           | Sorted                           | Yes                | Store sorted values with duplicates   |
| `multimap`       | `<map>`           | Sorted by key                    | Keys can repeat    | Multiple values for one key           |
| `queue`          | `<queue>`         | By insertion order               | Yes                | BFS                                   |
| `stack`          | `<stack>`         | By insertion order               | Yes                | DFS, simulation                       |
| `priority_queue` | `<queue>`         | Top element has highest priority | Yes                | Dijkstra, greedy algorithms           |
| `sort`           | `<algorithm>`     | Result depends on comparator     | Yes                | Sort arrays or vectors                |
| `find`           | `<algorithm>`     | -                                | -                  | Find an element in a range            |
| `accumulate`     | `<numeric>`       | -                                | -                  | Compute sum or combined value         |



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


##### array

`array` is a fixed-size container from the standard library.

Unlike a C-style array, `array` has useful member functions such as `size()`, `front()`, and `back()`.

```cpp
#include <array>
#include <iostream>
using namespace std;

int main() {
    array<int, 3> a = {1, 2, 3};

    cout << a.size() << endl;
    cout << a[0] << endl;

    for (int x : a) {
        cout << x << endl;
    }

    return 0;
}
```

Common array Operations

```cpp
array<int, 3> a = {1, 2, 3};

a.size();     // number of elements
a.empty();    // whether array is empty, false if size > 0
a.front();    // first element
a.back();     // last element
a.fill(0);    // set all elements to 0
```

##### deque

`deque` is a double-ended queue.

It supports efficient insertion and removal at both the front and the back.

```cpp
#include <deque>
#include <iostream>
using namespace std;

int main() {
    deque<int> dq;

    dq.push_back(2);
    dq.push_front(1);
    dq.push_back(3);

    cout << dq.front() << endl;  // 1
    cout << dq.back() << endl;   // 3

    dq.pop_front();
    dq.pop_back();

    return 0;
}
```

Common deque Operations

```cpp
dq.push_back(x);    // add x to the back
dq.push_front(x);   // add x to the front
dq.pop_back();      // remove the last element
dq.pop_front();     // remove the first element
dq.front();         // first element
dq.back();          // last element
dq.empty();
dq.size();
```

##### list

`list` is a doubly linked list.

It is useful when you need frequent insertion or deletion in the middle and already have an iterator to the position.

```cpp
#include <list>
#include <iostream>
using namespace std;

int main() {
    list<int> lst = {1, 2, 4};

    auto it = lst.begin();
    it++;
    lst.insert(it, 10);  // insert before the element pointed to by it

    for (int x : lst) {
        cout << x << endl;
    }

    return 0;
}
```

Common list Operations

```cpp
lst.push_back(x);
lst.push_front(x);
lst.pop_back();
lst.pop_front();
lst.insert(it, x);   // insert x before iterator it
lst.erase(it);       // erase element at iterator it
lst.front();
lst.back();
lst.empty();
lst.size();
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


##### tuple

`tuple` stores multiple values, possibly of different types.

```cpp
#include <tuple>
#include <iostream>
#include <string>
using namespace std;

int main() {
    tuple<int, string, double> student = {1, "Alice", 95.5};

    cout << get<0>(student) << endl;
    cout << get<1>(student) << endl;
    cout << get<2>(student) << endl;

    return 0;
}
```

Structured Binding

```cpp
tuple<int, string, double> student = {1, "Alice", 95.5};

auto [id, name, score] = student;
cout << id << " " << name << " " << score << endl;
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


##### multiset

`multiset` stores elements in sorted order and allows duplicates.

```cpp
#include <set>
#include <iostream>
using namespace std;

int main() {
    multiset<int> ms;

    ms.insert(3);
    ms.insert(1);
    ms.insert(3);

    cout << ms.count(3) << endl;  // 2

    for (int x : ms) {
        cout << x << endl;  // 1 3 3
    }

    return 0;
}
```

Remove One Occurrence

```cpp
auto it = ms.find(3);
// If 3 is not found, find() returns ms.end().
if (it != ms.end()) {
    ms.erase(it);  // remove only one 3
}
```

Remove All Occurrences

```cpp
ms.erase(3);  // remove all elements equal to 3
```

##### multimap

`multimap` stores key-value pairs in sorted order by key and allows duplicate keys.

```cpp
#include <map>
#include <iostream>
#include <string>
using namespace std;

int main() {
    multimap<string, int> scores;

    scores.insert({"Alice", 90});
    scores.insert({"Alice", 95});
    scores.insert({"Bob", 85});

    for (auto item : scores) {
        cout << item.first << " " << item.second << endl;
    }

    return 0;
}
```

Find All Values for One Key

```cpp
auto range = scores.equal_range("Alice");

for (auto it = range.first; it != range.second; it++) {
    cout << it->second << endl;
}
```



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
st.push(x);   // push x onto the top of the stack
st.pop();     // remove the top element from the stack
st.top();     // access the top element of the stack
st.empty();   // check whether the stack is empty
st.size();    // get the number of elements in the stack
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
q.push(x);  // add x to the back of the queue
q.pop();    // remove the front element from the queue
q.front();	// access the first element in the queue
q.back();	// access the last element in the queue
q.empty();
q.size();
```


##### Common Container Operations

Many STL containers share similar member functions.

```cpp
container.empty();   // whether the container is empty
container.size();    // number of elements
container.begin();   // iterator to the first element
container.end();     // iterator after the last element
container.clear();   // remove all elements, if supported
```

Common Complexity

| Operation            | `vector`         | `deque`   | `list`        | `set` / `map` | `unordered_set` / `unordered_map` |
| -------------------- | ---------------- | --------- | ------------- | ------------- | --------------------------------- |
| Access by index      | `O(1)`           | `O(1)`    | Not supported | Not supported | Not supported                     |
| Insert at back       | Amortized `O(1)` | `O(1)`    | `O(1)`        | -             | -                                 |
| Insert at front      | `O(n)`           | `O(1)`    | `O(1)`        | -             | -                                 |
| Search by value      | `O(n)`           | `O(n)`    | `O(n)`        | `O(log n)`    | Average `O(1)`                    |
| Erase by iterator    | `O(n)`           | `O(n)`    | `O(1)`        | `O(1)`        | Average `O(1)`                    |



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

priority_queue<
    int,          // element type
    vector<int>,  // underlying container
    greater<int>  // comparison rule
> pq;
```

| Feature               | `queue`                                    | `priority_queue`                                         |
| --------------------- | ------------------------------------------ | -------------------------------------------------------- |
| Header file           | `<queue>`                                  | `<queue>`                                                |
| Data structure idea   | First In, First Out                        | Heap-based priority container                            |
| Element removal order | Remove the earliest inserted element first | Remove the highest-priority element first                |
| Default behavior      | FIFO                                       | Max heap                                                 |
| Access element        | `q.front()`                                | `pq.top()`                                               |
| Insert element        | `q.push(x)`                                | `pq.push(x)`                                             |
| Remove element        | `q.pop()`                                  | `pq.pop()`                                               |
| Check empty           | `q.empty()`                                | `pq.empty()`                                             |
| Get size              | `q.size()`                                 | `pq.size()`                                              |
| Common use            | BFS, task scheduling in arrival order      | Dijkstra, greedy algorithms, finding max/min efficiently |

Use `queue` when elements should be processed in insertion order. 

Use `priority_queue` when elements should be processed by priority.

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


Sorting an Array

```cpp
int arr[5] = {3, 1, 4, 1, 5};

sort(arr, arr + 5);
```

Sort by Custom Rule

```cpp
vector<string> words = {"apple", "cat", "banana"};

sort(words.begin(), words.end(), [](const string& a, const string& b) {
    return a.size() < b.size();
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


More Algorithm Functions

```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v = {1, 2, 2, 3, 4};

int c = count(v.begin(), v.end(), 2);       // number of 2s
bool ok = binary_search(v.begin(), v.end(), 3);

auto lb = lower_bound(v.begin(), v.end(), 2);  // first >= 2
auto ub = upper_bound(v.begin(), v.end(), 2);  // first > 2

cout << (lb - v.begin()) << endl;
cout << (ub - v.begin()) << endl;
```

`lower_bound`, `upper_bound`, and `binary_search` require the range to be sorted.

##### numeric

Common functions from `<numeric>`:

```cpp
#include <numeric>
#include <vector>
using namespace std;

vector<int> v = {1, 2, 3, 4, 5};

int sum = accumulate(v.begin(), v.end(), 0);
```

`accumulate()` can also use a custom operation.

```cpp
int product = accumulate(v.begin(), v.end(), 1, [](int a, int b) {
    return a * b;
});
```

`iota()` fills a range with increasing values.

```cpp
vector<int> nums(5);
iota(nums.begin(), nums.end(), 1);  // 1 2 3 4 5
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


Iterator with `erase()`

When erasing elements while iterating, use the iterator returned by `erase()`.

```cpp
vector<int> v = {1, 2, 3, 4, 5};

for (auto it = v.begin(); it != v.end(); ) {
    if (*it % 2 == 0) {
        it = v.erase(it);
    } else {
        it++;
    }
}
```

Range-based for with Reference

```cpp
vector<int> v = {1, 2, 3};

for (auto& x : v) {
    x *= 2;
}
```

Use `const auto&` when you only need to read elements and want to avoid copying.

```cpp
for (const auto& x : v) {
    cout << x << endl;
}
```
