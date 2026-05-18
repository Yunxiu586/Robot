# Derivative-Based Optimization Methods

[toc]

### Problem and Notation

Consider the unconstrained problem

$$
\min_{\boldsymbol{x}\in \mathbb{R}^n} f(\boldsymbol{x})
$$

where $f:\mathbb{R}^n\to\mathbb{R}$ is continuously differentiable or twice continuously differentiable.

Use

$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

$$
\boldsymbol{G}_k=\nabla^2 f(\boldsymbol{x}_k)
$$

A general derivative-based iteration has the form

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_k+\alpha_k\boldsymbol{d}_k
$$

where $\boldsymbol{d}_k$ is a search direction and $\alpha_k>0$ is a step length.

A vector $\boldsymbol{d}_k$ is a descent direction at $\boldsymbol{x}_k$ if

$$
\boldsymbol{g}_k^T\boldsymbol{d}_k<0
$$

A point $\boldsymbol{x}^*$ is stationary if

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

### Taylor Expansion and Optimality Conditions

##### First-order expansion

Define
$$
\phi(t)=f(\boldsymbol{x}+t\boldsymbol{d})
$$
Then
$$
\phi(0)=f(\boldsymbol{x})
$$

$$
\phi(1)=f(\boldsymbol{x}+\boldsymbol{d})
$$

By the fundamental theorem of calculus
$$
\phi(1)-\phi(0)=\int_0^1 \phi'(t)\,dt
$$
Now compute $\phi'(t)$ by the chain rule
$$
\phi'(t)
=
\nabla f(\boldsymbol{x}+t\boldsymbol{d})^T
\frac{d}{dt}(\boldsymbol{x}+t\boldsymbol{d})
=
\nabla f(\boldsymbol{x}+t\boldsymbol{d})^T\boldsymbol{d}
$$
Therefore
$$
f(\boldsymbol{x}+\boldsymbol{d})-f(\boldsymbol{x})
=
\phi(1)-\phi(0)
=
\int_0^1 \nabla f(\boldsymbol{x}+t\boldsymbol{d})^T\boldsymbol{d}\,dt
$$
Separate the value at $\boldsymbol{x}$
$$
f(\boldsymbol{x}+\boldsymbol{d})-f(\boldsymbol{x})
=
\nabla f(\boldsymbol{x})^T\boldsymbol{d}
+
\int_0^1
\left[
\nabla f(\boldsymbol{x}+t\boldsymbol{d})-\nabla f(\boldsymbol{x})
\right]^T
\boldsymbol{d}\,dt
$$
Let
$$
r_1(\boldsymbol{d})
=
\int_0^1
\left[
\nabla f(\boldsymbol{x}+t\boldsymbol{d})-\nabla f(\boldsymbol{x})
\right]^T
\boldsymbol{d}\,dt
$$
Then
$$
|r_1(\boldsymbol{d})|
\le
\|\boldsymbol{d}\|
\sup_{0\le t\le 1}
\left\|
\nabla f(\boldsymbol{x}+t\boldsymbol{d})-\nabla f(\boldsymbol{x})
\right\|
$$
Since $f\in C^1$
$$
\sup_{0\le t\le 1}
\left\|
\nabla f(\boldsymbol{x}+t\boldsymbol{d})-\nabla f(\boldsymbol{x})
\right\|
\to 0
\qquad
\|\boldsymbol{d}\|\to 0
$$
Hence
$$
r_1(\boldsymbol{d})=o(\|\boldsymbol{d}\|)
$$
Therefore, if $f\in C^1$, then for small $\boldsymbol{d}$
$$
f(\boldsymbol{x}+\boldsymbol{d})
=
f(\boldsymbol{x})
+
\nabla f(\boldsymbol{x})^T\boldsymbol{d}
+
o(\|\boldsymbol{d}\|)
$$

##### Second-order expansion

Define

$$
\phi(t)=f(\boldsymbol{x}+t\boldsymbol{d})
$$

Then

$$
\phi(0)=f(\boldsymbol{x})
$$

$$
\phi(1)=f(\boldsymbol{x}+\boldsymbol{d})
$$

By the chain rule

$$
\phi'(t)
=
\nabla f(\boldsymbol{x}+t\boldsymbol{d})^T\boldsymbol{d}
$$

Thus

$$
\phi'(0)
=
\nabla f(\boldsymbol{x})^T\boldsymbol{d}
$$

Taking derivative again

$$
\phi''(t)
=
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
\boldsymbol{d}
$$

From the fundamental theorem of calculus

$$
\phi(1)-\phi(0)
=
\int_0^1 \phi'(s)\,ds
$$

For $\phi'(s)$, again use the fundamental theorem of calculus

$$
\phi'(s)
=
\phi'(0)+\int_0^s \phi''(t)\,dt
$$

$$
\phi(1)-\phi(0)
=
\int_0^1
\left[
\phi'(0)+\int_0^s \phi''(t)\,dt
\right]
ds
$$

Separate the two terms

$$
\phi(1)-\phi(0)
=
\phi'(0)
+
\int_0^1
\int_0^s
\phi''(t)\,dt\,ds
$$

Now change the order of integration

$$
\int_0^1
\int_0^s
\phi''(t)\,dt\,ds
=
\int_0^1
\int_t^1
\phi''(t)\,ds\,dt
$$

we get

$$
\int_0^1
\int_0^s
\phi''(t)\,dt\,ds
=
\int_0^1
(1-t)\phi''(t)\,dt
$$

Therefore

$$
\phi(1)
=
\phi(0)
+
\phi'(0)
+
\int_0^1
(1-t)\phi''(t)\,dt
$$

Substitute back to the multivariable function
$$
\phi(1)=f(\boldsymbol{x}+\boldsymbol{d})
$$

$$
\phi(0)=f(\boldsymbol{x})
$$

$$
\phi'(0)=\nabla f(\boldsymbol{x})^T\boldsymbol{d}
$$

$$
\phi''(t)
=
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
\boldsymbol{d}
$$

we obtain

$$
f(\boldsymbol{x}+\boldsymbol{d})
=
f(\boldsymbol{x})
+
\nabla f(\boldsymbol{x})^T\boldsymbol{d}
+
\int_0^1
(1-t)
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
\boldsymbol{d}
\,dt
$$
Separate the Hessian at $\boldsymbol{x}$
$$
\int_0^1
(1-t)
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
\boldsymbol{d}
\,dt
=
\frac{1}{2}
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x})
\boldsymbol{d}
+
r_2(\boldsymbol{d})
$$
where
$$
r_2(\boldsymbol{d})
=
\int_0^1
(1-t)
\boldsymbol{d}^T
\left[
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
-
\nabla^2 f(\boldsymbol{x})
\right]
\boldsymbol{d}
\,dt
$$
Using the matrix norm inequality
$$
|r_2(\boldsymbol{d})|
\le
\|\boldsymbol{d}\|^2
\int_0^1
(1-t)
\left\|
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
-
\nabla^2 f(\boldsymbol{x})
\right\|
\,dt
$$
Thus
$$
|r_2(\boldsymbol{d})|
\le
\frac{1}{2}
\|\boldsymbol{d}\|^2
\sup_{0\le t\le 1}
\left\|
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
-
\nabla^2 f(\boldsymbol{x})
\right\|
$$
Since $f\in C^2$
$$
\sup_{0\le t\le 1}
\left\|
\nabla^2 f(\boldsymbol{x}+t\boldsymbol{d})
-
\nabla^2 f(\boldsymbol{x})
\right\|
\to 0
\qquad
\|\boldsymbol{d}\|\to 0
$$
Hence
$$
r_2(\boldsymbol{d})=o(\|\boldsymbol{d}\|^2)
$$
If $f\in C^2$, then
$$
f(\boldsymbol{x}+\boldsymbol{d})=f(\boldsymbol{x})+\nabla f(\boldsymbol{x})^T\boldsymbol{d}+\frac{1}{2}\boldsymbol{d}^T\nabla^2 f(\boldsymbol{x})\boldsymbol{d}+o(\|\boldsymbol{d}\|^2)
$$

##### First-order necessary condition

If $\boldsymbol{x}^*$ is a local minimizer and $f\in C^1$, then

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

Proof

For any $\boldsymbol{d}\in\mathbb{R}^n$, define

$$
\phi(t)=f(\boldsymbol{x}^*+t\boldsymbol{d})
$$

Since $\boldsymbol{x}^*$ is a local minimizer, $t=0$ is a local minimizer of $\phi$. Hence

$$
\phi'(0)=0
$$

By the chain rule

$$
\phi'(0)=\nabla f(\boldsymbol{x}^*)^T\boldsymbol{d}
$$

Thus

$$
\nabla f(\boldsymbol{x}^*)^T\boldsymbol{d}=0
\qquad \forall \boldsymbol{d}\in\mathbb{R}^n
$$

Taking $\boldsymbol{d}=\nabla f(\boldsymbol{x}^*)$ gives

$$
\|\nabla f(\boldsymbol{x}^*)\|^2=0
$$

Therefore

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

##### Second-order necessary condition

If $\boldsymbol{x}^*$ is a local minimizer and $f\in C^2$, then

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

$$
\nabla^2 f(\boldsymbol{x}^*)\succeq \boldsymbol{0}
$$

Proof

Using the second-order expansion at $\boldsymbol{x}^*$ and $\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}$

$$
f(\boldsymbol{x}^*+t\boldsymbol{d})-f(\boldsymbol{x}^*)=\frac{1}{2}t^2\boldsymbol{d}^T\nabla^2 f(\boldsymbol{x}^*)\boldsymbol{d}+o(t^2)
$$

Since $\boldsymbol{x}^*$ is a local minimizer, the left-hand side is nonnegative for small $t$. Dividing by $t^2$ and letting $t\to0$ gives

$$
\boldsymbol{d}^T\nabla^2 f(\boldsymbol{x}^*)\boldsymbol{d}\ge 0
\qquad \forall \boldsymbol{d}\in\mathbb{R}^n
$$

Thus

$$
\nabla^2 f(\boldsymbol{x}^*)\succeq \boldsymbol{0}
$$

##### Second-order sufficient condition

If $f\in C^2$ and

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

$$
\nabla^2 f(\boldsymbol{x}^*)\succ \boldsymbol{0}
$$

then $\boldsymbol{x}^*$ is a strict local minimizer.

Proof

Because $\nabla^2 f(\boldsymbol{x}^*)\succ\boldsymbol{0}$, there exists $m>0$ such that

$$
\boldsymbol{d}^T\nabla^2 f(\boldsymbol{x}^*)\boldsymbol{d}\ge m\|\boldsymbol{d}\|^2
$$

Using Taylor expansion

$$
f(\boldsymbol{x}^*+\boldsymbol{d})-f(\boldsymbol{x}^*)=\frac{1}{2}\boldsymbol{d}^T\nabla^2 f(\boldsymbol{x}^*)\boldsymbol{d}+o(\|\boldsymbol{d}\|^2)
$$

For sufficiently small nonzero $\boldsymbol{d}$

$$
f(\boldsymbol{x}^*+\boldsymbol{d})-f(\boldsymbol{x}^*)\ge \frac{m}{4}\|\boldsymbol{d}\|^2>0
$$

Therefore $\boldsymbol{x}^*$ is a strict local minimizer.

### Descent Methods and Line Search

##### Descent framework

At iteration $k$, choose $\boldsymbol{d}_k$ so that

$$
\boldsymbol{g}_k^T\boldsymbol{d}_k<0
$$

Then choose $\alpha_k$ and set

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_k+\alpha_k\boldsymbol{d}_k
$$

##### Exact line search

The exact step length is

$$
\alpha_k\in \arg\min_{\alpha>0} f(\boldsymbol{x}_k+\alpha\boldsymbol{d}_k)
$$

For a differentiable one-dimensional function

$$
\phi(\alpha)=f(\boldsymbol{x}_k+\alpha\boldsymbol{d}_k)
$$

an interior exact line search step satisfies

$$
\phi'(\alpha_k)=\nabla f(\boldsymbol{x}_k+\alpha_k\boldsymbol{d}_k)^T\boldsymbol{d}_k=0
$$

### Steepest Descent Method

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
\|\boldsymbol{d}\|=1
$$

the steepest descent direction solves

$$
\min_{\|\boldsymbol{d}\|=1}
\boldsymbol{g}_k^T\boldsymbol{d}
$$

By the Cauchy-Schwarz inequality

$$
\boldsymbol{g}_k^T\boldsymbol{d}
\ge
-\|\boldsymbol{g}_k\|\|\boldsymbol{d}\|
=
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
\alpha_k\in\arg\min_{\alpha>0}f(\boldsymbol{x}_k-\alpha\boldsymbol{g}_k)
$$

Update

$$
\boldsymbol{x}_{k+1}
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

Its norm is

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
\min_{\lambda\ge 0}
\varphi(\lambda)
=
f(\boldsymbol{x}_1+\lambda\boldsymbol{d}_1)
$$

We have

$$
\boldsymbol{x}_1+\lambda\boldsymbol{d}_1
=
\begin{bmatrix}
1\\
1
\end{bmatrix}
+
\lambda
\begin{bmatrix}
-4\\
-2
\end{bmatrix}
=
\begin{bmatrix}
1-4\lambda\\
1-2\lambda
\end{bmatrix}
$$

Thus

$$
\varphi(\lambda)
=
2(1-4\lambda)^2+(1-2\lambda)^2
$$

Let

$$
\varphi'(\lambda)
=
-16(1-4\lambda)-4(1-2\lambda)
=
0
$$

Solving gives

$$
\lambda_1=\frac{5}{18}
$$

Therefore

$$
\boldsymbol{x}_2
=
\boldsymbol{x}_1+\lambda_1\boldsymbol{d}_1
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

Its norm is

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
\min_{\lambda\ge 0}
\varphi(\lambda)
=
f(\boldsymbol{x}_2+\lambda\boldsymbol{d}_2)
$$

We have

$$
\boldsymbol{x}_2+\lambda\boldsymbol{d}_2
=
\begin{bmatrix}
-\frac{1}{9}\\
\frac{4}{9}
\end{bmatrix}
+
\lambda
\begin{bmatrix}
\frac{4}{9}\\
-\frac{8}{9}
\end{bmatrix}
=
\begin{bmatrix}
-\frac{1}{9}+\frac{4}{9}\lambda\\
\frac{4}{9}-\frac{8}{9}\lambda
\end{bmatrix}
$$

Thus

$$
\varphi(\lambda)
=
\frac{2}{81}(-1+4\lambda)^2
+
\frac{16}{81}(1-2\lambda)^2
$$

Let

$$
\varphi'(\lambda)
=
\frac{16}{81}(-1+4\lambda)
-
\frac{64}{81}(1-2\lambda)
=
0
$$

Solving gives

$$
\lambda_2=\frac{5}{12}
$$

Therefore

$$
\boldsymbol{x}_3
=
\boldsymbol{x}_2+\lambda_2\boldsymbol{d}_2
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

Its norm is

$$
\|\boldsymbol{d}_3\|
=
\frac{4\sqrt{5}}{27}
>
\frac{1}{10}
$$

Starting from $\boldsymbol{x}_3$, perform one-dimensional search along $\boldsymbol{d}_3$

$$
\min_{\lambda\ge 0}
\varphi(\lambda)
=
f(\boldsymbol{x}_3+\lambda\boldsymbol{d}_3)
$$

We have

$$
\boldsymbol{x}_3+\lambda\boldsymbol{d}_3
=
\frac{2}{27}
\begin{bmatrix}
1\\
1
\end{bmatrix}
+
\lambda
\frac{4}{27}
\begin{bmatrix}
-2\\
-1
\end{bmatrix}
=
\frac{2}{27}
\begin{bmatrix}
1-4\lambda\\
1-2\lambda
\end{bmatrix}
$$

Thus

$$
\varphi(\lambda)
=
\frac{8}{27^2}(1-4\lambda)^2
+
\frac{4}{27^2}(1-2\lambda)^2
$$

Let

$$
\varphi'(\lambda)=0
$$

Solving gives

$$
\lambda_3=\frac{5}{18}
$$

Therefore

$$
\boldsymbol{x}_4
=
\boldsymbol{x}_3+\lambda_3\boldsymbol{d}_3
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
\phi'(\alpha_k)=0
$$

Substitute $\alpha=\alpha_k$

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

we have

$$
0\le \frac{r-1}{r+1}<1
$$

and therefore

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

### Newton Method

##### Quadratic approximation

At iteration $k$, let

$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

$$
\boldsymbol{G}_k=\nabla^2 f(\boldsymbol{x}_k)
$$

Assume that $f$ is twice differentiable. Near $\boldsymbol{x}_k$, use the second-order Taylor approximation

$$
f(\boldsymbol{x})
\approx
\psi_k(\boldsymbol{x})
=
f(\boldsymbol{x}_k)
+
\boldsymbol{g}_k^T(\boldsymbol{x}-\boldsymbol{x}_k)
+
\frac{1}{2}
(\boldsymbol{x}-\boldsymbol{x}_k)^T
\boldsymbol{G}_k
(\boldsymbol{x}-\boldsymbol{x}_k)
$$

Let

$$
\boldsymbol{d}=\boldsymbol{x}-\boldsymbol{x}_k
$$

Then the quadratic model can be written as

$$
\psi_k(\boldsymbol{d})
=
f(\boldsymbol{x}_k)
+
\boldsymbol{g}_k^T\boldsymbol{d}
+
\frac{1}{2}
\boldsymbol{d}^T\boldsymbol{G}_k\boldsymbol{d}
$$

To find the stationary point of the model, set

$$
\nabla \psi_k(\boldsymbol{d})=\boldsymbol{0}
$$

Since

$$
\nabla \psi_k(\boldsymbol{d})
=
\boldsymbol{g}_k+
\boldsymbol{G}_k\boldsymbol{d}
$$

we obtain the Newton equation

$$
\boldsymbol{G}_k\boldsymbol{d}_k=-\boldsymbol{g}_k
$$

If $\boldsymbol{G}_k$ is nonsingular, then

$$
\boldsymbol{d}_k
=
-\boldsymbol{G}_k^{-1}\boldsymbol{g}_k
$$

##### Pure Newton iteration

The pure Newton method takes the full Newton step

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+\boldsymbol{d}_k
$$

Therefore

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k
-
\boldsymbol{G}_k^{-1}\boldsymbol{g}_k
$$

The iteration is repeated by computing the new gradient and Hessian at $\boldsymbol{x}_{k+1}$.

##### Local convergence

Let $\boldsymbol{x}^*$ satisfy

$$
\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}
$$

Assume that $\nabla^2 f(\boldsymbol{x}^*)^{-1}$ exists and that the initial point is sufficiently close to $\boldsymbol{x}^*$.

Define the Newton mapping

$$
\boldsymbol{A}(\boldsymbol{x})
=
\boldsymbol{x}
-
\nabla^2 f(\boldsymbol{x})^{-1}\nabla f(\boldsymbol{x})
$$

Let

$$
\boldsymbol{y}=\boldsymbol{A}(\boldsymbol{x})
$$

Using $\nabla f(\boldsymbol{x}^*)=\boldsymbol{0}$, we have

$$
\boldsymbol{y}-\boldsymbol{x}^*
=
\boldsymbol{x}
-
\nabla^2 f(\boldsymbol{x})^{-1}\nabla f(\boldsymbol{x})
-
\boldsymbol{x}^*
$$

$$
\boldsymbol{y}-\boldsymbol{x}^*
=
(\boldsymbol{x}-\boldsymbol{x}^*)
-
\nabla^2 f(\boldsymbol{x})^{-1}
\left[
\nabla f(\boldsymbol{x})-
\nabla f(\boldsymbol{x}^*)
\right]
$$

$$
\boldsymbol{y}-\boldsymbol{x}^*
=
\nabla^2 f(\boldsymbol{x})^{-1}
\left[
\nabla f(\boldsymbol{x}^*)
-
\nabla f(\boldsymbol{x})
-
\nabla^2 f(\boldsymbol{x})(\boldsymbol{x}^*-\boldsymbol{x})
\right]
$$

If there exist constants $k_1,k_2>0$ such that

$$
\left\|
\nabla^2 f(\boldsymbol{x})^{-1}
\right\|
\le k_1
$$

and

$$
\frac{
\left\|
\nabla f(\boldsymbol{x}^*)
-
\nabla f(\boldsymbol{x})
-
\nabla^2 f(\boldsymbol{x})(\boldsymbol{x}^*-\boldsymbol{x})
\right\|
}{
\left\|
\boldsymbol{x}^*-\boldsymbol{x}
\right\|
}
\le k_2
$$

with

$$
k_1k_2<1
$$

then

$$
\left\|
\boldsymbol{y}-\boldsymbol{x}^*
\right\|
\le
k_1k_2
\left\|
\boldsymbol{x}^*-\boldsymbol{x}
\right\|
<
\left\|
\boldsymbol{x}^*-\boldsymbol{x}
\right\|
$$

Thus the Newton mapping decreases the distance to $\boldsymbol{x}^*$ locally.

When Newton method converges, it has at least quadratic convergence locally, namely

$$
\left\|
\boldsymbol{x}_{k+1}-\boldsymbol{x}^*
\right\|
\le
c
\left\|
\boldsymbol{x}_k-\boldsymbol{x}^*
\right\|^2
$$

where $c$ is a positive constant.

##### Example

Solve

$$
\min f(\boldsymbol{x})=(x_1-1)^4+x_2^2
$$

Take

$$
\boldsymbol{x}_1=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

The gradient and Hessian are

$$
\nabla f(\boldsymbol{x})
=
\begin{bmatrix}
4(x_1-1)^3\\
2x_2
\end{bmatrix}
$$

$$
\nabla^2 f(\boldsymbol{x})
=
\begin{bmatrix}
12(x_1-1)^2 & 0\\
0 & 2
\end{bmatrix}
$$

At $\boldsymbol{x}_1$,

$$
\boldsymbol{g}_1
=
\begin{bmatrix}
-4\\
2
\end{bmatrix}
$$

$$
\boldsymbol{G}_1
=
\begin{bmatrix}
12 & 0\\
0 & 2
\end{bmatrix}
$$

Thus

$$
\boldsymbol{x}_2
=
\boldsymbol{x}_1-
\boldsymbol{G}_1^{-1}\boldsymbol{g}_1
=
\begin{bmatrix}
0\\
1
\end{bmatrix}
-
\begin{bmatrix}
12 & 0\\
0 & 2
\end{bmatrix}^{-1}
\begin{bmatrix}
-4\\
2
\end{bmatrix}
=
\begin{bmatrix}
\frac{1}{3}\\
0
\end{bmatrix}
$$

At $\boldsymbol{x}_2$,

$$
\boldsymbol{g}_2
=
\begin{bmatrix}
-rac{32}{27}\\
0
\end{bmatrix}
$$

$$
\boldsymbol{G}_2
=
\begin{bmatrix}
\frac{48}{9} & 0\\
0 & 2
\end{bmatrix}
$$

Therefore

$$
\boldsymbol{x}_3
=
\boldsymbol{x}_2-
\boldsymbol{G}_2^{-1}\boldsymbol{g}_2
=
\begin{bmatrix}
\frac{5}{9}\\
0
\end{bmatrix}
$$

Continuing gives

$$
\boldsymbol{x}_4
=
\begin{bmatrix}
\frac{19}{27}\\
0
\end{bmatrix}
$$

$$
\boldsymbol{x}_5
=
\begin{bmatrix}
\frac{65}{81}\\
0
\end{bmatrix}
$$

The minimizer is

$$
\boldsymbol{x}^*
=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

##### Quadratic termination

For the strictly convex quadratic function

$$
f(\boldsymbol{x})
=
\frac{1}{2}\boldsymbol{x}^T\boldsymbol{A}\boldsymbol{x}
+
\boldsymbol{b}^T\boldsymbol{x}
+
c
$$

where

$$
\boldsymbol{A}\succ\boldsymbol{0}
$$

we have

$$
\nabla f(\boldsymbol{x})
=
\boldsymbol{A}\boldsymbol{x}+\boldsymbol{b}
$$

The stationary condition gives

$$
\boldsymbol{A}\boldsymbol{x}+\boldsymbol{b}=\boldsymbol{0}
$$

Thus

$$
\boldsymbol{x}^*=-\boldsymbol{A}^{-1}\boldsymbol{b}
$$

For any initial point $\boldsymbol{x}_1$,

$$
\boldsymbol{x}_2
=
\boldsymbol{x}_1
-
\boldsymbol{A}^{-1}\nabla f(\boldsymbol{x}_1)
$$

$$
\boldsymbol{x}_2
=
\boldsymbol{x}_1
-
\boldsymbol{A}^{-1}(\boldsymbol{A}\boldsymbol{x}_1+\boldsymbol{b})
=
-\boldsymbol{A}^{-1}\boldsymbol{b}
$$

Hence Newton method reaches the minimizer in one iteration for a strictly convex quadratic function. This property is called quadratic termination.

##### Limitation of the pure Newton method

When the initial point is far from the minimizer, the pure Newton method may fail to converge.

One reason is that the Newton direction

$$
\boldsymbol{d}
=
-
\nabla^2 f(\boldsymbol{x})^{-1}
\nabla f(\boldsymbol{x})
$$

is not necessarily a descent direction. The objective function value may increase. Even if the function value decreases, the full Newton step may not be the best point along the Newton direction.

### Damped Newton Method

##### Basic form

The damped Newton method adds a one-dimensional search along the Newton direction.

The iteration is

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

where

$$
\boldsymbol{d}_k
=
-
\boldsymbol{G}_k^{-1}\boldsymbol{g}_k
$$

and $\alpha_k$ is chosen by line search

$$
f(\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k)
=
\min_{\alpha}
f(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
$$

##### Algorithm

Choose an initial point $\boldsymbol{x}_1$ and a tolerance $\varepsilon>0$. Set $k=1$.

At iteration $k$, compute

$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

$$
\boldsymbol{G}_k=\nabla^2 f(\boldsymbol{x}_k)
$$

If

$$
\|\boldsymbol{g}_k\|<\varepsilon
$$

stop.

Otherwise set

$$
\boldsymbol{d}_k
=
-
\boldsymbol{G}_k^{-1}\boldsymbol{g}_k
$$

Choose $\alpha_k$ by line search

$$
\min_{\alpha}
f(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
=
f(\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k)
$$

Update

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

Set $k:=k+1$ and repeat.

Because the damped Newton method uses line search, the objective function value usually decreases and does not increase under exact line search. Under suitable assumptions, it has global convergence and second-order local convergence.

### Modified Newton Method

##### Motivation

The pure Newton method and damped Newton method have two common difficulties.

First, the Hessian may be singular, so the Newton direction cannot be computed.

Second, even if the Hessian is nonsingular, it may not be positive definite. Then the Newton direction may fail to be a descent direction.

##### Failure example

Consider

$$
\min f(\boldsymbol{x})
=
x_1^4+x_1x_2+(1+x_2)^2
$$

Take

$$
\boldsymbol{x}_1=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

At $\boldsymbol{x}_1$,

$$
\boldsymbol{g}_1
=
\begin{bmatrix}
0\\
2
\end{bmatrix}
$$

$$
\boldsymbol{G}_1
=
\begin{bmatrix}
0 & 1\\
1 & 2
\end{bmatrix}
$$

The Newton direction is

$$
\boldsymbol{d}_1
=
-
\boldsymbol{G}_1^{-1}\boldsymbol{g}_1
=
-
\begin{bmatrix}
0 & 1\\
1 & 2
\end{bmatrix}^{-1}
\begin{bmatrix}
0\\
2
\end{bmatrix}
=
\begin{bmatrix}
-2\\
0
\end{bmatrix}
$$

Along this direction,

$$
\phi(\alpha)
=
f(\boldsymbol{x}_1+
\alpha\boldsymbol{d}_1)
=
16\alpha^4+1
$$

Thus

$$
\phi'(\alpha)=64\alpha^3
$$

The one-dimensional minimizer is

$$
\alpha_1=0
$$

So the damped Newton method cannot generate a new point, although $\boldsymbol{x}_1$ is not a minimizer. The reason is that $\boldsymbol{G}_1$ is not positive definite.

##### Positive definite modification

The Newton equation is

$$
\boldsymbol{G}_k\boldsymbol{d}_k
=
-
\boldsymbol{g}_k
$$

The basic idea of modified Newton methods is to replace $\boldsymbol{G}_k$ by a symmetric positive definite matrix $\boldsymbol{M}_k$.

Solve

$$
\boldsymbol{M}_k\boldsymbol{d}_k
=
-
\boldsymbol{g}_k
$$

Then

$$
\boldsymbol{d}_k
=
-
\boldsymbol{M}_k^{-1}\boldsymbol{g}_k
$$

If

$$
\boldsymbol{M}_k\succ\boldsymbol{0}
$$

and

$$
\boldsymbol{g}_k\ne\boldsymbol{0}
$$

then

$$
\boldsymbol{g}_k^T\boldsymbol{d}_k
=
-
\boldsymbol{g}_k^T\boldsymbol{M}_k^{-1}\boldsymbol{g}_k
<0
$$

Thus $\boldsymbol{d}_k$ is a descent direction.

A simple choice is

$$
\boldsymbol{M}_k
=
\boldsymbol{G}_k+
\varepsilon_k\boldsymbol{I}
$$

where $\varepsilon_k>0$ is chosen so that $\boldsymbol{M}_k$ is positive definite.

If $\mu_i$ is an eigenvalue of $\boldsymbol{G}_k$, then $\mu_i+\varepsilon_k$ is an eigenvalue of $\boldsymbol{M}_k$. Choosing $\varepsilon_k$ sufficiently large makes all eigenvalues positive.

##### Saddle point case

If $\boldsymbol{x}_k$ is a saddle point, then it may happen that

$$
\boldsymbol{g}_k=\boldsymbol{0}
$$

and

$$
\boldsymbol{G}_k
\text{ is indefinite}
$$

Then the equation

$$
\boldsymbol{M}_k\boldsymbol{d}_k=-\boldsymbol{g}_k
$$

cannot give a useful descent direction. In this case, choose a negative curvature direction satisfying

$$
\boldsymbol{d}_k^T\boldsymbol{G}_k\boldsymbol{d}_k<0
$$

Along such a direction, a line search can decrease the objective function.

### Conjugate Gradient Method

##### Conjugate directions

Let $\boldsymbol{A}$ be a symmetric positive definite matrix. Two nonzero directions $\boldsymbol{d}_i$ and $\boldsymbol{d}_j$ are conjugate with respect to $\boldsymbol{A}$ if

$$
\boldsymbol{d}_i^T\boldsymbol{A}\boldsymbol{d}_j=0
$$

A set of directions $\boldsymbol{d}_1,\boldsymbol{d}_2,\ldots,\boldsymbol{d}_k$ is $\boldsymbol{A}$-conjugate if

$$
\boldsymbol{d}_i^T\boldsymbol{A}\boldsymbol{d}_j=0
\qquad
 i\ne j
$$

If $\boldsymbol{A}=\boldsymbol{I}$, conjugacy reduces to ordinary orthogonality.

For the quadratic function

$$
f(\boldsymbol{x})
=
\frac{1}{2}
(\boldsymbol{x}-\boldsymbol{x}^*)^T
\boldsymbol{A}
(\boldsymbol{x}-\boldsymbol{x}^*)
$$

the level sets are ellipsoids centered at $\boldsymbol{x}^*$. At a point $\boldsymbol{x}_1$,

$$
\nabla f(\boldsymbol{x}_1)
=
\boldsymbol{A}(\boldsymbol{x}_1-\boldsymbol{x}^*)
$$

If $\boldsymbol{d}_1$ is tangent to the level set at $\boldsymbol{x}_1$, then

$$
\boldsymbol{d}_1^T\nabla f(\boldsymbol{x}_1)=0
$$

Let

$$
\boldsymbol{d}_2=
\boldsymbol{x}^*-\boldsymbol{x}_1
$$

Then

$$
\boldsymbol{d}_1^T\boldsymbol{A}\boldsymbol{d}_2=0
$$

Thus a tangent direction and the direction from the point to the minimizer are conjugate with respect to $\boldsymbol{A}$.

##### Linear independence

If $\boldsymbol{A}\succ\boldsymbol{0}$ and $\boldsymbol{d}_1,\ldots,\boldsymbol{d}_k$ are nonzero $\boldsymbol{A}$-conjugate directions, then they are linearly independent.

Proof

Assume

$$
\sum_{j=1}^{k}\gamma_j\boldsymbol{d}_j
=
\boldsymbol{0}
$$

Left-multiply by $\boldsymbol{d}_i^T\boldsymbol{A}$

$$
\gamma_i
\boldsymbol{d}_i^T\boldsymbol{A}\boldsymbol{d}_i
=
0
$$

Since $\boldsymbol{A}\succ\boldsymbol{0}$ and $\boldsymbol{d}_i\ne\boldsymbol{0}$,

$$
\boldsymbol{d}_i^T\boldsymbol{A}\boldsymbol{d}_i>0
$$

Therefore

$$
\gamma_i=0
$$

for every $i$.

##### Expanding subspace theorem

Consider

$$
f(\boldsymbol{x})
=
\frac{1}{2}\boldsymbol{x}^T\boldsymbol{A}\boldsymbol{x}
+
\boldsymbol{b}^T\boldsymbol{x}
+
c
$$

where $\boldsymbol{A}\succ\boldsymbol{0}$. Let $\boldsymbol{d}_1,\ldots,\boldsymbol{d}_k$ be nonzero $\boldsymbol{A}$-conjugate directions. Starting from any $\boldsymbol{x}_1$, perform exact line search successively along these directions and obtain $\boldsymbol{x}_{k+1}$.

Let

$$
\mathcal{B}_k
=
\left\{
\boldsymbol{x}
\mid
\boldsymbol{x}=
\sum_{i=1}^{k}\lambda_i\boldsymbol{d}_i
\right\}
$$

Then $\boldsymbol{x}_{k+1}$ is the unique minimizer of $f$ on the affine space

$$
\boldsymbol{x}_1+
\mathcal{B}_k
$$

In particular, if $k=n$, then $\boldsymbol{x}_{n+1}$ is the unique minimizer of $f$ on $\mathbb{R}^n$.

The key proof idea is that exact line search gives

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_j=0
\qquad
j\le k
$$

Thus the gradient at $\boldsymbol{x}_{k+1}$ is orthogonal to the subspace spanned by the searched directions.

##### FR method for strictly convex quadratic functions

The Fletcher-Reeves conjugate gradient method combines steepest descent with conjugate directions.

Consider

$$
f(\boldsymbol{x})
=
\frac{1}{2}\boldsymbol{x}^T\boldsymbol{A}\boldsymbol{x}
+
\boldsymbol{b}^T\boldsymbol{x}
+
c
$$

where $\boldsymbol{A}\succ\boldsymbol{0}$.

The gradient is

$$
\boldsymbol{g}_k
=
\boldsymbol{A}\boldsymbol{x}_k+\boldsymbol{b}
$$

Start with the negative gradient

$$
\boldsymbol{d}_1=-\boldsymbol{g}_1
$$

Given $\boldsymbol{x}_k$ and $\boldsymbol{d}_k$, perform exact line search

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

where

$$
f(\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k)
=
\min_{\alpha}
f(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
$$

For a quadratic function, the exact step length has the explicit form

$$
\alpha_k
=
-
\frac{
\boldsymbol{g}_k^T\boldsymbol{d}_k
}{
\boldsymbol{d}_k^T\boldsymbol{A}\boldsymbol{d}_k
}
$$

After computing $\boldsymbol{g}_{k+1}$, define

$$
\boldsymbol{d}_{k+1}
=
-\boldsymbol{g}_{k+1}
+
\beta_k\boldsymbol{d}_k
$$

Choose $\beta_k$ so that $\boldsymbol{d}_{k+1}$ and $\boldsymbol{d}_k$ are $\boldsymbol{A}$-conjugate

$$
\boldsymbol{d}_k^T\boldsymbol{A}\boldsymbol{d}_{k+1}=0
$$

Substituting the recurrence gives

$$
\boldsymbol{d}_k^T\boldsymbol{A}(-\boldsymbol{g}_{k+1}+\beta_k\boldsymbol{d}_k)=0
$$

Hence

$$
\beta_k
=
\frac{
\boldsymbol{d}_k^T\boldsymbol{A}\boldsymbol{g}_{k+1}
}{
\boldsymbol{d}_k^T\boldsymbol{A}\boldsymbol{d}_k
}
$$

For strictly convex quadratic functions with exact line search, this can be written without matrix multiplication as

$$
\beta_k
=
\frac{
\|\boldsymbol{g}_{k+1}\|^2
}{
\|\boldsymbol{g}_k\|^2
}
$$

##### Orthogonality and conjugacy

For the quadratic FR method with exact line search, the generated directions and gradients satisfy

$$
\boldsymbol{d}_i^T\boldsymbol{A}\boldsymbol{d}_j=0
\qquad
j<i
$$

$$
\boldsymbol{g}_i^T\boldsymbol{g}_j=0
\qquad
j<i
$$

$$
\boldsymbol{g}_i^T\boldsymbol{d}_i
=
-
\boldsymbol{g}_i^T\boldsymbol{g}_i
$$

Thus the FR method terminates in at most $n$ exact line searches for strictly convex quadratic functions.

##### Algorithm for strictly convex quadratic functions

Choose an initial point $\boldsymbol{x}_1$ and set $k=1$.

At iteration $k$, compute

$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

If

$$
\|\boldsymbol{g}_k\|=0
$$

stop.

Construct the direction

$$
\boldsymbol{d}_k
=
-
\boldsymbol{g}_k
+
\beta_{k-1}\boldsymbol{d}_{k-1}
$$

where

$$
\beta_{0}=0
$$

and for $k>1$

$$
\beta_{k-1}
=
\frac{
\|\boldsymbol{g}_{k}\|^2
}{
\|\boldsymbol{g}_{k-1}\|^2
}
$$

Compute

$$
\alpha_k
=
-
\frac{
\boldsymbol{g}_k^T\boldsymbol{d}_k
}{
\boldsymbol{d}_k^T\boldsymbol{A}\boldsymbol{d}_k
}
$$

Update

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

If $k=n$, stop. Otherwise set $k:=k+1$ and repeat.

##### Nonlinear conjugate gradient method

For a general differentiable function, the explicit quadratic step length is no longer valid. The step length must be determined by a one-dimensional search.

The nonlinear FR method uses

$$
\boldsymbol{d}_{j+1}
=
-
\nabla f(\boldsymbol{y}_{j+1})
+
\beta_j\boldsymbol{d}_j
$$

where

$$
\beta_j
=
\frac{
\|\nabla f(\boldsymbol{y}_{j+1})\|^2
}{
\|\nabla f(\boldsymbol{y}_{j})\|^2
}
$$

The iteration is restarted after $n$ steps by taking a steepest descent direction again.

A typical restarted FR procedure is

$$
\boldsymbol{y}_1=\boldsymbol{x}_k
$$

$$
\boldsymbol{d}_1=-\nabla f(\boldsymbol{y}_1)
$$

At inner iteration $j$, choose $\alpha_j$ by line search

$$
f(\boldsymbol{y}_j+
\alpha_j\boldsymbol{d}_j)
=
\min_{\alpha\ge 0}
f(\boldsymbol{y}_j+
\alpha\boldsymbol{d}_j)
$$

Set

$$
\boldsymbol{y}_{j+1}
=
\boldsymbol{y}_j+
\alpha_j\boldsymbol{d}_j
$$

If $j<n$, compute $\beta_j$ and continue. If $j=n$, restart by setting

$$
\boldsymbol{x}_{k+1}=\boldsymbol{y}_{n+1}
$$

##### Other beta formulas

Besides the FR formula, common choices include PRP

$$
\beta_j^{\mathrm{PRP}}
=
\frac{
\boldsymbol{g}_{j+1}^T(\boldsymbol{g}_{j+1}-\boldsymbol{g}_j)
}{
\boldsymbol{g}_j^T\boldsymbol{g}_j
}
$$

Hestenes-Stiefel type formula

$$
\beta_j^{\mathrm{HS}}
=
\frac{
\boldsymbol{g}_{j+1}^T(\boldsymbol{g}_{j+1}-\boldsymbol{g}_j)
}{
\boldsymbol{d}_j^T(\boldsymbol{g}_{j+1}-\boldsymbol{g}_j)
}
$$

and Daniel's formula

$$
\beta_j^{\mathrm{D}}
=
\frac{
\boldsymbol{d}_j^T
\nabla^2 f(\boldsymbol{x}_{j+1})
\boldsymbol{g}_{j+1}
}{
\boldsymbol{d}_j^T
\nabla^2 f(\boldsymbol{x}_{j+1})
\boldsymbol{d}_j
}
$$

For strictly convex quadratic functions with exact line search and initial direction $-\boldsymbol{g}_1$, these formulas are equivalent. For general nonlinear functions, they give different search directions.

##### Descent issue with inexact line search

From

$$
\boldsymbol{d}_{k+1}
=
-
\boldsymbol{g}_{k+1}
+
\beta_k\boldsymbol{d}_k
$$

we obtain

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_{k+1}
=
-
\boldsymbol{g}_{k+1}^T\boldsymbol{g}_{k+1}
+
\beta_k
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_k
$$

With exact line search,

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_k=0
$$

so

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_{k+1}
=
-
\|\boldsymbol{g}_{k+1}\|^2
<0
$$

With inexact line search, $\boldsymbol{g}_{k+1}^T\boldsymbol{d}_k$ may not be zero, and the new direction may fail to be a descent direction. A common remedy is to restart with the steepest descent direction.

### Quasi-Newton Method

##### Quasi-Newton condition

Newton method is fast, but it requires second derivatives and the Hessian may be non-positive definite. Quasi-Newton methods replace the inverse Hessian by a matrix updated only from first-order information.

The Newton-type iteration is

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

with

$$
\boldsymbol{d}_k
=
-
\boldsymbol{H}_k\boldsymbol{g}_k
$$

where $\boldsymbol{H}_k$ approximates $\boldsymbol{G}_k^{-1}$.

After one step, define

$$
\boldsymbol{p}_k
=
\boldsymbol{x}_{k+1}-\boldsymbol{x}_k
$$

$$
\boldsymbol{q}_k
=
\boldsymbol{g}_{k+1}-\boldsymbol{g}_k
$$

Using the Taylor expansion of the gradient near $\boldsymbol{x}_{k+1}$,

$$
\nabla f(\boldsymbol{x}_k)
\approx
\nabla f(\boldsymbol{x}_{k+1})
+
\nabla^2 f(\boldsymbol{x}_{k+1})(\boldsymbol{x}_k-\boldsymbol{x}_{k+1})
$$

so

$$
\boldsymbol{q}_k
\approx
\nabla^2 f(\boldsymbol{x}_{k+1})\boldsymbol{p}_k
$$

If the Hessian is nonsingular, then

$$
\boldsymbol{p}_k
\approx
\nabla^2 f(\boldsymbol{x}_{k+1})^{-1}\boldsymbol{q}_k
$$

Thus the inverse Hessian approximation $\boldsymbol{H}_{k+1}$ is required to satisfy the quasi-Newton condition

$$
\boldsymbol{p}_k
=
\boldsymbol{H}_{k+1}\boldsymbol{q}_k
$$

This condition is also called the secant equation.

##### Rank-one correction

Let

$$
\boldsymbol{H}_{k+1}
=
\boldsymbol{H}_k+
\Delta\boldsymbol{H}_k
$$

A rank-one correction assumes

$$
\Delta\boldsymbol{H}_k
=
\eta_k
\boldsymbol{z}_k\boldsymbol{z}_k^T
$$

Imposing the secant equation gives

$$
\boldsymbol{p}_k
=
\boldsymbol{H}_k\boldsymbol{q}_k
+
\eta_k
\boldsymbol{z}_k\boldsymbol{z}_k^T\boldsymbol{q}_k
$$

After elimination, the rank-one update is

$$
\boldsymbol{H}_{k+1}
=
\boldsymbol{H}_k
+
\frac{
(\boldsymbol{p}_k-\boldsymbol{H}_k\boldsymbol{q}_k)
(\boldsymbol{p}_k-\boldsymbol{H}_k\boldsymbol{q}_k)^T
}{
\boldsymbol{q}_k^T(\boldsymbol{p}_k-\boldsymbol{H}_k\boldsymbol{q}_k)
}
$$

This update satisfies the secant equation, but positive definiteness is not always guaranteed.

##### DFP formula

The DFP method uses a symmetric rank-two correction

$$
\boldsymbol{H}_{k+1}
=
\boldsymbol{H}_k
+
\frac{
\boldsymbol{p}_k\boldsymbol{p}_k^T
}{
\boldsymbol{p}_k^T\boldsymbol{q}_k
}
-
\frac{
\boldsymbol{H}_k\boldsymbol{q}_k\boldsymbol{q}_k^T\boldsymbol{H}_k
}{
\boldsymbol{q}_k^T\boldsymbol{H}_k\boldsymbol{q}_k
}
$$

This formula satisfies

$$
\boldsymbol{p}_k
=
\boldsymbol{H}_{k+1}\boldsymbol{q}_k
$$

##### DFP algorithm

Choose $\boldsymbol{x}_1$, a tolerance $\varepsilon>0$, and

$$
\boldsymbol{H}_1=\boldsymbol{I}
$$

At iteration $k$, compute

$$
\boldsymbol{g}_k=\nabla f(\boldsymbol{x}_k)
$$

Set

$$
\boldsymbol{d}_k=-\boldsymbol{H}_k\boldsymbol{g}_k
$$

Choose $\alpha_k$ by line search

$$
f(\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k)
=
\min_{\alpha\ge 0}
f(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
$$

Update

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

If

$$
\|\nabla f(\boldsymbol{x}_{k+1})\|\le \varepsilon
$$

stop.

Otherwise define

$$
\boldsymbol{p}_k=\boldsymbol{x}_{k+1}-\boldsymbol{x}_k
$$

$$
\boldsymbol{q}_k=\boldsymbol{g}_{k+1}-\boldsymbol{g}_k
$$

and update $\boldsymbol{H}_{k+1}$ by the DFP formula.

##### Positive definiteness of DFP

If $\boldsymbol{H}_k\succ\boldsymbol{0}$ and $\boldsymbol{p}_k^T\boldsymbol{q}_k>0$, then the DFP update preserves positive definiteness.

With exact line search and $\boldsymbol{d}_k=-\boldsymbol{H}_k\boldsymbol{g}_k$,

$$
\boldsymbol{p}_k^T\boldsymbol{q}_k
=
\alpha_k\boldsymbol{d}_k^T(\boldsymbol{g}_{k+1}-\boldsymbol{g}_k)
$$

Since exact line search gives

$$
\boldsymbol{g}_{k+1}^T\boldsymbol{d}_k=0
$$

we have

$$
\boldsymbol{p}_k^T\boldsymbol{q}_k
=
-
\alpha_k\boldsymbol{d}_k^T\boldsymbol{g}_k
$$

Using $\boldsymbol{d}_k=-\boldsymbol{H}_k\boldsymbol{g}_k$,

$$
\boldsymbol{p}_k^T\boldsymbol{q}_k
=
\alpha_k
\boldsymbol{g}_k^T\boldsymbol{H}_k\boldsymbol{g}_k
>0
$$

Thus the DFP direction is a descent direction when $\boldsymbol{H}_k$ is positive definite.

##### Quadratic termination of DFP

For the strictly convex quadratic function

$$
f(\boldsymbol{x})
=
\frac{1}{2}\boldsymbol{x}^T\boldsymbol{A}\boldsymbol{x}
+
\boldsymbol{b}^T\boldsymbol{x}
+
c
$$

where $\boldsymbol{A}\succ\boldsymbol{0}$, the DFP method produces step vectors

$$
\boldsymbol{p}_i
=
\boldsymbol{x}_{i+1}-\boldsymbol{x}_i
=
\alpha_i\boldsymbol{d}_i
$$

that satisfy

$$
\boldsymbol{p}_i^T\boldsymbol{A}\boldsymbol{p}_j=0
\qquad
1\le i<j\le k
$$

and

$$
\boldsymbol{H}_{k+1}\boldsymbol{A}\boldsymbol{p}_i
=
\boldsymbol{p}_i
\qquad
1\le i\le k
$$

When $k=n$, let

$$
\boldsymbol{D}
=
\begin{bmatrix}
\boldsymbol{p}_1 & \boldsymbol{p}_2 & \cdots & \boldsymbol{p}_n
\end{bmatrix}
$$

Then

$$
\boldsymbol{H}_{n+1}\boldsymbol{A}\boldsymbol{D}
=
\boldsymbol{D}
$$

Since the conjugate nonzero vectors $\boldsymbol{p}_1,\ldots,\boldsymbol{p}_n$ are linearly independent, $\boldsymbol{D}$ is nonsingular. Therefore

$$
\boldsymbol{H}_{n+1}\boldsymbol{A}=\boldsymbol{I}
$$

and

$$
\boldsymbol{H}_{n+1}=\boldsymbol{A}^{-1}
$$

Hence DFP has quadratic termination.

##### BFGS formulas

Instead of approximating the inverse Hessian, one may approximate the Hessian itself by $\boldsymbol{B}_{k+1}$ and impose

$$
\boldsymbol{q}_k
=
\boldsymbol{B}_{k+1}\boldsymbol{p}_k
$$

The BFGS update for $\boldsymbol{B}_k$ is

$$
\boldsymbol{B}_{k+1}
=
\boldsymbol{B}_k
+
\frac{
\boldsymbol{q}_k\boldsymbol{q}_k^T
}{
\boldsymbol{q}_k^T\boldsymbol{p}_k
}
-
\frac{
\boldsymbol{B}_k\boldsymbol{p}_k\boldsymbol{p}_k^T\boldsymbol{B}_k
}{
\boldsymbol{p}_k^T\boldsymbol{B}_k\boldsymbol{p}_k
}
$$

If $\boldsymbol{B}_{k+1}$ is nonsingular, then

$$
\boldsymbol{H}_{k+1}=\boldsymbol{B}_{k+1}^{-1}
$$

The inverse BFGS update is

$$
\boldsymbol{H}_{k+1}^{\mathrm{BFGS}}
=
\boldsymbol{H}_k
+
\left(
1+
\frac{
\boldsymbol{q}_k^T\boldsymbol{H}_k\boldsymbol{q}_k
}{
\boldsymbol{p}_k^T\boldsymbol{q}_k
}
\right)
\frac{
\boldsymbol{p}_k\boldsymbol{p}_k^T
}{
\boldsymbol{p}_k^T\boldsymbol{q}_k
}
-
\frac{
\boldsymbol{p}_k\boldsymbol{q}_k^T\boldsymbol{H}_k
+
\boldsymbol{H}_k\boldsymbol{q}_k\boldsymbol{p}_k^T
}{
\boldsymbol{p}_k^T\boldsymbol{q}_k
}
$$

##### Broyden family

The DFP and BFGS inverse updates are symmetric rank-two corrections. Their weighted combination gives the Broyden family

$$
\boldsymbol{H}_{k+1}^{\theta}
=
(1-\theta)
\boldsymbol{H}_{k+1}^{\mathrm{DFP}}
+
\theta
\boldsymbol{H}_{k+1}^{\mathrm{BFGS}}
$$

where $\theta$ is a real parameter. When

$$
\theta=0
$$

we obtain DFP. When

$$
\theta=1
$$

we obtain BFGS.

For positive definiteness, $\theta$ is usually taken nonnegative. The Broyden family also satisfies the quasi-Newton condition.

### Trust Region Method

##### Basic idea

Line-search methods first choose a direction and then search along that direction. Trust region methods instead choose a neighborhood around the current point and minimize a local quadratic model inside that neighborhood.

Consider

$$
\min_{\boldsymbol{x}\in\mathbb{R}^n} f(\boldsymbol{x})
$$

At $\boldsymbol{x}_k$, define the quadratic model

$$
\phi_k(\boldsymbol{d})
=
f(\boldsymbol{x}_k)
+
\boldsymbol{g}_k^T\boldsymbol{d}
+
\frac{1}{2}
\boldsymbol{d}^T\boldsymbol{G}_k\boldsymbol{d}
$$

The trust region radius is $r_k>0$. The step is obtained from the subproblem

$$
\min_{\boldsymbol{d}}
\phi_k(\boldsymbol{d})
$$

subject to

$$
\|\boldsymbol{d}\|\le r_k
$$

Equivalently,

$$
\min_{\|\boldsymbol{d}\|\le r_k}
\left[
 f(\boldsymbol{x}_k)
+
\boldsymbol{g}_k^T\boldsymbol{d}
+
\frac{1}{2}
\boldsymbol{d}^T\boldsymbol{G}_k\boldsymbol{d}
\right]
$$

##### Optimality conditions for the subproblem

If $\boldsymbol{d}_k$ solves the trust region subproblem, then there exists $w\ge 0$ such that

$$
(\boldsymbol{G}_k+w\boldsymbol{I})\boldsymbol{d}_k
=
-
\boldsymbol{g}_k
$$

$$
w(\|\boldsymbol{d}_k\|-r_k)=0
$$

$$
w\ge 0
$$

$$
\|\boldsymbol{d}_k\|\le r_k
$$

If $\boldsymbol{G}_k+w\boldsymbol{I}$ is nonsingular, then

$$
\boldsymbol{d}_k
=
-
(\boldsymbol{G}_k+w\boldsymbol{I})^{-1}\boldsymbol{g}_k
$$

Therefore

$$
\|\boldsymbol{d}_k\|
=
\left\|
(\boldsymbol{G}_k+w\boldsymbol{I})^{-1}\boldsymbol{g}_k
\right\|
$$

If $r_k$ is sufficiently large, $w$ can be small and the step is close to the Newton direction

$$
\boldsymbol{d}_k
\approx
-
\boldsymbol{G}_k^{-1}\boldsymbol{g}_k
$$

If $r_k\to 0$, then $w\to +\infty$ and

$$
\boldsymbol{d}_k
\approx
-
\frac{1}{w}\boldsymbol{g}_k
$$

Thus the trust region step changes continuously between the steepest descent direction and the Newton direction as the radius changes.

##### Actual reduction and predicted reduction

After solving the subproblem, compare the actual decrease and the predicted decrease

$$
\rho_k
=
\frac{
f(\boldsymbol{x}_k)-f(\boldsymbol{x}_k+\boldsymbol{d}_k)
}{
f(\boldsymbol{x}_k)-\phi_k(\boldsymbol{d}_k)
}
$$

If $\rho_k$ is too small, the quadratic model is not trusted, and the step is rejected. If $\rho_k$ is large, the model is considered successful, and the step is accepted.

##### Algorithm

Choose $\boldsymbol{x}_1$, an initial trust region radius $r_1>0$, parameters

$$
0<\mu<\eta<1
$$

and tolerance $\varepsilon>0$. Common choices are

$$
\mu=\frac{1}{4}
$$

$$
\eta=\frac{3}{4}
$$

At iteration $k$, compute $f(\boldsymbol{x}_k)$, $\boldsymbol{g}_k$, and $\boldsymbol{G}_k$.

If

$$
\|\boldsymbol{g}_k\|\le\varepsilon
$$

stop.

Solve

$$
\min_{\|\boldsymbol{d}\|\le r_k}
\phi_k(\boldsymbol{d})
$$

and obtain $\boldsymbol{d}_k$.

Compute

$$
\rho_k
=
\frac{
f(\boldsymbol{x}_k)-f(\boldsymbol{x}_k+\boldsymbol{d}_k)
}{
f(\boldsymbol{x}_k)-\phi_k(\boldsymbol{d}_k)
}
$$

Accept or reject the step by

$$
\boldsymbol{x}_{k+1}
=
\begin{cases}
\boldsymbol{x}_k & \rho_k\le\mu\\
\boldsymbol{x}_k+\boldsymbol{d}_k & \rho_k>\mu
\end{cases}
$$

Update the radius by

$$
r_{k+1}
=
\begin{cases}
\frac{1}{2}r_k & \rho_k\le\mu\\
r_k & \mu<\rho_k<\eta\\
2r_k & \rho_k\ge\eta
\end{cases}
$$

Set $k:=k+1$ and repeat.

##### Convergence result

Assume that the level set

$$
S=
\{\boldsymbol{x}\mid f(\boldsymbol{x})\le f(\boldsymbol{x}_1)\}
$$

is bounded and closed, and that $f$, $\nabla f$, and $\nabla^2 f$ are continuous on $S$. Then the trust region method produces a sequence satisfying

$$
\lim_{k\to\infty}
\|\nabla f(\boldsymbol{x}_k)\|=0
$$

### Least Squares Method

##### Problem form

Some optimization problems have an objective function that is a sum of squares

$$
F(\boldsymbol{x})
=
\sum_{i=1}^{m}
f_i(\boldsymbol{x})^2
$$

where

$$
\boldsymbol{x}\in\mathbb{R}^n
$$

and usually

$$
m\ge n
$$

The problem

$$
\min F(\boldsymbol{x})
=
\min
\sum_{i=1}^{m}
f_i(\boldsymbol{x})^2
$$

is called a least squares problem.

If every $f_i(\boldsymbol{x})$ is linear, it is a linear least squares problem. If some $f_i(\boldsymbol{x})$ is nonlinear, it is a nonlinear least squares problem.

##### Linear least squares

Assume

$$
f_i(\boldsymbol{x})
=
\boldsymbol{p}_i^T\boldsymbol{x}-b_i
\qquad
 i=1,2,\ldots,m
$$

Let

$$
\boldsymbol{A}
=
\begin{bmatrix}
\boldsymbol{p}_1^T\\
\boldsymbol{p}_2^T\\
\vdots\\
\boldsymbol{p}_m^T
\end{bmatrix}
$$

and

$$
\boldsymbol{b}
=
\begin{bmatrix}
b_1\\
b_2\\
\vdots\\
b_m
\end{bmatrix}
$$

Then

$$
F(\boldsymbol{x})
=
(\boldsymbol{A}\boldsymbol{x}-\boldsymbol{b})^T
(\boldsymbol{A}\boldsymbol{x}-\boldsymbol{b})
$$

Expanding gives

$$
F(\boldsymbol{x})
=
\boldsymbol{x}^T\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x}
-
2\boldsymbol{b}^T\boldsymbol{A}\boldsymbol{x}
+
\boldsymbol{b}^T\boldsymbol{b}
$$

The stationary condition is

$$
\nabla F(\boldsymbol{x})
=
2\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x}
-
2\boldsymbol{A}^T\boldsymbol{b}
=
\boldsymbol{0}
$$

Thus the normal equation is

$$
\boldsymbol{A}^T\boldsymbol{A}\boldsymbol{x}
=
\boldsymbol{A}^T\boldsymbol{b}
$$

If $\boldsymbol{A}$ has full column rank, then $\boldsymbol{A}^T\boldsymbol{A}$ is symmetric positive definite and

$$
\boldsymbol{x}^*
=
(\boldsymbol{A}^T\boldsymbol{A})^{-1}
\boldsymbol{A}^T\boldsymbol{b}
$$

Because $F$ is convex, this stationary point is the global minimizer.

##### Nonlinear least squares

For nonlinear least squares, use a sequence of linear least squares approximations.

At $\boldsymbol{x}_k$, linearize each $f_i$ by the first-order Taylor polynomial

$$
\varphi_i(\boldsymbol{x})
=
f_i(\boldsymbol{x}_k)
+
\nabla f_i(\boldsymbol{x}_k)^T
(\boldsymbol{x}-\boldsymbol{x}_k)
$$

Equivalently,

$$
\varphi_i(\boldsymbol{x})
=
\nabla f_i(\boldsymbol{x}_k)^T\boldsymbol{x}
-
\left[
\nabla f_i(\boldsymbol{x}_k)^T\boldsymbol{x}_k
-
f_i(\boldsymbol{x}_k)
\right]
$$

Define

$$
\Phi(\boldsymbol{x})
=
\sum_{i=1}^{m}
\varphi_i(\boldsymbol{x})^2
$$

Let

$$
\boldsymbol{A}_k
=
\begin{bmatrix}
\nabla f_1(\boldsymbol{x}_k)^T\\
\nabla f_2(\boldsymbol{x}_k)^T\\
\vdots\\
\nabla f_m(\boldsymbol{x}_k)^T
\end{bmatrix}
$$

and

$$
\boldsymbol{f}_k
=
\begin{bmatrix}
f_1(\boldsymbol{x}_k)\\
f_2(\boldsymbol{x}_k)\\
\vdots\\
f_m(\boldsymbol{x}_k)
\end{bmatrix}
$$

Then

$$
\Phi(\boldsymbol{x})
=
(\boldsymbol{A}_k\boldsymbol{x}-\boldsymbol{b}_k)^T
(\boldsymbol{A}_k\boldsymbol{x}-\boldsymbol{b}_k)
$$

where

$$
\boldsymbol{b}_k
=
\boldsymbol{A}_k\boldsymbol{x}_k-
\boldsymbol{f}_k
$$

The normal equation for minimizing $\Phi$ is

$$
\boldsymbol{A}_k^T\boldsymbol{A}_k\boldsymbol{x}
=
\boldsymbol{A}_k^T
(\boldsymbol{A}_k\boldsymbol{x}_k-
\boldsymbol{f}_k)
$$

Move the term $\boldsymbol{A}_k^T\boldsymbol{A}_k\boldsymbol{x}_k$ to the left

$$
\boldsymbol{A}_k^T\boldsymbol{A}_k
(\boldsymbol{x}-\boldsymbol{x}_k)
=
-
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

If $\boldsymbol{A}_k$ has full column rank, then

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k
-
(\boldsymbol{A}_k^T\boldsymbol{A}_k)^{-1}
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

##### Relation to Newton method

From

$$
F(\boldsymbol{x})
=
\sum_{i=1}^{m}f_i(\boldsymbol{x})^2
$$

we have

$$
\nabla F(\boldsymbol{x}_k)
=
2\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

The Hessian of the approximation $\Phi$ is

$$
\boldsymbol{H}_k
=
2\boldsymbol{A}_k^T\boldsymbol{A}_k
$$

Thus

$$
\boldsymbol{H}_k(\boldsymbol{x}-\boldsymbol{x}_k)
=
-
\nabla F(\boldsymbol{x}_k)
$$

and

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k
-
\boldsymbol{H}_k^{-1}
\nabla F(\boldsymbol{x}_k)
$$

This has the same form as Newton's method, but $\boldsymbol{H}_k$ is the Hessian of the linearized least squares approximation, not the exact Hessian of $F$.

The Gauss-Newton direction is

$$
\boldsymbol{d}_k
=
-
(\boldsymbol{A}_k^T\boldsymbol{A}_k)^{-1}
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

To ensure decrease, use line search after computing this direction

$$
\min_{\alpha}
F(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
$$

Then update

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

##### Gauss-Newton algorithm

Choose an initial point $\boldsymbol{x}_1$ and tolerance $\varepsilon>0$. Set $k=1$.

At iteration $k$, compute

$$
\boldsymbol{f}_k
=
\begin{bmatrix}
f_1(\boldsymbol{x}_k)\\
f_2(\boldsymbol{x}_k)\\
\vdots\\
f_m(\boldsymbol{x}_k)
\end{bmatrix}
$$

and

$$
\boldsymbol{A}_k
=
\begin{bmatrix}
\nabla f_1(\boldsymbol{x}_k)^T\\
\nabla f_2(\boldsymbol{x}_k)^T\\
\vdots\\
\nabla f_m(\boldsymbol{x}_k)^T
\end{bmatrix}
$$

Solve

$$
\boldsymbol{A}_k^T\boldsymbol{A}_k\boldsymbol{d}
=
-
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

and obtain $\boldsymbol{d}_k$.

Choose $\alpha_k$ by line search

$$
F(\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k)
=
\min_{\alpha}
F(\boldsymbol{x}_k+
\alpha\boldsymbol{d}_k)
$$

Set

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\alpha_k\boldsymbol{d}_k
$$

If

$$
\|\boldsymbol{x}_{k+1}-\boldsymbol{x}_k\|\le\varepsilon
$$

stop. Otherwise set $k:=k+1$ and repeat.

##### Marquardt method

The matrix $\boldsymbol{A}_k^T\boldsymbol{A}_k$ may be singular or nearly singular. A common modification is to add a positive diagonal term.

The Marquardt direction is

$$
\boldsymbol{d}_k
=
-
(\boldsymbol{A}_k^T\boldsymbol{A}_k+
\alpha_k\boldsymbol{I})^{-1}
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

where

$$
\alpha_k>0
$$

If

$$
\alpha_k=0
$$

then $\boldsymbol{d}_k$ is the Gauss-Newton direction.

If $\alpha_k$ is sufficiently large, then

$$
(\boldsymbol{A}_k^T\boldsymbol{A}_k+
\alpha_k\boldsymbol{I})^{-1}
\approx
\frac{1}{\alpha_k}\boldsymbol{I}
$$

and

$$
\boldsymbol{d}_k
\approx
-
\frac{1}{\alpha_k}
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

Since

$$
\nabla F(\boldsymbol{x}_k)
=
2\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

this direction is close to the steepest descent direction. Therefore the Marquardt direction lies between the Gauss-Newton direction and the steepest descent direction.

##### Marquardt algorithm

Choose $\boldsymbol{x}_1$, an initial parameter $\alpha_1>0$, a factor $\beta>1$, and tolerance $\varepsilon>0$. Set $\alpha=\alpha_1$ and $k=1$.

At iteration $k$, first reduce the parameter

$$
\alpha:=\frac{\alpha}{\beta}
$$

Compute $\boldsymbol{f}_k$ and $\boldsymbol{A}_k$. Solve

$$
(\boldsymbol{A}_k^T\boldsymbol{A}_k+
\alpha\boldsymbol{I})\boldsymbol{d}
=
-
\boldsymbol{A}_k^T\boldsymbol{f}_k
$$

Set

$$
\boldsymbol{x}_{k+1}
=
\boldsymbol{x}_k+
\boldsymbol{d}_k
$$

If

$$
F(\boldsymbol{x}_{k+1})<F(\boldsymbol{x}_k)
$$

accept the step. Otherwise, if

$$
\|\boldsymbol{A}_k^T\boldsymbol{f}_k\|\le\varepsilon
$$

stop. If not, increase the parameter

$$
\alpha:=\beta\alpha
$$

and recompute the direction.

Typical empirical values are

$$
\alpha_1=0.01
$$

$$
\beta=10
$$

### Method Comparison

| Method | Main direction | Derivatives used | Step length or region | Main feature |
|---|---|---|---|---|
| Newton method | $-\boldsymbol{G}_k^{-1}\boldsymbol{g}_k$ | first and second derivatives | full step | fast local convergence, but may fail globally |
| Damped Newton | $-\boldsymbol{G}_k^{-1}\boldsymbol{g}_k$ | first and second derivatives | one-dimensional search | improves global behavior |
| Modified Newton | $-\boldsymbol{M}_k^{-1}\boldsymbol{g}_k$ | first and modified second derivatives | one-dimensional search | handles non-positive definite Hessians |
| Conjugate gradient | conjugate directions | first derivative and quadratic structure | exact or inexact line search | finite termination for strictly convex quadratics |
| Quasi-Newton | $-\boldsymbol{H}_k\boldsymbol{g}_k$ | first derivative | one-dimensional search | approximates inverse Hessian |
| Trust region | solution of local quadratic subproblem | first and second derivatives | trust region radius | balances Newton and steepest descent behavior |
| Gauss-Newton | $-(\boldsymbol{A}_k^T\boldsymbol{A}_k)^{-1}\boldsymbol{A}_k^T\boldsymbol{f}_k$ | residual Jacobian | line search optional | exploits least squares structure |
| Marquardt | $-(\boldsymbol{A}_k^T\boldsymbol{A}_k+\alpha_k\boldsymbol{I})^{-1}\boldsymbol{A}_k^T\boldsymbol{f}_k$ | residual Jacobian | adaptive damping | stabilizes Gauss-Newton |
