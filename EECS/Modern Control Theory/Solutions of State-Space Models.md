# Solutions of State-Space Models

[toc]

### Solution of the LTI State Equation

##### Response Decomposition

Consider the continuous-time linear time-invariant system

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}\qquad \boldsymbol{y}=C\boldsymbol{x}+D\boldsymbol{u}
$$

For a linear system, the effects of the initial condition and the external input can be considered separately. For an initial state $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$, the state response is the sum of the **zero-input response** and the **zero-state response**

$$
\boldsymbol{x}(t)=\boldsymbol{x}_{zi}(t)+\boldsymbol{x}_{zs}(t)
$$

with

$$
\boldsymbol{x}_{zi}(t)=e^{A(t-t_0)}\boldsymbol{x}_0
\qquad
\boldsymbol{x}_{zs}(t)=\int_{t_0}^{t}e^{A(t-\tau)}B\boldsymbol{u}(\tau)d\tau
$$

Hence

$$
\boldsymbol{x}(t)=e^{A(t-t_0)}\boldsymbol{x}_0+\int_{t_0}^{t}e^{A(t-\tau)}B\boldsymbol{u}(\tau)d\tau
$$

and the corresponding output is $\boldsymbol{y}(t)=C\boldsymbol{x}(t)+D\boldsymbol{u}(t)$. Thus

$$
\boldsymbol{y}_{zi}(t)=C\boldsymbol{x}_{zi}(t)
\qquad
\boldsymbol{y}_{zs}(t)=C\boldsymbol{x}_{zs}(t)+D\boldsymbol{u}(t)
$$

##### Homogeneous Solution

For the homogeneous state equation

$$
\dot{\boldsymbol{x}}=A\boldsymbol{x}\qquad \boldsymbol{x}(0)=\boldsymbol{x}_0
$$

successive differentiation gives $\boldsymbol{x}^{(k)}(t)=A^k\boldsymbol{x}(t)$ and therefore $\boldsymbol{x}^{(k)}(0)=A^k\boldsymbol{x}_0$. Expanding $\boldsymbol{x}(t)$ about $t=0$,

$$
\begin{aligned}
\boldsymbol{x}(t)
&=\boldsymbol{x}_0+t\dot{\boldsymbol{x}}(0)+\frac{t^2}{2!}\ddot{\boldsymbol{x}}(0)+\cdots\\
&=\left(I+At+\frac{A^2t^2}{2!}+\cdots\right)\boldsymbol{x}_0\\
&=e^{At}\boldsymbol{x}_0
\end{aligned}
$$

For an arbitrary initial time $t_0$,

$$
\boldsymbol{x}_{zi}(t)=e^{A(t-t_0)}\boldsymbol{x}(t_0)
$$

##### Forced Response

To obtain the zero-state response, set $\boldsymbol{x}(t_0)=\boldsymbol{0}$ in $\dot{\boldsymbol{x}}=A\boldsymbol{x}+B\boldsymbol{u}$. Since

$$
\frac{d}{dt}\left(e^{-At}\boldsymbol{x}(t)\right)=e^{-At}B\boldsymbol{u}(t)
$$

integration from $t_0$ to $t$ gives

$$
e^{-At}\boldsymbol{x}(t)-e^{-At_0}\boldsymbol{x}(t_0)
=\int_{t_0}^{t}e^{-A\tau}B\boldsymbol{u}(\tau)d\tau
$$

and therefore

$$
\boldsymbol{x}_{zs}(t)=\int_{t_0}^{t}e^{A(t-\tau)}B\boldsymbol{u}(\tau)d\tau
$$

##### Responses to Standard Inputs

For the following inputs, let $t_0=0$, let $\boldsymbol{K}$ be a constant input vector, and let $1(t)$ denote the unit-step function.

**eg. Impulse input.** Let $\boldsymbol{x}(0^-)=\boldsymbol{x}_0$. For $\boldsymbol{u}(t)=\boldsymbol{K}\delta(t)$,

$$
\begin{aligned}
\boldsymbol{x}(t)
&=e^{At}\boldsymbol{x}_0+\int_{0^-}^t e^{A(t-\tau)}B\boldsymbol{K}\delta(\tau)d\tau\\
&=e^{At}\boldsymbol{x}_0+\left(\int_{0^-}^t e^{A(t-\tau)}\delta(\tau)d\tau\right)B\boldsymbol{K}\\
&=e^{At}\boldsymbol{x}_0+e^{At}B\boldsymbol{K}
\end{aligned}
$$

**eg. Step input.** Let $\boldsymbol{x}(0)=\boldsymbol{x}_0$. For $\boldsymbol{u}(t)=\boldsymbol{K}1(t)$ and nonsingular $A$,

$$
\begin{aligned}
\boldsymbol{x}(t)
&=e^{At}\boldsymbol{x}_0+\int_0^t e^{A(t-\tau)}B\boldsymbol{K}d\tau\\
&=e^{At}\boldsymbol{x}_0+e^{At}\left(\int_0^t e^{-A\tau}d\tau\right)B\boldsymbol{K}\\
&=e^{At}\boldsymbol{x}_0+e^{At}(e^{-At}-I)(-A^{-1})B\boldsymbol{K}\\
&=e^{At}\boldsymbol{x}_0+A^{-1}(e^{At}-I)B\boldsymbol{K}
\end{aligned}
$$

If $A$ is singular, the integral form remains valid.

**eg. Ramp input.** Let $\boldsymbol{x}(0)=\boldsymbol{x}_0$. For $\boldsymbol{u}(t)=\boldsymbol{K}t1(t)$ and nonsingular $A$, let $\sigma=t-\tau$. Then

$$
\begin{aligned}
\boldsymbol{x}(t)
&=e^{At}\boldsymbol{x}_0+\int_0^t e^{A(t-\tau)}B\boldsymbol{K}\tau d\tau\\
&=e^{At}\boldsymbol{x}_0+\int_0^t e^{A\sigma}B\boldsymbol{K}(t-\sigma)d\sigma\\
&=e^{At}\boldsymbol{x}_0+tA^{-1}(e^{At}-I)B\boldsymbol{K}
-\left[tA^{-1}e^{At}-A^{-2}(e^{At}-I)\right]B\boldsymbol{K}\\
&=e^{At}\boldsymbol{x}_0+\left[A^{-2}(e^{At}-I)-tA^{-1}\right]B\boldsymbol{K}
\end{aligned}
$$

where integration by parts gives

$$
\int_0^t \sigma e^{A\sigma}d\sigma
=tA^{-1}e^{At}-A^{-2}(e^{At}-I)
$$

If $A$ is singular, the original convolution integral is used instead of the inverse-matrix form.

##### Free Motion and Stability

With $\boldsymbol{u}=\boldsymbol{0}$, the system undergoes **free motion**. Starting from $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$, the points $\boldsymbol{x}(t)=e^{A(t-t_0)}\boldsymbol{x}_0$ form the state trajectory. For fixed $A$ and $\boldsymbol{x}_0$, this zero-input trajectory is uniquely determined by the matrix exponential.

The equilibrium $\boldsymbol{x}=\boldsymbol{0}$ is asymptotically stable if every zero-input trajectory approaches the origin, equivalently

$$
\lim_{t\to\infty}e^{At}=0
$$

For a continuous-time LTI system, this holds if and only if every eigenvalue of $A$ has strictly negative real part

$$
\operatorname{Re}(\lambda_i)<0\qquad i=1,2,\ldots,n
$$

### Matrix Exponential

##### Definition and Properties

For a square matrix $A$, the **matrix exponential** is defined by the convergent power series

$$
e^{At}=I+At+\frac{A^2t^2}{2!}+\frac{A^3t^3}{3!}+\cdots
=\sum_{k=0}^{\infty}\frac{A^kt^k}{k!}
$$

Its basic properties are:

- **Identity at zero:** $e^{A0}=I$ and $\displaystyle\lim_{t\to0}e^{At}=I$.
- **Addition of time:** $e^{A(t_1+t_2)}=e^{At_1}e^{At_2}=e^{At_2}e^{At_1}$.
- **Inverse:** $(e^{At})^{-1}=e^{-At}$, since $e^{At}e^{-At}=e^{A(t-t)}=I$.
- **Derivative:** $\displaystyle\frac{d}{dt}e^{At}=Ae^{At}=e^{At}A$.
- **Commuting matrices:** if $AB=BA$, then $e^{(A+B)t}=e^{At}e^{Bt}=e^{Bt}e^{At}$.
- **Integer multiples of time:** $(e^{At})^m=e^{A(mt)}$ for every positive integer $m$.

For the derivative property, term-by-term differentiation gives

$$
\begin{aligned}
\frac{d}{dt}e^{At}
&=A+A^2t+\frac{A^3t^2}{2!}+\cdots\\
&=A\left(I+At+\frac{A^2t^2}{2!}+\cdots\right)
=Ae^{At}
\end{aligned}
$$

Since every power of $A$ commutes with $A$, the same series also gives $Ae^{At}=e^{At}A$.

If $AB=BA$, the binomial theorem applies to $(A+B)^k$, so

$$
\begin{aligned}
e^{(A+B)t}
&=\sum_{k=0}^{\infty}\frac{t^k}{k!}\sum_{j=0}^{k}\binom{k}{j}A^jB^{k-j}\\
&=\left(\sum_{j=0}^{\infty}\frac{A^jt^j}{j!}\right)
\left(\sum_{r=0}^{\infty}\frac{B^rt^r}{r!}\right)
=e^{At}e^{Bt}
\end{aligned}
$$

Finally, repeated use of the addition-of-time property gives

$$
(e^{At})^m=\underbrace{e^{At}e^{At}\cdots e^{At}}_{m\text{ factors}}=e^{A(mt)}
$$

##### Power-Series Method

The matrix exponential may be computed directly from

$$
e^{At}=I+At+\frac{A^2t^2}{2!}+\cdots
$$

This method is especially simple when powers of $A$ terminate or repeat in a simple pattern.

##### Canonical-Form Method

If $A=MJM^{-1}$, then $A^k=MJ^kM^{-1}$ for every nonnegative integer $k$. Hence

$$
e^{At}=M e^{Jt}M^{-1}
$$

If $A$ has $n$ distinct eigenvalues, it is diagonalizable. With

$$
A=M\Lambda M^{-1}
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\ldots,\lambda_n)
$$

we have

$$
\begin{aligned}
e^{At}
&=\sum_{k=0}^{\infty}\frac{A^kt^k}{k!}
=M\left(\sum_{k=0}^{\infty}\frac{\Lambda^kt^k}{k!}\right)M^{-1}\\
&=M\operatorname{diag}\left(e^{\lambda_1t},e^{\lambda_2t},\ldots,e^{\lambda_nt}\right)M^{-1}
\end{aligned}
$$

For a Jordan block $J_r(\lambda)=\lambda I+N$, where $N^r=0$,

$$
e^{J_r(\lambda)t}=e^{\lambda t}\left(I+Nt+\frac{N^2t^2}{2!}+\cdots+\frac{N^{r-1}t^{r-1}}{(r-1)!}\right)
$$

or explicitly

$$
e^{J_r(\lambda)t}=e^{\lambda t}
\begin{bmatrix}
1&t&\frac{t^2}{2!}&\cdots&\frac{t^{r-1}}{(r-1)!}\\
0&1&t&\cdots&\frac{t^{r-2}}{(r-2)!}\\
\vdots&\ddots&\ddots&\ddots&\vdots\\
0&\cdots&0&1&t\\
0&\cdots&\cdots&0&1
\end{bmatrix}
$$

**eg.** Compute $e^{At}$ for

$$
A=\begin{bmatrix}0&1&0\\0&0&1\\2&3&0\end{bmatrix}
$$

The characteristic polynomial is

$$
\det(\lambda I-A)=\lambda^3-3\lambda-2=(\lambda-2)(\lambda+1)^2
$$

For $\lambda=-1$, there is only one linearly independent eigenvector, so a Jordan form is required. Choose

$$
M=\begin{bmatrix}1&2&1\\-1&-1&2\\1&0&4\end{bmatrix}
\qquad
J=M^{-1}AM=
\begin{bmatrix}-1&1&0\\0&-1&0\\0&0&2\end{bmatrix}
$$

Then

$$
e^{Jt}=\begin{bmatrix}
e^{-t}&te^{-t}&0\\
0&e^{-t}&0\\
0&0&e^{2t}
\end{bmatrix}
$$

and $e^{At}=Me^{Jt}M^{-1}$ gives

$$
e^{At}=\frac{e^{-t}}{9}
\begin{bmatrix}
6t+e^{3t}+8&3t+2e^{3t}-2&-3t+e^{3t}-1\\
2(-3t+e^{3t}-1)&-3t+4e^{3t}+5&3t+2e^{3t}-2\\
2(3t+2e^{3t}-2)&3t+8e^{3t}-8&-3t+4e^{3t}+5
\end{bmatrix}
$$

##### Laplace-Transform Method

For $\dot{\boldsymbol{x}}=A\boldsymbol{x}$ with $\boldsymbol{x}(0)=\boldsymbol{x}_0$, the Laplace transform gives

$$
s\boldsymbol{X}(s)-\boldsymbol{x}_0=A\boldsymbol{X}(s)
$$

so

$$
\boldsymbol{X}(s)=(sI-A)^{-1}\boldsymbol{x}_0
$$

Comparing with $\boldsymbol{x}(t)=e^{At}\boldsymbol{x}_0$ gives

$$
\mathcal{L}\{e^{At}\}=(sI-A)^{-1}
\qquad
 e^{At}=\mathcal{L}^{-1}\{(sI-A)^{-1}\}
$$

For sufficiently large $|s|$, the same result follows from the resolvent expansion

$$
(sI-A)^{-1}=\frac{I}{s}+\frac{A}{s^2}+\frac{A^2}{s^3}+\cdots
$$

whose inverse Laplace transform is $I+At+A^2t^2/2!+\cdots=e^{At}$.

**eg.** Compute $e^{At}$ for

$$
A=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}
$$

Since

$$
sI-A=\begin{bmatrix}s&-1\\2&s+3\end{bmatrix}
$$

we obtain

$$
(sI-A)^{-1}
=\frac{1}{(s+1)(s+2)}
\begin{bmatrix}s+3&1\\-2&s\end{bmatrix}
$$

Taking the inverse Laplace transform entry by entry gives

$$
e^{At}=
\begin{bmatrix}
2e^{-t}-e^{-2t}&e^{-t}-e^{-2t}\\
-2e^{-t}+2e^{-2t}&-e^{-t}+2e^{-2t}
\end{bmatrix}
$$

##### Cayley-Hamilton Method

Let the characteristic polynomial of $A\in\mathbb{C}^{n\times n}$ be

$$
p_A(\lambda)=\det(\lambda I-A)
$$

The Cayley-Hamilton theorem states that $p_A(A)=0$. Therefore every power $A^k$ with $k\geq n$ can be reduced to a linear combination of $I,A,\ldots,A^{n-1}$, and the matrix exponential can be written as

$$
e^{At}=\alpha_0(t)I+\alpha_1(t)A+\cdots+\alpha_{n-1}(t)A^{n-1}
$$

If the eigenvalues $\lambda_1,\ldots,\lambda_n$ are distinct, let $\boldsymbol{v}_i$ be an eigenvector associated with $\lambda_i$. Applying both sides to $\boldsymbol{v}_i$ gives

$$
e^{\lambda_i t}=\alpha_0(t)+\alpha_1(t)\lambda_i+\cdots+\alpha_{n-1}(t)\lambda_i^{n-1}
$$

Hence the coefficients are determined by the Vandermonde system

$$
\begin{bmatrix}
1&\lambda_1&\cdots&\lambda_1^{n-1}\\
1&\lambda_2&\cdots&\lambda_2^{n-1}\\
\vdots&\vdots&\ddots&\vdots\\
1&\lambda_n&\cdots&\lambda_n^{n-1}
\end{bmatrix}
\begin{bmatrix}\alpha_0\\\alpha_1\\\vdots\\\alpha_{n-1}\end{bmatrix}
=
\begin{bmatrix}e^{\lambda_1t}\\e^{\lambda_2t}\\\vdots\\e^{\lambda_nt}\end{bmatrix}
$$

Since the eigenvalues are distinct, the Vandermonde matrix is nonsingular. Equivalently,

$$
e^{At}=\sum_{i=1}^{n}e^{\lambda_i t}
\prod_{\substack{j=1\\j\neq i}}^{n}\frac{A-\lambda_jI}{\lambda_i-\lambda_j}
$$

**eg.** Compute $e^{At}$ using the Cayley-Hamilton theorem for

$$
A=\begin{bmatrix}0&1&0\\0&0&1\\-6&-11&-6\end{bmatrix}
$$

The characteristic polynomial is

$$
p_A(\lambda)=\lambda^3+6\lambda^2+11\lambda+6=(\lambda+1)(\lambda+2)(\lambda+3)
$$

By the Cayley-Hamilton theorem,

$$
e^{At}=\alpha_0(t)I+\alpha_1(t)A+\alpha_2(t)A^2
$$

The distinct eigenvalues $-1,-2,-3$ give

$$
\begin{aligned}
\alpha_0-\alpha_1+\alpha_2&=e^{-t}\\
\alpha_0-2\alpha_1+4\alpha_2&=e^{-2t}\\
\alpha_0-3\alpha_1+9\alpha_2&=e^{-3t}
\end{aligned}
$$

so

$$
\begin{aligned}
\alpha_0(t)&=3e^{-t}-3e^{-2t}+e^{-3t}\\
\alpha_1(t)&=\frac{1}{2}\left(5e^{-t}-8e^{-2t}+3e^{-3t}\right)\\
\alpha_2(t)&=\frac{1}{2}\left(e^{-t}-2e^{-2t}+e^{-3t}\right)
\end{aligned}
$$

Therefore

$$
e^{At}=\left(3e^{-t}-3e^{-2t}+e^{-3t}\right)I
+\frac{5e^{-t}-8e^{-2t}+3e^{-3t}}{2}A
+\frac{e^{-t}-2e^{-2t}+e^{-3t}}{2}A^2
$$

### State-Transition Matrix

##### Definition and Matrix Exponential

For the homogeneous state equation $\dot{\boldsymbol{x}}=A\boldsymbol{x}$, the **state-transition matrix** $\Phi(t,t_0)$ maps the state at $t_0$ to the state at $t$

$$
\boldsymbol{x}(t)=\Phi(t,t_0)\boldsymbol{x}(t_0)
$$

It is the unique matrix solution of

$$
\frac{\partial}{\partial t}\Phi(t,t_0)=A\Phi(t,t_0)
\qquad
\Phi(t_0,t_0)=I
$$

For an LTI system,

$$
\Phi(t,t_0)=e^{A(t-t_0)}
$$

and, with $t_0=0$, $\Phi(t)=e^{At}$.

##### Properties and Interpretation

For an LTI system, the state-transition matrix has the following properties:

- **Composition:** $\Phi(t_2,t_0)=\Phi(t_2,t_1)\Phi(t_1,t_0)$.
- **Invertibility:** $\Phi^{-1}(t,t_0)=\Phi(t_0,t)$.
- **Time invariance:** $\Phi(t,t_0)$ depends only on $t-t_0$.
- **Integer multiples:** with $\Phi(t)=e^{At}$, $[\Phi(t)]^m=\Phi(mt)$ for every positive integer $m$.
- **Differentiation and commutation:** $\displaystyle\frac{\partial}{\partial t}\Phi(t,t_0)=A\Phi(t,t_0)=\Phi(t,t_0)A$.
- **Uniqueness:** for a given state matrix $A$, $\Phi(t,t_0)$ is uniquely determined by its matrix differential equation and initial condition.

The state-transition matrix propagates a state from one time to another. Its $i$th column is the zero-input trajectory generated from the initial condition equal to the $i$th coordinate vector.

##### Recovering the State Matrix

If the state-transition matrix of an LTI system is known, from $\dot\Phi(t)=A\Phi(t)$,

$$
A=\dot\Phi(t)\Phi^{-1}(t)
$$

Since $\Phi(0)=I$,

$$
A=\left.\dot\Phi(t)\Phi^{-1}(t)\right|_{t=0}
=\left.\frac{d}{dt}\Phi(t)\right|_{t=0}
$$

More generally,

$$
A=\left.\frac{\partial}{\partial t}\Phi(t,t_0)\right|_{t=t_0}
$$

because $\Phi(t_0,t_0)=I$ and $\partial\Phi/\partial t=A\Phi$.

**eg.** Given the state-transition matrix
$$
\Phi(t)=
\begin{bmatrix}
\frac{1}{2}\left(e^{-t}+e^{3t}\right)&\frac{1}{4}\left(-e^{-t}+e^{3t}\right)\\
-e^{-t}+e^{3t}&\frac{1}{2}\left(e^{-t}+e^{3t}\right)
\end{bmatrix}
$$

find the state matrix $A$.

Differentiating,

$$
\dot\Phi(t)=
\begin{bmatrix}
\frac{1}{2}\left(-e^{-t}+3e^{3t}\right)&\frac{1}{4}\left(e^{-t}+3e^{3t}\right)\\
e^{-t}+3e^{3t}&\frac{1}{2}\left(-e^{-t}+3e^{3t}\right)
\end{bmatrix}
$$

Therefore

$$
A=\left.\dot\Phi(t)\right|_{t=0}
=\begin{bmatrix}1&1\\4&1\end{bmatrix}
$$

### Solution of the LTV State Equation

##### State-Transition Matrix

Consider the continuous-time linear time-varying system

$$
\dot{\boldsymbol{x}}(t)=A(t)\boldsymbol{x}(t)+B(t)\boldsymbol{u}(t)
\qquad
\boldsymbol{y}(t)=C(t)\boldsymbol{x}(t)+D(t)\boldsymbol{u}(t)
$$

with $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$. If the coefficient matrices are piecewise continuous and the input is integrable, the state equation has a unique solution.

The **state-transition matrix** $\Phi(t,\tau)$ is the unique matrix satisfying

$$
\frac{\partial}{\partial t}\Phi(t,\tau)=A(t)\Phi(t,\tau)
\qquad
\Phi(\tau,\tau)=I
$$

The zero-input response is

$$
\boldsymbol{x}_{zi}(t)=\Phi(t,t_0)\boldsymbol{x}_0
$$

For a general LTV system, $\Phi(t,\tau)$ depends on both time arguments and normally has no closed-form expression directly in terms of $A(t)$; it is generally obtained from the matrix differential equation above.

In particular, the scalar-looking expression

$$
\Phi(t,t_0)=\exp\left(\int_{t_0}^{t}A(\tau)d\tau\right)
$$

is not valid in general. It is valid when the required commutation condition holds

$$
A(t)\left(\int_{t_0}^{t}A(\tau)d\tau\right)
=
\left(\int_{t_0}^{t}A(\tau)d\tau\right)A(t)
$$

##### Complete State Response

The solution of the nonhomogeneous LTV state equation is

$$
\boldsymbol{x}(t)=\Phi(t,t_0)\boldsymbol{x}_0
+\int_{t_0}^{t}\Phi(t,\tau)B(\tau)\boldsymbol{u}(\tau)d\tau
$$

The first term is the zero-input response and the integral term is the zero-state response. The corresponding output is

$$
\boldsymbol{y}(t)=C(t)\boldsymbol{x}(t)+D(t)\boldsymbol{u}(t)
$$

##### Properties

The state-transition matrix satisfies:

- **Identity:** $\Phi(t_0,t_0)=I$.
- **Composition:** $\Phi(t_2,t_1)\Phi(t_1,t_0)=\Phi(t_2,t_0)$.
- **Invertibility:** $\Phi^{-1}(t,t_0)=\Phi(t_0,t)$.
- **Differential equation:** $\displaystyle\frac{\partial}{\partial t}\Phi(t,t_0)=A(t)\Phi(t,t_0)$.
- **Uniqueness:** for a given $A(t)$ satisfying the stated regularity conditions, $\Phi(t,t_0)$ is uniquely determined.

