# Graph

### BFS

Breadth-First Search (BFS) explores a graph **level by level** from a starting vertex.

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(const vector<vector<int>>& graph, int start) {
    int n = graph.size();

    vector<bool> visited(n, false);
    vector<int> distance(n, -1);
    vector<int> parent(n, -1);

    queue<int> q;

    visited[start] = true;
    distance[start] = 0;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        cout << u << " ";

        for (int v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                distance[v] = distance[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }
    }
}
```



### DFS

Depth-First Search explores a graph by going **as deep as possible** along one path before backtracking.

```cpp
#include <iostream>
#include <vector>
using namespace std;

void dfsRecursive(const vector<vector<int>>& graph,
                  int u,
                  vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";

    for (int v : graph[u]) {
        if (!visited[v]) {
            dfsRecursive(graph, v, visited);
        }
    }
}

void dfs(const vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<bool> visited(n, false);

    dfsRecursive(graph, start, visited);
}
```

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

void dfsIterative(const vector<vector<int>>& graph, int start) {
    int n = graph.size();

    vector<bool> visited(n, false);
    stack<int> st;

    st.push(start);

    while (!st.empty()) {
        int u = st.top();
        st.pop();

        if (visited[u]) {
            continue;
        }

        visited[u] = true;
        cout << u << " ";

        for (int v : graph[u]) {
            if (!visited[v]) {
                st.push(v);
            }
        }
    }
}
```

