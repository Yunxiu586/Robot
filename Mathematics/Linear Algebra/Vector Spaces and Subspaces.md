# Vector Spaces and Subspaces

[toc]

### Vector Spaces

##### Definition

A vector space is a set of vectors where linear combinations stay in the space

If $\boldsymbol{u}$ and $\boldsymbol{v}$ are in $V$, then

$$
c\boldsymbol{u}+d\boldsymbol{v}\in V
$$

for all scalars $c$ and $d$

Every vector space contains the zero vector

$$
\boldsymbol{0}\in V
$$

##### Examples

The space $\mathbb{R}^{n}$ contains all column vectors with $n$ components

$$
\mathbb{R}^{n}
=
\left\{
\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}
:x_i\in\mathbb{R}
\right\}
$$

The set of all $m\times n$ matrices is also a vector space

### Subspaces

##### Definition

A subspace of $\mathbb{R}^{n}$ is a vector space inside $\mathbb{R}^{n}$

It must contain the zero vector and be closed under linear combinations

$$
\boldsymbol{0}\in S
$$

$$
c\boldsymbol{u}+d\boldsymbol{v}\in S
$$

A plane through the origin can be a subspace

A plane not through the origin is not a subspace

##### Span

The span of vectors is the set of all their linear combinations

$$
\operatorname{span}\{\boldsymbol{v}_1,\ldots,\boldsymbol{v}_k\}
=
\left\{
\sum_{i=1}^{k}c_i\boldsymbol{v}_i
\right\}
$$

Every span is a subspace

### Column Space

##### Definition

The column space contains all linear combinations of the columns of $\mathbf{A}$

$$
C(\mathbf{A})
=
\left\{
\mathbf{A}\boldsymbol{x}:\boldsymbol{x}\in\mathbb{R}^{n}
\right\}
$$

Equivalently

$$
C(\mathbf{A})
=
\operatorname{span}\{\boldsymbol{a}_1,\boldsymbol{a}_2,\ldots,\boldsymbol{a}_n\}
$$

For an $m\times n$ matrix, the column space is a subspace of $\mathbb{R}^{m}$

$$
C(\mathbf{A})\subseteq\mathbb{R}^{m}
$$

##### Solvability

The equation $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ is solvable exactly when $\boldsymbol{b}$ is in the column space

$$
\boldsymbol{b}\in C(\mathbf{A})
$$

If $\boldsymbol{b}$ is outside the column space, the system has no solution

$$
\boldsymbol{b}\notin C(\mathbf{A})
$$

##### Basis for the column space

The pivot columns of the original matrix $\mathbf{A}$ form a basis for $C(\mathbf{A})$

Do not take the pivot columns from $\mathbf{R}=\operatorname{rref}(\mathbf{A})$ for the column space of $\mathbf{A}$

The number of pivot columns is the rank

$$
\dim C(\mathbf{A})=\operatorname{rank}(\mathbf{A})
$$

### Nullspace

##### Definition

The nullspace contains all solutions to the homogeneous equation

$$
N(\mathbf{A})
=
\left\{
\boldsymbol{x}:\mathbf{A}\boldsymbol{x}=\boldsymbol{0}
\right\}
$$

For an $m\times n$ matrix, the nullspace is a subspace of $\mathbb{R}^{n}$

$$
N(\mathbf{A})\subseteq\mathbb{R}^{n}
$$

##### Finding the nullspace

Reduce $\mathbf{A}$ to $\mathbf{R}=\operatorname{rref}(\mathbf{A})$

Solve the equivalent equation

$$
\mathbf{R}\boldsymbol{x}=\boldsymbol{0}
$$

Pivot variables are written in terms of free variables

Set one free variable to $1$ and the others to $0$ to get one special solution

##### Nullity

The dimension of the nullspace is the number of free variables

$$
\dim N(\mathbf{A})=n-r
$$

where

$$
r=\operatorname{rank}(\mathbf{A})
$$

### Row Space and Left Nullspace

##### Row space

The row space is the space spanned by the rows of $\mathbf{A}$

It is also the column space of $\mathbf{A}^{T}$

$$
C(\mathbf{A}^{T})
$$

For an $m\times n$ matrix, the row space is a subspace of $\mathbb{R}^{n}$

$$
C(\mathbf{A}^{T})\subseteq\mathbb{R}^{n}
$$

The nonzero rows of $\mathbf{R}=\operatorname{rref}(\mathbf{A})$ form a basis for the row space

##### Left nullspace

The left nullspace is the nullspace of $\mathbf{A}^{T}$

$$
N(\mathbf{A}^{T})
=
\left\{
\boldsymbol{y}:\mathbf{A}^{T}\boldsymbol{y}=\boldsymbol{0}
\right\}
$$

Equivalently

$$
\boldsymbol{y}^{T}\mathbf{A}=\boldsymbol{0}^{T}
$$

For an $m\times n$ matrix, the left nullspace is a subspace of $\mathbb{R}^{m}$

$$
N(\mathbf{A}^{T})\subseteq\mathbb{R}^{m}
$$

### Independence, Basis, and Dimension

##### Linear independence

Vectors $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_k$ are linearly independent when the only combination giving zero is the trivial combination

$$
c_1\boldsymbol{v}_1+c_2\boldsymbol{v}_2+\cdots+c_k\boldsymbol{v}_k
=
\boldsymbol{0}
$$

implies

$$
c_1=c_2=\cdots=c_k=0
$$

If a nontrivial combination gives zero, the vectors are dependent

##### Basis

A basis is an independent set that spans the space

$$
V
=
\operatorname{span}\{\boldsymbol{v}_1,\ldots,\boldsymbol{v}_r\}
$$

The vectors must be enough to span and not too many to be dependent

##### Dimension

The dimension of a vector space is the number of vectors in any basis

$$
\dim V=r
$$

All bases of the same space have the same number of vectors

### Rank

##### Definition

The rank of $\mathbf{A}$ is the number of pivots

$$
r=\operatorname{rank}(\mathbf{A})
$$

It is also the dimension of the column space

$$
r=\dim C(\mathbf{A})
$$

It is also the dimension of the row space

$$
r=\dim C(\mathbf{A}^{T})
$$

Column rank equals row rank

##### Finding rank

Reduce $\mathbf{A}$ to echelon form or reduced row echelon form

Count the pivots

$$
\operatorname{rank}(\mathbf{A})
=
\text{number of pivots}
$$

The pivot columns identify independent columns in the original matrix

The nonzero rows of $\mathbf{R}$ identify a basis for the row space

##### Rank and nullity

For an $m\times n$ matrix

$$
\operatorname{rank}(\mathbf{A})+\dim N(\mathbf{A})=n
$$

Equivalently

$$
r+(n-r)=n
$$

##### Full rank

A matrix has full column rank when its columns are independent

$$
\operatorname{rank}(\mathbf{A})=n
$$

A matrix has full row rank when its rows are independent

$$
\operatorname{rank}(\mathbf{A})=m
$$

For an $m\times n$ matrix

$$
\operatorname{rank}(\mathbf{A})\le \min(m,n)
$$

##### Rank one matrices

A rank one matrix is an outer product

$$
\mathbf{A}=\boldsymbol{u}\boldsymbol{v}^{T}
$$

All columns are multiples of one vector $\boldsymbol{u}$

All rows are multiples of one vector $\boldsymbol{v}^{T}$

##### Rank of products

The rank of a product cannot exceed the rank of either factor

$$
\operatorname{rank}(\mathbf{A}\mathbf{B})
\le
\min\{\operatorname{rank}(\mathbf{A}),\operatorname{rank}(\mathbf{B})\}
$$

If $\mathbf{M}$ and $\mathbf{N}$ are invertible

$$
\operatorname{rank}(\mathbf{M}\mathbf{A}\mathbf{N})
=
\operatorname{rank}(\mathbf{A})
$$

### Complete Solution

##### Particular and nullspace parts

If $\boldsymbol{x}_p$ is one particular solution of $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$, then all solutions are

$$
\boldsymbol{x}=\boldsymbol{x}_p+\boldsymbol{x}_n
$$

where

$$
\boldsymbol{x}_n\in N(\mathbf{A})
$$

Thus the complete solution is one particular solution plus all nullspace solutions

##### Matrix form

If $\boldsymbol{s}_1,\ldots,\boldsymbol{s}_{n-r}$ form a basis for $N(\mathbf{A})$

$$
\boldsymbol{x}
=
\boldsymbol{x}_p+c_1\boldsymbol{s}_1+\cdots+c_{n-r}\boldsymbol{s}_{n-r}
$$

### Four Fundamental Subspaces

##### Subspaces of a matrix

For an $m\times n$ matrix $\mathbf{A}$

$$
C(\mathbf{A})\subseteq\mathbb{R}^{m}
$$

$$
N(\mathbf{A})\subseteq\mathbb{R}^{n}
$$

$$
C(\mathbf{A}^{T})\subseteq\mathbb{R}^{n}
$$

$$
N(\mathbf{A}^{T})\subseteq\mathbb{R}^{m}
$$

##### Dimensions

The dimensions are

$$
\dim C(\mathbf{A})=r
$$

$$
\dim N(\mathbf{A})=n-r
$$

$$
\dim C(\mathbf{A}^{T})=r
$$

$$
\dim N(\mathbf{A}^{T})=m-r
$$

##### Orthogonal pairs

The row space is orthogonal to the nullspace

$$
C(\mathbf{A}^{T})\perp N(\mathbf{A})
$$

The column space is orthogonal to the left nullspace

$$
C(\mathbf{A})\perp N(\mathbf{A}^{T})
$$
