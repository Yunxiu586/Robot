# Vectors and Matrices

[toc]

### Vectors

##### Column vectors

A vector in $\mathbb{R}^{n}$ is an ordered list of $n$ numbers

$$
\boldsymbol{x}
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

Vectors can be added and multiplied by scalars

$$
\boldsymbol{u}+\boldsymbol{v}
=
\begin{bmatrix}
u_1+v_1\\
u_2+v_2\\
\vdots\\
u_n+v_n
\end{bmatrix}
$$

$$
c\boldsymbol{u}
=
\begin{bmatrix}
cu_1\\
cu_2\\
\vdots\\
cu_n
\end{bmatrix}
$$

A linear combination of $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_k$ has scalar coefficients $c_1,\ldots,c_k$

$$
c_1\boldsymbol{v}_1+c_2\boldsymbol{v}_2+\cdots+c_k\boldsymbol{v}_k
$$

##### Length

The length of $\boldsymbol{x}$ is its Euclidean norm

$$
\lVert \boldsymbol{x}\rVert
=
\sqrt{x_1^2+x_2^2+\cdots+x_n^2}
=
\sqrt{\boldsymbol{x}^{T}\boldsymbol{x}}
$$

For $\boldsymbol{x}\ne\boldsymbol{0}$, a unit vector has length one

$$
\boldsymbol{u}
=
\frac{\boldsymbol{x}}{\lVert \boldsymbol{x}\rVert}
$$

$$
\lVert \boldsymbol{u}\rVert=1
$$

### Dot Products

##### Inner product

A row vector multiplied by a column vector gives the inner product

$$
\begin{bmatrix}
a_1&a_2&\cdots&a_n
\end{bmatrix}
\begin{bmatrix}
b_1\\
b_2\\
\vdots\\
b_n
\end{bmatrix}
=
\sum_{i=1}^{n}a_i b_i
$$

Equivalently

$$
\boldsymbol{a}^{T}\boldsymbol{b}
=
\sum_{i=1}^{n}a_i b_i
$$

##### Angle

For nonzero vectors, the dot product measures the angle between $\boldsymbol{a}$ and $\boldsymbol{b}$

$$
\boldsymbol{a}^{T}\boldsymbol{b}
=
\lVert \boldsymbol{a}\rVert \lVert \boldsymbol{b}\rVert \cos\theta
$$

$$
\cos\theta
=
\frac{\boldsymbol{a}^{T}\boldsymbol{b}}{\lVert \boldsymbol{a}\rVert \lVert \boldsymbol{b}\rVert}
$$

Two nonzero vectors are orthogonal when their dot product is zero

$$
\boldsymbol{a}^{T}\boldsymbol{b}=0
$$

##### Basic rules

The dot product is symmetric

$$
\boldsymbol{a}^{T}\boldsymbol{b}
=
\boldsymbol{b}^{T}\boldsymbol{a}
$$

It is linear in each vector

$$
\boldsymbol{a}^{T}(c\boldsymbol{u}+d\boldsymbol{v})
=
c\boldsymbol{a}^{T}\boldsymbol{u}+d\boldsymbol{a}^{T}\boldsymbol{v}
$$

### Outer Products

##### Column times row

A column vector multiplied by a row vector gives the outer product

$$
\begin{bmatrix}
a_1\\
a_2\\
\vdots\\
a_m
\end{bmatrix}
\begin{bmatrix}
b_1&b_2&\cdots&b_n
\end{bmatrix}
=
\begin{bmatrix}
a_1b_1&a_1b_2&\cdots&a_1b_n\\
a_2b_1&a_2b_2&\cdots&a_2b_n\\
\vdots&\vdots&\ddots&\vdots\\
a_mb_1&a_mb_2&\cdots&a_mb_n
\end{bmatrix}
$$

Equivalently

$$
\boldsymbol{a}\boldsymbol{b}^{T}
=
\begin{bmatrix}
a_1\boldsymbol{b}^{T}\\
a_2\boldsymbol{b}^{T}\\
\vdots\\
a_m\boldsymbol{b}^{T}
\end{bmatrix}
$$

or

$$
\boldsymbol{a}\boldsymbol{b}^{T}
=
\begin{bmatrix}
b_1\boldsymbol{a}&b_2\boldsymbol{a}&\cdots&b_n\boldsymbol{a}
\end{bmatrix}
$$

An outer product has rank at most one

$$
\operatorname{rank}(\boldsymbol{a}\boldsymbol{b}^{T})\le 1
$$

### Matrix Multiplication

##### Matrix times vector

Multiplying $\mathbf{A}$ by $\boldsymbol{x}$ gives a combination of the columns of $\mathbf{A}$

$$
\mathbf{A}\boldsymbol{x}
=
x_1\boldsymbol{a}_1+x_2\boldsymbol{a}_2+\cdots+x_n\boldsymbol{a}_n
$$

where

$$
\mathbf{A}
=
\begin{bmatrix}
\boldsymbol{a}_1&\boldsymbol{a}_2&\cdots&\boldsymbol{a}_n
\end{bmatrix}
$$

The equation $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ asks whether $\boldsymbol{b}$ is a combination of the columns of $\mathbf{A}$

##### Entry formula

Let $\mathbf{A}=(a_{ik})_{m\times p}$ and $\mathbf{B}=(b_{kj})_{p\times n}$

$$
\mathbf{C}=\mathbf{A}\mathbf{B}=(c_{ij})_{m\times n}
$$

where

$$
c_{ij}
=
\operatorname{row}_i(\mathbf{A})\operatorname{col}_j(\mathbf{B})
=
\sum_{k=1}^{p}a_{ik}b_{kj}
$$

##### Column picture

Each column of $\mathbf{C}$ is a linear combination of the columns of $\mathbf{A}$

$$
\operatorname{col}_j(\mathbf{C})
=
\mathbf{A}\operatorname{col}_j(\mathbf{B})
=
\sum_{k=1}^{p}b_{kj}\operatorname{col}_k(\mathbf{A})
$$

##### Row picture

Each row of $\mathbf{C}$ is a linear combination of the rows of $\mathbf{B}$

$$
\operatorname{row}_i(\mathbf{C})
=
\operatorname{row}_i(\mathbf{A})\mathbf{B}
=
\sum_{k=1}^{p}a_{ik}\operatorname{row}_k(\mathbf{B})
$$

##### Outer product picture

Matrix multiplication is also a sum of column-row products

$$
\mathbf{A}\mathbf{B}
=
\sum_{k=1}^{p}\operatorname{col}_k(\mathbf{A})\operatorname{row}_k(\mathbf{B})
$$

### Matrix Rules

##### Associative and distributive laws

Matrix multiplication is associative and distributive

$$
(\mathbf{A}\mathbf{B})\mathbf{C}
=
\mathbf{A}(\mathbf{B}\mathbf{C})
$$

$$
\mathbf{A}(\mathbf{B}+\mathbf{C})
=
\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}
$$

$$
(\mathbf{A}+\mathbf{B})\mathbf{C}
=
\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}
$$

Matrix multiplication is generally not commutative

$$
\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}
$$

##### Identity matrix

The identity matrix leaves vectors unchanged

$$
\mathbf{I}\boldsymbol{x}=\boldsymbol{x}
$$

For compatible matrices

$$
\mathbf{A}\mathbf{I}=\mathbf{A}
$$

$$
\mathbf{I}\mathbf{A}=\mathbf{A}
$$

##### Transpose

The transpose switches rows and columns

$$
(\mathbf{A}^{T})_{ij}=a_{ji}
$$

Basic transpose rules

$$
(\mathbf{A}+\mathbf{B})^{T}
=
\mathbf{A}^{T}+\mathbf{B}^{T}
$$

$$
(\mathbf{A}\mathbf{B})^{T}
=
\mathbf{B}^{T}\mathbf{A}^{T}
$$

$$
(\mathbf{A}^{T})^{T}
=
\mathbf{A}
$$

A symmetric matrix equals its transpose

$$
\mathbf{A}^{T}=\mathbf{A}
$$

### Inverse Matrices

##### Definition

The inverse of $\mathbf{A}$ is the matrix $\mathbf{A}^{-1}$ that gives the identity on both sides

$$
\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}
$$

$$
\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}
$$

Only square matrices can have a two-sided inverse

##### Solving by the inverse

If $\mathbf{A}$ is invertible, the equation $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ has the unique solution

$$
\boldsymbol{x}=\mathbf{A}^{-1}\boldsymbol{b}
$$

The inverse matrix solves all right hand sides $\boldsymbol{b}$ at once

##### Two by two inverse

For a $2\times2$ matrix

$$
\mathbf{A}
=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

If $ad-bc\ne0$

$$
\mathbf{A}^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d&-b\\
-c&a
\end{bmatrix}
$$

The number $ad-bc$ is the determinant

$$
\det\mathbf{A}=ad-bc
$$

##### Gauss-Jordan method

To find $\mathbf{A}^{-1}$, reduce the augmented matrix $[\mathbf{A}\ \mathbf{I}]$

$$
\begin{bmatrix}
\mathbf{A}&\mathbf{I}
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
\mathbf{I}&\mathbf{A}^{-1}
\end{bmatrix}
$$

The same row operations that change $\mathbf{A}$ into $\mathbf{I}$ change $\mathbf{I}$ into $\mathbf{A}^{-1}$

##### Invertible matrix theorem

For an $n\times n$ matrix $\mathbf{A}$, the following statements are equivalent

$\mathbf{A}$ has an inverse

$\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ has one solution for every $\boldsymbol{b}$

$\mathbf{A}\boldsymbol{x}=\boldsymbol{0}$ has only the zero solution

$\mathbf{A}$ has $n$ pivots

$\operatorname{rank}(\mathbf{A})=n$

The columns of $\mathbf{A}$ are independent

The columns of $\mathbf{A}$ span $\mathbb{R}^{n}$

$\det\mathbf{A}\ne0$

$0$ is not an eigenvalue of $\mathbf{A}$

##### Inverse rules

The inverse of a product reverses the order

$$
(\mathbf{A}\mathbf{B})^{-1}
=
\mathbf{B}^{-1}\mathbf{A}^{-1}
$$

The inverse of a transpose is the transpose of the inverse

$$
(\mathbf{A}^{T})^{-1}
=
(\mathbf{A}^{-1})^{T}
$$

If $\mathbf{A}$ is invertible

$$
(\mathbf{A}^{-1})^{-1}=\mathbf{A}
$$

### Special Matrices

##### Diagonal matrices

A diagonal matrix has nonzero entries only on the diagonal

$$
\mathbf{D}
=
\operatorname{diag}(d_1,d_2,\ldots,d_n)
$$

If every $d_i\ne0$

$$
\mathbf{D}^{-1}
=
\operatorname{diag}\left(\frac{1}{d_1},\frac{1}{d_2},\ldots,\frac{1}{d_n}\right)
$$

##### Triangular matrices

For an upper triangular matrix, entries below the diagonal are zero

$$
u_{ij}=0
\qquad
 i>j
$$

The determinant is the product of diagonal entries

$$
\det\mathbf{U}
=
u_{11}u_{22}\cdots u_{nn}
$$

A triangular matrix is invertible exactly when no diagonal entry is zero

##### Orthogonal matrices

A square matrix $\mathbf{Q}$ with orthonormal columns is an orthogonal matrix

$$
\mathbf{Q}^{T}\mathbf{Q}=\mathbf{I}
$$

For a square $\mathbf{Q}$, this also gives

$$
\mathbf{Q}^{-1}=\mathbf{Q}^{T}
$$

Orthogonal matrices preserve lengths and dot products

$$
\lVert \mathbf{Q}\boldsymbol{x}\rVert=\lVert \boldsymbol{x}\rVert
$$

$$
(\mathbf{Q}\boldsymbol{x})^{T}(\mathbf{Q}\boldsymbol{y})
=
\boldsymbol{x}^{T}\boldsymbol{y}
$$
