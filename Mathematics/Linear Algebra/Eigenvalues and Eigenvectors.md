# Eigenvalues and Eigenvectors

[toc]

### Introduction to Eigenvalues

##### Eigenvalue equation

A nonzero vector $\boldsymbol{x}$ is an eigenvector of $\mathbf{A}$ if multiplication by $\mathbf{A}$ only changes it by a scalar factor

$$
\mathbf{A}\boldsymbol{x}
=
\lambda\boldsymbol{x}
$$

The scalar $\lambda$ is the eigenvalue

Equivalently

$$
(\mathbf{A}-\lambda\mathbf{I})\boldsymbol{x}
=
\boldsymbol{0}
$$

The zero vector is not an eigenvector

##### Characteristic equation

Nonzero solutions exist when $\mathbf{A}-\lambda\mathbf{I}$ is singular

$$
\det(\mathbf{A}-\lambda\mathbf{I})=0
$$

The roots are the eigenvalues of $\mathbf{A}$

The polynomial

$$
p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I})
$$

is the characteristic polynomial

##### Eigenvectors

For each eigenvalue, the eigenvectors are the nonzero vectors in the nullspace

$$
\boldsymbol{x}\in N(\mathbf{A}-\lambda\mathbf{I})
$$

Equivalently, solve

$$
(\mathbf{A}-\lambda\mathbf{I})\boldsymbol{x}=\boldsymbol{0}
$$

### Finding Eigenvalues and Eigenvectors

##### Computation steps

Start from the eigenvalue equation

$$
\mathbf{A}\boldsymbol{x}=\lambda\boldsymbol{x}
$$

Move all terms to one side

$$
(\mathbf{A}-\lambda\mathbf{I})\boldsymbol{x}=\boldsymbol{0}
$$

Require a nonzero nullspace

$$
\det(\mathbf{A}-\lambda\mathbf{I})=0
$$

Solve the characteristic equation for $\lambda$

For each $\lambda$, find the nullspace of $\mathbf{A}-\lambda\mathbf{I}$

##### Two by two formula

For

$$
\mathbf{A}
=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

The characteristic equation is

$$
\det(\mathbf{A}-\lambda\mathbf{I})
=
\begin{vmatrix}
a-\lambda&b\\
c&d-\lambda
\end{vmatrix}
=0
$$

Therefore

$$
\lambda^2-(a+d)\lambda+(ad-bc)=0
$$

Using trace and determinant

$$
\lambda^2-\operatorname{trace}(\mathbf{A})\lambda+\det\mathbf{A}=0
$$

##### Eigenvector calculation

After finding $\lambda$, solve

$$
(\mathbf{A}-\lambda\mathbf{I})\boldsymbol{x}=\boldsymbol{0}
$$

For a $2\times2$ matrix this is usually one independent equation

Choose one free variable and solve for the other

Any nonzero multiple is the same eigenvector direction

### Trace and Determinant

##### Sum of eigenvalues

The trace is the sum of the eigenvalues, counted with algebraic multiplicity

$$
\operatorname{trace}(\mathbf{A})
=
\lambda_1+\lambda_2+\cdots+\lambda_n
$$

##### Product of eigenvalues

The determinant is the product of the eigenvalues, counted with algebraic multiplicity

$$
\det\mathbf{A}
=
\lambda_1\lambda_2\cdots\lambda_n
$$

##### Singular matrix

A square matrix is singular exactly when zero is an eigenvalue

$$
\det\mathbf{A}=0
\quad\Longleftrightarrow\quad
0\text{ is an eigenvalue}
$$

##### Similar matrices

Similar matrices have the same eigenvalues

$$
\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}
$$

because

$$
\det(\mathbf{B}-\lambda\mathbf{I})
=
\det(\mathbf{A}-\lambda\mathbf{I})
$$

### Diagonalizing a Matrix

##### Eigenvector matrix

Put independent eigenvectors into the columns of $\mathbf{S}$

$$
\mathbf{S}
=
\begin{bmatrix}
\boldsymbol{x}_1&\boldsymbol{x}_2&\cdots&\boldsymbol{x}_n
\end{bmatrix}
$$

Then

$$
\mathbf{A}\mathbf{S}
=
\mathbf{S}\boldsymbol{\Lambda}
$$

where

$$
\boldsymbol{\Lambda}
=
\operatorname{diag}(\lambda_1,\lambda_2,\ldots,\lambda_n)
$$

##### Diagonalization

If $\mathbf{S}$ is invertible

$$
\mathbf{A}
=
\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}
$$

Equivalently

$$
\mathbf{S}^{-1}\mathbf{A}\mathbf{S}
=
\boldsymbol{\Lambda}
$$

The matrix is diagonalizable when it has $n$ independent eigenvectors

##### Powers of a matrix

Diagonalization makes powers simple

$$
\mathbf{A}^{k}
=
\mathbf{S}\boldsymbol{\Lambda}^{k}\mathbf{S}^{-1}
$$

where

$$
\boldsymbol{\Lambda}^{k}
=
\operatorname{diag}(\lambda_1^{k},\lambda_2^{k},\ldots,\lambda_n^{k})
$$

##### Repeated eigenvalues

A repeated eigenvalue may or may not have enough independent eigenvectors

The algebraic multiplicity is its multiplicity as a root of the characteristic polynomial

The geometric multiplicity is the dimension of its eigenspace

$$
\dim N(\mathbf{A}-\lambda\mathbf{I})
$$

For diagonalization, the total number of independent eigenvectors must be $n$

### Difference Equations

##### Powers and long term behavior

For a difference equation

$$
\boldsymbol{u}_{k+1}=\mathbf{A}\boldsymbol{u}_{k}
$$

The solution is

$$
\boldsymbol{u}_{k}=\mathbf{A}^{k}\boldsymbol{u}_{0}
$$

If $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$

$$
\boldsymbol{u}_{k}
=
\mathbf{S}\boldsymbol{\Lambda}^{k}\mathbf{S}^{-1}\boldsymbol{u}_{0}
$$

The powers are controlled by the sizes of the eigenvalues

$$
\lambda_i^{k}
$$

### Differential Equations

##### First-order system

For a linear system

$$
\frac{d\boldsymbol{u}}{dt}
=
\mathbf{A}\boldsymbol{u}
$$

If $\mathbf{A}\boldsymbol{x}=\lambda\boldsymbol{x}$, one special solution is

$$
\boldsymbol{u}(t)
=
e^{\lambda t}\boldsymbol{x}
$$

##### General solution

With independent eigenvectors

$$
\boldsymbol{u}(t)
=
c_1e^{\lambda_1t}\boldsymbol{x}_1+
\cdots+
c_ne^{\lambda_nt}\boldsymbol{x}_n
$$

Stability is controlled by the real parts of the eigenvalues

$$
\operatorname{Re}(\lambda_i)<0
$$

### Symmetric Matrices

##### Real eigenvalues

A real symmetric matrix has real eigenvalues

$$
\mathbf{A}^{T}=\mathbf{A}
$$

##### Orthogonal eigenvectors

Eigenvectors of a symmetric matrix corresponding to different eigenvalues are orthogonal

If

$$
\mathbf{A}\boldsymbol{x}=\lambda\boldsymbol{x}
$$

and

$$
\mathbf{A}\boldsymbol{y}=\mu\boldsymbol{y}
$$

with $\lambda\ne\mu$, then

$$
\boldsymbol{x}^{T}\boldsymbol{y}=0
$$

##### Spectral theorem

A real symmetric matrix can be diagonalized by an orthogonal matrix

$$
\mathbf{A}
=
\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{T}
$$

where

$$
\mathbf{Q}^{T}\mathbf{Q}=\mathbf{I}
$$

Equivalently

$$
\mathbf{Q}^{T}\mathbf{A}\mathbf{Q}=\boldsymbol{\Lambda}
$$

##### Orthogonal projection form

A symmetric matrix can be written as a sum of eigenvalue times projection matrices

$$
\mathbf{A}
=
\lambda_1\boldsymbol{q}_1\boldsymbol{q}_1^{T}
+
\lambda_2\boldsymbol{q}_2\boldsymbol{q}_2^{T}
+
\cdots+
\lambda_n\boldsymbol{q}_n\boldsymbol{q}_n^{T}
$$

### Positive Definite Matrices

##### Definition

A symmetric matrix is positive definite when

$$
\boldsymbol{x}^{T}\mathbf{A}\boldsymbol{x}>0
\qquad
\boldsymbol{x}\ne\boldsymbol{0}
$$

##### Eigenvalue test

A symmetric matrix is positive definite exactly when all eigenvalues are positive

$$
\lambda_i>0
\qquad
 i=1,2,\ldots,n
$$

##### Pivot test

For a symmetric matrix, positive pivots without row exchanges give positive definiteness

$$
d_i>0
\qquad
 i=1,2,\ldots,n
$$

##### Determinant test

For a symmetric matrix, positive leading principal determinants give positive definiteness

$$
\det\mathbf{A}_k>0
\qquad
 k=1,2,\ldots,n
$$

where $\mathbf{A}_k$ is the leading $k\times k$ submatrix

### Markov Matrices

##### Steady state

For a Markov matrix, columns add to one

$$
\sum_{i=1}^{n}a_{ij}=1
$$

Then $1$ is an eigenvalue

$$
\lambda=1
$$

A steady state satisfies

$$
\mathbf{A}\boldsymbol{x}=\boldsymbol{x}
$$

Equivalently

$$
(\mathbf{A}-\mathbf{I})\boldsymbol{x}=\boldsymbol{0}
$$
