# Infinite Series

[toc]

### Tests for Constant-Term Series

##### Definition of convergence

For the series

$$
\sum_{n=1}^{\infty}a_n
$$

let

$$
S_n=\sum_{i=1}^{n}a_i
$$

If the limit

$$
\lim_{n\to\infty}S_n
$$

exists, then the series converges and

$$
\sum_{n=1}^{\infty}a_n=\lim_{n\to\infty}S_n
$$

##### Properties of convergent series

| Property | Statement |
|---|---|
| Constant multiple | If $\sum\limits_{n=1}^{\infty}a_n=S$, then $\sum\limits_{n=1}^{\infty}ca_n=cS$ |
| Sum and difference | If $\sum\limits_{n=1}^{\infty}a_n=S_1$ and $\sum\limits_{n=1}^{\infty}b_n=S_2$, then $\sum\limits_{n=1}^{\infty}(a_n\pm b_n)=S_1\pm S_2$ |
| Finite modification | Adding or removing finitely many terms does not affect convergence |
| Grouping terms | Grouping consecutive terms of a convergent series, without rearranging their order, preserves convergence and the same sum |
| Necessary condition | If $\sum\limits_{n=1}^{\infty}a_n$ converges, then $\lim\limits_{n\to\infty}a_n=0$ |
| Divergence test | If $\lim_{n\to\infty}a_n$ does not exist, or exists but is not equal to $0$, then $\sum_{n=1}^{\infty}a_n$ diverges |

##### Cauchy criterion

A necessary condition for

$$
\sum_{n=1}^{\infty}u_n
$$

to converge is

$$
\lim_{n\to\infty}u_n=0
$$

The necessary and sufficient condition is that for every $\varepsilon>0$, there exists $N\in\mathbb N$ such that for all $n>N$ and all $p\in\mathbb N$

$$
|u_{n+1}+u_{n+2}+\cdots+u_{n+p}|<\varepsilon
$$

##### Convergence tests

Assume $a_n>0$ and $b_n>0$ for all  $n$.

| Test | Criterion | Conclusion |
|---|---|---|
| Bounded partial sums | $S_n=\sum\limits_{i=1}^{n}a_i$ is bounded above | $\sum\limits_{n=1}^{\infty}a_n$ converges |
| Limit comparison | $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=l$ and $0<l<+\infty$ | $\sum a_n$ and $\sum b_n$ have the same convergence behavior |
| Limit comparison | $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=0$ and $\sum b_n$ converges | $\sum a_n$ converges |
| Limit comparison | $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n}=+\infty$ and $\sum b_n$ diverges | $\sum a_n$ diverges |
| D'Alembert ratio test | $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=r<1$ | $\sum a_n$ converges |
| D'Alembert ratio test | $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=r>1$ | $\sum a_n$ diverges |
| D'Alembert ratio test | $\lim\limits_{n\to\infty}\dfrac{a_{n+1}}{a_n}=1$ | inconclusive |
| Cauchy root test | $\lim\limits_{n\to\infty}\sqrt[n]{a_n}=\rho<1$ | $\sum a_n$ converges |
| Cauchy root test | $\lim\limits_{n\to\infty}\sqrt[n]{a_n}=\rho>1$ | $\sum a_n$ diverges |
| Cauchy root test | $\lim\limits_{n\to\infty}\sqrt[n]{a_n}=1$ | inconclusive |

##### P-series

If

$$
\lim_{n\to\infty}nu_n=l>0
$$

or

$$
\lim_{n\to\infty}nu_n=+\infty
$$

then

$$
\sum_{n=1}^{\infty}u_n
$$

diverges

If $p>1$ and

$$
\lim_{n\to\infty}n^p u_n=l
\qquad
0\le l<+\infty
$$

then

$$
\sum_{n=1}^{\infty}u_n
$$

converges

##### Leibniz theorem

For the alternating series

$$
\sum_{n=1}^{\infty}(-1)^n u_n
$$

if $u_n\ge0$, $\{u_n\}$ is monotone decreasing, and

$$
\lim_{n\to\infty}u_n=0
$$

then the series converges

Moreover

$$
|S|\le u_1
\qquad
|r_n|\le u_{n+1}
$$

##### Common series

| Series | Form | Convergence |
|---|---|---|
| Harmonic series | $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n}=1+\frac12+\frac13+\cdots$ | Divergent |
| p-series | $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n^p}=1+\frac{1}{2^p}+\frac{1}{3^p}+\cdots$ | Converges for $p>1$ and diverges for $p\le1$ |
| Geometric series | $\displaystyle \sum_{n=1}^{\infty}aq^{n-1}=a+aq+aq^2+\cdots$ | Converges for $|q|<1$ |

For the geometric series with $|q|<1$

$$
\sum_{n=1}^{\infty}aq^{n-1}=\frac{a}{1-q}
$$

### Power Series

##### Definition

A series of the form

$$
\sum_{n=0}^{\infty}a_nx^n
=a_0+a_1x+a_2x^2+\cdots+a_nx^n+\cdots
$$

is called a power series

##### Radius of convergence

For the power series

$$
\sum_{n=0}^{\infty}a_nx^n
$$

let

$$
l=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|
$$

or

$$
l=\lim_{n\to\infty}\sqrt[n]{|a_n|}
$$

provided the corresponding limit exists. For the ratio formula, assume $a_n\ne0$ for all sufficiently large $n$.

Then the radius of convergence is

$$
R=\frac{1}{l}\quad l\ne0
$$

$$
R=+\infty\quad l=0
$$

$$
R=0\quad l=+\infty
$$

If $0<R<+\infty$, the endpoints $x=\pm R$ must be checked separately.

##### Properties of power series

**Abel's theorem and absolute convergence**

If a power series converges at $x=x_1\ne0$, then it converges absolutely for

$$
|x|<|x_1|
$$

If a power series diverges at $x=x_2\ne0$, then it diverges for

$$
|x|>|x_2|
$$

**Termwise integration and differentiation**

If $x\in(-R,R)$ and

$$
S(x)=\sum_{n=0}^{\infty}a_nx^n
$$

then

$$
\int_0^x S(t)\,dt
=
\int_0^x\left(\sum_{n=0}^{\infty}a_nt^n\right)dt
=
\sum_{n=0}^{\infty}\int_0^x a_nt^n\,dt
$$

$$
S'(x)
=\left(\sum_{n=0}^{\infty}a_nx^n\right)'
=
\sum_{n=1}^{\infty}na_nx^{n-1}
$$

The new power series obtained by termwise integration or differentiation has the same radius of convergence

##### Taylor series

If $f(x)$ has a Taylor expansion at $x=x_0$, then

$$
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n
$$

##### Maclaurin series

At $x_0=0$

$$
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n
$$

##### Examples

**eg.**

**Problem.**

Let $x_1=2021$ and

$$
x_n^2-2(x_n+1)x_{n+1}+2021=0
\qquad
n\ge1
$$

Prove that $\{x_n\}$ converges and find

$$
\lim_{n\to\infty}x_n
$$

**Solution.**

$$
x_{n+1}=\frac{x_n^2+2021}{2(x_n+1)}>0
$$

Let

$$
a=\sqrt{2022}-1
\qquad
a^2+2a-2021=0
$$

Then

$$
\begin{aligned}
x_{n+1}-a
&=\frac{x_n^2+2021}{2(x_n+1)}-a \\
&=\frac{x_n^2+2021-2a(x_n+1)}{2(x_n+1)} \\
&=\frac{x_n^2+a^2+2a-2a(x_n+1)}{2(x_n+1)} \\
&=\frac{(x_n-a)^2}{2(x_n+1)}\ge0
\end{aligned}
$$

Since $x_1=2021>a$, induction gives

$$
x_n\ge a
$$

Moreover,

$$
\begin{aligned}
x_{n+1}-x_n
&=\frac{x_n^2+2021}{2(x_n+1)}-x_n \\
&=\frac{-x_n^2-2x_n+2021}{2(x_n+1)} \\
&=-\frac{(x_n-a)(x_n+a+2)}{2(x_n+1)}\le0.
\end{aligned}
$$

Therefore $\{x_n\}$ is monotone decreasing and bounded below by $a$, so it converges.

Let

$$
\lim_{n\to\infty}x_n=L.
$$

Then

$$
L^2-2(L+1)L+2021=0
$$

that is

$$
L^2+2L-2021=0
\qquad
L=-1\pm\sqrt{2022}.
$$

Since $L\ge a>0$,

$$
\lim_{n\to\infty}x_n=\sqrt{2022}-1
$$

**eg.**

**Problem.**

Let $\{a_n\}$ satisfy

$$
a_1=1
\qquad
 a_{n+1}=\frac{a_n}{(n+1)(a_n+1)}
\qquad
n\ge1
$$

Find

$$
\lim_{n\to\infty}n!a_n
$$

**Solution.**

$$
b_n=n!a_n
$$

$$
b_{n+1}=(n+1)!a_{n+1}
=\frac{(n+1)!a_n}{(n+1)(a_n+1)}
=\frac{n!a_n}{a_n+1}
=\frac{b_n}{\dfrac{b_n}{n!}+1}
$$

$$
\frac{1}{b_{n+1}}=\frac{1}{b_n}+\frac{1}{n!}
$$

$$
\lim_{n\to\infty}\frac{1}{b_n}
=\frac{1}{b_1}+\lim_{n\to\infty}\sum_{k=1}^{n-1}\frac{1}{k!}
=\lim_{n\to\infty}\sum_{k=0}^{n-1}\frac{1}{k!}=e
$$

$$
\lim_{n\to\infty}b_n=\frac{1}{e}
$$

$$
\lim_{n\to\infty}n!a_n=\frac{1}{e}
$$

**eg.**

**Problem.**

Evaluate

$$
\lim_{x\to1^-}(1-x)^3\sum_{n=1}^{\infty}n^2x^n
$$

**Solution.**

For $|x|<1$,

$$
\sum_{n=1}^{\infty}x^n=\frac{x}{1-x}
$$

$$
\sum_{n=1}^{\infty}nx^n
=x\left(\sum_{n=1}^{\infty}x^n\right)'
=x\left(\frac{x}{1-x}\right)'
=\frac{x}{(1-x)^2}
$$

$$
\begin{aligned}
\sum_{n=1}^{\infty}n^2x^n
&=x\left(\sum_{n=1}^{\infty}nx^n\right)' \\
&=x\left(\frac{x}{(1-x)^2}\right)' \\
&=\frac{x(1+x)}{(1-x)^3}
\end{aligned}
$$

Therefore,

$$
(1-x)^3\sum_{n=1}^{\infty}n^2x^n=x(1+x)
$$

and

$$
\lim_{x\to1^-}x(1+x)=2
$$

**eg.**

**Problem.**

Find the interval of convergence and the sum function of

$$
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^{2n}}{n(2n-1)}
$$

**Solution.**

$$
S(x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^{2n}}{n(2n-1)}
$$

For $|x|<1$,

$$
S'(x)=\sum_{n=1}^{\infty}\frac{2(-1)^{n-1}x^{2n-1}}{2n-1}
$$

$$
S''(x)=2\sum_{n=1}^{\infty}(-x^2)^{n-1}
=\frac{2}{1+x^2}
$$

At $x=\pm1$,

$$
\sum_{n=1}^{\infty}\left|\frac{(-1)^{n-1}x^{2n}}{n(2n-1)}\right|
=\sum_{n=1}^{\infty}\frac{1}{n(2n-1)}
$$

converges because

$$
\frac{1}{n(2n-1)}\sim\frac{1}{2n^2}.
$$

Therefore, the interval of convergence is

$$
[-1,1].
$$

Since $S(0)=0$ and $S'(0)=0$,

$$
S'(x)=2\arctan x
$$

$$
S(x)=\int_0^x2\arctan t\,dt
=2x\arctan x-2\int_0^x\frac{t}{1+t^2}\,dt
=2x\arctan x-\ln(1+x^2)
$$

By continuity, the same sum function holds on $[-1,1]$.

**eg.**

**Problem.**

Let $\{x_n\}$ satisfy

$$
x_0=\frac{1}{3}
\qquad
x_{n+1}=\frac{x_n^2}{1-x_n+x_n^2}
\qquad
n\ge0
$$

Prove that

$$
\sum_{n=0}^{\infty}x_n
$$

converges and find its sum

**Solution.**

$$
x_{n+1}-1=\frac{x_n^2}{1-x_n+x_n^2}-1
=\frac{x_n-1}{1-x_n+x_n^2}
$$

$$
\frac{1}{x_{n+1}-1}
=\frac{1-x_n+x_n^2}{x_n-1}
=\frac{1+x_n(x_n-1)}{x_n-1}
=\frac{1}{x_n-1}+x_n
$$

$$
x_n=\frac{1}{x_{n+1}-1}-\frac{1}{x_n-1}
$$

$$
\sum_{k=0}^{n}x_k
=\frac{1}{x_{n+1}-1}-\frac{1}{x_0-1}
=\frac{1}{x_{n+1}-1}+\frac{3}{2}
$$

$$
x_0=\frac13\ge0
\qquad
x_{n+1}=\frac{x_n^2}{1-x_n+x_n^2}\ge0
\qquad
x_n\ge0
$$

$$
x_{n+1}-x_n
=\frac{-x_n(x_n-1)^2}{1-x_n+x_n^2}\le0
$$

$$
\{x_n\}\text{ is monotone decreasing}
\qquad
\{x_n\}\text{ converges}
$$

$$
\lim_{n\to\infty}x_n=x
\qquad
0\le x<\frac13
$$

$$
x(1-x+x^2)=x^2
\qquad
x(x-1)^2=0
\qquad
x=0
$$

$$
\sum_{k=0}^{\infty}x_k=-1+\frac32=\frac12
$$

**eg.**

**Problem.**

Suppose the positive-term series

$$
\sum_{n=1}^{\infty}a_n
$$

converges. Prove that there exists a convergent positive-term series

$$
\sum_{n=1}^{\infty}b_n
$$

such that

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=0
$$

**Solution.**

$$
R_n=\sum_{i=n}^{\infty}a_i
\qquad
 a_n=R_n-R_{n+1}
$$

$$
\{R_n\}\text{ is monotone decreasing}
\qquad
\lim_{n\to\infty}R_n=0
$$

$$
b_n=\sqrt{R_n}-\sqrt{R_{n+1}}
$$

$$
\sum_{k=1}^{n}b_k
=\sqrt{R_1}-\sqrt{R_{n+1}}
$$

$$
\lim_{n\to\infty}\frac{a_n}{b_n}
=\lim_{n\to\infty}\frac{R_n-R_{n+1}}{\sqrt{R_n}-\sqrt{R_{n+1}}}
=\lim_{n\to\infty}\left(\sqrt{R_n}+\sqrt{R_{n+1}}\right)=0
$$

**eg.**

**Problem.**

Let

$$
u_n=\int_0^1\frac{dt}{(1+t^4)^n}
\qquad
n\ge1
$$

Prove that $\{u_n\}$ converges and find

$$
\lim_{n\to\infty}u_n
$$

Prove that

$$
\sum_{n=1}^{\infty}(-1)^n u_n
$$

is conditionally convergent

**Solution.**

$$
u_n=\int_0^1\frac{dt}{(1+t^4)^n}
\ge
\int_0^1\frac{dt}{(1+t^4)^{n+1}}
=u_{n+1}
$$

Thus $\{u_n\}$ is monotone decreasing and bounded below by $0$, so it converges.

For any $\varepsilon\in(0,1)$,

$$
u_n
=
\int_0^\varepsilon\frac{dt}{(1+t^4)^n}
+
\int_\varepsilon^1\frac{dt}{(1+t^4)^n}
\le
\varepsilon+\frac{1-\varepsilon}{(1+\varepsilon^4)^n}
$$

Therefore,

$$
0\le\lim_{n\to\infty}u_n\le\varepsilon.
$$

Letting $\varepsilon\to0^+$ gives

$$
\lim_{n\to\infty}u_n=0.
$$

Hence

$$
\sum_{n=1}^{\infty}(-1)^n u_n
$$

converges by Leibniz theorem.

For $n>1$,

$$
u_n
=\int_0^1\frac{dt}{(1+t^4)^n}
\ge
\int_0^1\frac{dt}{(1+t)^n}
=\frac{1-2^{1-n}}{n-1}>0.
$$

Since

$$
\frac{1-2^{1-n}}{n-1}\sim\frac{1}{n},
$$

we have

$$
\sum_{n=1}^{\infty}u_n\text{ diverges}.
$$

Therefore,

$$
\sum_{n=1}^{\infty}(-1)^nu_n
$$

is conditionally convergent.
