# Trajectory Smoothing

### Bézier Curve

A Bézier curve starts at the first control point and ends at the last control point, but generally does not pass through the intermediate control points. 

**Global control** : modifying any control point changes the shape of the entire curve.

An $n$th-degree Bézier curve is defined by $n+1$ control points $P_0,P_1,...,P_n$.
$$
B(t) = \sum_{i=0}^{n} {C_n^i} \cdot t^{i} \cdot (1-t)^{n-i} \cdot P_i, \quad t \in [0, 1]
$$

$$
{C_n^i} = \frac{n!}{i!(n-i)!}
$$

The $t$ is a continuous parameter representing the **positional progress** along the curve.

By sampling a series of specific $t$ values, the corresponding path point coordinates are calculated, resulting in a discrete trajectory executable by the robot. Sampling 11 points corresponds to $t=0,0.1,0.2,...,1$.



### B-spline Curve

A B‑spline curve is defined by control points, a **knot vector**, and the **degree**.

**Local support** : modifying one control point only affects the curve locally (over about “degree $+1$” knot spans), making it highly suitable for long and complex trajectories.

A B‑spline curve of degree $p$ is defined by $n+1$ control points $P_0,P_1,...,P_n$ and a knot vector $U=\{u_0,u_1,...,u_m\}$, where $m=n+p+1$.
$$
C(u) = \sum_{i=0}^{n} N_{i,p}(u) \cdot P_i
$$
$N_{i,0}(u)$ is the $p$th‑degree B‑spline basis function defined on the knot vector $U$, computed by the Cox–de Boor recurrence formula.

If $p=0$
$$
N_{i,0}(u) = 
\begin{cases}
1, & \text{if } u_i \leq u < u_{i+1} \\
0, & \text{otherwise}
\end{cases} \\
$$
If $p>0$
$$
N_{i,p}(u) = \frac{u - u_i}{u_{i+p} - u_i} N_{i,p-1}(u) + \frac{u_{i+p+1} - u}{u_{i+p+1} - u_{i+1}} N_{i+1,p-1}(u)
$$
where
$$
\sum_{i=0}^{n} N_{i,p}(u) = 1 \quad \text{for } u \in \left[u_{p}, u_{n+1}\right]
$$
**eg.** Given the knot vector $U=\{0,0,0,0,1,2,2,2\}$ and $u=0.5$, compute the cubic B-spline basis functions $N_{i,3}(u)$ for $i=0,1,2,3$ using the recurrence formula with the convention $0/0=0$.

Only $N_{3,0}(0.5)=1$ since $u∈[u_3,u_4)=[0,1).$ All others are $0$.
$$
[N_{0,0},N_{1,0},N_{2,0},N_{3,0}]_{u=0.5}=[0,0,0,1]
$$
When $p=1$, 
$$
\begin{align*}
N_{0,1}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{0-0.5}{0-0} \cdot 0 = 0 \\
N_{1,1}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{0-0.5}{0-0} \cdot 0 = 0 \\
N_{2,1}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{1-0.5}{1-0} \cdot 1 = 0.5 \\
N_{3,1}(0.5) &= \frac{0.5-0}{1-0} \cdot 1 + \frac{2-0.5}{2-1} \cdot 0 = 0.5 \\
\end{align*}
$$
then
$$
[N_{0,1},N_{1,1},N_{2,1},N_{3,1}]_{u=0.5}=[0,0,0.5,0.5]
$$
When $p=2$, 
$$
\begin{align*}
N_{0,2}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{0-0.5}{0-0} \cdot 0 = 0 \\
N_{1,2}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{1-0.5}{1-0} \cdot 0.5 = 0.25 = \frac{1}{4}\\
N_{2,2}(0.5) &= \frac{0.5-0}{1-0} \cdot 0.5 + \frac{2-0.5}{2-0} \cdot 0.5 = 0.25 + 0.375 = 0.625 = \frac{5}{8}\\
N_{3,2}(0.5) &= \frac{0.5-0}{2-0} \cdot 0.5 + \frac{2-0.5}{2-1} \cdot 0 = 0.125 = \frac{1}{8} \\
\end{align*}
$$
then
$$
[N_{0,2},N_{1,2},N_{2,2},N_{3,2}]_{u=0.5}=[0,\frac{1}{4},\frac{5}{8},\frac{1}{8}]
$$
When $p=3$, 
$$
\begin{align*}
N_{0,3}(0.5) &= \frac{0.5-0}{0-0} \cdot 0 + \frac{1-0.5}{1-0} \cdot 0.25 = 0.125 = \frac{1}{8} \\
N_{1,3}(0.5) &= \frac{0.5-0}{1-0} \cdot 0.25 + \frac{2-0.5}{2-0} \cdot 0.625 = 0.125 + 0.46875 = 0.59375 = \frac{19}{32} \\
N_{2,3}(0.5) &= \frac{0.5-0}{2-0} \cdot 0.625 + \frac{2-0.5}{2-0} \cdot 0.125 = 0.15625 + 0.09375 = 0.25 = \frac{1}{4} \\
N_{3,3}(0.5) &= \frac{0.5-0}{2-0} \cdot 0.125 + \frac{2-0.5}{2-1} \cdot 0 = 0.03125 = \frac{1}{32}
\end{align*}
$$
then
$$
[N_{0,3},N_{1,3},N_{2,3},N_{3,3}]_{u=0.5}=[\frac{1}{8},\frac{19}{32},\frac{1}{4},\frac{1}{32}]
$$
The computed values of the basis functions are below.

| $u$  | $N_{0,3}(u)$ | $N_{1,3}(u)$ | $N_{2,3}(u)$ | $N_{3,3}(u)$ |
| :--: | :----------: | :----------: | :----------: | :----------: |
| 0.0  |    1.0000    |    0.0000    |    0.0000    |    0.0000    |
| 0.5  |    0.0625    |    0.5625    |    0.3750    |    0.0000    |
| 1.0  |    0.0000    |    0.1667    |    0.6667    |    0.1667    |
| 1.5  |    0.0000    |    0.0208    |    0.4792    |    0.5000    |
| 2.0  |    0.0000    |    0.0000    |    0.0000    |    1.0000    |

Through the following calculations, 5 points on the B-spline curve are derived.
$$
\begin{align*}
C(0) = \sum_{i=0}^{3} N_{i,p}(0) \cdot P_i	\\
C(0.5) = \sum_{i=0}^{3} N_{i,p}(0) \cdot P_i	\\
C(1.0) = \sum_{i=0}^{3} N_{i,p}(0) \cdot P_i	\\
C(1.5) = \sum_{i=0}^{3} N_{i,p}(0) \cdot P_i	\\
C(2.0) = \sum_{i=0}^{3} N_{i,p}(0) \cdot P_i
\end{align*}
$$

### astar_bsline

```python
def astar(start, goal, grid):
    rows, cols = grid.shape
    open_set = []	# a priority queue that stores the nodes to be explored
    # each element is a tuple (f_score, node)
    # f_score = g_score + h_score, node is the node coordinate (x, y)
    heapq.heappush(open_set, (0, start))	# push the start node into the priority queue with f_score = 0
    came_from = {}			# record the parent of each node for path reconstruction
    g_score = {start: 0}	# record the actual cost g_score from the start to each node

    def heuristic(a, b):
        # return Euclidean distance
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    visited = set()
    while open_set:
       	# pop the node with the smallest f_score
    	# f_score is received by _, current receives the node coordinate
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue			# skip if already visited
        visited.add(current)	# mark as visited

        # if the current node is the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]	# reverse the path to go from start to goal

        # explore all neighbors of the current node
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            # accessing grid must be [y, x] because of NumPy's indexing order
            # check if the neighbor is within bounds and not an obstacle
            if (0 <= neighbor[0] < cols and 0 <= neighbor[1] < rows and grid[neighbor[1], neighbor[0]] == 0):
                # compute the actual cost from start to neighbor
                # movement cost from current to neighbor is sqrt(dx^2+dy^2)
                tentative_g = g_score[current] + math.sqrt(dx**2 + dy**2)
                # if the neighbor hasn't been explored, or a smaller g_score is found
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current		# record parent node
                    g_score[neighbor] = tentative_g		# update g_score
                    f_score = tentative_g + heuristic(neighbor, goal)	# ompute f_score
                    heapq.heappush(open_set, (f_score, neighbor))	# add the neighbor to the priority queue
    return None
```



```python
def compute_angles(points):
    """calculate the turning angle (in radians) for each point, straight ≈ 0"""
    points = np.asarray(points, dtype=float)
    n = len(points)
    if n < 3:
        # degenerate case, set all to π, meaning all are retained
        return np.array([np.pi] * n, dtype=float)
    
    angles = np.empty(n, dtype=float)
    # starting point has no previous point, so vector v1 cannot be calculated
    # setting it to π (maximum value) ensures retention during simplification
    angles[0] = np.pi	# considered a corner
    # ending point has no subsequent point, so vector v2 cannot be calculated
    angles[-1] = np.pi	# end point set to π
    
    for i in range(1, n - 1):
        v1 = points[i]   - points[i - 1]	# previous segment vector
        v2 = points[i+1] - points[i]		# next segment vector
        n1 = np.linalg.norm(v1)				# vector length
        n2 = np.linalg.norm(v2)
        if n1 < 1e-12 or n2 < 1e-12:		# avoid division by zero
            angles[i] = 0.0
            continue
        cos_angle = np.dot(v1, v2) / (n1 * n2)		# cosine value
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angles[i] = np.arccos(cos_angle)			# arccos to get angle in radians
    return angles
```



```python
def simplify_path(points, corner_deg=30, corner_dilate=1):
    """
    Enhanced simplification : compresses straight segments while preserving corners
    
    Args:
        points: Path point set
        corner_deg: Minimum turning angle considered a "corner", recommended 20 ~ 45
        corner_dilate: Dilate corner indices by ±k to avoid corridor gaps at corners
    """
    points = np.asarray(points, dtype=float)
    n = len(points)
    if n <= 2:
        return points.copy()

    # select corners using angle threshold
    angles = compute_angles(points)
    theta = np.deg2rad(corner_deg)     
    # find indices where turning angle exceeds threshold
    corner_idx = np.where(angles >= theta)[0] 
    # np.concatenate joins [0], corner_idx, [n-1]
    # np.unique removes duplicates and sorts
    corner_idx = np.unique(np.concatenate(([0], corner_idx, [n-1])))

    # dilate corner indices to reduce corridor gaps
    if corner_dilate > 0:
        extra = []
        for idx in corner_idx:
            # expand each corner point to include ±corner_dilate neighboring points
            for j in range(idx - corner_dilate, idx + corner_dilate + 1):
                if 0 <= j < n:	# check if j is within the valid range of indices [0, n-1]
                    extra.append(j)
        corner_idx = np.unique(np.concatenate((corner_idx, np.array(extra, dtype=int))))

    out = points[corner_idx]  # extract corner points
    return np.array(out, dtype=float)
```



```python
def bsline_smoothing(points, num_points=200, smooth_factor=0.5):
    """
    Enhanced B-spline smoothing with arc-length parameterization and smoothing factor
    
    Args:
        points: Set of path points
        num_points: Number of output points
        smooth_factor: Smoothing factor. 0 for exact interpolation (passing through all points), 
                      larger values yield smoother curves.
    """
    points = np.array(points, dtype=float)
    if len(points) < 4:  # Less than 4 points cannot form a cubic B-spline
        return points

    # splprep expects coordinates in (M, N) shape
    # where M is dimension (x,y) and N is number of points
    points_t = points.T  

    """
    splprep minimizes the following objective function:
        J = Σ |P_i - C(u_i)|² + s * ∫ |C''(t)|² dt
    
    Where:
        Σ |P_i - C(u_i)|² (fitting term):
            P_i is the i-th input point.
            C(u_i) is the point on the B-spline curve at parameter u_i.
            This term measures the sum of squared distances between input points and the curve.
            Smaller values make the curve adhere more closely to the original points.

        ∫ |C''(t)|² dt (smoothness term):
            C''(t) is the second derivative (curvature) of the curve.
            This term measures the total bending energy of the curve.
            Smaller values produce smoother, less curved paths.

        s (smoothing factor):
            Balances the two objectives.
            s = 0: Only fitting term matters → exact interpolation through all points, potentially jagged curves.
            s > 0: Trade-off between fitting accuracy and smoothness. Larger s prioritizes smoothness.
            s → ∞: Overwhelming emphasis on smoothness → approaches a straight line.
    """
    """
    tck: Tuple containing spline representation
        t - knot vector: Non-decreasing sequence with k+1 repeated knots at ends for cubic splines (k=3)
        c - control points
        k - spline degree
    """
    # create B-spline representation using splprep
    # s is the smoothing factor, k=3 indicates cubic spline
    tck, u = splprep(points_t, s=smooth_factor, k=3)

    # evaluate spline at new parameter points
    u_new = np.linspace(0, 1, num_points)
    x_new, y_new = splev(u_new, tck)

    return np.column_stack((x_new, y_new))
```



```python
grid = np.zeros((60, 80))
grid[0:40, 15:19] = 1   # obstacle
grid[20:60, 30:33] = 1
grid[40:43, 40:60] = 1

start = (0, 0)
goal = (79, 58)

path = astar(start, goal, grid)
if path is None:
    raise RuntimeError("No path found by A*")
print(f"length of path: {len(path)}")

path_simplify = simplify_path(path, corner_deg=30, corner_dilate=1)  
print(f"length of path_simplify:{len(path_simplify)}") 

path_bsline = bsline_smoothing(path_simplify, round(len(path_simplify) * 1.5), smooth_factor=0.5)
print(f"length of path_bsline:{len(path_bsline)}") 

if path_bsline is None:
    raise RuntimeError("BSline Path is None!!")

path = np.array(path)
path_simplify = np.array(path_simplify)
path_bsline = np.array(path_bsline)
```

