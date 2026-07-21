# Minimum Snap

[toc]

### Polynomial Trajectory and Objective

##### Piecewise Polynomial

Given waypoints at prescribed times, the trajectory is divided into $M$ polynomial segments. For one spatial coordinate, segment $i$ is defined on $t\in[0,T_i]$ as

$$
p_i(t)=\sum_{k=0}^{n}c_{i,k}t^k
$$

Define the polynomial basis and coefficient vector

$$
\boldsymbol{\beta}(t)=
\begin{bmatrix}
1&t&t^2&\cdots&t^n
\end{bmatrix}^{T}
$$

$$
\boldsymbol{c}_i=
\begin{bmatrix}
c_{i,0}&c_{i,1}&\cdots&c_{i,n}
\end{bmatrix}^{T}
$$

Then

$$
p_i(t)=\boldsymbol{\beta}(t)^T\boldsymbol{c}_i
$$

For the standard closed-form minimum-snap formulation, each segment is commonly represented by a seventh-degree polynomial

$$
n=7
$$

Its eight coefficients match the position, velocity, acceleration, and jerk at the two endpoints. Higher polynomial orders may be used when additional equality or inequality constraints are required.

##### Minimum-Snap Objective

Snap is the fourth derivative of position

$$
s_i(t)=p_i^{(4)}(t)
$$

The one-dimensional objective is

$$
J=\sum_{i=1}^{M}\int_{0}^{T_i}\left(p_i^{(4)}(t)\right)^2dt
$$

Each polynomial segment uses its own local time $t\in[0,T_i]$, so the local time is reset to zero at the beginning of every segment.

For a three-dimensional position trajectory $\boldsymbol{r}(t)=[x(t),y(t),z(t)]^T$
$$
J=\sum_{i=1}^{M}\int_{0}^{T_i}\left\|\boldsymbol{r}_i^{(4)}(t)\right\|_2^2dt
$$

The $x$, $y$, and $z$ coordinates are independent when they share the same segment times and have no coupled constraints.

##### Snap Cost Matrix $\mathbf{Q}$

The fourth derivative of the polynomial is

$$
p_i^{(4)}(t)=\boldsymbol{\beta}^{(4)}(t)^T\boldsymbol{c}_i
$$

Therefore

$$
J_i=\boldsymbol{c}_i^T\mathbf{Q}_i\boldsymbol{c}_i
$$

with

$$
\mathbf{Q}_i=\int_{0}^{T_i}\boldsymbol{\beta}^{(4)}(t)\boldsymbol{\beta}^{(4)}(t)^Tdt
$$

Using zero-based coefficient indices $k,l\in\{0,1,\ldots,n\}$

$$
(\mathbf{Q}_i)_{kl}=
\begin{cases}
\dfrac{k!}{(k-4)!}\dfrac{l!}{(l-4)!}\dfrac{T_i^{k+l-7}}{k+l-7},&k,l\geq4\\[8pt]
0,&k<4\ \text{or}\ l<4
\end{cases}
$$

Stack all segment coefficients

$$
\boldsymbol{c}=
\begin{bmatrix}
\boldsymbol{c}_1\\
\boldsymbol{c}_2\\
\vdots\\
\boldsymbol{c}_M
\end{bmatrix}
$$

The complete cost matrix is block diagonal

$$
\mathbf{Q}=\operatorname{diag}\left(\mathbf{Q}_1,\mathbf{Q}_2,\ldots,\mathbf{Q}_M\right)
$$

Hence

$$
J=\boldsymbol{c}^T\mathbf{Q}\boldsymbol{c}
$$

### Constraints and Variable Mapping

##### Boundary and Continuity Constraints

The trajectory must pass through the waypoints

$$
p_i(T_i)=w_i
$$

$$
p_{i+1}(0)=w_i
$$

The common seventh-degree formulation enforces continuity of position, velocity, acceleration, and jerk

$$
p_i^{(r)}(T_i)=p_{i+1}^{(r)}(0)
\qquad r=0,1,2,3
$$

Thus the piecewise trajectory is $C^3$ continuous. The general constrained-QP formulation can enforce continuity through a higher selected derivative order, while the compact square-$\mathbf{A}$ formulation below uses endpoint derivatives through jerk. The start and goal derivatives may be prescribed, for example

$$
p_1^{(r)}(0)=d_{\mathrm{start}}^{(r)}
\qquad r=0,1,2,3
$$

$$
p_M^{(r)}(T_M)=d_{\mathrm{goal}}^{(r)}
\qquad r=0,1,2,3
$$

Only position must be fixed at an intermediate waypoint. Its velocity, acceleration, and jerk can remain free and are chosen by the optimizer.

##### Endpoint Mapping Matrix $\mathbf{A}$

For a seventh-degree segment, define its endpoint-derivative vector

$$
\boldsymbol{d}_i=
\begin{bmatrix}
p_i(0)\\
p_i^{(1)}(0)\\
p_i^{(2)}(0)\\
p_i^{(3)}(0)\\
p_i(T_i)\\
p_i^{(1)}(T_i)\\
p_i^{(2)}(T_i)\\
p_i^{(3)}(T_i)
\end{bmatrix}
$$

The derivative basis satisfies

$$
\beta_k^{(r)}(t)=
\begin{cases}
\dfrac{k!}{(k-r)!}t^{k-r},&k\geq r\\[8pt]
0,&k<r
\end{cases}
$$

The mapping matrix is

$$
\mathbf{A}_i=
\begin{bmatrix}
\boldsymbol{\beta}(0)^T\\
\boldsymbol{\beta}^{(1)}(0)^T\\
\boldsymbol{\beta}^{(2)}(0)^T\\
\boldsymbol{\beta}^{(3)}(0)^T\\
\boldsymbol{\beta}(T_i)^T\\
\boldsymbol{\beta}^{(1)}(T_i)^T\\
\boldsymbol{\beta}^{(2)}(T_i)^T\\
\boldsymbol{\beta}^{(3)}(T_i)^T
\end{bmatrix}
$$

It converts polynomial coefficients into endpoint derivatives

$$
\boldsymbol{d}_i=\mathbf{A}_i\boldsymbol{c}_i
$$

Therefore

$$
\boldsymbol{c}_i=\mathbf{A}_i^{-1}\boldsymbol{d}_i
$$

In implementation, solve $\mathbf{A}_i\boldsymbol{c}_i=\boldsymbol{d}_i$ instead of explicitly forming $\mathbf{A}_i^{-1}$.

For all segments

$$
\mathbf{A}=\operatorname{diag}\left(\mathbf{A}_1,\mathbf{A}_2,\ldots,\mathbf{A}_M\right)
$$

$$
\boldsymbol{d}=\mathbf{A}\boldsymbol{c}
$$

$$
\boldsymbol{c}=\mathbf{A}^{-1}\boldsymbol{d}
$$

##### Selection Matrix $\mathbf{C}$

For segment $i$, define the endpoint-derivative vector

$$
\boldsymbol{d}_i=
\begin{bmatrix}
p_{i-1}\\
v_{i-1}\\
a_{i-1}\\
j_{i-1}\\
p_i\\
v_i\\
a_i\\
j_i
\end{bmatrix}
$$

Stacking all $M$ segments gives

$$
\boldsymbol{d}=
\begin{bmatrix}
\boldsymbol{d}_1\\
\boldsymbol{d}_2\\
\vdots\\
\boldsymbol{d}_M
\end{bmatrix}
\in\mathbb{R}^{8M}
$$

Every internal waypoint appears twice in $\boldsymbol{d}$: once as the end of segment $i$ and once as the start of segment $i+1$. The repeated entries have the form

$$
\boldsymbol{d}=
\begin{bmatrix}
\cdots\\
p_i\\
v_i\\
a_i\\
j_i\\
p_i\\
v_i\\
a_i\\
j_i\\
\cdots
\end{bmatrix}
$$

The first copy belongs to the end of segment $i$, while the second copy belongs to the start of segment $i+1$.

To avoid treating the two copies as independent variables, collect each waypoint derivative only once and arrange the unique variables as

$$
\boldsymbol{D}=
\begin{bmatrix}
\boldsymbol{d}_{F}\\
\boldsymbol{d}_{P}
\end{bmatrix}
$$

For the usual minimum-snap problem, $\boldsymbol{d}_{F}$ contains all waypoint positions and the prescribed derivatives at the start and goal

$$
\boldsymbol{d}_{F}=
\begin{bmatrix}
p_0&
v_0&
a_0&
j_0&
p_1&
\cdots&
p_{M-1}&
p_M&
v_M&
a_M&
j_M
\end{bmatrix}^{T}
$$

The vector $\boldsymbol{d}_{P}$ contains the unknown velocity, acceleration, and jerk at the internal waypoints

$$
\boldsymbol{d}_{P}=
\begin{bmatrix}
v_1&
a_1&
j_1&
\cdots&
v_{M-1}&
a_{M-1}&
j_{M-1}
\end{bmatrix}^{T}
$$

The entries of $\boldsymbol{d}_{F}$ remain fixed, while the optimizer chooses $\boldsymbol{d}_{P}$ to minimize the total snap cost.

The binary selection matrix $\mathbf{C}$ maps the unique variables in $\boldsymbol{D}$ back to the segment-wise endpoint vector $\boldsymbol{d}$

$$
\boldsymbol{d}=\mathbf{C}^{T}\boldsymbol{D}
$$

The matrix has the dimensions

$$
\mathbf{C}^{T}\in\mathbb{R}^{8M\times4(M+1)}
$$

Each row of $\mathbf{C}^{T}$ contains one entry equal to $1$ and all remaining entries equal to $0$. Therefore, each row selects one entry from $\boldsymbol{D}$ and places it in the corresponding position of $\boldsymbol{d}$.

Its structure can be written schematically as

$$
\mathbf{C}^{T}=
\begin{bmatrix}
\text{select }p_0\\
\text{select }v_0\\
\text{select }a_0\\
\text{select }j_0\\
\text{select }p_1\\
\text{select }v_1\\
\text{select }a_1\\
\text{select }j_1\\
\text{select }p_1\\
\text{select }v_1\\
\text{select }a_1\\
\text{select }j_1\\
\vdots\\
\text{select }p_M\\
\text{select }v_M\\
\text{select }a_M\\
\text{select }j_M
\end{bmatrix}
$$

The same internal variables are selected twice: once for the end of one segment and once for the start of the next segment. Hence

$$
p_i(T_i)=p_{i+1}(0)
$$

$$
v_i(T_i)=v_{i+1}(0)
$$

$$
a_i(T_i)=a_{i+1}(0)
$$

$$
j_i(T_i)=j_{i+1}(0)
$$

Therefore, $\mathbf{C}$ does not calculate any derivative. It only selects, reorders, and duplicates the unique variables in $\boldsymbol{D}$, so adjacent polynomial segments automatically share the same position, velocity, acceleration, and jerk.

### Closed-Form Solution

##### Fixed and Free Derivatives

Typical fixed variables are

- all waypoint positions
- prescribed start derivatives
- prescribed goal derivatives

Typical free variables are the velocity, acceleration, and jerk at internal waypoints

$$
\boldsymbol{d}_{P}=
\begin{bmatrix}
v_1&a_1&j_1&\cdots&v_{M-1}&a_{M-1}&j_{M-1}
\end{bmatrix}^{T}
$$

The optimizer chooses $\boldsymbol{d}_{P}$ to minimize the total snap cost.

##### Reduced Cost Matrix $\mathbf{R}$

Substitute

$$
\boldsymbol{c}=\mathbf{A}^{-1}\mathbf{C}^{T}\boldsymbol{D}
$$

into

$$
J=\boldsymbol{c}^{T}\mathbf{Q}\boldsymbol{c}
$$

Then

$$
J=\boldsymbol{D}^{T}\mathbf{C}\mathbf{A}^{-T}\mathbf{Q}\mathbf{A}^{-1}\mathbf{C}^{T}\boldsymbol{D}
$$

Define

$$
\mathbf{R}=\mathbf{C}\mathbf{A}^{-T}\mathbf{Q}\mathbf{A}^{-1}\mathbf{C}^{T}
$$

Partition $\mathbf{R}$ according to fixed and free derivatives

$$
\mathbf{R}=
\begin{bmatrix}
\mathbf{R}_{FF}&\mathbf{R}_{FP}\\
\mathbf{R}_{PF}&\mathbf{R}_{PP}
\end{bmatrix}
$$

The cost becomes

$$
J=
\begin{bmatrix}
\boldsymbol{d}_{F}\\
\boldsymbol{d}_{P}
\end{bmatrix}^{T}
\begin{bmatrix}
\mathbf{R}_{FF}&\mathbf{R}_{FP}\\
\mathbf{R}_{PF}&\mathbf{R}_{PP}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{d}_{F}\\
\boldsymbol{d}_{P}
\end{bmatrix}
$$

##### Optimal Free Derivatives and Polynomial Recovery

Differentiate the cost with respect to $\boldsymbol{d}_{P}$

$$
\frac{\partial J}{\partial\boldsymbol{d}_{P}}
=2\mathbf{R}_{PF}\boldsymbol{d}_{F}+2\mathbf{R}_{PP}\boldsymbol{d}_{P}
$$

Set the derivative to zero

$$
\mathbf{R}_{PP}\boldsymbol{d}_{P}^{*}=-\mathbf{R}_{PF}\boldsymbol{d}_{F}
$$

Hence

$$
\boldsymbol{d}_{P}^{*}=-\mathbf{R}_{PP}^{-1}\mathbf{R}_{PF}\boldsymbol{d}_{F}
$$

In implementation, solve the linear system instead of explicitly computing $\mathbf{R}_{PP}^{-1}$.

Recover the complete derivative vector

$$
\boldsymbol{D}^{*}=
\begin{bmatrix}
\boldsymbol{d}_{F}\\
\boldsymbol{d}_{P}^{*}
\end{bmatrix}
$$

Recover all polynomial coefficients

$$
\boldsymbol{c}^{*}=\mathbf{A}^{-1}\mathbf{C}^{T}\boldsymbol{D}^{*}
$$

This is the closed-form solution for fixed segment times and equality constraints.

### Time Allocation and Implementation

##### Segment Time

The cost depends strongly on each duration $T_i$. Under the normalized time $\tau=t/T_i$

$$
\int_{0}^{T_i}\left(p_i^{(4)}(t)\right)^2dt
=
\frac{1}{T_i^{7}}
\int_{0}^{1}\left(\frac{d^4p_i}{d\tau^4}\right)^2d\tau
$$

Longer segment times reduce the snap cost. Therefore, the segment times must either be fixed or optimized together with a time penalty

$$
J_{\mathrm{total}}=J_{\mathrm{snap}}+\lambda_T\sum_{i=1}^{M}T_i
$$

A common initialization assigns time according to segment length

$$
T_i\propto\left\|\boldsymbol{w}_i-\boldsymbol{w}_{i-1}\right\|_2
$$

Time allocation is nonlinear because $\mathbf{Q}_i$ and $\mathbf{A}_i$ depend on $T_i$. It is usually optimized outside the closed-form coefficient solve.

##### Three-Dimensional Extension and Algorithm

For $x$, $y$, and $z$, use the same matrices $\mathbf{A}$, $\mathbf{C}$, and $\mathbf{Q}$ but different fixed waypoint values. Solve the three coordinate problems independently and combine them as

$$
\boldsymbol{r}(t)=
\begin{bmatrix}
x(t)&y(t)&z(t)
\end{bmatrix}^{T}
$$

The classical workflow is

+ Specify waypoints and segment times
+ Construct the block-diagonal matrices $\mathbf{Q}$ and $\mathbf{A}$
+ Construct $\mathbf{C}$ and arrange fixed and free endpoint derivatives
+ Form $\mathbf{R}=\mathbf{C}\mathbf{A}^{-T}\mathbf{Q}\mathbf{A}^{-1}\mathbf{C}^{T}$
+ Solve $\mathbf{R}_{PP}\boldsymbol{d}_{P}^{*}=-\mathbf{R}_{PF}\boldsymbol{d}_{F}$
+ Recover $\boldsymbol{c}^{*}=\mathbf{A}^{-1}\mathbf{C}^{T}\boldsymbol{D}^{*}$

+ Evaluate the piecewise polynomial and its derivatives

The roles of the principal matrices are

| Matrix | Meaning |
|---|---|
| $\mathbf{Q}$ | Measures the integrated squared snap |
| $\mathbf{A}$ | Maps polynomial coefficients to endpoint derivatives |
| $\mathbf{C}$ | Reorders and duplicates shared endpoint variables |
| $\mathbf{R}$ | Expresses the snap cost directly in endpoint derivatives |

Optional corridor, velocity, acceleration, or actuator limits can be added as linear constraints. Once inequality constraints are introduced, the problem is solved as a constrained quadratic program rather than by the pure closed-form solution above.
