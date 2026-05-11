# TopoTraj

[toc]

### Abstract

Gradient-based trajectory optimization (GTO) has gained wide popularity for quadrotor trajectory replanning. However, it suffers from local minima, which is not only fatal to safety but also unfavorable for smooth navigation.

The paper proposes a replanning method based on GTO addressing this issue systematically. A path-guided optimization (PGO) approach is devised to tackle infeasible local minima, which improves the replanning success rate significantly.

A topological path searching algorithm is developed to capture a collection of distinct useful paths in 3-D environments, each of which then guides an independent trajectory optimization. It activates a more comprehensive exploration of the solution space and outputs superior replanned trajectories.

### Path-Guided Trajectory Optimization

##### Optimization Failure Analysis

GTO formulates trajectory replanning as a non-linear optimization problem that trades off smoothness, safety, and dynamically feasibility.

Typical GTO methods incorporate the gradients of a Euclidean signed distance field in a collision cost to push the trajectory out of obstacles.

If a trajectory is in collision and crosses “valleys” or “ridges” in the ESDF, the gradients of ESDF change abruptly, and gradients of the objective function push different parts of the trajectory in opposing directions.

Therefore, optimization depending solely on the ESDF fails inevitably at times. Extra information is introduced to produce an objective function whose gradients consistently deform the trajectory to the free space.

##### Problem Formulation

The trajectory segment in collision is reparameterized as a $p_b$ degree uniform B-spline with control points

$$
\{Q_i\}_{i=0}^{N}
$$

PGO consists of two different phases.

**First phase**. A geometric guiding path attracts the initial trajectory to the free space.
$$
f_{p1}
=
\lambda_{1s}f_s
+
\lambda_{1g}f_g
$$

The smoothness cost is designed as an elastic band cost function that simulates the elastic forces of a sequence of springs.

$$
f_s
=
\sum_{i=p_b-1}^{N-p_b+1}
\left\|Q_{i+1}-2Q_i+Q_{i-1}\right\|^2
$$

Each control point $Q_i$ is assigned with an associated point $G_i$ on the guiding path, which is uniformly sampled along the guiding path.

$$
f_g
=
\sum_{i=p_b}^{N-p_b}
\left\|Q_i-G_i\right\|^2
$$

This is an unconstrained quadratic programming problem, so its optimal solution can be obtained in closed form.

**Second phase**. the warmup trajectory is further refined into a smooth, safe, and dynamically feasible one.
$$
f_{p2}
=
\lambda_{2s}f_s
+
\lambda_{2c}f_c
+
\lambda_{2d}\left(f_v+f_a\right)
$$

$f_c$ is the collision cost evaluated on the ESDF.

$f_v$ and $f_a$ penalize infeasible velocity and acceleration.

The formulations of $f_c$, $f_v$, and $f_a$ are simplified based on the convex hull property of B-spline. It suffices to constrain the control points of the B-spline to ensure safety and dynamic feasibility.

###  Topological Path Searching

##### Topology Equivalence Relation

Homotopy captures insufficient useful trajectories in 3-D environments.

Visibility deformation is useful in 3-D space, but computationally expensive for equivalence checking.

Uniform visibility deformation captures abundant useful trajectories and is more efficient for equivalence checking.

Two trajectories $\tau_1(s)$ and $\tau_2(s)$ are parameterized by

$$
s\in[0\ 1]
$$

with the same start and end

$$
\tau_1(0)=\tau_2(0)
$$

$$
\tau_1(1)=\tau_2(1)
$$

They belong to the same uniform visibility deformation class if for all $s$, line $\tau_1(s)\tau_2(s)$ is collision-free.

To test UVD relation, uniformly discretize $s$ by

$$
s_i=\frac{i}{K}
$$

$$
i=0\ 1\ K
$$

and check collision for lines

$$
\tau_1(s_i)\tau_2(s_i)
$$

For piece-wise straight line paths, the path is parameterized uniformly so that

$$
\left\|
\frac{d\tau(s)}{ds}
\right\|
=
\mathrm{const}
$$

##### Topological Roadmap

A UVD roadmap $G$ captures an abundant set of paths from different UVD classes.

Two kinds of graph nodes are used: guard and connector.

Guards explore different part of the free space. Any two guards are not visible to each other.

Connectors connect different guards to form paths of the roadmap.

```pseudocode
Initialize
AddGuard(G, s), AddGuard(G, g)

while t <= tmax and Nsample <= Nmax
    ps <- Sample
    gvis <- VisibleGuards(G, ps)

    if gvis.size == 0
        AddGuard(G, ps)

    if gvis.size == 2
        path1 <- Path(gvis[0], ps, gvis[1])
        distinct <- True
        Ns <- SharedNeighbors(G, gvis[0], gvis[1])

        for each ns in Ns
            path2 <- Path(gvis[0], ns, gvis[1])
            if Equivalent(path1, path2)
                distinct <- False
                if Len(path1) < Len(path2)
                    Replace(G, ps, ns)
                break

        if distinct
            AddConnector(G, ps, gvis[0], gvis[1])
```

With the UVD roadmap, a depth-first search augmented by a visited node list is applied to search for paths between $s$ and $g$.

##### Path Shortening & Pruning

Some paths obtained from the roadmap may be detoured. Such paths are unfavorable, since in the first phase of PGO it can deform a trajectory excessively and make it unsmooth.

For each path $P_r$, a topologically equivalent shortcut path $P_s$ is found.

```pseudocode
Pd <- Discretize(Pr)
Ps <- {Pd.front}

for each pd in Pd
    ld <- Line(Ps.back, pd)

    if not LineVisib(ld)
        pb <- BlockPoint(ld)
        po <- PushAwayObs(pb, ld)
        Ps.push_back(po)

Ps.push_back(Pd.back)
```

The center of the first occupied voxel blocking the view is pushed away from obstacles in the direction orthogonal to $l_d$ and coplanar to the ESDF gradient at $p_b$.

To exclude repeated paths, the equivalence between any two paths is checked and only topologically distinct ones are preserved.

### Real-time Topological Trajectory Replanning

A segment of the global trajectory within a specific horizon is checked periodically for safety.

Once collisions are detected, topological roadmap construction is triggered within a cube determined by the start and end position of the segment and

$$
(r_x\ r_y\ r_z)
$$

Paths extracted from the roadmap are shortened and pruned. Each path invokes an independent PGO.

The number of alternative UVD classes grows exponentially with the number of obstacles, so only the first $K_{\max}$ shortest paths are selected.

Paths more than $r_{\max}$ times longer than the shortest one are excluded.

Practically,

$$
K_{\max}=5
$$

is sufficient.