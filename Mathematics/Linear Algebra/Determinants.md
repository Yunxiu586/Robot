# Determinants

[toc]

### Properties of Determinants

##### Identity

The determinant of the identity matrix is one

$$
\det\mathbf{I}=1
$$

##### Row exchange

Exchanging two rows changes the sign of the determinant

$$
\det(\mathbf{P}\mathbf{A})=-\det\mathbf{A}
$$

for one row exchange

##### Linearity in one row

The determinant is linear in each row separately

$$
\det
\begin{bmatrix}
\alpha\boldsymbol{r}_1+\beta\boldsymbol{s}_1\\
\boldsymbol{r}_2\\
\vdots\\
\boldsymbol{r}_n
\end{bmatrix}
=
\alpha
\det
\begin{bmatrix}
\boldsymbol{r}_1\\
\boldsymbol{r}_2\\
\vdots\\
\boldsymbol{r}_n
\end{bmatrix}
+
\beta
\det
\begin{bmatrix}
\boldsymbol{s}_1\\
\boldsymbol{r}_2\\
\vdots\\
\boldsymbol{r}_n
\end{bmatrix}
$$

##### Equal rows

If two rows are equal, the determinant is zero

$$
\det\mathbf{A}=0
$$

##### Row elimination

Adding a multiple of one row to another row does not change the determinant

$$
\det(\mathbf{E}\mathbf{A})=\det\mathbf{A}
$$

##### Scaling a row

Multiplying one row by $c$ multiplies the determinant by $c$

$$
\det(\text{matrix with row }i\text{ scaled by }c)
=
c\det\mathbf{A}
$$

Multiplying all rows by $c$ gives

$$
\det(c\mathbf{A})=c^{n}\det\mathbf{A}
$$

### Computing Determinants

##### Two by two matrix

$$
\det
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
=
ad-bc
$$

##### Three by three matrix

For

$$
\mathbf{A}
=
\begin{bmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{bmatrix}
$$

Expansion along the first row gives

$$
\det\mathbf{A}
=
a(ei-fh)-b(di-fg)+c(dh-eg)
$$

##### Triangular matrix

For a triangular matrix, the determinant is the product of the diagonal entries

$$
\det\mathbf{U}
=
u_{11}u_{22}\cdots u_{nn}
$$

##### Elimination method

Use elimination to change $\mathbf{A}$ to an upper triangular matrix $\mathbf{U}$

Row replacement does not change the determinant

Row exchange changes the sign

Row scaling changes the determinant by the scale factor

If there are no row exchanges and no row scalings

$$
\det\mathbf{A}=\det\mathbf{U}=u_{11}u_{22}\cdots u_{nn}
$$

If $s$ row exchanges are used and no row scalings are used

$$
\det\mathbf{A}=(-1)^{s}u_{11}u_{22}\cdots u_{nn}
$$

### Determinants and Invertibility

##### Singular matrix

A square matrix is singular exactly when its determinant is zero

$$
\mathbf{A}\text{ is singular}
\quad\Longleftrightarrow\quad
\det\mathbf{A}=0
$$

Equivalently

$$
\operatorname{rank}(\mathbf{A})<n
$$

##### Invertible matrix

A square matrix is invertible exactly when its determinant is nonzero

$$
\mathbf{A}\text{ is invertible}
\quad\Longleftrightarrow\quad
\det\mathbf{A}\ne0
$$

Equivalently

$$
\operatorname{rank}(\mathbf{A})=n
$$

##### Zero determinant

A zero determinant means the columns are dependent and the volume collapses

$$
\det\mathbf{A}=0
$$

$$
C(\mathbf{A})\ne\mathbb{R}^{n}
$$

### Determinant Rules

##### Product rule

The determinant of a product is the product of the determinants

$$
\det(\mathbf{A}\mathbf{B})
=
\det\mathbf{A}\det\mathbf{B}
$$

##### Inverse matrix

If $\mathbf{A}$ is invertible

$$
\det(\mathbf{A}^{-1})
=
\frac{1}{\det\mathbf{A}}
$$

##### Transpose

The transpose has the same determinant

$$
\det(\mathbf{A}^{T})=\det\mathbf{A}
$$

##### Powers

For a square matrix

$$
\det(\mathbf{A}^{k})=(\det\mathbf{A})^{k}
$$

##### Similar matrices

If $\mathbf{S}$ is invertible, similar matrices have the same determinant

$$
\det(\mathbf{S}^{-1}\mathbf{A}\mathbf{S})=
\det\mathbf{A}
$$

### Permutations

##### Permutation formula

The determinant is a signed sum over all permutations

$$
\det\mathbf{A}
=
\sum_{\pi}
\operatorname{sign}(\pi)
a_{1\pi(1)}a_{2\pi(2)}\cdots a_{n\pi(n)}
$$

##### Even and odd permutations

An even permutation has sign $+1$ and an odd permutation has sign $-1$

$$
\operatorname{sign}(\pi)\in\{1,-1\}
$$

The sign changes whenever two columns or two rows are exchanged

### Cofactors

##### Minor

Delete row $i$ and column $j$ to form the minor matrix $\mathbf{M}_{ij}$

##### Cofactor

$$
C_{ij}
=
(-1)^{i+j}\det\mathbf{M}_{ij}
$$

##### Cofactor expansion

Expansion along row $i$

$$
\det\mathbf{A}
=
\sum_{j=1}^{n}a_{ij}C_{ij}
$$

Expansion along column $j$

$$
\det\mathbf{A}
=
\sum_{i=1}^{n}a_{ij}C_{ij}
$$

Cofactor expansion is useful when a row or column has many zeros

### Inverses and Cramer's Rule

##### Cofactor formula

The cofactor matrix is

$$
\mathbf{C}=(C_{ij})
$$

The adjugate matrix is the transpose of the cofactor matrix

$$
\operatorname{adj}(\mathbf{A})=\mathbf{C}^{T}
$$

The inverse is given by cofactors when $\det\mathbf{A}\ne0$

$$
\mathbf{A}^{-1}
=
\frac{1}{\det\mathbf{A}}\operatorname{adj}(\mathbf{A})
$$

##### Cramer's rule

For $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ with $\det\mathbf{A}\ne0$

$$
x_j
=
\frac{\det\mathbf{A}_j}{\det\mathbf{A}}
$$

where $\mathbf{A}_j$ is $\mathbf{A}$ with column $j$ replaced by $\boldsymbol{b}$

Cramer's rule is important theoretically but elimination is usually faster for computation

### Volume

##### Area and volume factor

The absolute value of the determinant is the area or volume scaling factor

$$
\text{volume after }\mathbf{A}
=
|\det\mathbf{A}|\text{ volume before}
$$

##### Orientation

A positive determinant preserves orientation

A negative determinant reverses orientation

A zero determinant collapses volume into a lower-dimensional set
