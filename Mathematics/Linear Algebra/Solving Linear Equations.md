# Solving Linear Equations

[toc]

### The Problem

##### Linear system

A system of $m$ equations in $n$ unknowns is written as

$$
\mathbf{A}\boldsymbol{x}=\boldsymbol{b}
$$

with

$$
\mathbf{A}
=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix}
$$

$$
\boldsymbol{x}
=
\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}
\qquad
\boldsymbol{b}
=
\begin{bmatrix}
b_1\\b_2\\\vdots\\b_m
\end{bmatrix}
$$

The column picture asks for a combination of the columns of $\mathbf{A}$

$$
x_1\boldsymbol{a}_1+x_2\boldsymbol{a}_2+\cdots+x_n\boldsymbol{a}_n
=
\boldsymbol{b}
$$

The row picture asks for the intersection of equations

$$
\operatorname{row}_i(\mathbf{A})\boldsymbol{x}=b_i
$$

### Elimination

##### Row operations

Elimination uses row operations that keep the solution set unchanged

Interchange two equations

Multiply an equation by a nonzero number

Add a multiple of one equation to another equation

##### Pivot

A pivot is the first nonzero entry used to eliminate entries below it

For a pivot $a_{kk}\ne0$, the multiplier for row $i$ is

$$
\ell_{ik}
=
\frac{a_{ik}}{a_{kk}}
$$

The new row $i$ is

$$
\operatorname{row}_i
\leftarrow
\operatorname{row}_i-
\ell_{ik}\operatorname{row}_k
$$

##### Upper triangular form

Elimination changes $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ into

$$
\mathbf{U}\boldsymbol{x}=\boldsymbol{c}
$$

where $\mathbf{U}$ is upper triangular

$$
\mathbf{U}
=
\begin{bmatrix}
u_{11}&u_{12}&\cdots&u_{1n}\\
0&u_{22}&\cdots&u_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&u_{nn}
\end{bmatrix}
$$

##### Back substitution

For a nonsingular triangular system, solve from the last equation upward

$$
x_n
=
\frac{c_n}{u_{nn}}
$$

$$
x_i
=
\frac{c_i-\sum_{j=i+1}^{n}u_{ij}x_j}{u_{ii}}
$$

### Elimination Matrices

##### Elementary matrix

Each row operation can be represented by multiplication by an elementary matrix

$$
\mathbf{E}\mathbf{A}
=
\text{new matrix after one row operation}
$$

If elimination changes $\mathbf{A}$ to $\mathbf{U}$

$$
\mathbf{E}_{k}\cdots\mathbf{E}_{2}\mathbf{E}_{1}\mathbf{A}
=
\mathbf{U}
$$

##### Inverse operation

The inverse elementary matrix reverses the row operation

$$
\mathbf{E}^{-1}\mathbf{E}=\mathbf{I}
$$

The inverse of subtracting $\ell$ times row $k$ is adding $\ell$ times row $k$

### Factorization

##### LU factorization

When no row exchanges are needed, elimination gives

$$
\mathbf{A}=\mathbf{L}\mathbf{U}
$$

where $\mathbf{L}$ is lower triangular and $\mathbf{U}$ is upper triangular

$$
\mathbf{L}
=
\begin{bmatrix}
1&0&\cdots&0\\
\ell_{21}&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
\ell_{n1}&\ell_{n2}&\cdots&1
\end{bmatrix}
$$

The multipliers from elimination go into $\mathbf{L}$

##### Solving with LU

To solve $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ with $\mathbf{A}=\mathbf{L}\mathbf{U}$, solve two triangular systems

$$
\mathbf{L}\boldsymbol{c}=\boldsymbol{b}
$$

$$
\mathbf{U}\boldsymbol{x}=\boldsymbol{c}
$$

Forward substitution solves the first system and back substitution solves the second

##### Row exchanges

If row exchanges are needed, a permutation matrix $\mathbf{P}$ records them

$$
\mathbf{P}\mathbf{A}=\mathbf{L}\mathbf{U}
$$

A permutation matrix has exactly one $1$ in each row and each column

$$
\mathbf{P}^{-1}=\mathbf{P}^{T}
$$

### Echelon Forms

##### Row echelon form

A row echelon form has pivots moving to the right as the rows go down

All zero rows, if any, are below the nonzero rows

Entries below each pivot are zero

##### Reduced row echelon form

The reduced row echelon form has pivots equal to $1$ and zeros above and below each pivot

$$
\mathbf{R}=\operatorname{rref}(\mathbf{A})
$$

The reduced row echelon form reveals pivot variables and free variables

##### Pivot variables and free variables

Pivot columns contain pivots

Free columns do not contain pivots

If $\mathbf{A}$ has $n$ columns and rank $r$, then

$$
\text{number of free variables}=n-r
$$

### Existence and Uniqueness

##### Consistency

The system $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ is consistent when at least one solution exists

An inconsistent system has a zero row in $\mathbf{A}$ with a nonzero entry in the augmented column

$$
\begin{bmatrix}
0&0&\cdots&0&|&c
\end{bmatrix}
\qquad
c\ne0
$$

This represents

$$
0=c
$$

##### Unique solution

A unique solution occurs when every variable is a pivot variable

For a square matrix this means

$$
\operatorname{rank}(\mathbf{A})=n
$$

Equivalently

$$
N(\mathbf{A})=\{\boldsymbol{0}\}
$$

##### Infinitely many solutions

If the system is consistent and at least one variable is free, then there are infinitely many solutions

$$
n-r>0
$$

The free variables produce the nullspace part of the solution

##### No solution

No solution occurs when $\boldsymbol{b}$ is not in the column space of $\mathbf{A}$

$$
\boldsymbol{b}\notin C(\mathbf{A})
$$

### Complete Solution

##### Homogeneous equation

The homogeneous equation always has the zero solution

$$
\mathbf{A}\boldsymbol{x}=\boldsymbol{0}
$$

Nonzero solutions exist exactly when there are free variables

$$
\operatorname{rank}(\mathbf{A})<n
$$

##### Special solutions

To find the nullspace, set one free variable equal to $1$ and the other free variables equal to $0$

Each choice gives a special solution

The special solutions form a basis for $N(\mathbf{A})$

##### Particular solution

To find one particular solution of $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$, set all free variables equal to zero and solve for pivot variables

This gives $\boldsymbol{x}_p$

##### Complete solution

All solutions have the form

$$
\boldsymbol{x}=\boldsymbol{x}_p+\boldsymbol{x}_n
$$

where

$$
\boldsymbol{x}_n\in N(\mathbf{A})
$$

If the special solutions are $\boldsymbol{s}_1,\ldots,\boldsymbol{s}_{n-r}$, then

$$
\boldsymbol{x}
=
\boldsymbol{x}_p+c_1\boldsymbol{s}_1+\cdots+c_{n-r}\boldsymbol{s}_{n-r}
$$

### Invertible Systems

##### Square full-rank case

For an $n\times n$ matrix, the following are equivalent

$\mathbf{A}$ is invertible

$\mathbf{A}$ has $n$ pivots

$\operatorname{rank}(\mathbf{A})=n$

$\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ has exactly one solution for every $\boldsymbol{b}$

$\mathbf{A}\boldsymbol{x}=\boldsymbol{0}$ has only the zero solution

##### Solving all right hand sides

Solving $\mathbf{A}\mathbf{X}=\mathbf{I}$ gives the inverse matrix

$$
\mathbf{X}=\mathbf{A}^{-1}
$$

Gauss-Jordan elimination gives

$$
\begin{bmatrix}
\mathbf{A}&\mathbf{I}
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
\mathbf{I}&\mathbf{A}^{-1}
\end{bmatrix}
$$
