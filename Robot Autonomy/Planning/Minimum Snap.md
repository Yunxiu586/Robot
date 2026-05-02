# Minimum Snap

[toc]

### Minimum snap

##### Objective

**Minimum snap trajectory optimization** usually represents a trajectory segment as a polynomial and minimizes the squared 4th derivative of position.

For a one-dimensional trajectory segment

$$
p(t)=a_0+a_1t+a_2t^2+\cdots+a_nt^n
$$

Define the coefficient vector as

$$
\boldsymbol{c}=
\begin{bmatrix}
a_0 & a_1 & a_2 & \cdots & a_n
\end{bmatrix}^T
$$

Here, $\boldsymbol{c}$ is the optimization variable in the QP(**quadratic programming**). The polynomial can be written in vector form as

$$
p(t)=\boldsymbol{b}(t)^T\boldsymbol{c}
$$

where

$$
\boldsymbol{b}(t)=
\begin{bmatrix}
1 & t & t^2 & \cdots & t^n
\end{bmatrix}^T
$$

The minimum snap objective is

$$
J=\int_0^T \left(p^{(4)}(t)\right)^2dt
$$

The goal is to find polynomial coefficients that make the fourth derivative of the trajectory as small as possible.

##### Derivation of the Quadratic Form

Starting from the polynomial

$$
p(t)=\sum_{k=0}^{n}a_kt^k
$$

Its 4th derivative is

$$
p^{(4)}(t)=\sum_{k=4}^{n}k(k-1)(k-2)(k-3)a_kt^{k-4}
$$

Define the derivative basis vector $\boldsymbol{d}(t)$ as

$$
p^{(4)}(t)=\boldsymbol{d}(t)^T\boldsymbol{c}
$$

The \(k\)-th element of $\boldsymbol{d}(t)$, with zero-based indexing, is

$$
d_k(t)=
\begin{cases}
\dfrac{k!}{(k-4)!}t^{k-4}, & k\ge 4 \\
0, & k<4
\end{cases}
$$

Then the squared snap term becomes

$$
\left(p^{(4)}(t)\right)^2
=
\left(\boldsymbol{d}(t)^T\boldsymbol{c}\right)^2
=
\boldsymbol{c}^T\boldsymbol{d}(t)\boldsymbol{d}(t)^T\boldsymbol{c}
$$

Substituting this into the integral

$$
J=
\int_0^T
\boldsymbol{c}^T\boldsymbol{d}(t)\boldsymbol{d}(t)^T\boldsymbol{c}\,dt
$$

Since $\boldsymbol{c}$ does not depend on time, it can be moved outside the integral

$$
J=
\boldsymbol{c}^T
\left(
\int_0^T \boldsymbol{d}(t)\boldsymbol{d}(t)^Tdt
\right)
\boldsymbol{c}
$$

Define

$$
\mathbf{Q}=
\int_0^T \boldsymbol{d}(t)\boldsymbol{d}(t)^Tdt
$$

The element at row $k$, column $l$ is

$$
Q_{kl}=\int_0^T d_k(t)d_l(t)dt
$$

For $k,l\ge 4$ ,

$$
d_k(t)=\dfrac{k!}{(k-4)!}t^{k-4} \\
d_l(t)=\dfrac{l!}{(l-4)!}t^{l-4}
$$

Therefore

$$
Q_{kl}
=
\int_0^T
\left(\dfrac{k!}{(k-4)!}t^{k-4}\right)
\left(\dfrac{l!}{(l-4)!}t^{l-4}\right)dt
=
\dfrac{k!}{(k-4)!}
\dfrac{l!}{(l-4)!}
\int_0^T t^{k+l-8}dt
$$

The complete expression is

$$
Q_{kl}=
\begin{cases}
\dfrac{k!}{(k-4)!}
\dfrac{l!}{(l-4)!}
\dfrac{T^{k+l-7}}{k+l-7}, & k,l\ge 4 \\
0, & k<4 \text{ or } l<4
\end{cases}
$$

Therefore
$$
J=\boldsymbol{c}^T\mathbf{Q}\boldsymbol{c}
$$

This is why the squared integral of snap can be written as a quadratic form.

##### Multiple Trajectory Segments

For a multi-segment trajectory, suppose there are $M$ polynomial segments

$$
p_1(t),p_2(t),\ldots,p_M(t)
$$

Each segment has its own coefficient vector

$$
\boldsymbol{c}_i=
\begin{bmatrix}
a_{i,0} & a_{i,1} & \cdots & a_{i,n}
\end{bmatrix}^T
$$

The complete optimization variable is

$$
\boldsymbol{c}=
\begin{bmatrix}
\boldsymbol{c}_1 \\
\boldsymbol{c}_2 \\
\vdots \\
\boldsymbol{c}_M
\end{bmatrix}
$$

For segment $i$, the snap cost is

$$
J_i=\boldsymbol{c}_i^T\mathbf{Q}_i\boldsymbol{c}_i
$$

The total cost is

$$
J=\sum_{i=1}^{M}\boldsymbol{c}_i^T\mathbf{Q}_i\boldsymbol{c}_i
$$

This can be written as

$$
J=\boldsymbol{c}^T\mathbf{Q}\boldsymbol{c}
$$

where the global matrix $\mathbf{Q}$ is block diagonal

$$
\mathbf{Q}=
\begin{bmatrix}
\mathbf{Q}_1 & \mathbf{0} & \cdots & \mathbf{0} \\
\mathbf{0} & \mathbf{Q}_2 & \cdots & \mathbf{0} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{0} & \mathbf{0} & \cdots & \mathbf{Q}_M
\end{bmatrix}
$$

##### Quadratic Programming

A standard quadratic program is usually written as

$$
\min_{\boldsymbol{c}} \quad
\frac{1}{2}\boldsymbol{c}^T\mathbf{P}\boldsymbol{c}+\boldsymbol{q}^T\boldsymbol{c}
$$

subject to linear constraints such as

$$
\mathbf{A}_{eq}\boldsymbol{c}=\boldsymbol{b}_{eq}
$$

or

$$
\mathbf{A}\boldsymbol{c}\le \boldsymbol{b}
$$

$\boldsymbol{c}$ is the optimization variable, which contains all polynomial coefficients. $\boldsymbol{q}$ is the coefficient vector of the linear term.

A nonzero $\boldsymbol{q}$ appears when the objective includes a **tracking** or **reference penalty** with a nonzero offset.

For pure minimum snap, to match the standard QP form
$$
\frac{1}{2}\boldsymbol{c}^T\mathbf{P}\boldsymbol{c}
=
\boldsymbol{c}^T\mathbf{Q}\boldsymbol{c}
$$

we set

$$
\mathbf{P}=2\mathbf{Q}
$$

Thus, for minimum snap

$$
\min_{\boldsymbol{c}}\quad
\frac{1}{2}\boldsymbol{c}^T(2\mathbf{Q})\boldsymbol{c}
$$

with

$$
\mathbf{P}=2\mathbf{Q}, \qquad \boldsymbol{q}=\boldsymbol{0}
$$

### Discrete Minimum Snap

##### Corridor Center Penalty

To make the trajectory prefer the center of the safe corridor, a center penalty is often added. Let the center of the corridor assigned to point $\boldsymbol{p}_i$ be

$$
\boldsymbol{c}_i =
\begin{bmatrix}
c_{ix} \\
c_{iy}
\end{bmatrix}
$$

The center penalty is

$$
J_{\mathrm{center}}
= \lambda \sum_{i=0}^{N-1} \left\| \boldsymbol{p}_i - \boldsymbol{c}_i \right\|^2
$$

where $\lambda > 0$ controls how strongly the trajectory is attracted to the corridor center.

For one point,
$$
\left\| \boldsymbol{p}_i - \boldsymbol{c}_i \right\|^2
=
(x_i-c_{ix})^2 + (y_i-c_{iy})^2
$$

Expanding the $x$ part,

$$
(x_i-c_{ix})^2 = x_i^2 - 2c_{ix}x_i + c_{ix}^2
$$

Expanding the $y$ part,

$$
(y_i-c_{iy})^2 = y_i^2 - 2c_{iy}y_i + c_{iy}^2
$$

The constant terms $c_{ix}^2$ and $c_{iy}^2$ do not affect the optimizer, so they can be ignored.

Therefore, the useful part of the center penalty is

$$
J_{\mathrm{center}}
=
\lambda \sum_{i=0}^{N-1}
\left(
 x_i^2 + y_i^2 - 2c_{ix}x_i - 2c_{iy}y_i
\right)
+ \text{constant}
$$

This produces both a quadratic term and a linear term.

If the optimization variable is interleaved as

$$
\boldsymbol{\xi} =
\begin{bmatrix}
x_0 & y_0 & x_1 & y_1 & \cdots & x_{N-1} & y_{N-1}
\end{bmatrix}^{T}
$$

define the interleaved center vector
$$
\boldsymbol{c} =
\begin{bmatrix}
c_{0x} & c_{0y} & c_{1x} & c_{1y} & \cdots & c_{(N-1)x} & c_{(N-1)y}
\end{bmatrix}^{T}
$$

Then

$$
J_{\mathrm{center}}
= \lambda \left\| \boldsymbol{\xi} - \boldsymbol{c} \right\|^2
$$

Expanding,

$$
J_{\mathrm{center}}
= \lambda (\boldsymbol{\xi}-\boldsymbol{c})^T(\boldsymbol{\xi}-\boldsymbol{c})
$$

$$
J_{\mathrm{center}}
= \lambda \boldsymbol{\xi}^T\boldsymbol{\xi}
-2\lambda \boldsymbol{c}^T\boldsymbol{\xi}
+\lambda \boldsymbol{c}^T\boldsymbol{c}
$$

Ignoring the constant term,

$$
J_{\mathrm{center}}
= \boldsymbol{\xi}^T(\lambda \mathbf{I})\boldsymbol{\xi}
+ (-2\lambda\boldsymbol{c})^T\boldsymbol{\xi}
$$

Thus, the center penalty contributes

$$
\mathbf{Q}_{\mathrm{center}} = \lambda \mathbf{I}
$$

and

$$
\boldsymbol{q}_{\mathrm{center}} = -2\lambda \boldsymbol{c}
$$

This is the main source of the linear term in the discrete-point minimum snap QP.

##### Discrete Minimum Snap

In a discrete trajectory, there is no continuous derivative. Therefore, the fourth derivative is approximated by a fourth-order finite difference.

For a scalar sequence $x_0,x_1,\dots,x_{N-1}$, the fourth-order finite difference is

$$
\Delta^4 x_i = x_i - 4x_{i+1} + 6x_{i+2} - 4x_{i+3} + x_{i+4}
$$

This has the same coefficient pattern as the fourth derivative of a polynomial-like discrete sequence.

Define a **difference matrix** $\mathbf{S} \in \mathbb{R}^{(N-4) \times N}$ such that

$$
\mathbf{S}\boldsymbol{x} =
\begin{bmatrix}
\Delta^4 x_0 \\
\Delta^4 x_1 \\
\vdots \\
\Delta^4 x_{N-5}
\end{bmatrix}
$$

where

$$
\boldsymbol{x} =
\begin{bmatrix}
x_0 & x_1 & \cdots & x_{N-1}
\end{bmatrix}^{T}
$$

The matrix $\mathbf{S}$ has the form

$$
\mathbf{S} =
\begin{bmatrix}
1 & -4 & 6 & -4 & 1 & 0 & \cdots & 0 \\
0 & 1 & -4 & 6 & -4 & 1 & \cdots & 0 \\
0 & 0 & 1 & -4 & 6 & -4 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots
\end{bmatrix}
$$

Then the discrete snap cost in the $x$ direction is

$$
J_x = \left\| \mathbf{S}\boldsymbol{x} \right\|^2
$$

Expanding it gives

$$
J_x
= (\mathbf{S}\boldsymbol{x})^T(\mathbf{S}\boldsymbol{x})
= \boldsymbol{x}^T \mathbf{S}^T \mathbf{S} \boldsymbol{x}
$$

Therefore, the discrete snap cost is a quadratic form. The matrix

$$
\mathbf{Q}_x = \mathbf{S}^T\mathbf{S}
$$

is the Hessian contribution of the $x$-direction smoothness term.

Similarly, for the $y$ direction,

$$
J_y = \boldsymbol{y}^T \mathbf{S}^T \mathbf{S} \boldsymbol{y}
$$

where

$$
\boldsymbol{y} =
\begin{bmatrix}
y_0 & y_1 & \cdots & y_{N-1}
\end{bmatrix}^{T}
$$

Thus, the 2D discrete snap cost is

$$
J_{\mathrm{smooth}}
= \boldsymbol{x}^T \mathbf{S}^T\mathbf{S}\boldsymbol{x}
+ \boldsymbol{y}^T \mathbf{S}^T\mathbf{S}\boldsymbol{y}
$$

Using the interleaved decision vector $\boldsymbol{\xi}$, then the smoothness objective can still be written as

$$
J_{\mathrm{smooth}} = \boldsymbol{\xi}^T \mathbf{Q}_{\mathrm{smooth}} \boldsymbol{\xi}
$$

The matrix $\mathbf{Q}_{\mathrm{smooth}}$ is assembled by placing $\mathbf{S}^T\mathbf{S}$ into the entries corresponding to all $x_i$ variables and another copy of $\mathbf{S}^T\mathbf{S}$ into the entries corresponding to all $y_i$ variables.

Define Hessian matrix

$$
\mathbf{H} = \mathbf{S}^T\mathbf{S}
$$

Using $\mathbf{H}=\mathbf{S}^T\mathbf{S}$, this becomes

$$
J_{\mathrm{smooth}}
=
\boldsymbol{x}^T\mathbf{H}\boldsymbol{x}
+
\boldsymbol{y}^T\mathbf{H}\boldsymbol{y}
$$

Let

$$
\mathbf{H}=
\begin{bmatrix}
H_{00} & H_{01} & \cdots & H_{0,N-1} \\
H_{10} & H_{11} & \cdots & H_{1,N-1} \\
\vdots & \vdots & \ddots & \vdots \\
H_{N-1,0} & H_{N-1,1} & \cdots & H_{N-1,N-1}
\end{bmatrix}
$$

Then the interleaved two-dimensional smoothness matrix is

$$
\mathbf{Q}_{\mathrm{smooth}}
=
\begin{bmatrix}
H_{00}\mathbf{I}_2 & H_{01}\mathbf{I}_2 & \cdots & H_{0,N-1}\mathbf{I}_2 \\
H_{10}\mathbf{I}_2 & H_{11}\mathbf{I}_2 & \cdots & H_{1,N-1}\mathbf{I}_2 \\
\vdots & \vdots & \ddots & \vdots \\
H_{N-1,0}\mathbf{I}_2 & H_{N-1,1}\mathbf{I}_2 & \cdots & H_{N-1,N-1}\mathbf{I}_2
\end{bmatrix}
$$

Each block is a $2 \times 2$ matrix:

$$
H_{ij}\mathbf{I}_2
=
\begin{bmatrix}
H_{ij} & 0 \\
0 & H_{ij}
\end{bmatrix}
$$

Expanding the matrix explicitly, we get

$$
\mathbf{Q}_{\mathrm{smooth}}
=
\begin{bmatrix}
H_{00} & 0 & H_{01} & 0 & \cdots & H_{0,N-1} & 0 \\
0 & H_{00} & 0 & H_{01} & \cdots & 0 & H_{0,N-1} \\
H_{10} & 0 & H_{11} & 0 & \cdots & H_{1,N-1} & 0 \\
0 & H_{10} & 0 & H_{11} & \cdots & 0 & H_{1,N-1} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
H_{N-1,0} & 0 & H_{N-1,1} & 0 & \cdots & H_{N-1,N-1} & 0 \\
0 & H_{N-1,0} & 0 & H_{N-1,1} & \cdots & 0 & H_{N-1,N-1}
\end{bmatrix}
$$

For the interleaved decision vector,

$$
\boldsymbol{\xi}_{2i}=x_i
$$

and

$$
\boldsymbol{\xi}_{2i+1}=y_i
$$

where $i=0,1,\dots,N-1$.

The entries of $\mathbf{Q}_{\mathrm{smooth}}$ are arranged as follows:

$$
\mathbf{Q}_{\mathrm{smooth}}(2i,2j)=H_{ij}
$$

$$
\mathbf{Q}_{\mathrm{smooth}}(2i+1,2j+1)=H_{ij}
$$

$$
\mathbf{Q}_{\mathrm{smooth}}(2i,2j+1)=0
$$

$$
\mathbf{Q}_{\mathrm{smooth}}(2i+1,2j)=0
$$

This means that $x_i$ and $x_j$ are coupled by the smoothness cost, and $y_i$ and $y_j$ are coupled by the smoothness cost. However, $x_i$ and $y_j$ do not produce a smoothness cross term.

The **objective** is
$$
J = J_{\mathrm{smooth}} + J_{\mathrm{center}}
$$

Substituting the matrix forms,

$$
J
= \boldsymbol{\xi}^T\mathbf{Q}_{\mathrm{smooth}}\boldsymbol{\xi}
+ \boldsymbol{\xi}^T(\lambda\mathbf{I})\boldsymbol{\xi}
+ (-2\lambda\boldsymbol{c})^T\boldsymbol{\xi}
$$

Therefore,

$$
J
= \boldsymbol{\xi}^T\mathbf{Q}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
$$

where

$$
\mathbf{Q} = \mathbf{Q}_{\mathrm{smooth}} + \lambda\mathbf{I}
$$

$$
\boldsymbol{q} = -2\lambda\boldsymbol{c}
$$

##### Safe Corridor Constraints

A safe corridor is usually represented as a **convex polygon** in 2D or a convex polyhedron in 3D. For a 2D convex polygon, the safe region can be written as the intersection of half-spaces

$$
\mathbf{A}_i \boldsymbol{p}_i \leq \boldsymbol{b}_i
$$

where $\mathbf{A}_i$ is a matrix and $\boldsymbol{b}_i$ is a vector.

If the polygon has $m_i$ edges, then

$$
\mathbf{A}_i =
\begin{bmatrix}
\boldsymbol{n}_{i1}^T \\
\boldsymbol{n}_{i2}^T \\
\vdots \\
\boldsymbol{n}_{im_i}^T
\end{bmatrix}
$$

and

$$
\boldsymbol{b}_i =
\begin{bmatrix}
b_{i1} \\
b_{i2} \\
\vdots \\
b_{im_i}
\end{bmatrix}
$$

Each row represents one boundary line of the polygon.

For one edge, the constraint is

$$
\boldsymbol{n}_{ij}^T\boldsymbol{p}_i \leq b_{ij}
$$

where $\boldsymbol{n}_{ij}$ is the outward normal vector of that edge.

For point $\boldsymbol{p}_i$, we have

$$
\boldsymbol{p}_i =
\begin{bmatrix}
x_i \\
y_i
\end{bmatrix}
$$

One half-space constraint is

$$
n_{ij,x}x_i + n_{ij,y}y_i \leq b_{ij}
$$

Since the global decision vector is

$$
\boldsymbol{\xi}
=
\begin{bmatrix}
x_0 & y_0 & x_1 & y_1 & \cdots & x_i & y_i & \cdots & x_{N-1} & y_{N-1}
\end{bmatrix}^{T}
$$

this constraint becomes one row in the global linear constraint matrix

$$
\begin{bmatrix}
0 & 0 & \cdots & n_{ij,x} & n_{ij,y} & \cdots & 0 & 0
\end{bmatrix}
\boldsymbol{\xi}
\leq b_{ij}
$$

Therefore, safe corridor constraints are linear constraints.

The start and goal points are usually fixed

$$
\boldsymbol{p}_0 = \boldsymbol{p}_{\mathrm{start}}
$$

$$
\boldsymbol{p}_{N-1} = \boldsymbol{p}_{\mathrm{goal}}
$$

In coordinates,

$$
x_0 = x_{\mathrm{start}}, \quad y_0 = y_{\mathrm{start}}
$$

$$
x_{N-1} = x_{\mathrm{goal}}, \quad y_{N-1} = y_{\mathrm{goal}}
$$

These are equality constraints. They can also be written as linear constraints.

Collecting all equality and inequality constraints gives
$$
\mathbf{A}\boldsymbol{\xi} \leq \boldsymbol{b}
$$

or, in the form required by OSQP,

$$
\boldsymbol{l} \leq \mathbf{A}\boldsymbol{\xi} \leq \boldsymbol{u}
$$

where $\mathbf{A}$ is the global constraint matrix, while $\boldsymbol{l}$ and $\boldsymbol{u}$ are lower and upper bound vectors.

For an equality constraint

$$
\boldsymbol{a}_k^T\boldsymbol{\xi} = d_k
$$

OSQP uses

$$
l_k = u_k = d_k
$$

For an inequality constraint

$$
\boldsymbol{a}_k^T\boldsymbol{\xi} \leq d_k
$$

OSQP uses

$$
l_k = -\infty, \quad u_k = d_k
$$

### OSQP Quadratic Programming

##### OSQP

**Operator Splitting Quadratic Program** (OSQP) solves convex quadratic programs of the form
$$
\min_{\boldsymbol{\xi}} \quad
\frac{1}{2}\boldsymbol{\xi}^T\mathbf{P}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
$$

subject to

$$
\boldsymbol{l} \leq \mathbf{A}\boldsymbol{\xi} \leq \boldsymbol{u}
$$

where

- $\boldsymbol{\xi}$ is the decision vector.
- $\mathbf{P}$ is the Hessian matrix.
- $\boldsymbol{q}$ is the linear cost vector.
- $\mathbf{A}$ is the constraint matrix.
- $\boldsymbol{l}$ and $\boldsymbol{u}$ are lower and upper bound vectors.

To make both forms identical, choose

$$
\mathbf{P} = 2\mathbf{Q}
$$

and keep the same linear vector

$$
\boldsymbol{q} = -2\lambda\boldsymbol{c}
$$

Then

$$
\frac{1}{2}\boldsymbol{\xi}^T(2\mathbf{Q})\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
=
\boldsymbol{\xi}^T\mathbf{Q}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
$$

##### Convexity

For the two-dimensional interleaved decision vector, the smoothness cost is

$$
J_{\mathrm{smooth}}
=
\boldsymbol{\xi}^T\mathbf{Q}_{\mathrm{smooth}}\boldsymbol{\xi}
$$

Because

$$
J_{\mathrm{smooth}}
=
\|\mathbf{S}\boldsymbol{x}\|_2^2
+
\|\mathbf{S}\boldsymbol{y}\|_2^2
$$

and both terms are nonnegative, we have

$$
J_{\mathrm{smooth}}\ge 0
$$

for any $\boldsymbol{\xi}\in\mathbb{R}^{2N}$.

Therefore,

$$
\mathbf{Q}_{smooth}\succeq 0
$$

The two-dimensional discrete minimum snap smoothness cost is convex.

Since

$$
\mathbf{Q}_{smooth}\succeq 0
$$

and

$$
\lambda\mathbf{I}\succ 0
$$

for $\lambda>0$, we have

$$
\mathbf{Q}\succ 0
$$

Therefore, with a positive center penalty weight, the total objective becomes strictly convex.

##### OSQP ADMM Principle

OSQP solves

$$
\min_{\boldsymbol{\xi}} \quad
\frac{1}{2}\boldsymbol{\xi}^T\mathbf{P}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
$$

subject to

$$
\boldsymbol{l} \leq \mathbf{A}\boldsymbol{\xi} \leq \boldsymbol{u}
$$

Introduce an auxiliary vector $\boldsymbol{r}$ such that

$$
\boldsymbol{r} = \mathbf{A}\boldsymbol{\xi}
$$

The constraints become

$$
\boldsymbol{l} \leq \boldsymbol{r} \leq \boldsymbol{u}
$$

The problem can be rewritten as

$$
\min_{\boldsymbol{\xi},\boldsymbol{r}} \quad
\frac{1}{2}\boldsymbol{\xi}^T\mathbf{P}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
+ I_{[\boldsymbol{l},\boldsymbol{u}]}(\boldsymbol{r})
$$

subject to

$$
\mathbf{A}\boldsymbol{\xi} - \boldsymbol{r} = \boldsymbol{0}
$$

where $I_{[\boldsymbol{l},\boldsymbol{u}]}(\boldsymbol{r})$ is the **indicator function**

$$
I_{[\boldsymbol{l},\boldsymbol{u}]}(\boldsymbol{r}) =
\begin{cases}
0, & \boldsymbol{l} \leq \boldsymbol{r} \leq \boldsymbol{u} \\
+\infty, & \text{otherwise}
\end{cases}
$$

This separates the quadratic objective and the box constraint.

##### ADMM update intuition

**Alternating Direction Method of Multipliers** (ADMM) introduces a **dual vector** $\boldsymbol{\nu}$ and a **penalty parameter** $\rho > 0$. The algorithm alternates between updating the primal variable $\boldsymbol{\xi}$, projecting the auxiliary vector $\boldsymbol{r}$ into the box $[\boldsymbol{l},\boldsymbol{u}]$, and updating the dual variable $\boldsymbol{\nu}$.

**The first step** updates $\boldsymbol{\xi}$ by solving a linear system related to the quadratic objective and the constraint residual.
$$
\boldsymbol{\xi}^{k+1}
\leftarrow
\arg\min_{\boldsymbol{\xi}}
\left(
\frac{1}{2}\boldsymbol{\xi}^T\mathbf{P}\boldsymbol{\xi}
+ \boldsymbol{q}^T\boldsymbol{\xi}
+ \frac{\rho}{2}
\left\|\mathbf{A}\boldsymbol{\xi} - \boldsymbol{r}^{k} + \frac{1}{\rho}\boldsymbol{\nu}^{k}\right\|^2
\right)
$$

**The second step** updates $\boldsymbol{r}$ by projection
$$
\boldsymbol{r}^{k+1}
=
\Pi_{[\boldsymbol{l},\boldsymbol{u}]}
\left(
\mathbf{A}\boldsymbol{\xi}^{k+1}
+ \frac{1}{\rho}\boldsymbol{\nu}^{k}
\right)
$$

The projection is element-wise

$$
\Pi_{[\boldsymbol{l},\boldsymbol{u}]}(s)_i
=
\min\left(\max(s_i,l_i),u_i\right)
$$

**The third step** updates the dual variable
$$
\boldsymbol{\nu}^{k+1}
=
\boldsymbol{\nu}^{k}
+ \rho\left(\mathbf{A}\boldsymbol{\xi}^{k+1} - \boldsymbol{r}^{k+1}\right)
$$

The term

$$
\mathbf{A}\boldsymbol{\xi}^{k+1} - \boldsymbol{r}^{k+1}
$$

measures violation of the equality relation $\boldsymbol{r} = \mathbf{A}\boldsymbol{\xi}$.
