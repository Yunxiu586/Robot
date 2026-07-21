# Steepest Descent

[toc]

##### Basic idea

The negative gradient direction is the direction in which the first-order approximation decreases most rapidly under the Euclidean norm.

For small $\alpha>0$

$$
f(\boldsymbol{x}_k+\alpha\boldsymbol{d})
=
f(\boldsymbol{x}_k)
+
\alpha\boldsymbol{g}_k^T\boldsymbol{d}
+
o(\alpha)
$$

For all directions satisfying

$$
\|\boldsymbol{d}\|\le1
$$

the steepest descent direction solves

$$
\begin{aligned}
\min_{\boldsymbol{d}}\quad & \boldsymbol{g}_k^T\boldsymbol{d} \\
\text{s.t.}\quad & \|\boldsymbol{d}\|\le 1
\end{aligned}
$$
By the Cauchy-Schwarz inequality
$$
\left|\boldsymbol{g}_k^T\boldsymbol{d}\right|
\le
\|\boldsymbol{g}_k\|\|\boldsymbol{d}\|
\le
\|\boldsymbol{g}_k\|
$$

$$
\boldsymbol{g}_k^T\boldsymbol{d}
\ge
-\|\boldsymbol{g}_k\|\|\boldsymbol{d}\|
\ge
-\|\boldsymbol{g}_k\|
$$

Equality holds when

$$
\boldsymbol{d}
=
-\frac{\boldsymbol{g}_k}{\|\boldsymbol{g}_k\|}
$$

Thus the usual search direction is

$$
\boldsymbol{d}_k=-\boldsymbol{g}_k
$$

##### Algorithm

Choose an initial point $\boldsymbol{x}_0$ and a tolerance $\varepsilon>0$. 

At iteration $k$, compute
$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

If

$$
\|\boldsymbol{g}_k\|\le \varepsilon
$$

stop.

Otherwise set

$$
\boldsymbol{d}_k=-\boldsymbol{g}_k
$$

Choose $\alpha_k$ by one-dimensional search

$$
\alpha_k\in\arg\min_{\alpha>0}f(\boldsymbol{x}_k+\alpha\boldsymbol{d}_k)
$$

Update

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+\alpha_k\boldsymbol{d}_k
=
\boldsymbol{x}_k-\alpha_k\boldsymbol{g}_k
$$

If $\boldsymbol{g}_k\ne\boldsymbol{0}$, then
$$
\boldsymbol{g}_k^T\boldsymbol{d}_k
=
-\boldsymbol{g}_k^T\boldsymbol{g}_k
=
-\|\boldsymbol{g}_k\|^2
<
0
$$

Therefore $-\boldsymbol{g}_k$ is a descent direction.

##### Example

Solve

$$
\min f(\boldsymbol{x})=2x_1^2+x_2^2
$$

Initial point

$$
\boldsymbol{x}_1=
\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

Stopping tolerance

$$
\varepsilon=\frac{1}{10}
$$

The gradient is

$$
\nabla f(\boldsymbol{x})
=
\begin{bmatrix}
4x_1\\
2x_2
\end{bmatrix}
$$

**First iteration**. At
$$
\boldsymbol{x}_1=
\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

the steepest descent direction is

$$
\boldsymbol{d}_1
=
-\nabla f(\boldsymbol{x}_1)
=
\begin{bmatrix}
-4\\
-2
\end{bmatrix}
$$

$$
\|\boldsymbol{d}_1\|
=
\sqrt{16+4}
=
2\sqrt{5}
>
\frac{1}{10}
$$

Starting from $\boldsymbol{x}_1$, perform one-dimensional search along $\boldsymbol{d}_1$

$$
\min_{\alpha\ge 0}
\varphi(\alpha)
=
f(\boldsymbol{x}_1+\alpha\boldsymbol{d}_1)
$$

We have

$$
\boldsymbol{x}_1+\alpha\boldsymbol{d}_1
=
\begin{bmatrix}
1\\
1
\end{bmatrix}
+
\alpha
\begin{bmatrix}
-4\\
-2
\end{bmatrix}
=
\begin{bmatrix}
1-4\alpha\\
1-2\alpha
\end{bmatrix}
$$

Thus

$$
\varphi(\alpha)
=
2(1-4\alpha)^2+(1-2\alpha)^2
$$

Let

$$
\varphi'(\alpha)
=
-16(1-4\alpha)-4(1-2\alpha)
=
0
$$

$$
\alpha_1=\frac{5}{18}
$$

Therefore

$$
\boldsymbol{x}_2
=
\boldsymbol{x}_1+\alpha_1\boldsymbol{d}_1
=
\begin{bmatrix}
-\frac{1}{9}\\
\frac{4}{9}
\end{bmatrix}
$$

**Second iteration**. At $\boldsymbol{x}_2$, the steepest descent direction is
$$
\boldsymbol{d}_2
=
-\nabla f(\boldsymbol{x}_2)
=
\begin{bmatrix}
\frac{4}{9}\\
-\frac{8}{9}
\end{bmatrix}
$$

$$
\|\boldsymbol{d}_2\|
=
\sqrt{
\left(\frac{4}{9}\right)^2
+
\left(-\frac{8}{9}\right)^2
}
=
\frac{4\sqrt{5}}{9}
>
\frac{1}{10}
$$

Starting from $\boldsymbol{x}_2$, perform one-dimensional search along $\boldsymbol{d}_2$

$$
\min_{\alpha\ge 0}
\varphi(\alpha)
=
f(\boldsymbol{x}_2+\alpha\boldsymbol{d}_2)
$$

We have

$$
\boldsymbol{x}_2+\alpha\boldsymbol{d}_2
=
\begin{bmatrix}
-\frac{1}{9}\\
\frac{4}{9}
\end{bmatrix}
+
\alpha
\begin{bmatrix}
\frac{4}{9}\\
-\frac{8}{9}
\end{bmatrix}
=
\begin{bmatrix}
-\frac{1}{9}+\frac{4}{9}\alpha\\
\frac{4}{9}-\frac{8}{9}\alpha
\end{bmatrix}
$$

Thus

$$
\varphi(\alpha)
=
\frac{2}{81}(-1+4\alpha)^2
+
\frac{16}{81}(1-2\alpha)^2
$$

Let

$$
\varphi'(\alpha)
=
\frac{16}{81}(-1+4\alpha)
-
\frac{64}{81}(1-2\alpha)
=
0
$$

$$
\alpha_2=\frac{5}{12}
$$

Therefore

$$
\boldsymbol{x}_3
=
\boldsymbol{x}_2+\alpha_2\boldsymbol{d}_2
=
\frac{2}{27}
\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

**Third iteration**. At $\boldsymbol{x}_3$, the steepest descent direction is
$$
\boldsymbol{d}_3
=
-\nabla f(\boldsymbol{x}_3)
=
\frac{4}{27}
\begin{bmatrix}
-2\\
-1
\end{bmatrix}
$$

$$
\|\boldsymbol{d}_3\|
=
\frac{4\sqrt{5}}{27}
>
\frac{1}{10}
$$

Starting from $\boldsymbol{x}_3$, perform one-dimensional search along $\boldsymbol{d}_3$

$$
\min_{\alpha\ge 0}
\varphi(\alpha)
=
f(\boldsymbol{x}_3+\alpha\boldsymbol{d}_3)
$$

We have

$$
\boldsymbol{x}_3+\alpha\boldsymbol{d}_3
=
\frac{2}{27}
\begin{bmatrix}
1\\
1
\end{bmatrix}
+
\alpha
\frac{4}{27}
\begin{bmatrix}
-2\\
-1
\end{bmatrix}
=
\frac{2}{27}
\begin{bmatrix}
1-4\alpha\\
1-2\alpha
\end{bmatrix}
$$

Thus

$$
\varphi(\alpha)
=
\frac{8}{27^2}(1-4\alpha)^2
+
\frac{4}{27^2}(1-2\alpha)^2
$$

Let

$$
\varphi'(\alpha)=0
$$

$$
\alpha_3=\frac{5}{18}
$$

Therefore

$$
\boldsymbol{x}_4
=
\boldsymbol{x}_3+\alpha_3\boldsymbol{d}_3
=
\frac{2}{27}
\begin{bmatrix}
-\frac{1}{9}\\
\frac{4}{9}
\end{bmatrix}
=
\frac{2}{243}
\begin{bmatrix}
-1\\
4
\end{bmatrix}
$$

At this point

$$
\|\nabla f(\boldsymbol{x}_4)\|
=
\frac{8\sqrt{5}}{243}
<
\frac{1}{10}
$$

The stopping criterion is satisfied, so the approximate solution is

$$
\boldsymbol{x}
=
\frac{2}{243}
\begin{bmatrix}
-1\\
4
\end{bmatrix}
$$

The exact minimizer is

$$
\boldsymbol{x}^*
=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

##### Convergence

Let

$$
\phi(\alpha)
=
f(\boldsymbol{x}_k-\alpha\boldsymbol{g}_k)
$$

By the chain rule

$$
\phi'(\alpha)
=
\nabla f(\boldsymbol{x}_k-\alpha\boldsymbol{g}_k)^T
\frac{d}{d\alpha}
(\boldsymbol{x}_k-\alpha\boldsymbol{g}_k)
=
-\nabla f(\boldsymbol{x}_k-\alpha\boldsymbol{g}_k)^T\boldsymbol{g}_k
$$

If exact line search is used, then

$$
\alpha_k
\in
\arg\min_{\alpha>0}
\phi(\alpha)
$$

If $\alpha_k$ is an interior minimizer, then the first-order necessary condition gives

$$
\phi'(\alpha_k)
=
-\nabla f(\boldsymbol{x}_k-\alpha_k\boldsymbol{g}_k)^T\boldsymbol{g}_k
=0
$$

By the iteration formula

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k-\alpha_k\boldsymbol{g}_k
$$

$$
\nabla f(\boldsymbol{x}_k-\alpha_k\boldsymbol{g}_k)
=
\nabla f(\boldsymbol{x}_{k+1})
=
\boldsymbol{g}_{k+1}
$$

we get

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{g}_k=0
$$

Therefore the sequence $\{\boldsymbol{x}_{k}\}$ often moves along a zigzag path.

When $\boldsymbol{x}_{k}$ is close to the minimizer $\boldsymbol{x}^*$, each step length becomes small. The iterates move from one side of the valley to the other, and the convergence speed is reduced.

Thus two consecutive gradients are orthogonal. The orthogonality relation is one reason for the typical **zigzag behavior**.

Let

$$
e_k \ge 0
$$

be the error at iteration $k$, and suppose

$$
e_k \to 0
$$

The **convergence ratio** is defined by

$$
\rho
=
\lim_{k\to\infty}
\frac{e_{k+1}}{e_k}
$$

if the limit exists.

More generally, use

$$
\rho
=
\limsup_{k\to\infty}
\frac{e_{k+1}}{e_k}
$$

If

$$
0<\rho<1
$$

then the sequence converges linearly.

For objective function values, the error is usually

$$
e_k
=
f(\boldsymbol{x}_k)-f(\boldsymbol{x}^*)
$$

Thus the convergence ratio is

$$
\rho
=
\limsup_{k\to\infty}
\frac{
f(\boldsymbol{x}_{k+1})-f(\boldsymbol{x}^*)
}{
f(\boldsymbol{x}_{k})-f(\boldsymbol{x}^*)
}
$$

It measures the asymptotic factor by which the error is reduced from one iteration to the next.

**Theorem.**

Assume that $f(\boldsymbol{x})$ has continuous second-order partial derivatives, and that $\boldsymbol{x}^*$ is a local minimizer.

Let

$$
\boldsymbol{G}^*
=
\nabla^2 f(\boldsymbol{x}^*)
$$

Assume that $\boldsymbol{G}^*$ is symmetric positive definite. Let the smallest eigenvalue of $\boldsymbol{G}^*$ be $a>0$, and let the largest eigenvalue be $A$.

If the sequence $\{\boldsymbol{x}_k\}$ generated by the steepest descent method converges to $\boldsymbol{x}^*$, then the objective function value sequence $\{f(\boldsymbol{x}_k)\}$ converges linearly to $f(\boldsymbol{x}^*)$, and its **convergence ratio** is no greater than

$$
\left(\frac{A-a}{A+a}\right)^2
$$

That is,

$$
\limsup_{k\to\infty}
\frac{
f(\boldsymbol{x}_{k+1})-f(\boldsymbol{x}^*)
}{
f(\boldsymbol{x}_k)-f(\boldsymbol{x}^*)
}
\le
\left(\frac{A-a}{A+a}\right)^2
$$
Now define
$$
r=\frac{A}{a}
$$

where $r$ is the **condition number** of the symmetric positive definite matrix $\boldsymbol{G}^*$. 

Thus

$$
\left(\frac{A-a}{A+a}\right)^2
=
\left(\frac{r-1}{r+1}\right)^2
$$

Since $A\ge a>0$,

$$
r\ge 1
$$

$$
0\le \frac{r-1}{r+1}<1
$$

$$
0\le
\left(\frac{r-1}{r+1}\right)^2
<1
$$

The convergence ratio is therefore less than $1$, so the objective function values converge linearly.

The size of this ratio depends directly on the condition number $r$. If $r$ is close to $1$, then

$$
\left(\frac{r-1}{r+1}\right)^2
$$

is close to $0$, and the convergence is fast.

If $r$ is large, then

$$
\left(\frac{r-1}{r+1}\right)^2
$$

is also close to $1$, and the convergence is slow.

Geometrically, a small condition number means that the level sets of $f$ near $\boldsymbol{x}^*$ are close to circles. A large condition number means that the level sets are long and narrow ellipses.

For steepest descent with exact line search, consecutive gradients satisfy

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{g}_k=0
$$

Hence the method often moves from one side of a narrow valley to the other. When the condition number is large, this zigzag behavior becomes more serious, and the decrease of the objective function becomes slow.
