# Controllability and Observability

[toc]

### Controllability of Linear Time-Invariant Systems

##### State Controllability

Consider the continuous-time linear time-invariant system

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}
$$

The system is **state controllable at time $t_0$** if it is possible to construct an unconstrained control vector $\boldsymbol{u}(t)$ that transfers an initial state $\boldsymbol{x}(t_0)$ to any final state $\boldsymbol{x}(t_1)$ in a finite time interval $t_0\leq t\leq t_1$. 

If every state is controllable, the system is **completely state controllable**. Otherwise, the system is **not completely state controllable**.

##### Controllability Gramian

Without loss of generality, let $t_0=0$. Define the **controllability Gramian**

$$
W_c[0,t_1]=\int_0^{t_1}e^{-At}BB^Te^{-A^Tt}dt
$$

The system is completely state controllable if and only if $W_c[0,t_1]$ is nonsingular for a finite $t_1>0$.

**Proof. Sufficiency.** Suppose $W_c[0,t_1]$ is nonsingular. For arbitrary initial and final states $\boldsymbol{x}_0$ and $\boldsymbol{x}_f$, the state equation gives

$$
\boldsymbol{x}(t_1)=e^{At_1}\boldsymbol{x}_0+\int_0^{t_1}e^{A(t_1-t)}B\boldsymbol{u}(t)dt
$$

Multiplying by $e^{-At_1}$,

$$
e^{-At_1}\boldsymbol{x}(t_1)-\boldsymbol{x}_0=\int_0^{t_1}e^{-At}B\boldsymbol{u}(t)dt
$$

Let $\boldsymbol{q}=e^{-At_1}\boldsymbol{x}_f-\boldsymbol{x}_0$ and choose

$$
\boldsymbol{u}(t)=B^Te^{-A^Tt}W_c^{-1}[0,t_1]\boldsymbol{q}
$$

Then

$$
\begin{aligned}
e^{-At_1}\boldsymbol{x}(t_1)-\boldsymbol{x}_0
&=\int_0^{t_1}e^{-At}BB^Te^{-A^Tt}W_c^{-1}[0,t_1]\boldsymbol{q}\,dt=W_c[0,t_1]W_c^{-1}[0,t_1]\boldsymbol{q}\\
&=\boldsymbol{q}=e^{-At_1}\boldsymbol{x}_f-\boldsymbol{x}_0
\end{aligned}
$$

Hence $\boldsymbol{x}(t_1)=\boldsymbol{x}_f$. Since $\boldsymbol{x}_0$ and $\boldsymbol{x}_f$ are arbitrary, the system is completely state controllable.

**Necessity.** Suppose $W_c[0,t_1]$ is singular. Since $W_c[0,t_1]$ is symmetric and positive semidefinite, there exists a nonzero vector $\boldsymbol{v}$ such that

$$
\begin{aligned}
0
=\boldsymbol{v}^TW_c[0,t_1]\boldsymbol{v}
=\int_0^{t_1}\boldsymbol{v}^Te^{-At}BB^Te^{-A^Tt}\boldsymbol{v}\,dt
=\int_0^{t_1}\left\|B^Te^{-A^Tt}\boldsymbol{v}\right\|^2dt
\end{aligned}
$$

The integrand is continuous and nonnegative, so $B^Te^{-A^Tt}\boldsymbol{v}=\boldsymbol{0}$ for every $t\in[0,t_1]$, equivalently $\boldsymbol{v}^Te^{-At}B=\boldsymbol{0}^T$. Therefore, for every admissible input,

$$
\boldsymbol{v}^T\int_0^{t_1}e^{-At}B\boldsymbol{u}(t)dt=0
$$

Taking $\boldsymbol{x}_0=\boldsymbol{0}$ and $\boldsymbol{x}_f=e^{At_1}\boldsymbol{v}$ would require

$$
\int_0^{t_1}e^{-At}B\boldsymbol{u}(t)dt=e^{-At_1}\boldsymbol{x}_f=\boldsymbol{v}
$$

but left multiplication by $\boldsymbol{v}^T$ gives $0=\boldsymbol{v}^T\boldsymbol{v}$, a contradiction. Hence the system is not completely state controllable.

##### Controllability Matrix

Define the **controllability matrix**

$$
\mathcal{C}=\begin{bmatrix}B&AB&A^2B&\cdots&A^{n-1}B\end{bmatrix}
$$

The system is completely state controllable if and only if

$$
\operatorname{rank}\mathcal{C}=n
$$

**Proof.** First suppose $\operatorname{rank}\mathcal{C}<n$. Then there exists a nonzero vector $\boldsymbol{v}$ such that $\boldsymbol{v}^T\mathcal{C}=\boldsymbol{0}^T$, so

$$
\boldsymbol{v}^TB=\boldsymbol{0}^T\qquad
\boldsymbol{v}^TAB=\boldsymbol{0}^T\qquad\cdots\qquad
\boldsymbol{v}^TA^{n-1}B=\boldsymbol{0}^T
$$

By the Cayley-Hamilton theorem, every $A^k$ with $k\geq n$ is a linear combination of $I,A,\ldots,A^{n-1}$, hence $\boldsymbol{v}^TA^kB=\boldsymbol{0}^T$ for every $k\geq0$. Therefore

$$
\boldsymbol{v}^Te^{-At}B
=\boldsymbol{v}^T\left(I-At+\frac{A^2t^2}{2!}-\cdots\right)B
=\boldsymbol{0}^T
$$

and thus $\boldsymbol{v}^TW_c[0,t_1]\boldsymbol{v}=0$. Hence $W_c[0,t_1]$ is singular and the system is not completely state controllable.

Conversely, suppose $W_c[0,t_1]$ is singular. From the preceding proof, there exists $\boldsymbol{v}\neq\boldsymbol{0}$ such that $\boldsymbol{v}^Te^{-At}B=\boldsymbol{0}^T$ for all $t\in[0,t_1]$. Differentiating at $t=0$ gives

$$
\left.\frac{d^k}{dt^k}\left(\boldsymbol{v}^Te^{-At}B\right)\right|_{t=0}
=(-1)^k\boldsymbol{v}^TA^kB
=\boldsymbol{0}^T
\qquad k=0,1,\ldots,n-1
$$

so $\boldsymbol{v}^T\mathcal{C}=\boldsymbol{0}^T$ and $\operatorname{rank}\mathcal{C}<n$. Therefore $W_c[0,t_1]$ is nonsingular if and only if $\operatorname{rank}\mathcal{C}=n$.

**eg.** Consider

$$
\dot{\boldsymbol{x}}=
\begin{bmatrix}
-1&-4&-2\\
0&6&1\\
1&7&-1
\end{bmatrix}\boldsymbol{x}
+
\begin{bmatrix}2\\0\\1\end{bmatrix}u
$$

Then

$$
AB=\begin{bmatrix}-4\\1\\1\end{bmatrix}
\qquad
A^2B=\begin{bmatrix}-2\\7\\2\end{bmatrix}
\qquad
\mathcal{C}=\begin{bmatrix}
2&-4&-2\\
0&1&7\\
1&1&2
\end{bmatrix}
$$

Since $\det\mathcal{C}=-36\neq0$, $\operatorname{rank}\mathcal{C}=3$. The system is completely state controllable.

##### PBH Controllability Test

The system is completely state controllable if and only if

$$
\operatorname{rank}\begin{bmatrix}\lambda_iI-A&B\end{bmatrix}=n
$$

for every eigenvalue $\lambda_i$ of $A$.

**Proof.** Suppose the rank condition fails for an eigenvalue $\lambda$. Then there exists a nonzero row vector $\boldsymbol{v}^T$ such that

$$
\boldsymbol{v}^T(\lambda I-A)=\boldsymbol{0}^T
\qquad
\boldsymbol{v}^TB=\boldsymbol{0}^T
$$

Thus $\boldsymbol{v}^TA=\lambda\boldsymbol{v}^T$, and recursively $\boldsymbol{v}^TA^k=\lambda^k\boldsymbol{v}^T$. Hence

$$
\boldsymbol{v}^TA^kB=\lambda^k\boldsymbol{v}^TB=\boldsymbol{0}^T
\qquad k=0,1,\ldots,n-1
$$

so $\boldsymbol{v}^T\mathcal{C}=\boldsymbol{0}^T$ and $\operatorname{rank}\mathcal{C}<n$.

Conversely, suppose $\operatorname{rank}\mathcal{C}<n$ and define

$$
\mathcal{N}=\left\{\boldsymbol{v}^T:\boldsymbol{v}^TA^kB=\boldsymbol{0}^T,\ k=0,1,\ldots,n-1\right\}
$$

Then $\mathcal{N}$ contains a nonzero vector. For $\boldsymbol{v}^T\in\mathcal{N}$, the Cayley-Hamilton theorem gives $\boldsymbol{v}^TA^nB=\boldsymbol{0}^T$, so

$$
(\boldsymbol{v}^TA)A^kB=\boldsymbol{v}^TA^{k+1}B=\boldsymbol{0}^T
\qquad k=0,1,\ldots,n-1
$$

where the case $k=n-1$ follows from $\boldsymbol{v}^TA^nB=\boldsymbol{0}^T$. Thus $\mathcal{N}$ is invariant under the linear map $\boldsymbol{v}^T\mapsto\boldsymbol{v}^TA$. Over the complex field, this map has a nonzero eigenvector $\boldsymbol{w}^T\in\mathcal{N}$, so for some eigenvalue $\lambda$ of $A$,

$$
\boldsymbol{w}^TA=\lambda\boldsymbol{w}^T
\qquad
\boldsymbol{w}^TB=\boldsymbol{0}^T
$$

Therefore $\boldsymbol{w}^T\begin{bmatrix}\lambda I-A&B\end{bmatrix}=\boldsymbol{0}^T$ and $\operatorname{rank}\begin{bmatrix}\lambda I-A&B\end{bmatrix}<n$. Hence the PBH controllability test is equivalent to $\operatorname{rank}\mathcal{C}=n$.

**eg.** Consider

$$
\dot{\boldsymbol{x}}=
\begin{bmatrix}
-7&0&0\\
0&-5&0\\
0&0&-1
\end{bmatrix}\boldsymbol{x}
+
\begin{bmatrix}2\\0\\9\end{bmatrix}u
$$

The eigenvalues are $-7,-5,-1$. The corresponding rank matrices are

$$
\left[-7I-A\ \ B\right]=
\begin{bmatrix}
0&0&0&2\\
0&-2&0&0\\
0&0&-6&9
\end{bmatrix}
\qquad
\left[-5I-A\ \ B\right]=
\begin{bmatrix}
2&0&0&2\\
0&0&0&0\\
0&0&-4&9
\end{bmatrix}
$$

$$
\left[-I-A\ \ B\right]=
\begin{bmatrix}
6&0&0&2\\
0&4&0&0\\
0&0&0&9
\end{bmatrix}
$$

Their ranks are $3,2,3$, respectively. Since the corresponding matrix has rank $2<3$ at $\lambda=-5$, the system is not completely state controllable.

##### Alternative Form of the Condition for Complete State Controllability

**Diagonal canonical form.** Suppose $A$ has $n$ distinct eigenvalues and $P^{-1}AP=\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$. With $\boldsymbol{x}=P\boldsymbol{z}$ and $\bar B=P^{-1}B$,

$$
\dot{\boldsymbol{z}}=\Lambda\boldsymbol{z}+\bar B\boldsymbol{u}
$$

The system is completely state controllable if and only if no row of $\bar B$ consists entirely of zeros.

**Proof.** Let $\bar B_i$ denote the $i$th row of $\bar B$. Since controllability is unchanged by a nonsingular state transformation,
$$
\operatorname{rank}\mathcal{C}
=\operatorname{rank}\begin{bmatrix}\bar B&\Lambda\bar B&\cdots&\Lambda^{n-1}\bar B\end{bmatrix}
$$

whose $i$th row is

$$
\begin{bmatrix}\bar B_i&\lambda_i\bar B_i&\cdots&\lambda_i^{n-1}\bar B_i\end{bmatrix}
$$

If $\bar B_i=\boldsymbol{0}^T$ for some $i$, the corresponding row of the controllability matrix is zero and its rank is less than $n$.

Conversely, suppose every $\bar B_i\neq\boldsymbol{0}^T$ but the controllability matrix has rank less than $n$. Then there exists a nonzero vector $\boldsymbol{q}=\begin{bmatrix}q_1&\cdots&q_n\end{bmatrix}^T$ such that

$$
\sum_{i=1}^n q_i\lambda_i^k\bar B_i=\boldsymbol{0}^T
\qquad k=0,1,\ldots,n-1
$$

For each input column $j$, these equations give

$$
\begin{bmatrix}
1&1&\cdots&1\\
\lambda_1&\lambda_2&\cdots&\lambda_n\\
\vdots&\vdots&\ddots&\vdots\\
\lambda_1^{n-1}&\lambda_2^{n-1}&\cdots&\lambda_n^{n-1}
\end{bmatrix}
\begin{bmatrix}
q_1\bar b_{1j}\\
q_2\bar b_{2j}\\
\vdots\\
q_n\bar b_{nj}
\end{bmatrix}
=\boldsymbol{0}
$$

The Vandermonde matrix is nonsingular because the eigenvalues are distinct, so $q_i\bar b_{ij}=0$ for every $i,j$. Since each row $\bar B_i$ contains a nonzero element, $q_i=0$ for every $i$, contradicting $\boldsymbol{q}\neq\boldsymbol{0}$. Hence the controllability matrix has rank $n$.

**Jordan canonical form.** Let $S^{-1}AS=J$ and $\bar B=S^{-1}B$. For an eigenvalue $\lambda_i$, let its algebraic multiplicity be $a_i$, its geometric multiplicity be $g_i$, and let its $g_i$ Jordan blocks have orders $r_{i1},\ldots,r_{ig_i}$. The system is completely state controllable if and only if, for every $\lambda_i$:

- if $a_i=1$, the corresponding row of $\bar B$ is nonzero
- if $a_i>1$ and $g_i=1$, the row of $\bar B$ corresponding to the last row of the Jordan block is nonzero
- if $g_i>1$, the rows of $\bar B$ corresponding to the last row of the Jordan blocks associated with $\lambda_i$ are linearly independent

Equivalently, if $\bar B_{ik}^{(r_{ik})}$ denotes the last row of $\bar B$ corresponding to the $k$th Jordan block of $\lambda_i$,

$$
\operatorname{rank}
\begin{bmatrix}
\bar B_{i1}^{(r_{i1})}\\
\bar B_{i2}^{(r_{i2})}\\
\vdots\\
\bar B_{ig_i}^{(r_{ig_i})}
\end{bmatrix}
=g_i
$$

For a scalar input, this requires $g_i=1$ for every eigenvalue and a nonzero input entry at the last row of every Jordan block.

**eg.** Let $A\in\mathbb{R}^{7\times7}$ be in Jordan canonical form with a simple eigenvalue $\lambda_1$, one Jordan block $J_2(\lambda_2)$ associated with the double eigenvalue $\lambda_2$, and two Jordan blocks $J_2(\lambda_3)$ associated with the quadruple eigenvalue $\lambda_3$:

$$
A=
\begin{bmatrix}
\lambda_1&0&0&0&0&0&0\\
0&\lambda_2&1&0&0&0&0\\
0&0&\lambda_2&0&0&0&0\\
0&0&0&\lambda_3&1&0&0\\
0&0&0&0&\lambda_3&0&0\\
0&0&0&0&0&\lambda_3&1\\
0&0&0&0&0&0&\lambda_3
\end{bmatrix}
\qquad
B=
\begin{bmatrix}
\boldsymbol{b}_1\\
\boldsymbol{b}_2\\
\boldsymbol{b}_3\\
\boldsymbol{b}_4\\
\boldsymbol{b}_5\\
\boldsymbol{b}_6\\
\boldsymbol{b}_7
\end{bmatrix}
$$

where each $\boldsymbol{b}_j$ is a row vector of the input matrix.

For $\lambda=\lambda_1$, all blocks of $\lambda_1I-A$ except the first $1\times1$ block are nonsingular. The first row has no pivot in $\lambda_1I-A$, so

$$
\operatorname{rank}\begin{bmatrix}\lambda_1I-A&B\end{bmatrix}=7
\quad\Longleftrightarrow\quad
\boldsymbol{b}_1\neq\boldsymbol{0}^T
$$

For $\lambda=\lambda_2$, the $\lambda_2$ Jordan block contributes

$$
\lambda_2I-J_2(\lambda_2)=
\begin{bmatrix}0&-1\\0&0\end{bmatrix}
$$

so its first row has a state-space pivot while its last row must be completed by $\boldsymbol{b}_3$. Hence

$$
\operatorname{rank}\begin{bmatrix}\lambda_2I-A&B\end{bmatrix}=7
\quad\Longleftrightarrow\quad
\boldsymbol{b}_3\neq\boldsymbol{0}^T
$$

For $\lambda=\lambda_3$, each of the two Jordan blocks contributes one state-space pivot. The rows corresponding to the last rows of those blocks have zero state-space parts after elimination, so

$$
\operatorname{rank}\begin{bmatrix}\lambda_3I-A&B\end{bmatrix}
=5+
\operatorname{rank}
\begin{bmatrix}
\boldsymbol{b}_5\\
\boldsymbol{b}_7
\end{bmatrix}
$$

Thus

$$
\operatorname{rank}\begin{bmatrix}\lambda_3I-A&B\end{bmatrix}=7
\quad\Longleftrightarrow\quad
\operatorname{rank}
\begin{bmatrix}
\boldsymbol{b}_5\\
\boldsymbol{b}_7
\end{bmatrix}=2
$$

By the eigenvalue rank condition, the system is completely state controllable if and only if $\boldsymbol{b}_1\neq\boldsymbol{0}^T$, $\boldsymbol{b}_3\neq\boldsymbol{0}^T$, and $\begin{bmatrix}\boldsymbol{b}_5\\\boldsymbol{b}_7\end{bmatrix}$ has rank $2$. These are exactly the Jordan-form conditions for the three eigenvalues.

**eg.** Consider the Jordan-form system

$$
\dot{\boldsymbol{x}}=
\begin{bmatrix}
-2&1&0&0&0&0&0\\
0&-2&1&0&0&0&0\\
0&0&-2&0&0&0&0\\
0&0&0&-2&0&0&0\\
0&0&0&0&-3&1&0\\
0&0&0&0&0&-3&0\\
0&0&0&0&0&0&-3
\end{bmatrix}\boldsymbol{x}
+
\begin{bmatrix}
0&0&0\\
0&0&0\\
0&4&0\\
0&0&7\\
0&0&0\\
1&0&0\\
0&4&1
\end{bmatrix}\boldsymbol{u}
$$

For $\lambda=-2$, the Jordan blocks are $J_3(-2)$ and $J_1(-2)$, and their last-row input vectors are

$$
\begin{bmatrix}
0&4&0\\
0&0&7
\end{bmatrix}
$$

which has rank $2$. For $\lambda=-3$, the Jordan blocks are $J_2(-3)$ and $J_1(-3)$, and their last-row input vectors are

$$
\begin{bmatrix}
1&0&0\\
0&4&1
\end{bmatrix}
$$

which also has rank $2$. Therefore the system is completely state controllable.

### Observability of Linear Time-Invariant Systems

##### State Observability

Consider

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}
\qquad
\boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}
$$

The system is **observable at time $t_0$** if, with the system in state $\boldsymbol{x}(t_0)$, it is possible to determine this state from the observation of the output over a finite time interval. 

If every state $\boldsymbol{x}(t_0)$ can be determined from the output, the system is **completely observable**.

Since $A,B,C,D$ and the input are known, the forced part of the output is known and may be subtracted from the measured output. Thus observability is determined from the unforced system

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}
\qquad
\boldsymbol{y}=C\boldsymbol{x}
$$

A nonzero initial state $\boldsymbol{x}_0$ is **unobservable** if it cannot be distinguished from the zero state from the output over a finite interval; for the unforced system this is equivalent to $Ce^{A(t-t_0)}\boldsymbol{x}_0=\boldsymbol{0}$ throughout that interval.

##### Observability Gramian

Without loss of generality, let $t_0=0$. Define the **observability Gramian**

$$
W_o[0,t_1]=\int_0^{t_1}e^{A^Tt}C^TCe^{At}dt
=\int_0^{t_1}(Ce^{At})^T(Ce^{At})dt
$$

The system is completely observable if and only if $W_o[0,t_1]$ is nonsingular for a finite $t_1>0$.

**Proof. Sufficiency.** For the unforced system,

$$
\boldsymbol{y}(t)=Ce^{At}\boldsymbol{x}_0
$$

If $W_o[0,t_1]$ is nonsingular, then

$$
\begin{aligned}
\int_0^{t_1}e^{A^Tt}C^T\boldsymbol{y}(t)dt
=\int_0^{t_1}e^{A^Tt}C^TCe^{At}\boldsymbol{x}_0dt
=W_o[0,t_1]\boldsymbol{x}_0
\end{aligned}
$$

and therefore

$$
\boldsymbol{x}_0=W_o^{-1}[0,t_1]\int_0^{t_1}e^{A^Tt}C^T\boldsymbol{y}(t)dt
$$

Thus $\boldsymbol{x}_0$ is uniquely determined from the observed output and the system is completely observable.

**Necessity.** Suppose $W_o[0,t_1]$ is singular. Then there exists a nonzero vector $\boldsymbol{v}$ such that

$$
\begin{aligned}
0
=\boldsymbol{v}^TW_o[0,t_1]\boldsymbol{v}
=\int_0^{t_1}\boldsymbol{v}^Te^{A^Tt}C^TCe^{At}\boldsymbol{v}\,dt
=\int_0^{t_1}\left\|Ce^{At}\boldsymbol{v}\right\|^2dt
\end{aligned}
$$

Hence $Ce^{At}\boldsymbol{v}=\boldsymbol{0}$ for every $t\in[0,t_1]$. The nonzero initial state $\boldsymbol{v}$ and the zero state therefore produce the same output over the observation interval, so $\boldsymbol{v}$ cannot be uniquely determined and the system is not completely observable.

##### Observability Matrix

Define the **observability matrix**

$$
\mathcal{O}=
\begin{bmatrix}
C\\
CA\\
CA^2\\
\vdots\\
CA^{n-1}
\end{bmatrix}
$$

The system is completely observable if and only if

$$
\operatorname{rank}\mathcal{O}=n
$$

##### PBH Observability Test

The system is completely observable if and only if

$$
\operatorname{rank}
\begin{bmatrix}
\lambda_iI-A\\
C
\end{bmatrix}
=n
$$

for every eigenvalue $\lambda_i$ of $A$.

##### Alternative Form of the Condition for Complete Observability

If $A$ has $n$ distinct eigenvalues and $P^{-1}AP=\Lambda$, define $\bar C=CP$. The system is completely observable if and only if no column of $\bar C$ consists entirely of zeros.

If $S^{-1}AS=J$ is in Jordan canonical form and $\bar C=CS$, then for every eigenvalue $\lambda_i$:

- if $a_i=1$, the corresponding column of $\bar C$ is nonzero
- if $a_i>1$ and $g_i=1$, the column of $\bar C$ corresponding to the first state of the Jordan block is nonzero
- if $g_i>1$, the columns of $\bar C$ corresponding to the first state of the Jordan blocks associated with $\lambda_i$ are linearly independent

Equivalently, if $\bar C_{ik}^{(1)}$ denotes the column of $\bar C$ corresponding to the first state of the $k$th Jordan block of $\lambda_i$,

$$
\operatorname{rank}
\begin{bmatrix}
\bar C_{i1}^{(1)}&
\bar C_{i2}^{(1)}&
\cdots&
\bar C_{ig_i}^{(1)}
\end{bmatrix}
=g_i
$$

For a scalar output, this requires $g_i=1$ for every eigenvalue and a nonzero output entry at the first state of every Jordan block.

### Principle of Duality

##### Dual System

Since the direct-transmission matrix does not affect state controllability or observability, consider the real LTI system

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}
\qquad
\boldsymbol{y}=C\boldsymbol{x}
$$

with $\boldsymbol{x}\in\mathbb{R}^n$, $\boldsymbol{u}\in\mathbb{R}^r$, and $\boldsymbol{y}\in\mathbb{R}^m$. Its **dual system** is

$$
\dot{\boldsymbol{x}}_d=A^T\boldsymbol{x}_d+C^T\boldsymbol{u}_d
\qquad
\boldsymbol{y}_d=B^T\boldsymbol{x}_d
$$

where $\boldsymbol{u}_d\in\mathbb{R}^m$ and $\boldsymbol{y}_d\in\mathbb{R}^r$.

##### Principle of Duality

A system is completely state controllable if and only if its dual system is completely observable. Similarly, a system is completely observable if and only if its dual system is completely state controllable.

**Proof.** The controllability matrix of the dual system is

$$
\mathcal{C}_d
=
\begin{bmatrix}
C^T&A^TC^T&(A^T)^2C^T&\cdots&(A^T)^{n-1}C^T
\end{bmatrix}
=
\begin{bmatrix}
C\\
CA\\
CA^2\\
\vdots\\
CA^{n-1}
\end{bmatrix}^{T}
=\mathcal{O}^T
$$

and its observability matrix is

$$
\mathcal{O}_d
=
\begin{bmatrix}
B^T\\
B^TA^T\\
B^T(A^T)^2\\
\vdots\\
B^T(A^T)^{n-1}
\end{bmatrix}
=
\begin{bmatrix}
B&AB&A^2B&\cdots&A^{n-1}B
\end{bmatrix}^{T}
=\mathcal{C}^T
$$

Since a matrix and its transpose have the same rank, $\operatorname{rank}\mathcal{C}_d=\operatorname{rank}\mathcal{O}$ and $\operatorname{rank}\mathcal{O}_d=\operatorname{rank}\mathcal{C}$. Therefore the condition for complete state controllability of either system is exactly the condition for complete observability of its dual.

### Invariance under Nonsingular State Transformations

##### Nonsingular State Transformation

Using the state transformation introduced previously, let $\boldsymbol{x}=P\boldsymbol{z}$ with nonsingular $P$. Then

$$
\bar A=P^{-1}AP
\qquad
\bar B=P^{-1}B
\qquad
\bar C=CP
\qquad
\bar D=D
$$

##### Invariance of Controllability and Observability

Complete state controllability and complete observability are invariant under a nonsingular state transformation.

**Proof.** From $\bar A=P^{-1}AP$, for every nonnegative integer $k$, $\bar A^k\bar B=P^{-1}A^kB$. Hence

$$
\bar{\mathcal{C}}
=
\begin{bmatrix}
\bar B&\bar A\bar B&\cdots&\bar A^{n-1}\bar B
\end{bmatrix}
=
P^{-1}
\begin{bmatrix}
B&AB&\cdots&A^{n-1}B
\end{bmatrix}
=P^{-1}\mathcal{C}
$$

and therefore $\operatorname{rank}\bar{\mathcal{C}}=\operatorname{rank}\mathcal{C}$.

Similarly, $\bar C\bar A^k=CA^kP$, so

$$
\bar{\mathcal{O}}
=
\begin{bmatrix}
\bar C\\
\bar C\bar A\\
\vdots\\
\bar C\bar A^{n-1}
\end{bmatrix}
=
\begin{bmatrix}
C\\
CA\\
\vdots\\
CA^{n-1}
\end{bmatrix}P
=\mathcal{O}P
$$

Since $P$ and $P^{-1}$ are nonsingular, $\operatorname{rank}\bar{\mathcal{O}}=\operatorname{rank}\mathcal{O}$. Thus neither complete state controllability nor complete observability depends on the choice of state coordinates.

### Transformations to Canonical Forms

Consider the SISO LTI system $\dot{\boldsymbol{x}}=A\boldsymbol{x}+Bu$, $y=C\boldsymbol{x}+Du$, with characteristic polynomial

$$
\det(sI-A)=s^n+a_1s^{n-1}+a_2s^{n-2}+\cdots+a_{n-1}s+a_n
$$

##### Transformation to Controllable Canonical Form

Suppose the system is completely state controllable. Define

$$
A_c=
\begin{bmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_n&-a_{n-1}&-a_{n-2}&\cdots&-a_1
\end{bmatrix}
\qquad
B_c=
\begin{bmatrix}
0\\
\vdots\\
0\\
1
\end{bmatrix}
$$

and construct

$$
T_c=
\begin{bmatrix}
A^{n-1}B&A^{n-2}B&\cdots&AB&B
\end{bmatrix}
\begin{bmatrix}
1&0&0&\cdots&0\\
a_1&1&0&\cdots&0\\
a_2&a_1&1&\cdots&0\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
a_{n-1}&a_{n-2}&\cdots&a_1&1
\end{bmatrix}
=
\begin{bmatrix}
\boldsymbol{p}_1&\boldsymbol{p}_2&\cdots&\boldsymbol{p}_n
\end{bmatrix}
$$

where

$$
\begin{aligned}
\boldsymbol{p}_1&=A^{n-1}B+a_1A^{n-2}B+a_2A^{n-3}B+\cdots+a_{n-2}AB+a_{n-1}B\\
\boldsymbol{p}_2&=A^{n-2}B+a_1A^{n-3}B+a_2A^{n-4}B+\cdots+a_{n-3}AB+a_{n-2}B\\
&\ \vdots\\
\boldsymbol{p}_{n-1}&=AB+a_1B
\qquad
\boldsymbol{p}_n=B
\end{aligned}
$$

The first matrix in the product for $T_c$ is obtained from the controllability matrix $\mathcal{C}=\begin{bmatrix}B&AB&\cdots&A^{n-1}B\end{bmatrix}$ by reversing its columns, so it is nonsingular. The second matrix is lower triangular with unit diagonal. Hence $T_c$ is nonsingular.

With the state transformation $\boldsymbol{x}=T_c\boldsymbol{z}$,

$$
\dot{\boldsymbol{z}}=A_c\boldsymbol{z}+B_cu
\qquad
y=\bar C\boldsymbol{z}+Du
\qquad
\bar C=CT_c=\begin{bmatrix}C\boldsymbol{p}_1&C\boldsymbol{p}_2&\cdots&C\boldsymbol{p}_n\end{bmatrix}
$$

so

$$
T_c^{-1}AT_c=A_c
\qquad
T_c^{-1}B=B_c
\qquad
CT_c=\bar C
\qquad
\bar D=D
$$

**Proof.** By the Cayley-Hamilton theorem,

$$
A^n+a_1A^{n-1}+a_2A^{n-2}+\cdots+a_{n-1}A+a_nI=0
$$

Multiplying by $B$ gives

$$
A^nB+a_1A^{n-1}B+a_2A^{n-2}B+\cdots+a_{n-1}AB+a_nB=0
$$

For the first column of $T_c$,

$$
\begin{aligned}
A\boldsymbol{p}_1
&=A\left(A^{n-1}B+a_1A^{n-2}B+\cdots+a_{n-2}AB+a_{n-1}B\right)\\
&=A^nB+a_1A^{n-1}B+\cdots+a_{n-2}A^2B+a_{n-1}AB\\
&=\left(A^nB+a_1A^{n-1}B+\cdots+a_{n-1}AB+a_nB\right)-a_nB\\
&=-a_nB=-a_n\boldsymbol{p}_n
\end{aligned}
$$

For the second column,

$$
\begin{aligned}
A\boldsymbol{p}_2
&=A\left(A^{n-2}B+a_1A^{n-3}B+\cdots+a_{n-3}AB+a_{n-2}B\right)\\
&=A^{n-1}B+a_1A^{n-2}B+\cdots+a_{n-3}A^2B+a_{n-2}AB\\
&=\left(A^{n-1}B+a_1A^{n-2}B+\cdots+a_{n-2}AB+a_{n-1}B\right)-a_{n-1}B\\
&=\boldsymbol{p}_1-a_{n-1}\boldsymbol{p}_n
\end{aligned}
$$

Continuing in the same way,

$$
A\boldsymbol{p}_{n-1}=\boldsymbol{p}_{n-2}-a_2\boldsymbol{p}_n
\qquad
A\boldsymbol{p}_n=AB=\boldsymbol{p}_{n-1}-a_1\boldsymbol{p}_n
$$

and therefore, for $j=2,\ldots,n$,

$$
A\boldsymbol{p}_j=\boldsymbol{p}_{j-1}-a_{n-j+1}\boldsymbol{p}_n
$$

Hence

$$
\begin{aligned}
AT_c
&=\begin{bmatrix}A\boldsymbol{p}_1&A\boldsymbol{p}_2&\cdots&A\boldsymbol{p}_n\end{bmatrix}\\
&=\begin{bmatrix}
-a_n\boldsymbol{p}_n&
\boldsymbol{p}_1-a_{n-1}\boldsymbol{p}_n&
\boldsymbol{p}_2-a_{n-2}\boldsymbol{p}_n&
\cdots&
\boldsymbol{p}_{n-1}-a_1\boldsymbol{p}_n
\end{bmatrix}\\
&=\begin{bmatrix}\boldsymbol{p}_1&\boldsymbol{p}_2&\cdots&\boldsymbol{p}_n\end{bmatrix}
\begin{bmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_n&-a_{n-1}&-a_{n-2}&\cdots&-a_1
\end{bmatrix}
=T_cA_c
\end{aligned}
$$

Since $T_c$ is nonsingular, left multiplication by $T_c^{-1}$ gives $T_c^{-1}AT_c=A_c$. Also $B=\boldsymbol{p}_n$, so

$$
B=\begin{bmatrix}\boldsymbol{p}_1&\boldsymbol{p}_2&\cdots&\boldsymbol{p}_n\end{bmatrix}
\begin{bmatrix}0&\cdots&0&1\end{bmatrix}^T
=T_cB_c
$$

and therefore $T_c^{-1}B=B_c$. Finally, substituting $\boldsymbol{x}=T_c\boldsymbol{z}$ into the output equation gives $y=CT_c\boldsymbol{z}+Du$, so $\bar C=CT_c$ and $\bar D=D$.

Equivalently, if $\mathcal{C}_c=\begin{bmatrix}B_c&A_cB_c&\cdots&A_c^{n-1}B_c\end{bmatrix}$, then

$$
T_c=\mathcal{C}\mathcal{C}_c^{-1}
\qquad
\mathcal{C}_c^{-1}=
\begin{bmatrix}
a_{n-1}&a_{n-2}&\cdots&a_1&1\\
a_{n-2}&a_{n-3}&\cdots&1&0\\
\vdots&\vdots&&\vdots&\vdots\\
a_1&1&\cdots&0&0\\
1&0&\cdots&0&0
\end{bmatrix}
$$

**eg.** Consider

$$
A=
\begin{bmatrix}
1&2&0\\
3&-1&1\\
0&2&0
\end{bmatrix}
\qquad
B=
\begin{bmatrix}
2\\1\\1
\end{bmatrix}
\qquad
C=\begin{bmatrix}0&0&1\end{bmatrix}
$$

The controllability matrix is $\mathcal{C}=\begin{bmatrix}B&AB&A^2B\end{bmatrix}$ with $\det\mathcal{C}=32\neq0$, so the system is completely state controllable. The characteristic polynomial is $\det(sI-A)=s^3-9s+2$, so $a_1=0$, $a_2=-9$, and $a_3=2$. Since $AB=\begin{bmatrix}4&6&2\end{bmatrix}^T$ and $A^2B=\begin{bmatrix}16&8&12\end{bmatrix}^T$,

$$
T_c
=\begin{bmatrix}A^2B-9B&AB&B\end{bmatrix}
=
\begin{bmatrix}
-2&4&2\\
-1&6&1\\
3&2&1
\end{bmatrix}
$$

with $\det T_c=-32\neq0$. Therefore

$$
\bar A=
\begin{bmatrix}
0&1&0\\
0&0&1\\
-2&9&0
\end{bmatrix}
\qquad
\bar B=
\begin{bmatrix}
0\\0\\1
\end{bmatrix}
\qquad
\bar C=\begin{bmatrix}3&2&1\end{bmatrix}
$$

##### Transformation to Observable Canonical Form

Suppose the system is completely observable. Define

$$
A_o=A_c^T=
\begin{bmatrix}
0&0&\cdots&0&-a_n\\
1&0&\cdots&0&-a_{n-1}\\
0&1&\cdots&0&-a_{n-2}\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&1&-a_1
\end{bmatrix}
\qquad
C_o=\begin{bmatrix}0&0&\cdots&0&1\end{bmatrix}
$$

Construct the inverse transformation directly as

$$
T_o^{-1}=
\begin{bmatrix}
1&a_1&a_2&\cdots&a_{n-1}\\
0&1&a_1&\cdots&a_{n-2}\\
0&0&1&\cdots&a_{n-3}\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
0&0&\cdots&1&a_1\\
0&0&\cdots&0&1
\end{bmatrix}
\begin{bmatrix}
CA^{n-1}\\
CA^{n-2}\\
\vdots\\
CA\\
C
\end{bmatrix}
=
\begin{bmatrix}
\boldsymbol{q}_1^T\\
\boldsymbol{q}_2^T\\
\vdots\\
\boldsymbol{q}_n^T
\end{bmatrix}
$$

where

$$
\begin{aligned}
\boldsymbol{q}_1^T&=CA^{n-1}+a_1CA^{n-2}+a_2CA^{n-3}+\cdots+a_{n-2}CA+a_{n-1}C\\
\boldsymbol{q}_2^T&=CA^{n-2}+a_1CA^{n-3}+a_2CA^{n-4}+\cdots+a_{n-3}CA+a_{n-2}C\\
&\ \vdots\\
\boldsymbol{q}_{n-1}^T&=CA+a_1C
\qquad
\boldsymbol{q}_n^T=C
\end{aligned}
$$

The second matrix in the product for $T_o^{-1}$ is obtained from the observability matrix $\mathcal{O}=\begin{bmatrix}C^T&(CA)^T&\cdots&(CA^{n-1})^T\end{bmatrix}^T$ by reversing its block rows, so it is nonsingular. The first matrix is upper triangular with unit diagonal. Hence $T_o^{-1}$ and $T_o$ are nonsingular.

With the state transformation $\boldsymbol{x}=T_o\boldsymbol{z}$, equivalently $\boldsymbol{z}=T_o^{-1}\boldsymbol{x}$,

$$
\dot{\boldsymbol{z}}=A_o\boldsymbol{z}+\bar Bu
\qquad
y=C_o\boldsymbol{z}+Du
\qquad
\bar B=T_o^{-1}B=
\begin{bmatrix}
\boldsymbol{q}_1^TB\\
\boldsymbol{q}_2^TB\\
\vdots\\
\boldsymbol{q}_n^TB
\end{bmatrix}
$$

so

$$
T_o^{-1}AT_o=A_o
\qquad
T_o^{-1}B=\bar B
\qquad
CT_o=C_o
\qquad
\bar D=D
$$

**Proof.** By the Cayley-Hamilton theorem,

$$
A^n+a_1A^{n-1}+a_2A^{n-2}+\cdots+a_{n-1}A+a_nI=0
$$

Left multiplication by $C$ gives

$$
CA^n+a_1CA^{n-1}+a_2CA^{n-2}+\cdots+a_{n-1}CA+a_nC=0
$$

For the first row of $T_o^{-1}$,

$$
\begin{aligned}
\boldsymbol{q}_1^TA
&=\left(CA^{n-1}+a_1CA^{n-2}+\cdots+a_{n-2}CA+a_{n-1}C\right)A\\
&=CA^n+a_1CA^{n-1}+\cdots+a_{n-2}CA^2+a_{n-1}CA\\
&=\left(CA^n+a_1CA^{n-1}+\cdots+a_{n-1}CA+a_nC\right)-a_nC\\
&=-a_nC=-a_n\boldsymbol{q}_n^T
\end{aligned}
$$

For the second row,

$$
\begin{aligned}
\boldsymbol{q}_2^TA
&=\left(CA^{n-2}+a_1CA^{n-3}+\cdots+a_{n-3}CA+a_{n-2}C\right)A\\
&=CA^{n-1}+a_1CA^{n-2}+\cdots+a_{n-3}CA^2+a_{n-2}CA\\
&=\left(CA^{n-1}+a_1CA^{n-2}+\cdots+a_{n-2}CA+a_{n-1}C\right)-a_{n-1}C\\
&=\boldsymbol{q}_1^T-a_{n-1}\boldsymbol{q}_n^T
\end{aligned}
$$

Continuing in the same way,

$$
\boldsymbol{q}_{n-1}^TA=\boldsymbol{q}_{n-2}^T-a_2\boldsymbol{q}_n^T
\qquad
\boldsymbol{q}_n^TA=CA=\boldsymbol{q}_{n-1}^T-a_1\boldsymbol{q}_n^T
$$

and therefore, for $j=2,\ldots,n$,

$$
\boldsymbol{q}_j^TA=\boldsymbol{q}_{j-1}^T-a_{n-j+1}\boldsymbol{q}_n^T
$$

Hence

$$
\begin{aligned}
T_o^{-1}A
&=
\begin{bmatrix}
\boldsymbol{q}_1^TA\\
\boldsymbol{q}_2^TA\\
\vdots\\
\boldsymbol{q}_n^TA
\end{bmatrix}=
\begin{bmatrix}
-a_n\boldsymbol{q}_n^T\\
\boldsymbol{q}_1^T-a_{n-1}\boldsymbol{q}_n^T\\
\boldsymbol{q}_2^T-a_{n-2}\boldsymbol{q}_n^T\\
\vdots\\
\boldsymbol{q}_{n-1}^T-a_1\boldsymbol{q}_n^T
\end{bmatrix}=
\begin{bmatrix}
0&0&\cdots&0&-a_n\\
1&0&\cdots&0&-a_{n-1}\\
0&1&\cdots&0&-a_{n-2}\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&1&-a_1
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{q}_1^T\\
\boldsymbol{q}_2^T\\
\vdots\\
\boldsymbol{q}_n^T
\end{bmatrix}
=A_oT_o^{-1}
\end{aligned}
$$

Right multiplication by $T_o$ gives $T_o^{-1}AT_o=A_o$. Since the last row of $T_o^{-1}$ is $\boldsymbol{q}_n^T=C$,

$$
C=\begin{bmatrix}0&0&\cdots&0&1\end{bmatrix}T_o^{-1}=C_oT_o^{-1}
$$

and therefore $CT_o=C_o$. The input and direct-transmission terms follow directly from $\boldsymbol{z}=T_o^{-1}\boldsymbol{x}$:

$$
\bar B=T_o^{-1}B
\qquad
\bar D=D
$$

Thus the transformed system is in observable canonical form.

### Controllability Decomposition

##### Controllability Decomposition

Suppose the LTI system is not completely state controllable and

$$
\operatorname{rank}\mathcal{C}=n_c<n
$$

Choose $n_c$ linearly independent columns $\boldsymbol{p}_1,\ldots,\boldsymbol{p}_{n_c}$ of $\mathcal{C}$ and complete them to a basis of $\mathbb{R}^n$. With

$$
P_c=
\begin{bmatrix}
\boldsymbol{p}_1&\cdots&\boldsymbol{p}_{n_c}&
\boldsymbol{p}_{n_c+1}&\cdots&\boldsymbol{p}_n
\end{bmatrix}
$$

and $\boldsymbol{x}=P_c\boldsymbol{z}$, partition $\boldsymbol{z}=\begin{bmatrix}\boldsymbol{z}_c^T&\boldsymbol{z}_{\bar c}^T\end{bmatrix}^T$, where $\boldsymbol{z}_c\in\mathbb{R}^{n_c}$. Then the transformed system has the form

$$
\begin{bmatrix}
\dot{\boldsymbol{z}}_c\\
\dot{\boldsymbol{z}}_{\bar c}
\end{bmatrix}
=
\begin{bmatrix}
A_{11}&A_{12}\\
0&A_{22}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_c\\
\boldsymbol{z}_{\bar c}
\end{bmatrix}
+
\begin{bmatrix}
B_1\\
0
\end{bmatrix}\boldsymbol{u}
\qquad
\boldsymbol{y}=
\begin{bmatrix}
C_1&C_2
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_c\\
\boldsymbol{z}_{\bar c}
\end{bmatrix}
+D\boldsymbol{u}
$$

where $(A_{11},B_1)$ is completely state controllable.

**Proof.** Let $\mathscr{R}=\operatorname{im}\mathcal{C}$. Every column of $B$ belongs to $\mathscr{R}$. Moreover,

$$
A\mathcal{C}
=
\begin{bmatrix}
AB&A^2B&\cdots&A^nB
\end{bmatrix}
$$

and the Cayley-Hamilton theorem expresses $A^nB$ as a linear combination of $B,AB,\ldots,A^{n-1}B$. Hence $A\mathscr{R}\subseteq\mathscr{R}$.

The first $n_c$ columns of $P_c$ form a basis for $\mathscr{R}$. Therefore the coordinates of $B$ and of $A\boldsymbol{p}_j$ for $j=1,\ldots,n_c$ have zero components along the last $n-n_c$ basis vectors. Thus

$$
P_c^{-1}AP_c=
\begin{bmatrix}
A_{11}&A_{12}\\
0&A_{22}
\end{bmatrix}
\qquad
P_c^{-1}B=
\begin{bmatrix}
B_1\\
0
\end{bmatrix}
$$

and $CP_c=\begin{bmatrix}C_1&C_2\end{bmatrix}$. The transformed controllability matrix is

$$
P_c^{-1}\mathcal{C}
=
\begin{bmatrix}
B_1&A_{11}B_1&\cdots&A_{11}^{n-1}B_1\\
0&0&\cdots&0
\end{bmatrix}
$$

Its rank is $n_c$, so the upper block has rank $n_c$. By the Cayley-Hamilton theorem applied to the $n_c\times n_c$ matrix $A_{11}$, the same rank is obtained from $\begin{bmatrix}B_1&A_{11}B_1&\cdots&A_{11}^{n_c-1}B_1\end{bmatrix}$; hence $(A_{11},B_1)$ is completely state controllable.

##### Controllable and Uncontrollable Parts

The transformed equations separate the states into a controllable part and an uncontrollable part:

$$
\dot{\boldsymbol{z}}_c=A_{11}\boldsymbol{z}_c+A_{12}\boldsymbol{z}_{\bar c}+B_1\boldsymbol{u}
\qquad
\dot{\boldsymbol{z}}_{\bar c}=A_{22}\boldsymbol{z}_{\bar c}
$$

The control input does not enter the uncontrollable part. The transformation is not unique because the remaining $n-n_c$ basis vectors may be chosen in different ways.

##### Controllable and Uncontrollable Modes

Because $A$ and $P_c^{-1}AP_c$ are similar and the transformed state matrix is block upper triangular,

$$
\det(sI-A)
=
\det
\begin{bmatrix}
sI-A_{11}&-A_{12}\\
0&sI-A_{22}
\end{bmatrix}
=
\det(sI-A_{11})\det(sI-A_{22})
$$

The eigenvalues of $A_{11}$ are the **controllable modes**, and the eigenvalues of $A_{22}$ are the **uncontrollable modes**. The uncontrollable modes belong to the autonomous part $\dot{\boldsymbol{z}}_{\bar c}=A_{22}\boldsymbol{z}_{\bar c}$ and cannot be affected through the input matrix $B$.

**eg.** Consider
$$
A=
\begin{bmatrix}
1&2&-1\\
0&1&0\\
0&-4&3
\end{bmatrix}
\qquad
B=
\begin{bmatrix}
0\\
0\\
1
\end{bmatrix}
\qquad
C=
\begin{bmatrix}
1&-1&1
\end{bmatrix}
$$

The controllability matrix is

$$
\mathcal{C}
=
\begin{bmatrix}
B&AB&A^2B
\end{bmatrix}
=
\begin{bmatrix}
0&-1&-4\\
0&0&0\\
1&3&9
\end{bmatrix}
$$

so $\operatorname{rank}\mathcal{C}=2$. Choose the first two columns of $\mathcal{C}$ and complete them with $\begin{bmatrix}0&1&0\end{bmatrix}^T$:

$$
P_c=
\begin{bmatrix}
0&-1&0\\
0&0&1\\
1&3&0
\end{bmatrix}
\qquad
P_c^{-1}=
\begin{bmatrix}
3&0&1\\
-1&0&0\\
0&1&0
\end{bmatrix}
$$

With $\boldsymbol{x}=P_c\boldsymbol{z}$,

$$
\bar A=P_c^{-1}AP_c=
\begin{bmatrix}
0&-3&2\\
1&4&-2\\
0&0&1
\end{bmatrix}
\qquad
\bar B=P_c^{-1}B=
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
\qquad
\bar C=CP_c=
\begin{bmatrix}
1&2&-1
\end{bmatrix}
$$

Thus $\boldsymbol{z}_c=\begin{bmatrix}z_1&z_2\end{bmatrix}^T$ is the controllable part and $z_{\bar c}=z_3$ is the uncontrollable part, with $\dot z_{\bar c}=z_{\bar c}$.

### Observability Decomposition

##### Observability Decomposition

Suppose the system is not completely observable and $\operatorname{rank}\mathcal{O}=n_o<n$. Choose $n_o$ linearly independent rows of $\mathcal{O}$ and complete them to a nonsingular matrix $R_o$. Let $P_o=R_o^{-1}$ and use the same transformation convention $\boldsymbol{x}=P_o\boldsymbol{z}$, equivalently $\boldsymbol{z}=R_o\boldsymbol{x}$. Partition $\boldsymbol{z}=\begin{bmatrix}\boldsymbol{z}_o^T&\boldsymbol{z}_{\bar o}^T\end{bmatrix}^T$. Then

$$
\begin{bmatrix}
\dot{\boldsymbol{z}}_o\\
\dot{\boldsymbol{z}}_{\bar o}
\end{bmatrix}
=
\begin{bmatrix}
A_{11}&0\\
A_{21}&A_{22}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_o\\
\boldsymbol{z}_{\bar o}
\end{bmatrix}
+
\begin{bmatrix}
B_1\\
B_2
\end{bmatrix}\boldsymbol{u}
\qquad
\boldsymbol{y}=
\begin{bmatrix}
C_1&0
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_o\\
\boldsymbol{z}_{\bar o}
\end{bmatrix}
+D\boldsymbol{u}
$$

where $(C_1,A_{11})$ is completely observable.

**Proof.** The dual system has controllability matrix $\mathcal{C}_d=\mathcal{O}^T$. Thus the selected independent rows of $\mathcal{O}$ become independent columns of $\mathcal{C}_d$. Let $P_d=R_o^T$. Applying the controllability decomposition to the dual system gives

$$
P_d^{-1}A^TP_d=
\begin{bmatrix}
A_{11}^T&A_{12}^d\\
0&A_{22}^T
\end{bmatrix}
\qquad
P_d^{-1}C^T=
\begin{bmatrix}
C_1^T\\
0
\end{bmatrix}
$$

Taking transposes and using $P_d^T=R_o$ yields

$$
R_oAR_o^{-1}=
\begin{bmatrix}
A_{11}&0\\
(A_{12}^d)^T&A_{22}
\end{bmatrix}
\qquad
CR_o^{-1}=
\begin{bmatrix}
C_1&0
\end{bmatrix}
$$

while $R_oB=\begin{bmatrix}B_1^T&B_2^T\end{bmatrix}^T$. Therefore the transformed system has the stated form. Its observability matrix is

$$
\bar{\mathcal{O}}
=
\begin{bmatrix}
C_1&0\\
C_1A_{11}&0\\
\vdots&\vdots\\
C_1A_{11}^{n-1}&0
\end{bmatrix}
$$

and has rank $n_o$. By the Cayley-Hamilton theorem for $A_{11}$, $\begin{bmatrix}C_1^T&(C_1A_{11})^T&\cdots&(C_1A_{11}^{n_o-1})^T\end{bmatrix}^T$ also has rank $n_o$, so $(C_1,A_{11})$ is completely observable.

##### Observable and Unobservable Parts

The output depends directly only on the observable part. The state equations are

$$
\dot{\boldsymbol{z}}_o=A_{11}\boldsymbol{z}_o+B_1\boldsymbol{u}
\qquad
\dot{\boldsymbol{z}}_{\bar o}=A_{21}\boldsymbol{z}_o+A_{22}\boldsymbol{z}_{\bar o}+B_2\boldsymbol{u}
$$

and $\boldsymbol{y}=C_1\boldsymbol{z}_o+D\boldsymbol{u}$. Hence the unobservable part does not appear directly in the output.

**eg.** Consider
$$
A=
\begin{bmatrix}
-2&2&-1\\
0&-2&0\\
1&-4&0
\end{bmatrix}
\qquad
B=
\begin{bmatrix}
0\\
0\\
1
\end{bmatrix}
\qquad
C=
\begin{bmatrix}
1&-1&1
\end{bmatrix}
$$

The observability matrix is

$$
\mathcal{O}
=
\begin{bmatrix}
C\\
CA\\
CA^2
\end{bmatrix}
=
\begin{bmatrix}
1&-1&1\\
-1&0&-1\\
1&2&1
\end{bmatrix}
$$

and $\operatorname{rank}\mathcal{O}=2$. Choose the first two rows and complete them with $\begin{bmatrix}1&0&0\end{bmatrix}$:

$$
R_o=
\begin{bmatrix}
1&-1&1\\
-1&0&-1\\
1&0&0
\end{bmatrix}
\qquad
R_o^{-1}=
\begin{bmatrix}
0&0&1\\
-1&-1&0\\
0&-1&-1
\end{bmatrix}
$$

With $\boldsymbol{z}=R_o\boldsymbol{x}$,

$$
\bar A=R_oAR_o^{-1}=
\begin{bmatrix}
0&1&0\\
-2&-3&0\\
-2&-1&-1
\end{bmatrix}
\qquad
\bar B=R_oB=
\begin{bmatrix}
1\\
-1\\
0
\end{bmatrix}
\qquad
\bar C=CR_o^{-1}=
\begin{bmatrix}
1&0&0
\end{bmatrix}
$$

Thus $\boldsymbol{z}_o=\begin{bmatrix}z_1&z_2\end{bmatrix}^T$ is the observable part and $z_{\bar o}=z_3$ is the unobservable part.

### Controllability and Observability Decomposition

##### State Decomposition

By applying nonsingular state transformations, the state can be partitioned into four parts,

$$
\boldsymbol{z}=
\begin{bmatrix}
\boldsymbol{z}_{co}\\
\boldsymbol{z}_{c\bar o}\\
\boldsymbol{z}_{\bar c o}\\
\boldsymbol{z}_{\bar c\bar o}
\end{bmatrix}
$$

where $\boldsymbol{z}_{co}$ is controllable and observable, $\boldsymbol{z}_{c\bar o}$ is controllable and unobservable, $\boldsymbol{z}_{\bar c o}$ is uncontrollable and observable, and $\boldsymbol{z}_{\bar c\bar o}$ is uncontrollable and unobservable.

##### Decomposed State-Space Representation

With the state ordered as above, a corresponding decomposed representation has the block structure

$$
\begin{bmatrix}
\dot{\boldsymbol{z}}_{co}\\
\dot{\boldsymbol{z}}_{c\bar o}\\
\dot{\boldsymbol{z}}_{\bar c o}\\
\dot{\boldsymbol{z}}_{\bar c\bar o}
\end{bmatrix}
=
\begin{bmatrix}
A_{co}&0&A_{13}&0\\
A_{21}&A_{c\bar o}&A_{23}&A_{24}\\
0&0&A_{\bar c o}&0\\
0&0&A_{43}&A_{\bar c\bar o}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_{co}\\
\boldsymbol{z}_{c\bar o}\\
\boldsymbol{z}_{\bar c o}\\
\boldsymbol{z}_{\bar c\bar o}
\end{bmatrix}
+
\begin{bmatrix}
B_{co}\\
B_{c\bar o}\\
0\\
0
\end{bmatrix}\boldsymbol{u}
$$

and

$$
\boldsymbol{y}
=
\begin{bmatrix}
C_{co}&0&C_{\bar c o}&0
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{z}_{co}\\
\boldsymbol{z}_{c\bar o}\\
\boldsymbol{z}_{\bar c o}\\
\boldsymbol{z}_{\bar c\bar o}
\end{bmatrix}
+D\boldsymbol{u}
$$

The zero blocks express the two defining structural properties: the input acts only on the controllable states, while only the observable states contribute directly to the output.

