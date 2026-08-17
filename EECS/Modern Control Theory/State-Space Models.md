# State-Space Models

[toc]

### State-Space Representation

##### State Variables and State

The **state** of a dynamic system is the smallest set of variables whose values at an initial time $t_0$, together with the input for $t\geq t_0$, completely determine the behavior of the system for $t\geq t_0$. The variables forming this set are the **state variables**; they need not be physically measurable or observable.

If $n$ state variables are required, they form the **state vector**

$$
\boldsymbol{x}(t)=\begin{bmatrix}x_1(t)&x_2(t)&\cdots&x_n(t)\end{bmatrix}^{T}
$$

The **state space** is the $n$-dimensional space whose coordinate axes are the state variables, and each state is represented by a point in this space. The choice of state variables is not unique, although the number of state variables is the same for different state-space representations of the same system.

##### State and Output Equations

For a general continuous-time system,

$$
\dot{\boldsymbol{x}}=\boldsymbol{f}(\boldsymbol{x},\boldsymbol{u},t)\qquad \boldsymbol{y}=\boldsymbol{g}(\boldsymbol{x},\boldsymbol{u},t)
$$

If the system is linear,

$$
\dot{\boldsymbol{x}}=A(t)\boldsymbol{x}+B(t)\boldsymbol{u}\qquad \boldsymbol{y}=C(t)\boldsymbol{x}+D(t)\boldsymbol{u}
$$

where $A(t)$ is the **state matrix**, $B(t)$ the **input matrix**, $C(t)$ the **output matrix**, and $D(t)$ the **direct transmission matrix**. For $\boldsymbol{x}\in\mathbb{R}^n$, $\boldsymbol{u}\in\mathbb{R}^r$, and $\boldsymbol{y}\in\mathbb{R}^m$,

$$
A\in\mathbb{R}^{n\times n}\qquad B\in\mathbb{R}^{n\times r}\qquad C\in\mathbb{R}^{m\times n}\qquad D\in\mathbb{R}^{m\times r}
$$

If the coefficient matrices are constant, the system is linear time-invariant:

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}\qquad \boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}
$$

For a strictly proper transfer function, $D=0$.

##### All-Integrator Representation

In a continuous-time system, integrators serve as memory devices, so their outputs can be chosen as state variables. An $n$th-order system involves $n$ integrators and can be written as $n$ first-order state equations by choosing the integrator outputs as states.

**eg.** Consider the first-order lag
$$
G(s)=\frac{Y(s)}{U(s)}=\frac{K}{Ts+1}
$$

Then

$$
(Ts+1)Y(s)=KU(s)
$$

and in the time domain

$$
T\dot y+y=Ku
$$

Hence

$$
\dot y=-\frac{1}{T}y+\frac{K}{T}u
$$

or equivalently, for an initial time $t_0$

$$
y(t)=y(t_0)+\int_{t_0}^{t}\left[\frac{K}{T}u(\tau)-\frac{1}{T}y(\tau)\right]d\tau
$$

### Construction of State-Space Models

##### From Physical Laws

A state-space model may be obtained directly from the governing physical laws. Choose a set of independent variables sufficient to specify the dynamic condition of the system, use the physical equations to express their first derivatives, and write the measured variables as functions of the states and inputs.

For an electrical network, Kirchhoff's voltage and current laws provide the algebraic relations needed to form the first-order state equations after the state variables have been chosen.

**eg.** Consider a circuit in which the voltage source $u$ drives an inductor $L$ in series with a parallel $R$-$C$ branch. Let $v_C$ be the voltage across the parallel branch and $i_L$ the current through the inductor. Choose

$$
x_1=v_C\qquad x_2=i_L
$$

Kirchhoff's current law gives

$$
x_2=C\dot x_1+\frac{1}{R}x_1
$$

$$
\dot x_1=-\frac{1}{RC}x_1+\frac{1}{C}x_2
$$

Kirchhoff's voltage law gives

$$
x_1+L\dot x_2=u
$$

$$
\dot x_2=-\frac{1}{L}x_1+\frac{1}{L}u
$$

Therefore

$$
\dot{\boldsymbol{x}}
=
\begin{bmatrix}
-\frac{1}{RC}&\frac{1}{C}\\
-\frac{1}{L}&0
\end{bmatrix}
\boldsymbol{x}
+
\begin{bmatrix}
0\\
\frac{1}{L}
\end{bmatrix}u
$$

If the capacitor voltage is taken as the output,

$$
y=\begin{bmatrix}1&0\end{bmatrix}\boldsymbol{x}
$$

##### Transfer-Function and State-Space Descriptions

A transfer function gives the input-output relation under zero initial conditions. A state-space representation introduces the state variables and gives both the state equation and the output equation; different sets of state variables may represent the same system.

##### State-Space Representation from a Transfer Function

For a SISO rational transfer function, use the coefficient convention

$$
G(s)=\frac{Y(s)}{U(s)}=\frac{b_0s^n+b_1s^{n-1}+\cdots+b_{n-1}s+b_n}{s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n}
$$

where leading numerator coefficients are zero when the numerator degree is less than $n$. 

The state-space equations $\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}$ and $\boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}$ give $G(s)=C(sI-A)^{-1}B+D$, so a finite-dimensional state-space representation produces a proper transfer function. 

If $b_0=0$, $G(s)$ is strictly proper and $D=0$; if $b_0\neq0$, $G(s)$ is proper but not strictly proper and $D=b_0$. A transfer function whose numerator degree exceeds $n$ cannot be represented by this ordinary form without input derivatives or a more general description.

A state-space representation is **minimal** if no lower-order state-space representation has the same transfer function. For a SISO rational transfer function, common pole-zero factors are canceled before determining the minimum order.

### State-Space Representations in Canonical Forms

##### SISO Transfer Function

Use the coefficient convention

$$
G(s)=\frac{Y(s)}{U(s)}=\frac{b_0s^n+b_1s^{n-1}+\cdots+b_{n-1}s+b_n}{s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n}
$$

where leading numerator coefficients are zero when the numerator degree is less than $n$. Polynomial division gives

$$
G(s)=b_0+\frac{(b_1-a_1b_0)s^{n-1}+\cdots+(b_{n-1}-a_{n-1}b_0)s+(b_n-a_nb_0)}{s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n}
$$

Hence the direct-transmission term is $D=b_0$; for a strictly proper transfer function, $b_0=0$.

##### Controllable Canonical Form (CCF)

$$
A_c=\begin{bmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_n&-a_{n-1}&-a_{n-2}&\cdots&-a_1
\end{bmatrix}
\qquad
B_c=\begin{bmatrix}0\\0\\\vdots\\0\\1\end{bmatrix}
$$

$$
C_c=\begin{bmatrix}b_n-a_nb_0&b_{n-1}-a_{n-1}b_0&\cdots&b_1-a_1b_0\end{bmatrix}
\qquad D_c=b_0
$$

**Proof.** Define

$$
Q(s)=\frac{U(s)}{s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n}
$$

so

$$
\left(s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n\right)Q(s)=U(s)
$$

$$
s^nQ(s)=U(s)-\left(a_1s^{n-1}+\cdots+a_{n-1}s+a_n\right)Q(s)
$$

With zero initial conditions, choose $x_1=q$, $x_2=\dot q$, $\ldots$, $x_n=q^{(n-1)}$. Then

$$
\dot x_1=x_2\qquad \dot x_2=x_3\qquad \cdots\qquad \dot x_{n-1}=x_n
$$

and inverse transformation of the denominator equation gives

$$
q^{(n)}=-a_nx_1-a_{n-1}x_2-\cdots-a_2x_{n-1}-a_1x_n+u
$$

hence $\dot{\boldsymbol{x}}=A_c\boldsymbol{x}+B_cu$.

Also,

$$
\begin{aligned}
Y(s)
&=\left(b_0s^n+b_1s^{n-1}+\cdots+b_{n-1}s+b_n\right)Q(s)\\
&=b_0U(s)+\left[(b_1-a_1b_0)s^{n-1}+\cdots+(b_{n-1}-a_{n-1}b_0)s+(b_n-a_nb_0)\right]Q(s)
\end{aligned}
$$

Taking the inverse Laplace transform under zero initial conditions,

$$
y=(b_n-a_nb_0)x_1+(b_{n-1}-a_{n-1}b_0)x_2+\cdots+(b_1-a_1b_0)x_n+b_0u
$$

which gives $C_c$ and $D_c$ above.

##### Observable Canonical Form (OCF)

$$
A_o=\begin{bmatrix}
0&0&\cdots&0&-a_n\\
1&0&\cdots&0&-a_{n-1}\\
0&1&\cdots&0&-a_{n-2}\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&1&-a_1
\end{bmatrix}
\qquad
B_o=\begin{bmatrix}
b_n-a_nb_0\\
b_{n-1}-a_{n-1}b_0\\
\vdots\\
b_2-a_2b_0\\
b_1-a_1b_0
\end{bmatrix}
$$

$$
C_o=\begin{bmatrix}0&0&\cdots&0&1\end{bmatrix}
\qquad D_o=b_0
$$

Thus $A_o=A_c^T$.

**Proof.** The state equations are

$$
\begin{aligned}
\dot x_1&=-a_nx_n+(b_n-a_nb_0)u\\
\dot x_2&=x_1-a_{n-1}x_n+(b_{n-1}-a_{n-1}b_0)u\\
&\ \vdots\\
\dot x_{n-1}&=x_{n-2}-a_2x_n+(b_2-a_2b_0)u\\
\dot x_n&=x_{n-1}-a_1x_n+(b_1-a_1b_0)u
\end{aligned}
$$

with $y=x_n+b_0u$, so $x_n=y-b_0u$. From the last state equation,

$$
\begin{aligned}
x_{n-1}
&=\dot x_n+a_1x_n-(b_1-a_1b_0)u\\
&=\dot y+a_1y-b_0\dot u-b_1u
\end{aligned}
$$

Using the preceding state equation gives

$$
\begin{aligned}
x_{n-2}
&=\dot x_{n-1}+a_2x_n-(b_2-a_2b_0)u\\
&=\ddot y+a_1\dot y+a_2y-b_0\ddot u-b_1\dot u-b_2u
\end{aligned}
$$

Repeating this substitution yields

$$
x_1=y^{(n-1)}+a_1y^{(n-2)}+\cdots+a_{n-2}\dot y+a_{n-1}y-b_0u^{(n-1)}-b_1u^{(n-2)}-\cdots-b_{n-1}u
$$

and therefore

$$
\dot x_1=y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}\dot y-b_0u^{(n)}-b_1u^{(n-1)}-\cdots-b_{n-1}\dot u
$$

The first state equation also gives

$$
\dot x_1=-a_n(y-b_0u)+(b_n-a_nb_0)u=-a_ny+b_nu
$$

Equating the two expressions for $\dot x_1$ gives

$$
y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}\dot y+a_ny=b_0u^{(n)}+b_1u^{(n-1)}+\cdots+b_{n-1}\dot u+b_nu
$$

whose zero-initial-condition transfer function is the stated $G(s)$.

**eg.** Consider

$$
y^{(3)}+5\ddot y+7\dot y+3y=\dot u+2u
$$

$$
y^{(3)}+5\ddot y+7\dot y+3y=\ddot u+3\dot u+2u
$$

With zero initial conditions,

$$
G_1(s)=\frac{s+2}{s^3+5s^2+7s+3}
\qquad
G_2(s)=\frac{s^2+3s+2}{s^3+5s^2+7s+3}
$$

For the common denominator, $a_1=5$, $a_2=7$, and $a_3=3$. For $G_1$, $(b_0,b_1,b_2,b_3)=(0,0,1,2)$; for $G_2$, $(b_0,b_1,b_2,b_3)=(0,1,3,2)$.

The second transfer function contains a common factor,

$$
G_2(s)=\frac{(s+1)(s+2)}{(s+1)^2(s+3)}
$$

so the third-order state-space form obtained from the uncanceled differential equation retains the canceled factor. Using the common unreduced denominator, both controllable canonical forms have

$$
A_c=\begin{bmatrix}0&1&0\\0&0&1\\-3&-7&-5\end{bmatrix}
\qquad
B_c=\begin{bmatrix}0\\0\\1\end{bmatrix}
$$

For $G_1(s)$ and $G_2(s)$, respectively,

$$
C_{c1}=\begin{bmatrix}2&1&0\end{bmatrix}\qquad D_{c1}=0
\qquad
C_{c2}=\begin{bmatrix}2&3&1\end{bmatrix}\qquad D_{c2}=0
$$

Thus the common unreduced denominator gives the same $A_c$ and $B_c$, while the numerator coefficients appear in $C_c$.

Both observable canonical forms have

$$
A_o=\begin{bmatrix}0&0&-3\\1&0&-7\\0&1&-5\end{bmatrix}
\qquad
C_o=\begin{bmatrix}0&0&1\end{bmatrix}
\qquad D_o=0
$$

with

$$
B_{o1}=\begin{bmatrix}2\\1\\0\end{bmatrix}
\qquad
B_{o2}=\begin{bmatrix}2\\3\\1\end{bmatrix}
$$

Thus the common unreduced denominator gives the same $A_o$ and $C_o$, while the numerator coefficients appear in $B_o$.

### Change of State Variables

##### Nonsingular State Transformation

Let $P$ be a nonsingular constant matrix and define

$$
\boldsymbol{x}=P\boldsymbol{z}\qquad \boldsymbol{z}=P^{-1}\boldsymbol{x}
$$

Substitution into $\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}$ and $\boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}$ gives

$$
\dot{\boldsymbol{z}}=P^{-1}AP\boldsymbol{z}+P^{-1}B\boldsymbol{u}
\qquad
\boldsymbol{y}=CP\boldsymbol{z}+D\boldsymbol{u}
$$

Hence

$$
\bar A=P^{-1}AP\qquad \bar B=P^{-1}B\qquad \bar C=CP\qquad \bar D=D
$$

Because $P$ is nonsingular, $\boldsymbol{x}$ and $\boldsymbol{z}$ are in one-to-one correspondence and either set may be used as state variables.

##### Similarity and Eigenvalue Invariance

The matrices $A$ and $\bar A=P^{-1}AP$ are **similar**. Their characteristic polynomials are identical because

$$
\det(\lambda I-\bar A)=\det\left(P^{-1}(\lambda I-A)P\right)=\det(\lambda I-A)
$$

Therefore similar state matrices have the same eigenvalues, including algebraic multiplicities. Thus the eigenvalues of the state matrix are invariant under a nonsingular state transformation.

### Diagonalization

##### Diagonal Canonical Form

Suppose $A\in\mathbb{C}^{n\times n}$ has distinct eigenvalues $\lambda_1,\ldots,\lambda_n$ with associated eigenvectors $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_n$. The eigenvectors are linearly independent, so

$$
P=\begin{bmatrix}\boldsymbol{v}_1&\boldsymbol{v}_2&\cdots&\boldsymbol{v}_n\end{bmatrix}
$$

is nonsingular. Since $AP=P\Lambda$, where $\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\ldots,\lambda_n)$,

$$
P^{-1}AP=\Lambda
$$

With $\boldsymbol{x}=P\boldsymbol{z}$,

$$
\dot{\boldsymbol{z}}=\Lambda\boldsymbol{z}+P^{-1}B\boldsymbol{u}
$$

so the scalar state equations are uncoupled. If $\bar{\boldsymbol{b}}_i^T$ is the $i$th row of $P^{-1}B$, then $\dot z_i=\lambda_i z_i+\bar{\boldsymbol{b}}_i^T\boldsymbol{u}$.

A repeated eigenvalue does not by itself prevent diagonalization; diagonalization is possible whenever $A$ has $n$ linearly independent eigenvectors.

##### Companion Matrix and Vandermonde Matrix

For

$$
p(s)=s^n+a_1s^{n-1}+a_2s^{n-2}+\cdots+a_{n-1}s+a_n
$$

the companion state matrix used in controllable canonical form is

$$
A_c=\begin{bmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_n&-a_{n-1}&-a_{n-2}&\cdots&-a_1
\end{bmatrix}
$$

with $\det(sI-A_c)=p(s)$. If $\lambda_i$ is an eigenvalue, an associated eigenvector is

$$
\boldsymbol{v}_i=\begin{bmatrix}1&\lambda_i&\lambda_i^2&\cdots&\lambda_i^{n-1}\end{bmatrix}^{T}
$$

For distinct eigenvalues $\lambda_1,\ldots,\lambda_n$, the transformation matrix is the Vandermonde matrix

$$
P=\begin{bmatrix}\boldsymbol{v}_1&\boldsymbol{v}_2&\cdots&\boldsymbol{v}_n\end{bmatrix}
=\begin{bmatrix}
1&1&\cdots&1\\
\lambda_1&\lambda_2&\cdots&\lambda_n\\
\lambda_1^2&\lambda_2^2&\cdots&\lambda_n^2\\
\vdots&\vdots&\ddots&\vdots\\
\lambda_1^{n-1}&\lambda_2^{n-1}&\cdots&\lambda_n^{n-1}
\end{bmatrix}
$$

**Proof.** Since $p(\lambda_i)=0$,

$$
\lambda_i^n+a_1\lambda_i^{n-1}+a_2\lambda_i^{n-2}+\cdots+a_{n-1}\lambda_i+a_n=0
$$

and therefore

$$
\begin{aligned}
A_c\boldsymbol{v}_i
&=\begin{bmatrix}
\lambda_i\\
\lambda_i^2\\
\vdots\\
\lambda_i^{n-1}\\
-a_n-a_{n-1}\lambda_i-\cdots-a_2\lambda_i^{n-2}-a_1\lambda_i^{n-1}
\end{bmatrix}\\
&=\begin{bmatrix}\lambda_i&\lambda_i^2&\cdots&\lambda_i^{n-1}&\lambda_i^n\end{bmatrix}^{T}
=\lambda_i\boldsymbol{v}_i
\end{aligned}
$$

so $\boldsymbol{v}_i$ is an eigenvector associated with $\lambda_i$.

**eg.** Consider

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+Bu
$$

with

$$
A=\begin{bmatrix}2&-1&-1\\0&-1&0\\0&2&1\end{bmatrix}\qquad B=\begin{bmatrix}7\\2\\3\end{bmatrix}
$$

The eigenvalues are $\lambda_1=2$, $\lambda_2=1$, and $\lambda_3=-1$. Choose

$$
\boldsymbol{v}_1=\begin{bmatrix}1\\0\\0\end{bmatrix}\qquad
\boldsymbol{v}_2=\begin{bmatrix}1\\0\\1\end{bmatrix}\qquad
\boldsymbol{v}_3=\begin{bmatrix}0\\-1\\1\end{bmatrix}
$$

Then

$$
P=\begin{bmatrix}\boldsymbol{v}_1&\boldsymbol{v}_2&\boldsymbol{v}_3\end{bmatrix}
=\begin{bmatrix}1&1&0\\0&0&-1\\0&1&1\end{bmatrix}
$$

$$
P^{-1}AP=\begin{bmatrix}2&0&0\\0&1&0\\0&0&-1\end{bmatrix}
\qquad
P^{-1}B=\begin{bmatrix}2\\5\\-2\end{bmatrix}
$$

With $\boldsymbol{x}=P\boldsymbol{z}$,

$$
\dot{\boldsymbol{z}}=
\begin{bmatrix}2&0&0\\0&1&0\\0&0&-1\end{bmatrix}\boldsymbol{z}
+\begin{bmatrix}2\\5\\-2\end{bmatrix}u
$$

### Jordan Form

##### Algebraic and Geometric Multiplicity

For an eigenvalue $\lambda$ of $A$, the **geometric multiplicity** is the dimension of its **eigenspace**
$$
E_\lambda=\ker(A-\lambda I)=\{\boldsymbol{v}\mid(A-\lambda I)\boldsymbol{v}=\boldsymbol{0}\}
$$
It is found by solving $(A-\lambda I)\boldsymbol{v}=\boldsymbol{0}$ and counting the number of linearly independent eigenvectors associated with $\lambda$
$$
g_\lambda=\dim\ker(A-\lambda I)=n-\operatorname{rank}(A-\lambda I)
$$

The **algebraic multiplicity** is the multiplicity of $\lambda$ as a root of the characteristic polynomial. Compute and factor the characteristic polynomial as

$$
p_A(\mu)=\det(\mu I-A)=(\mu-\lambda)^{a_\lambda}q(\mu)\qquad q(\lambda)\neq 0
$$

Then $a_\lambda$ is the algebraic multiplicity of $\lambda$. For every eigenvalue

$$
1\leq g_\lambda\leq a_\lambda
$$

The matrix $A$ is diagonalizable if and only if $g_\lambda=a_\lambda$ for every eigenvalue.

##### Generalized Eigenvectors

If the eigenvectors of $A$ do not form a basis, generalized eigenvectors are used. A nonzero vector $\boldsymbol{v}$ is a **generalized eigenvector** associated with an eigenvalue $\lambda$ if

$$
(A-\lambda I)^k\boldsymbol{v}=\boldsymbol{0}\qquad (A-\lambda I)^{k-1}\boldsymbol{v}\neq\boldsymbol{0}
$$

for some positive integer $k$. The smallest such $k$ is the **grade** of $\boldsymbol{v}$. An ordinary eigenvector is therefore a generalized eigenvector of grade one.

A sequence $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_r$ is a **Jordan chain** associated with $\lambda$ if

$$
(A-\lambda I)\boldsymbol{v}_1=\boldsymbol{0}\qquad
(A-\lambda I)\boldsymbol{v}_j=\boldsymbol{v}_{j-1}
\qquad j=2,\ldots,r
$$

Thus $\boldsymbol{v}_1$ is an eigenvector and $\boldsymbol{v}_j$ is a generalized eigenvector of grade $j$. Equivalently,

$$
A\boldsymbol{v}_1=\lambda\boldsymbol{v}_1\qquad
A\boldsymbol{v}_j=\boldsymbol{v}_{j-1}+\lambda\boldsymbol{v}_j
\qquad j=2,\ldots,r
$$

The vectors in a Jordan chain are linearly independent.

##### Jordan Canonical Form

Let $A\in\mathbb{C}^{n\times n}$ have distinct eigenvalues $\lambda_1,\ldots,\lambda_q$. For $\lambda_i$, denote its algebraic and geometric multiplicities by $a_i=a_{\lambda_i}$ and $g_i=g_{\lambda_i}$, respectively, with $\sum_{i=1}^{q}a_i=n$.

A basis of generalized eigenvectors can be arranged into Jordan chains. If $S$ is the nonsingular matrix formed from these basis vectors, then

$$
AS=SJ
\qquad
J=S^{-1}AS=\operatorname{diag}(J_1,J_2,\ldots,J_q)
$$

The matrix $J$ is the **Jordan canonical form** of $A$, where $J_i$ contains all Jordan blocks associated with $\lambda_i$:

$$
J_i=\operatorname{diag}\left(J_{r_{i1}}(\lambda_i),J_{r_{i2}}(\lambda_i),\ldots,J_{r_{ig_i}}(\lambda_i)\right)
$$

Each **Jordan block** has the form

$$
J_r(\lambda)=
\begin{bmatrix}
\lambda&1&0&\cdots&0\\
0&\lambda&1&\cdots&0\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
0&0&\cdots&\lambda&1\\
0&0&\cdots&0&\lambda
\end{bmatrix}
$$

For each eigenvalue $\lambda_i$,

$$
g_i=\text{number of Jordan blocks associated with }\lambda_i
\qquad
\sum_{j=1}^{g_i}r_{ij}=a_i
$$

Thus $J_i\in\mathbb{C}^{a_i\times a_i}$, and the total number of Jordan blocks is $\sum_{i=1}^{q}g_i$. Each block corresponds to one Jordan chain, and its size equals the length of that chain. For a chain $\boldsymbol{v}_1,\ldots,\boldsymbol{v}_r$,

$$
S_r=\begin{bmatrix}\boldsymbol{v}_1&\boldsymbol{v}_2&\cdots&\boldsymbol{v}_r\end{bmatrix}
\qquad
AS_r=S_rJ_r(\lambda)
$$

For the state equation $\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}$, the transformation $\boldsymbol{x}=S\boldsymbol{z}$ gives

$$
\dot{\boldsymbol{z}}=J\boldsymbol{z}+\bar B\boldsymbol{u}
\qquad
\bar B=S^{-1}B
$$

Different Jordan blocks are decoupled. Within a block $J_r(\lambda)$,

$$
\dot z_1=\lambda z_1+z_2\qquad
\dot z_2=\lambda z_2+z_3\qquad
\cdots\qquad
\dot z_r=\lambda z_r
$$

so coupling remains only within a Jordan block of size greater than one. The matrix $A$ is diagonalizable if and only if every Jordan block has size one, equivalently $g_i=a_i$ for every eigenvalue.

### Transfer Matrices and Interconnected Systems

##### Transfer Matrix from a State-Space Model

For a linear time-invariant system with zero initial conditions, the **transfer matrix** $G(s)$ is defined by

$$
\boldsymbol{Y}(s)=G(s)\boldsymbol{U}(s)
$$

where $G(s)\in\mathbb{C}^{m\times r}$. Its $(i,j)$ entry is the transfer function from the $j$th input to the $i$th output with all other inputs set to zero.

For

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}\qquad
\boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}
$$

the Laplace transform with $\boldsymbol{x}(0)=\boldsymbol{0}$ gives

$$
s\boldsymbol{X}(s)=A\boldsymbol{X}(s)+B\boldsymbol{U}(s)
$$

$$
\boldsymbol{X}(s)=(sI-A)^{-1}B\boldsymbol{U}(s)
$$

$$
\boldsymbol{Y}(s)=C\boldsymbol{X}(s)+D\boldsymbol{U}(s)
=\left[C(sI-A)^{-1}B+D\right]\boldsymbol{U}(s)
$$

Therefore

$$
G(s)=C(sI-A)^{-1}B+D
$$

Since

$$
(sI-A)^{-1}
=\frac{1}{s}\left(I-\frac{A}{s}\right)^{-1}
=\frac{1}{s}I+\frac{1}{s^2}A+O\left(\frac{1}{s^3}\right)
$$

we have

$$
G(s)=D+\frac{1}{s}CB+\frac{1}{s^2}CAB+O\left(\frac{1}{s^3}\right)
$$

Thus $G(s)$ is a **proper rational matrix**. If $D=0$, $G(s)$ is **strictly proper**; if $D\neq 0$, it is proper but not strictly proper. In particular,

$$
\lim_{s\to\infty}G(s)=D
$$

A given zero-initial-condition input-output relation has a unique transfer matrix although its state-space representation is not unique. In particular, under the nonsingular state transformation

$$
\bar A=P^{-1}AP\qquad
\bar B=P^{-1}B\qquad
\bar C=CP\qquad
\bar D=D
$$

the transformed representation has

$$
\begin{aligned}
\bar G(s)
&=\bar C(sI-\bar A)^{-1}\bar B+\bar D\\
&=CP\left[P^{-1}(sI-A)P\right]^{-1}P^{-1}B+D\\
&=C(sI-A)^{-1}B+D\\
&=G(s)
\end{aligned}
$$

##### State-Space Models of Interconnected Systems

Consider two subsystems

$$
\begin{aligned}
\Sigma_1:\quad
\dot{\boldsymbol{x}}_1&=A_1\boldsymbol{x}_1+B_1\boldsymbol{u}_1&
\boldsymbol{y}_1&=C_1\boldsymbol{x}_1+D_1\boldsymbol{u}_1\\
\Sigma_2:\quad
\dot{\boldsymbol{x}}_2&=A_2\boldsymbol{x}_2+B_2\boldsymbol{u}_2&
\boldsymbol{y}_2&=C_2\boldsymbol{x}_2+D_2\boldsymbol{u}_2
\end{aligned}
$$

where $\boldsymbol{u}_i\in\mathbb{R}^{r_i}$ and $\boldsymbol{y}_i\in\mathbb{R}^{m_i}$, with transfer matrices

$$
G_i(s)=C_i(sI-A_i)^{-1}B_i+D_i
$$

For an interconnection, first check that each connected output and input have the same dimension, write the input-output signal relations, and then collect the states as

$$
\boldsymbol{x}=
\begin{bmatrix}
\boldsymbol{x}_1\\
\boldsymbol{x}_2
\end{bmatrix}
$$

**Parallel connection.** Let

$$
\boldsymbol{u}_1=\boldsymbol{u}_2=\boldsymbol{u}\qquad
\boldsymbol{y}=\boldsymbol{y}_1+\boldsymbol{y}_2
$$

which requires

$$
r_1=r_2\qquad m_1=m_2
$$

Then

$$
\dot{\boldsymbol{x}}
=
\begin{bmatrix}
A_1&0\\
0&A_2
\end{bmatrix}
\boldsymbol{x}
+
\begin{bmatrix}
B_1\\
B_2
\end{bmatrix}
\boldsymbol{u}
$$

$$
\boldsymbol{y}
=
\begin{bmatrix}
C_1&C_2
\end{bmatrix}
\boldsymbol{x}
+
(D_1+D_2)\boldsymbol{u}
$$

and

$$
G(s)=G_1(s)+G_2(s)
$$

**Series connection.** Let $\Sigma_1$ be followed by $\Sigma_2$

$$
\boldsymbol{u}_1=\boldsymbol{u}\qquad
\boldsymbol{u}_2=\boldsymbol{y}_1\qquad
\boldsymbol{y}=\boldsymbol{y}_2
$$

which requires

$$
m_1=r_2
$$

Then

$$
\dot{\boldsymbol{x}}
=
\begin{bmatrix}
A_1&0\\
B_2C_1&A_2
\end{bmatrix}
\boldsymbol{x}
+
\begin{bmatrix}
B_1\\
B_2D_1
\end{bmatrix}
\boldsymbol{u}
$$

$$
\boldsymbol{y}
=
\begin{bmatrix}
D_2C_1&C_2
\end{bmatrix}
\boldsymbol{x}
+
D_2D_1\boldsymbol{u}
$$

and

$$
G(s)=G_2(s)G_1(s)
$$

**Negative-feedback connection.** Let $\Sigma_1$ be the forward subsystem and $\Sigma_2$ the feedback subsystem

$$
\boldsymbol{u}_1=\boldsymbol{u}-\boldsymbol{y}_2\qquad
\boldsymbol{u}_2=\boldsymbol{y}_1\qquad
\boldsymbol{y}=\boldsymbol{y}_1
$$

which requires

$$
m_1=r_2\qquad m_2=r_1
$$

When direct-transmission terms are present, the feedback interconnection is well-posed if $I+D_2D_1$, equivalently $I+D_1D_2$, is nonsingular. Define

$$
E=(I+D_2D_1)^{-1}\qquad
F=(I+D_1D_2)^{-1}
$$

Then

$$
\dot{\boldsymbol{x}}
=
\begin{bmatrix}
A_1-B_1ED_2C_1&-B_1EC_2\\
B_2FC_1&A_2-B_2FD_1C_2
\end{bmatrix}
\boldsymbol{x}
+
\begin{bmatrix}
B_1E\\
B_2FD_1
\end{bmatrix}
\boldsymbol{u}
$$

$$
\boldsymbol{y}
=
\begin{bmatrix}
FC_1&-FD_1C_2
\end{bmatrix}
\boldsymbol{x}
+
FD_1\boldsymbol{u}
$$

and

$$
G(s)
=
\left[I+G_1(s)G_2(s)\right]^{-1}G_1(s)
=
G_1(s)\left[I+G_2(s)G_1(s)\right]^{-1}
$$

For MIMO systems the order of the transfer-matrix products must be preserved.

### Discrete-Time, Time-Varying, and Nonlinear State-Space Models

##### Discrete-Time State-Space Models

A discrete-time linear time-invariant system is represented by the first-order difference equations

$$
\boldsymbol{x}[k+1]=A\boldsymbol{x}[k]+B\boldsymbol{u}[k]\qquad
\boldsymbol{y}[k]=C\boldsymbol{x}[k]+D\boldsymbol{u}[k]
$$

##### Time-Varying State-Space Models

A continuous-time linear time-varying system has the form

$$
\dot{\boldsymbol{x}}(t)=A(t)\boldsymbol{x}(t)+B(t)\boldsymbol{u}(t)\qquad
\boldsymbol{y}(t)=C(t)\boldsymbol{x}(t)+D(t)\boldsymbol{u}(t)
$$

##### Nonlinear State-Space Models

A nonlinear time-varying system has the form

$$
\dot{\boldsymbol{x}}=\boldsymbol{f}(\boldsymbol{x},\boldsymbol{u},t)\qquad
\boldsymbol{y}=\boldsymbol{g}(\boldsymbol{x},\boldsymbol{u},t)
$$

A nonlinear time-invariant system has the form

$$
\dot{\boldsymbol{x}}=\boldsymbol{f}(\boldsymbol{x},\boldsymbol{u})\qquad
\boldsymbol{y}=\boldsymbol{g}(\boldsymbol{x},\boldsymbol{u})
$$

For the time-invariant system, let $(\boldsymbol{x}_0,\boldsymbol{u}_0)$ be an equilibrium operating point

$$
\boldsymbol{f}(\boldsymbol{x}_0,\boldsymbol{u}_0)=\boldsymbol{0}\qquad
\boldsymbol{y}_0=\boldsymbol{g}(\boldsymbol{x}_0,\boldsymbol{u}_0)
$$

Define the deviations

$$
\delta\boldsymbol{x}=\boldsymbol{x}-\boldsymbol{x}_0\qquad
\delta\boldsymbol{u}=\boldsymbol{u}-\boldsymbol{u}_0\qquad
\delta\boldsymbol{y}=\boldsymbol{y}-\boldsymbol{y}_0
$$

Retaining only the first-order terms of the Taylor expansion gives

$$
\delta\dot{\boldsymbol{x}}=A\delta\boldsymbol{x}+B\delta\boldsymbol{u}\qquad
\delta\boldsymbol{y}=C\delta\boldsymbol{x}+D\delta\boldsymbol{u}
$$

where
$$
A=\left.\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{x}}\right|_{(\boldsymbol{x}_0,\boldsymbol{u}_0)}
\qquad
B=\left.\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{u}}\right|_{(\boldsymbol{x}_0,\boldsymbol{u}_0)}
\qquad
C=\left.\frac{\partial\boldsymbol{g}}{\partial\boldsymbol{x}}\right|_{(\boldsymbol{x}_0,\boldsymbol{u}_0)}
\qquad
D=\left.\frac{\partial\boldsymbol{g}}{\partial\boldsymbol{u}}\right|_{(\boldsymbol{x}_0,\boldsymbol{u}_0)}
$$
