# A*

[toc]

##### Problem

Let the search problem be represented as a weighted graph

$$
G=(V,E)
$$

where $V$ is the set of vertices or states, $E$ is the set of directed or undirected edges, and

$$
c(u,v) \geq 0
$$

is the transition cost from node $u$ to node $v$.

Given a start node $s$ and a goal node $t$, the objective is to find a path

$$
P=(s,\ldots,t)
$$

that minimizes the total path cost

$$
C(P)=\sum_{(u,v)\in P} c(u,v)
$$

##### Definition

**A\*** is an informed graph-search algorithm for finding a minimum-cost path from a start node to a goal node. It evaluates each candidate node by
$$
f(n)=g(n)+h(n)
$$

where

$$
g(n)
$$

is the exact accumulated cost from the start node to node $n$,

$$
h(n)
$$

is the heuristic estimate of the remaining cost from node $n$ to a goal node, and

$$
f(n)
$$

is the estimated total cost of a solution path passing through node $n$.

A* expands the node with the smallest current value of $f(n)$.

##### A* Search Algorithm

A* usually maintains the following structures.

- **Open set** $\mathcal{P}$ stores the frontier nodes that have been discovered but not yet expanded. A priority queue is commonly used to retrieve the node in the open set with the minimum $f(n)$.
- **Closed set** $\mathcal{C}$ stores the nodes already expanded.
- Parent pointer stores the predecessor of each node for path reconstruction.
- Cost table stores the best known value of $g(n)$ for each node.

```pseudocode
A*(G, s, t):
    P.push(s, h(s));
    C <- empty;

    g(s) <- 0;
    f(s) <- h(s);
    parent(s) <- null;

    while not P.empty() do
        n <- P.top();
        P.pop();

        if C.contains(n) then
            continue;
        C.insert(n);

        if n is t then
            return ReconstructPath(parent, t);
            
        for each neighbor m of n do
            if m is invalid or occupied then
                continue;
            tentative_g <- g(n) + c(n, m);
            if g(m) is undefined or tentative_g < g(m) then
                parent(m) <- n;
                g(m) <- tentative_g;
                f(m) <- g(m) + h(m);
                P.push(m, f(m));

    return empty;
```

##### Heuristic Function

A useful heuristic should be:

- **Informative** : close to the true remaining cost.
- **Admissible** : never overestimates the optimal remaining cost.
- **Consistent ** : satisfies a triangle-inequality condition over graph edges.
- **Efficient** : cheap to compute compared with the search itself.

Let $h^*(n)$ denote the true optimal cost from node $n$ to a goal node. A heuristic is **admissible** if
$$
0 \leq h(n) \leq h^*(n)
$$

for every node $n$. This means that $h(n)$ is optimistic. It may underestimate the true remaining cost, but it must not overestimate it.

With an admissible heuristic, A* can preserve optimality under standard assumptions.

A heuristic is **consistent** if, for every edge $(n,m)$,

$$
h(n) \leq c(n,m)+h(m)
$$

and

$$
h(t)=0
$$

for every goal node $t$.

##### demo

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

struct Node {
    int x, y;
    double f;   // Estimated total cost through the current node.

    bool operator>(const Node &other) const { return f > other.f; }
    // The first const means that other cannot be modified.
    // The second const means that this function cannot modify the current Node object.
};

struct PairHash {
    size_t operator()(const pair<int,int> &p) const noexcept {
        return hash<long long>()(((long long)p.first << 32) ^ (long long)p.second);
    }
};
/*
PairHash is a custom hash function for std::pair<int, int>, since
std::unordered_map does not provide a default hash for pair keys.

It combines the two integer coordinates into a 64-bit value:
    the first integer is cast to long long and shifted left by 32 bits;
    the second integer is merged using bitwise XOR (^).

The combined value is then hashed by std::hash<long long>.
*/

vector<pair<int,int>> astar(pair<int,int> start, pair<int,int> goal, const vector<vector<int>> &grid) {
    int rows = grid.size();
    int cols = grid[0].size();

    auto heuristic = [&](pair<int,int> a, pair<int,int> b) {
        // Euclidean distance heuristic.
        return sqrt((a.first - b.first) * (a.first - b.first) +
                    (a.second - b.second) * (a.second - b.second));
    };

    // Min-priority queue ordered by f-score.
    priority_queue<Node, vector<Node>, greater<Node>> open_set;

    unordered_map<pair<int,int>, pair<int,int>, PairHash> came_from;
    unordered_map<pair<int,int>, double, PairHash> g_score;
    set<pair<int,int>> visited;

    g_score[start] = 0.0;
    open_set.push({start.first, start.second, heuristic(start, goal)});

    // 8-connected grid motion.
    vector<pair<int,int>> dirs = {
        {1,0}, {-1,0}, {0,1}, {0,-1},
        {1,1}, {-1,1}, {-1,-1}, {1,-1}
    };

    while (!open_set.empty()) {
        Node current = open_set.top();
        open_set.pop();

        pair<int,int> cur = {current.x, current.y};

        // Skip nodes that have already been expanded.
        if (visited.count(cur)) continue;
        visited.insert(cur);

        if (cur == goal) {
            vector<pair<int,int>> path;

            // Reconstruct the path from goal to start.
            while (came_from.find(cur) != came_from.end()) {
                path.push_back(cur);
                cur = came_from[cur];
            }

            path.push_back(start);
            reverse(path.begin(), path.end());

            return path;
        }

        for (auto &d : dirs) {
            int nx = cur.first + d.first;
            int ny = cur.second + d.second;

            // Check map bounds.
            if (nx < 0 || nx >= cols || ny < 0 || ny >= rows) continue;

            // Skip occupied cells.
            if (grid[ny][nx] != 0) continue;

            pair<int,int> neighbor = {nx, ny};

            // Movement cost is 1 for straight moves and sqrt(2) for diagonal moves.
            double tentative_g = g_score[cur] + sqrt(d.first * d.first + d.second * d.second);

            // Update the node if a better path is found.
            if (!g_score.count(neighbor) || tentative_g < g_score[neighbor]) {
                g_score[neighbor] = tentative_g;

                double f = tentative_g + heuristic(neighbor, goal);
                open_set.push({nx, ny, f});

                came_from[neighbor] = cur;
            }
        }
    }

    return {};
}
```

