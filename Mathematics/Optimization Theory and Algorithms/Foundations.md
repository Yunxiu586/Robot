# Foundations

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

### Hessian Matrix

##### Definition

For a twice continuously differentiable function

$$
f:
\mathbb{R}^n\to\mathbb{R}
$$

the Hessian matrix at $\boldsymbol{x}$ is

$$
\nabla^2 f(\boldsymbol{x})
=
\begin{bmatrix}
\dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1\partial x_n} \\
\dfrac{\partial^2 f}{\partial x_2\partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial^2 f}{\partial x_n\partial x_1} & \dfrac{\partial^2 f}{\partial x_n\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

Each entry is

$$
[\nabla^2 f(\boldsymbol{x})]_{ij}
=
\frac{\partial^2 f(\boldsymbol{x})}{\partial x_i\partial x_j}
$$

Using the notation

$$
\boldsymbol{G}
=
\nabla^2 f(\boldsymbol{x})
$$

or at iteration $k$

$$
\boldsymbol{G}_k
=
\nabla^2 f(\boldsymbol{x}_k)
$$

##### Symmetry

If $f\in C^2$, then the mixed partial derivatives are equal

$$
\frac{\partial^2 f}{\partial x_i\partial x_j}
=
\frac{\partial^2 f}{\partial x_j\partial x_i}
$$

Hence

$$
\nabla^2 f(\boldsymbol{x})^T
=
\nabla^2 f(\boldsymbol{x})
$$

Thus the Hessian matrix is symmetric.

##### Quadratic form

For any direction $\boldsymbol{d}\in\mathbb{R}^n$, the Hessian defines the quadratic form

$$
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x})
\boldsymbol{d}
$$

Let

$$
\phi(t)=f(\boldsymbol{x}+t\boldsymbol{d})
$$

Then

$$
\phi''(0)
=
\boldsymbol{d}^T
\nabla^2 f(\boldsymbol{x})
\boldsymbol{d}
$$

Therefore the quadratic form gives the second-order change of $f$ along direction $\boldsymbol{d}$.

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
