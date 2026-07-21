# B-spline

[toc]

A B-spline curve is defined by control points, a **knot vector**, and the **degree**.

A degree-$p$ B-spline is a piecewise polynomial curve. Modifying $P_i$ only affects the parameter interval

$$
[u_i,u_{i+p+1})
$$

which gives B-splines their **local control** property.

##### Relationship to Bézier Curves

A Bézier curve is a special B-spline curve. A degree-$p$ Bézier curve with $p+1$ control points is obtained from the clamped knot vector

$$
U=\{\underbrace{0,\ldots,0}_{p+1},\underbrace{1,\ldots,1}_{p+1}\}
$$

Its B-spline basis functions reduce to the Bernstein basis functions

$$
N_{i,p}(u)=\binom{p}{i}u^i(1-u)^{p-i}
$$

Therefore,

$$
C(u)=\sum_{i=0}^{p}N_{i,p}(u)P_i
=\sum_{i=0}^{p}\binom{p}{i}u^i(1-u)^{p-i}P_i
$$

A general B-spline consists of multiple polynomial segments joined at knots. By inserting each internal knot until its multiplicity becomes $p$, every nonzero knot span can be represented as a Bézier segment without changing the curve shape.

##### Knot Terminology

The knot vector is a nondecreasing sequence

$$
U=\{u_0,u_1,\ldots,u_m\},
\qquad
u_0\leq u_1\leq\cdots\leq u_m
$$

- **Knot**: one entry $u_i$ in the knot vector
- **Knot value**: the numerical parameter value of a knot; repeated knots may have the same knot value
- **Knot multiplicity**: the number of times a knot value is repeated
- **Knot interval**: the interval between two consecutive knots, $[u_i,u_{i+1})$
- **Knot span**: a nonzero knot interval satisfying $u_i<u_{i+1}$
- **Knot-span length**:
  $$
  \Delta u_i=u_{i+1}-u_i
  $$

Repeated knots produce zero-length knot intervals. The standard parameter domain of the curve is

$$
u\in[u_p,u_{n+1}]
$$

Common knot vectors include:

- **Uniform**: all nonzero knot spans have equal length
- **Non-uniform**: knot-span lengths are not necessarily equal
- **Open clamped**: the first and last knot values each have multiplicity $p+1$, so the curve interpolates its first and last control points

##### Basis Function Representation

A B‑spline curve of degree $p$ is defined by $n+1$ control points $P_0,P_1,...,P_n$ and a knot vector $U=\{u_0,u_1,...,u_m\}$, where $m=n+p+1$.
$$
C(u) = \sum_{i=0}^{n} N_{i,p}(u) \cdot P_i
$$
$N_{i,p}(u)$ is the $p$th-degree B-spline basis function defined on the knot vector $U$, computed by the Cox–de Boor recurrence formula.

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

For an **open uniform knot vector**, the first $p+1$ knots are equal, the last $p+1$ knots are equal, and the middle knots increase uniformly
$$
u_i =
\begin{cases}
0, & 0 \leq i \leq p \\
i-p, & p+1 \leq i \leq n \\
n-p+1, & n+1 \leq i \leq n+p+1
\end{cases}
$$
**eg.** Given the knot vector $U=\{0,0,0,0,1,2,2,2\}$ and $u=0.5$, compute the cubic B-spline basis functions $N_{i,3}(u)$ for $i=0,1,2,3$ using the recurrence formula with the convention $0/0=0$.

Here $m=7$, and $p=3$. Thus,
$$
n=m-p-1=7-3-1=3
$$

So the curve has control points

$$
P_0,P_1,P_2,P_3
$$

Therefore, the valid parameter interval is
$$
[u_p,u_{n+1}] = [u_3,u_4]
$$
Hence,
$$
u \in [0,1]
$$
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
| 0.5  |    0.1250    |    0.5938    |    0.2500    |    0.0313    |
| 1.0  |    0.0000    |    0.2500    |    0.5000    |    0.2500    |

The corresponding curve points are

$$
\begin{aligned}
C(0) &= \sum_{i=0}^{3} N_{i,3}(0)P_i \\
C(0.5) &= \sum_{i=0}^{3} N_{i,3}(0.5)P_i \\
C(1.0) &= \sum_{i=0}^{3} N_{i,3}(1.0)P_i
\end{aligned}
$$

##### Matrix Representation

For a uniform B-spline curve, each knot span has the same length

$$
\Delta u = u_{k+1} - u_k
$$

where $u \in [u_k,u_{k+1})$ is the current parameter interval and $k$ is the index of the current knot interval.

The global parameter $u$ can be normalized into a local parameter

$$
s(u) = \frac{u-u_k}{\Delta u}, \quad s(u) \in [0,1)
$$

Then the B-spline curve on this local interval can be written in matrix form as

$$
C(s(u)) = \boldsymbol{s}(u)^T \mathbf{M}_{p+1}\mathbf{P}_k
$$

where

$$
\boldsymbol{s}(u)=
\begin{bmatrix}
1 & s(u) & s^2(u) & \cdots & s^p(u)
\end{bmatrix}^T
$$

$p$ is the degree of the B-spline curve, $\mathbf{M}_{p+1}$ is the basis matrix of the B-spline that determined only by the degree $p$, and $\mathbf{P}_k$ contains the $p+1$ local control points that affect the curve segment on $u\in[u_k,u_{k+1})$
$$
\mathbf{P}_k=
\begin{bmatrix}
P_{k-p} \\
P_{k-p+1} \\
\vdots \\
P_k
\end{bmatrix}
$$

It only uses the local control points

$$
P_{k-p},P_{k-p+1},...,P_k
$$

because of the local support property of B-spline basis functions.

For a cubic B-spline, $p=3$. Thus,

$$
\boldsymbol{s}(u)=
\begin{bmatrix}
1 & s(u) & s^2(u) & s^3(u)
\end{bmatrix}^T
$$

and

$$
\mathbf{P}_k=
\begin{bmatrix}
P_{k-3} \\
P_{k-2} \\
P_{k-1} \\
P_k
\end{bmatrix}
$$

The cubic B-spline basis matrix is

$$
\mathbf{M}_4=
\frac{1}{6}
\begin{bmatrix}
1 & 4 & 1 & 0 \\
-3 & 0 & 3 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1
\end{bmatrix}
$$

Therefore,

$$
C(s(u)) =
\begin{bmatrix}
1 & s & s^2 & s^3
\end{bmatrix}
\frac{1}{6}
\begin{bmatrix}
1 & 4 & 1 & 0 \\
-3 & 0 & 3 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1
\end{bmatrix}
\begin{bmatrix}
P_{k-3} \\
P_{k-2} \\
P_{k-1} \\
P_k
\end{bmatrix}
$$

where $s=s(u)$.

Expanding the matrix multiplication gives
$$
C(s)=
B_0(s)P_{k-3}
+
B_1(s)P_{k-2}
+
B_2(s)P_{k-1}
+
B_3(s)P_k
$$

where

$$
\begin{align*}
B_0(s) &= \frac{1}{6}(1-3s+3s^2-s^3) \\
B_1(s) &= \frac{1}{6}(4-6s^2+3s^3) \\
B_2(s) &= \frac{1}{6}(1+3s+3s^2-3s^3) \\
B_3(s) &= \frac{1}{6}s^3
\end{align*}
$$

These four basis functions satisfy

$$
B_0(s)+B_1(s)+B_2(s)+B_3(s)=1
$$

for

$$
s\in[0,1]
$$

Therefore, the curve point $C(s)$ is a weighted average of the four local control points.

##### Important Properties

- Non-negativity

  $$
  N_{i,p}(u)\geq0
  $$

- Partition of unity

  $$
  \sum_{i=0}^{n}N_{i,p}(u)=1
  $$

- Local support

  $$
  N_{i,p}(u)=0,
  \qquad
  u\notin[u_i,u_{i+p+1})
  $$

- Local convex-hull property: on $u\in[u_k,u_{k+1})$, the curve lies in the convex hull of

  $$
  P_{k-p},P_{k-p+1},\ldots,P_k
  $$

- Continuity: at an internal knot of multiplicity $r$, a degree-$p$ B-spline is generally

  $$
  C^{p-r}
  $$

  continuous. Increasing knot multiplicity reduces smoothness.

- Endpoint interpolation: for an open clamped knot vector,

  $$
  C(u_p)=P_0,
  \qquad
  C(u_{n+1})=P_n
  $$

- Affine invariance: translating, rotating, or scaling the control points applies the same transformation to the curve.

##### Continuity

For an internal knot value $\xi$ with multiplicity $r$, a degree-$p$ B-spline is generally $C^{p-r}$ continuous. Thus,

$$
\lim_{u\to\xi^-}
\frac{d^q\boldsymbol{C}(u)}{du^q}
=
\lim_{u\to\xi^+}
\frac{d^q\boldsymbol{C}(u)}{du^q},
\qquad
q=0,1,\ldots,p-r
$$

For a cubic B-spline, $p=3$.

| Internal-knot multiplicity $r$ |  Continuity   | Motion implication                                           |
| :----------------------------: | :-----------: | :----------------------------------------------------------- |
|              $1$               |     $C^2$     | Position, velocity, and acceleration are continuous; jerk may be discontinuous |
|              $2$               |     $C^1$     | Position and velocity are continuous; acceleration may be discontinuous |
|              $3$               |     $C^0$     | Position is continuous; velocity may be discontinuous        |
|              $4$               | Discontinuous | The knot can separate two independent curve pieces           |

Each nonzero knot span of a cubic B-spline can be converted into a cubic Bézier segment by knot insertion. Therefore, continuity can also be expressed using the control points of two adjacent cubic Bézier segments.

Let the left segment have control points

$$
\boldsymbol{A}_0,\boldsymbol{A}_1,\boldsymbol{A}_2,\boldsymbol{A}_3
$$

and the right segment have control points

$$
\boldsymbol{B}_0,\boldsymbol{B}_1,\boldsymbol{B}_2,\boldsymbol{B}_3
$$

The derivatives with respect to the global parameter $u$ are

$$
\boldsymbol{C}'_k(u)
=
\frac{1}{\Delta u}
\begin{bmatrix}
0 & 1 & 2s & 3s^2
\end{bmatrix}
\mathbf{M}_4\mathbf{P}_k
$$

$$
\boldsymbol{C}''_k(u)
=
\frac{1}{\Delta u^2}
\begin{bmatrix}
0 & 0 & 2 & 6s
\end{bmatrix}
\mathbf{M}_4\mathbf{P}_k
$$

$$
\boldsymbol{C}^{(3)}_k(u)
=
\frac{1}{\Delta u^3}
\begin{bmatrix}
0 & 0 & 0 & 6
\end{bmatrix}
\mathbf{M}_4\mathbf{P}_k
$$

For equal parameter intervals,
$$
\boldsymbol{C}_L(1)=\boldsymbol{A}_3,
\qquad
\boldsymbol{C}_R(0)=\boldsymbol{B}_0
$$

$$
\boldsymbol{C}'_L(1)=3(\boldsymbol{A}_3-\boldsymbol{A}_2),
\qquad
\boldsymbol{C}'_R(0)=3(\boldsymbol{B}_1-\boldsymbol{B}_0)
$$

$$
\boldsymbol{C}''_L(1)=6(\boldsymbol{A}_3-2\boldsymbol{A}_2+\boldsymbol{A}_1),
\qquad
\boldsymbol{C}''_R(0)=6(\boldsymbol{B}_2-2\boldsymbol{B}_1+\boldsymbol{B}_0)
$$

Equating the endpoint positions gives the $C^0$ condition; additionally equating the first derivatives gives $C^1$; equating the second derivatives as well gives $C^2$.

- $C^0$ condition
  $$
  \boldsymbol{A}_3=\boldsymbol{B}_0
  $$

- $C^1$ conditions

  $$
  \boldsymbol{A}_3=\boldsymbol{B}_0
  $$

  $$
  \boldsymbol{A}_3-\boldsymbol{A}_2
  =
  \boldsymbol{B}_1-\boldsymbol{B}_0
  $$

- $C^2$ conditions

$$
\boldsymbol{A}_3=\boldsymbol{B}_0
$$

$$
\boldsymbol{A}_3-\boldsymbol{A}_2
=
\boldsymbol{B}_1-\boldsymbol{B}_0
$$

$$
\boldsymbol{A}_3-2\boldsymbol{A}_2+\boldsymbol{A}_1
=
\boldsymbol{B}_2-2\boldsymbol{B}_1+\boldsymbol{B}_0
$$

Equivalently, after selecting the left-segment control points,

$$
\boldsymbol{B}_0=\boldsymbol{A}_3
$$

$$
\boldsymbol{B}_1=2\boldsymbol{A}_3-\boldsymbol{A}_2
$$

$$
\boldsymbol{B}_2=4\boldsymbol{A}_3-4\boldsymbol{A}_2+\boldsymbol{A}_1
$$

##### Geometric Continuity

Geometric continuity concerns the curve shape rather than parameter speed. In general,

$$
C^k \Longrightarrow G^k
$$

but not conversely.

Let two cubic segments meet at

$$
\boldsymbol{A}_3=\boldsymbol{B}_0
$$

- $G^1$ continuity: equal tangent direction

  $$
  \boldsymbol{B}_1-\boldsymbol{B}_0
  =
  \lambda
  \left(
  \boldsymbol{A}_3-\boldsymbol{A}_2
  \right),
  \qquad
  \lambda>0
  $$

- $G^2$ continuity: $G^1$ continuity and equal curvature

$$
\boldsymbol{T}(u)
=
\frac{\boldsymbol{C}'(u)}
{\left\|\boldsymbol{C}'(u)\right\|}
$$

$$
\left.
\frac{d\boldsymbol{T}}{ds}
\right|_{\xi^-}
=
\left.
\frac{d\boldsymbol{T}}{ds}
\right|_{\xi^+}
$$

$$
\kappa
=
\left\|
\frac{d\boldsymbol{T}}{ds}
\right\|
$$

where $\boldsymbol{T}(u)$ is the unit tangent vector, $s$ is arc length. The vector $d\boldsymbol{T}/ds$ is the curvature vector, and its magnitude $\kappa$ is the curvature.

- $G^3$ continuity: $G^2$ continuity and equal curvature variation

  $$
  \left.
  \frac{d^3\boldsymbol{C}}{ds^3}
  \right|_{\xi^-}
  =
  \left.
  \frac{d^3\boldsymbol{C}}{ds^3}
  \right|_{\xi^+}
  $$

