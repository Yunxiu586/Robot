# Orthogonality

[toc]

### Orthogonal Vectors

##### Dot product test

Vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ are orthogonal when their dot product is zero

$$
\boldsymbol{x}^{T}\boldsymbol{y}=0
$$

The zero vector is orthogonal to every vector

$$
\boldsymbol{0}^{T}\boldsymbol{x}=0
$$

##### Length and angle

The dot product gives the angle by

$$
\boldsymbol{x}^{T}\boldsymbol{y}
=
\lVert \boldsymbol{x}\rVert \lVert \boldsymbol{y}\rVert\cos\theta
$$

Orthogonality means $\theta=90^{\circ}$ for nonzero vectors

### Orthogonal Subspaces

##### Definition

Two subspaces are orthogonal when every vector in one subspace is orthogonal to every vector in the other subspace

$$
\boldsymbol{x}^{T}\boldsymbol{y}=0
$$

for all $\boldsymbol{x}\in S$ and $\boldsymbol{y}\in T$

##### Fundamental orthogonal pairs

The row space is orthogonal to the nullspace

$$
C(\mathbf{A}^{T})\perp N(\mathbf{A})
$$

The column space is orthogonal to the left nullspace

$$
C(\mathbf{A})\perp N(\mathbf{A}^{T})
$$

##### Orthogonal complements

For an $m\times n$ matrix $\mathbf{A}$

$$
N(\mathbf{A})=C(\mathbf{A}^{T})^{\perp}
$$

$$
N(\mathbf{A}^{T})=C(\mathbf{A})^{\perp}
$$

The dimensions add to the whole space

$$
\dim C(\mathbf{A}^{T})+\dim N(\mathbf{A})=n
$$

$$
\dim C(\mathbf{A})+\dim N(\mathbf{A}^{T})=m
$$

### Projection onto a Line

##### Projection vector

Project $\boldsymbol{b}$ onto the line through $\boldsymbol{a}$

$$
\boldsymbol{p}=\hat{x}\boldsymbol{a}
$$

The error $\boldsymbol{e}=\boldsymbol{b}-\boldsymbol{p}$ is orthogonal to $\boldsymbol{a}$

$$
\boldsymbol{a}^{T}(\boldsymbol{b}-\hat{x}\boldsymbol{a})=0
$$

Solving for $\hat{x}$ gives

$$
\hat{x}
=
\frac{\boldsymbol{a}^{T}\boldsymbol{b}}{\boldsymbol{a}^{T}\boldsymbol{a}}
$$

Therefore

$$
\boldsymbol{p}
=
\boldsymbol{a}\frac{\boldsymbol{a}^{T}\boldsymbol{b}}{\boldsymbol{a}^{T}\boldsymbol{a}}
$$

##### Projection matrix

Projection onto the line through $\boldsymbol{a}$ is

$$
\boldsymbol{p}=\mathbf{P}\boldsymbol{b}
$$

where

$$
\mathbf{P}
=
\frac{\boldsymbol{a}\boldsymbol{a}^{T}}{\boldsymbol{a}^{T}\boldsymbol{a}}
$$

A projection matrix satisfies

$$
\mathbf{P}^{2}=\mathbf{P}
$$

For an orthogonal projection

$$
\mathbf{P}^{T}=\mathbf{P}
$$

### Projection onto a Subspace

##### Closest vector

Let the columns of $\mathbf{A}$ span the subspace

The projection of $\boldsymbol{b}$ onto $C(\mathbf{A})$ has the form

$$
\boldsymbol{p}=\mathbf{A}\hat{\boldsymbol{x}}
$$

The error is orthogonal to the whole column space

$$
\mathbf{A}^{T}(\boldsymbol{b}-\mathbf{A}\hat{\boldsymbol{x}})=\boldsymbol{0}
$$

##### Normal equations

The least squares solution satisfies

$$
\mathbf{A}^{T}\mathbf{A}\hat{\boldsymbol{x}}
=
\mathbf{A}^{T}\boldsymbol{b}
$$

If the columns of $\mathbf{A}$ are independent, then $\mathbf{A}^{T}\mathbf{A}$ is invertible

$$
\hat{\boldsymbol{x}}
=
(\mathbf{A}^{T}\mathbf{A})^{-1}\mathbf{A}^{T}\boldsymbol{b}
$$

##### Projection matrix onto a column space

The projection matrix onto $C(\mathbf{A})$ is

$$
\mathbf{P}
=
\mathbf{A}(\mathbf{A}^{T}\mathbf{A})^{-1}\mathbf{A}^{T}
$$

Then

$$
\boldsymbol{p}=\mathbf{P}\boldsymbol{b}
$$

and

$$
\boldsymbol{e}=\boldsymbol{b}-\boldsymbol{p}
$$

The residual is in the left nullspace

$$
\boldsymbol{e}\in N(\mathbf{A}^{T})
$$

### Least Squares

##### Overdetermined systems

When $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ has no exact solution, least squares chooses $\hat{\boldsymbol{x}}$ to minimize the residual

$$
\lVert\mathbf{A}\boldsymbol{x}-\boldsymbol{b}\rVert^{2}
$$

The best approximation is the projection of $\boldsymbol{b}$ onto the column space of $\mathbf{A}$

$$
\boldsymbol{p}=\mathbf{A}\hat{\boldsymbol{x}}
$$

##### Error equation

At the minimum, the residual is orthogonal to every column of $\mathbf{A}$

$$
\mathbf{A}^{T}(\mathbf{A}\hat{\boldsymbol{x}}-\boldsymbol{b})=\boldsymbol{0}
$$

Equivalently

$$
\mathbf{A}^{T}\mathbf{A}\hat{\boldsymbol{x}}
=
\mathbf{A}^{T}\boldsymbol{b}
$$

### Orthonormal Vectors

##### Orthonormal columns

Vectors $\boldsymbol{q}_1,\ldots,\boldsymbol{q}_n$ are orthonormal when

$$
\boldsymbol{q}_i^{T}\boldsymbol{q}_j
=
\begin{cases}
0&i\ne j\\
1&i=j
\end{cases}
$$

If the columns of $\mathbf{Q}$ are orthonormal, then

$$
\mathbf{Q}^{T}\mathbf{Q}=\mathbf{I}
$$

##### Easy least squares

If $\mathbf{Q}$ has orthonormal columns, then the least squares solution is

$$
\hat{\boldsymbol{x}}=\mathbf{Q}^{T}\boldsymbol{b}
$$

and the projection is

$$
\boldsymbol{p}=\mathbf{Q}\mathbf{Q}^{T}\boldsymbol{b}
$$

The projection matrix is

$$
\mathbf{P}=\mathbf{Q}\mathbf{Q}^{T}
$$

##### Square orthogonal matrix

If $\mathbf{Q}$ is square and has orthonormal columns, then

$$
\mathbf{Q}^{T}\mathbf{Q}=\mathbf{I}
$$

$$
\mathbf{Q}\mathbf{Q}^{T}=\mathbf{I}
$$

Thus

$$
\mathbf{Q}^{-1}=\mathbf{Q}^{T}
$$

### Gram-Schmidt

##### Goal

Gram-Schmidt turns independent vectors $\boldsymbol{a}_1,\ldots,\boldsymbol{a}_n$ into orthonormal vectors $\boldsymbol{q}_1,\ldots,\boldsymbol{q}_n$ with the same span

$$
\operatorname{span}\{\boldsymbol{a}_1,\ldots,\boldsymbol{a}_k\}
=
\operatorname{span}\{\boldsymbol{q}_1,\ldots,\boldsymbol{q}_k\}
$$

##### First vector

Normalize the first vector

$$
\boldsymbol{q}_1
=
\frac{\boldsymbol{a}_1}{\lVert\boldsymbol{a}_1\rVert}
$$

##### Orthogonalization step

Subtract from $\boldsymbol{a}_k$ its projections onto the previous $\boldsymbol{q}$ vectors

$$
\boldsymbol{u}_k
=
\boldsymbol{a}_k
-
(\boldsymbol{q}_1^{T}\boldsymbol{a}_k)\boldsymbol{q}_1
-
\cdots
-
(\boldsymbol{q}_{k-1}^{T}\boldsymbol{a}_k)\boldsymbol{q}_{k-1}
$$

Then normalize

$$
\boldsymbol{q}_k
=
\frac{\boldsymbol{u}_k}{\lVert\boldsymbol{u}_k\rVert}
$$

##### Coefficients

The Gram-Schmidt coefficients are

$$
r_{ij}=\boldsymbol{q}_i^{T}\boldsymbol{a}_j
\qquad
 i<j
$$

and

$$
r_{jj}=\lVert\boldsymbol{u}_j\rVert
$$

### QR Factorization

##### Factorization

Gram-Schmidt gives

$$
\mathbf{A}=\mathbf{Q}\mathbf{R}
$$

where $\mathbf{Q}$ has orthonormal columns and $\mathbf{R}$ is upper triangular

$$
\mathbf{Q}^{T}\mathbf{Q}=\mathbf{I}
$$

##### Entries of R

The entries of $\mathbf{R}$ satisfy

$$
r_{ij}=\boldsymbol{q}_i^{T}\boldsymbol{a}_j
\qquad
 i\le j
$$

and

$$
r_{ij}=0
\qquad
 i>j
$$

##### Least squares by QR

If $\mathbf{A}=\mathbf{Q}\mathbf{R}$, the least squares problem becomes

$$
\mathbf{R}\hat{\boldsymbol{x}}
=
\mathbf{Q}^{T}\boldsymbol{b}
$$

This avoids forming $\mathbf{A}^{T}\mathbf{A}$ directly
