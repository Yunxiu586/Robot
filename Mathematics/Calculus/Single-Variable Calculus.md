# Single-Variable Calculus

[toc]

### Limits

##### Limits of sequences

| Property                   | Statement                                                    |
| -------------------------- | ------------------------------------------------------------ |
| Uniqueness and boundedness | If a sequence $\{x_n\}$ converges, then its limit is unique and $\{x_n\}$ is bounded. |
| Monotone convergence       | A monotone bounded sequence has a finite limit.              |
| Order preservation         | If $x_n \le y_n$, $\lim\limits_{n\to\infty}x_n=a$, and $\lim\limits_{n\to\infty}y_n=b$, then $a\le b$. |
| Sign preservation          | If $\lim\limits_{n\to\infty}x_n=a>0$ or $a<0$, then there exists $N\in\mathbb{N}$ such that, for $n>N$, $x_n>0$ or $x_n<0$. |

##### Existence criteria for limits

**Squeeze theorem**.

If
$$
y_n\le x_n\le z_n
\\
\lim_{n\to\infty}y_n=\lim_{n\to\infty}z_n=a
$$

then

$$
\lim_{n\to\infty}x_n=a
$$

**Monotone bounded criterion**.

A monotone bounded sequence converges.

**One-sided limits**.

For a finite point $x_0$,
$$
\lim_{x\to x_0}f(x)=a
\iff
\lim_{x\to x_0^+}f(x)=a
\quad\text{and}\quad
\lim_{x\to x_0^-}f(x)=a
$$

##### Two important limits

$$
\lim_{x\to0}\frac{\sin x}{x}=1
$$

More generally, if $\lim\limits_{x\to x_0}f(x)=0$, then
$$
\lim_{x\to x_0}\frac{\sin f(x)}{f(x)}=1
$$

The exponential limit is

$$
\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e
$$

Equivalent forms are

$$
\lim_{x\to0}(1+x)^{1/x}=e
$$

and, if $\lim\limits_{x\to x_0}g(x)=\infty$,

$$
\lim_{x\to x_0}\left(1+\frac{1}{g(x)}\right)^{g(x)}=e
$$

If $\lim\limits_{x\to x_0}g(x)=0$, then

$$
\lim_{x\to x_0}\left(1+g(x)\right)^{1/g(x)}=e
$$

For sequences,

$$
\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e
$$

##### L'Hospital's rule

L'Hospital's rule applies to indeterminate forms of type
$$
\frac{0}{0},
\qquad
\frac{\infty}{\infty}.
$$

Assume that $f$ and $g$ are differentiable in a punctured neighborhood of the limiting point, $g'(x)\ne0$, and
$$
f(x),g(x)\to0
\quad\text{or}\quad
|f(x)|,|g(x)|\to\infty.
$$

Other forms can often be transformed into these forms:

| Form                          | Common transformation                                     |
| ----------------------------- | --------------------------------------------------------- |
| $0\cdot\infty$                | Put one factor in the denominator.                        |
| $\infty-\infty$               | Combine terms by a common denominator or rationalization. |
| $1^\infty$, $0^0$, $\infty^0$ | Take logarithms first.                                    |

If

$$
\lim_{x\to x_0}\frac{f'(x)}{g'(x)}=k,
$$

where $k$ is finite or infinite, then

$$
\lim_{x\to x_0}\frac{f(x)}{g(x)}=k.
$$

##### Equivalent infinitesimals as $x\to0$

$$
\sin x\sim \arcsin x\sim x
$$

$$
\tan x\sim \arctan x\sim x
$$

$$
\ln(1+x)\sim e^x-1\sim x
$$

$$
x-\sin x\sim \frac{x^3}{6}
$$

$$
1-\cos x\sim \frac{x^2}{2}
$$

$$
(1+x)^a-1\sim ax
$$

A more precise first-order form is

$$
(1+x)^a=1+ax+o(x)
$$

##### Continuity and discontinuities

A function $f$ is continuous at $x_0$ if and only if

$$
f(x_0)=f(x_0+0)=f(x_0-0)
$$

| Type        | Name                      | Description                                                  |
| ----------- | ------------------------- | ------------------------------------------------------------ |
| First kind  | Removable discontinuity   | $\lim\limits_{x\to x_0}f(x)$ exists, but $f(x_0)$ is undefined or not equal to this limit. |
| First kind  | Jump discontinuity        | The one-sided limits exist and are finite, but they are not equal. |
| Second kind | Infinite discontinuity    | At least one of $f(x_0+0)$ and $f(x_0-0)$ is infinite.       |
| Second kind | Oscillatory discontinuity | The function oscillates without approaching a finite one-sided limit. |

##### Examples

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{x\to3}\frac{\sqrt{x^3+9}-6}{2-\sqrt{x^3-23}}
$$

**Solution.**

$$
\lim_{x\to3}\frac{\sqrt{x^3+9}-6}{2-\sqrt{x^3-23}}
=
\lim_{x\to3}\left(-\frac{6}{2}\right)
\frac{\sqrt{\dfrac{x^3-27}{36}+1}-1}{\sqrt{\dfrac{x^3-27}{4}+1}-1}
=
\lim_{x\to3}\left(-\frac{6}{2}\right)\frac{1/36}{1/4}
=-\frac{1}{3}
$$

$$
\begin{aligned}
\lim_{x\to3}\frac{\sqrt{x^3+9}-6}{2-\sqrt{x^3-23}}
&=\lim_{x\to3}
\frac{(2+\sqrt{x^3-23})(\sqrt{x^3+9}+6)(\sqrt{x^3+9}-6)}
{(2+\sqrt{x^3-23})(\sqrt{x^3+9}+6)(2-\sqrt{x^3-23})}\\
&=\lim_{x\to3}
\frac{2+\sqrt{x^3-23}}{\sqrt{x^3+9}+6}\cdot
\frac{x^3+9-36}{4-(x^3-23)}\\
&=\frac{4}{12}\cdot(-1)=-\frac{1}{3}
\end{aligned}
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{x\to\infty}\sqrt{x^2+x+1}\,\frac{x-\ln(e^x+x)}{x}
$$

**Solution.**

$$
\lim_{x\to\infty}\sqrt{x^2+x+1}\,\frac{x-\ln(e^x+x)}{x}
=
\lim_{x\to\infty}\frac{\sqrt{x^2+x+1}}{x}\ln\frac{e^x}{e^x+x}
=1\cdot0=0
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{x\to\infty}\frac{e^x}{(1+x^{-1})^{x^2}}
$$

**Solution.**

$$
\lim_{x\to\infty}\frac{e^x}{(1+x^{-1})^{x^2}}
\ne
\lim_{x\to\infty}\frac{e^x}{\left[(1+x^{-1})^x\right]^x}
=
\lim_{x\to\infty}\frac{e^x}{e^x}=1
$$

$$
\lim_{x\to\infty}\frac{e^x}{(1+x^{-1})^{x^2}}
=
\lim_{x\to\infty}e^{x-x^2\ln(1+x^{-1})}
$$

$$
\lim_{x\to\infty}\frac{x^{-1}-\ln(1+x^{-1})}{x^{-2}}
=
\lim_{x\to\infty}\frac{\dfrac{1}{2}x^{-2}+o(x^{-2})}{x^{-2}}
=\frac{1}{2}
$$

$$
\therefore
\lim_{x\to\infty}\frac{e^x}{(1+x^{-1})^{x^2}}=e^{1/2}
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{x\to0}\frac{1-\cos x\sqrt{\cos2x}\sqrt[3]{\cos3x}}{x^2}
$$

**Solution.**

Numerator rationalization
$$
=
\lim_{x\to0}\frac{1}{6}\frac{1-\cos^6x\cos^3 2x\cos^2 3x}{x^2}.
$$

By L'Hospital's rule
$$
\lim_{x\to0}\frac{1}{6}
\left(
\frac{6}{2}+\frac{3\cdot2\cdot2}{2}+\frac{2\cdot3\cdot3}{2}
\right)=3.
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{n\to\infty}n\left(
\frac{1}{n^2}+\frac{1}{n^2+1}+\cdots+\frac{1}{n^2+n}
\right)
$$

**Solution.**

$$
\frac{n(n+1)}{n^2+n}
\le
\frac{n}{n^2}+\frac{n}{n^2+1}+\cdots+\frac{n}{n^2+n}
\le
\frac{n(n+1)}{n^2}
$$

$$
\lim_{n\to\infty}\frac{n(n+1)}{n^2+n}=1,
\lim_{n\to\infty}\frac{n(n+1)}{n^2}=1
$$

$$
\lim_{n\to\infty}n\left(
\frac{1}{n^2}+\frac{1}{n^2+1}+\cdots+\frac{1}{n^2+n}
\right)=1
$$

**eg.**

**Problem.** For a fixed real number $x$, evaluate the following limit.

$$
x\in(-\infty,+\infty),
\qquad
\lim_{n\to\infty}\frac{1}{n^2}\sum_{i=1}^n
\sqrt{(ne^x+i)(ne^x+i+1)}
$$

**Solution.**

Method 1

$$
n^2e^x+\frac{n(n+1)}{2}
=
\sum_{i=1}^n(ne^x+i)
\le
\sum_{i=1}^n\sqrt{(ne^x+i)(ne^x+i+1)}
\\
\le
\sum_{i=1}^n(ne^x+i+1)
=n^2e^x+\frac{n(n+1)}{2}+n
$$

$$
\lim_{n\to\infty}\frac{1}{n^2}\left(n^2e^x+\frac{n(n+1)}{2}\right)
\le
\lim_{n\to\infty}\frac{1}{n^2}\sum_{i=1}^n\sqrt{(ne^x+i)(ne^x+i+1)}
\\
\le
\lim_{n\to\infty}\frac{1}{n^2}\left(n^2e^x+\frac{n(n+1)}{2}+n\right)
$$

$$
\text{original expression}=e^x+\frac{1}{2}
$$

Method 2

$$
\begin{aligned}
\text{original expression}
&=
\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^n
\sqrt{\left(e^x+\frac{i}{n}\right)\left(e^x+\frac{i+1}{n}\right)}\\
&=
\int_0^1(e^x+t)\,dt
=e^x+\frac{1}{2}
\end{aligned}
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{n\to\infty}n^2\left(2^{1/n}-2^{1/(n+3)}\right)
$$

**Solution.**

$$
\begin{aligned}
\lim_{n\to\infty}n^2\left(2^{1/n}-2^{1/(n+3)}\right)
&=
\lim_{n\to\infty}n^2(2^\xi)'\left(\frac{1}{n}-\frac{1}{n+3}\right)\\
&=
\lim_{n\to\infty}n^2 2^\xi\ln2\cdot\frac{3}{n(n+3)}\\
&=3\ln2
\end{aligned}
$$

**eg.**

**Problem.** For $\alpha\in(0,1)$, evaluate the following limit.

$$
\alpha\in(0,1),
\qquad
\lim_{n\to\infty}\left[(n+1)^\alpha-n^\alpha\right]
$$

**Solution.**

$$
\alpha=\frac{1}{2}:
\lim_{n\to\infty}(\sqrt{n+1}-\sqrt n)
=
\lim_{n\to\infty}\frac{1}{\sqrt{n+1}+\sqrt n}=0
$$

$$
f(x)=x^\alpha
\\
f(n+1)-f(n)=f'(\xi)(n+1-n)=f'(\xi)=\alpha\xi^{\alpha-1}
$$

$$
\lim_{n\to\infty}\left[(n+1)^\alpha-n^\alpha\right]
=
\lim_{n\to\infty}\alpha\xi^{\alpha-1}=0
$$

**eg.**

**Problem.** Use Stolz theorem to evaluate the following limit.

$$
\lim_{n\to\infty}\frac{1^k+2^k+\cdots+n^k}{n^{k+1}}
$$

**Solution.**

If $b_n$ is strictly increasing, $b_n\to+\infty$, and

$$
\lim_{n\to\infty}
\frac{a_n-a_{n-1}}{b_n-b_{n-1}}
=L
$$

then

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=L
$$

$$
\text{Stolz theorem:}
\lim_{n\to\infty}\frac{a_n}{b_n}
=
\lim_{n\to\infty}\frac{a_n-a_{n-1}}{b_n-b_{n-1}}
$$

$$
\lim_{n\to\infty}\frac{1^k+2^k+\cdots+n^k}{n^{k+1}}
$$

$$
\begin{aligned}
\lim_{n\to\infty}\frac{1^k+2^k+\cdots+n^k}{n^{k+1}}
&=
\lim_{n\to\infty}\frac{n^k}{n^{k+1}-(n-1)^{k+1}}\\
&=
\lim_{n\to\infty}
\frac{n^k}{n^{k+1}-\left[n^{k+1}-(k+1)n^k+\dfrac{(k+1)k}{2!}n^{k-1}+\cdots\right]}\\
&=
\lim_{n\to\infty}
\frac{n^k}{(k+1)n^k-\dfrac{(k+1)k}{2!}n^{k-1}+\cdots}\\
&=
\lim_{n\to\infty}
\frac{1}{(k+1)-\dfrac{(k+1)k}{2!}n^{-1}+\cdots}
=
\frac{1}{k+1}
\end{aligned}
$$

**eg.**

**Problem.** For the sequence defined below, evaluate $\lim\limits_{n\to\infty}nx_n$.

$$
x_0=1,
\qquad
x_n=\ln(1+x_{n-1}),\quad n\ge1,
\qquad
\lim_{n\to\infty}nx_n
$$

**Solution.**

$$
\begin{aligned}
\lim_{n\to\infty}nx_n
&=
\lim_{n\to\infty}\frac{n}{1/x_n}
=
\lim_{n\to\infty}\frac{n-(n-1)}{1/x_n-1/x_{n-1}}\\
&=
\lim_{n\to\infty}\frac{x_nx_{n-1}}{x_{n-1}-x_n}
=
\lim_{n\to\infty}\frac{x_{n-1}\ln(1+x_{n-1})}{x_{n-1}-\ln(1+x_{n-1})}\\
&=
\lim_{x\to0}\frac{x\ln(1+x)}{x-\ln(1+x)}\\
&=
\lim_{x\to0}\frac{x(x+o(x))}{x-\left(x-\dfrac{1}{2}x^2+o(x^2)\right)}=2
\end{aligned}
$$

**eg.**

**Problem.** Given that $f(x)$ is continuous and $f(0)\ne0$, evaluate the following limit.

$$
f(x)\text{ is continuous},\quad f(0)\ne0,
\qquad
\lim_{x\to0}\frac{2\int_0^x(x-t)f(t)\,dt}{x\int_0^x f(x-t)\,dt}
$$

**Solution.**

$$
u=x-t
\\
\int_0^x f(x-t)\,dt
=
\int_0^x f(u)\,du
=
\int_0^x f(t)\,dt
$$

Let
$$
A(x)=\int_0^x f(t)\,dt,
\qquad
B(x)=\int_0^x tf(t)\,dt.
$$

Then
$$
\begin{aligned}
\lim_{x\to0}\frac{2\int_0^x(x-t)f(t)\,dt}{x\int_0^x f(x-t)\,dt}
&=
\lim_{x\to0}\frac{2xA(x)-2B(x)}{xA(x)}.
\end{aligned}
$$

Using L'Hospital's rule,
$$
\begin{aligned}
\lim_{x\to0}\frac{2xA(x)-2B(x)}{xA(x)}
&=
\lim_{x\to0}\frac{2A(x)+2xf(x)-2xf(x)}{A(x)+xf(x)}\\
&=
\lim_{x\to0}\frac{2A(x)}{A(x)+xf(x)}\\
&=
\lim_{x\to0}\frac{2A(x)/x}{A(x)/x+f(x)}.
\end{aligned}
$$

Since
$$
\lim_{x\to0}\frac{A(x)}{x}=f(0),
$$

we get
$$
\lim_{x\to0}\frac{2\int_0^x(x-t)f(t)\,dt}{x\int_0^x f(x-t)\,dt}
=
\frac{2f(0)}{f(0)+f(0)}=1.
$$

---

### Derivatives

##### Differentiability

A function $f$ is differentiable at $x_0$ if and only if the left and right derivatives exist and are equal

$$
f'(x_0)=f'_+(x_0)=f'_-(x_0).
$$

Differentiability implies continuity

$$
f\text{ is differentiable at }x_0
\Longrightarrow
f\text{ is continuous at }x_0.
$$

##### Common derivatives

$$
(a^x)'=a^x\ln a
\\
(\ln x)'=\frac{1}{x}
$$

$$
(\log_a x)'=\frac{1}{x\ln a}, a>0, a\ne1.
$$

$$
(\sec x)'=\sec x\tan x
\\
(\tan x)'=\sec^2x
$$

$$
(\csc x)'=-\csc x\cot x
\\
(\cot x)'=-\csc^2x
$$

$$
(\arctan x)'=\frac{1}{1+x^2}
\\
(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}
$$

$$
(\operatorname{arccot}x)'=-\frac{1}{1+x^2}
\\
(\arccos x)'=-\frac{1}{\sqrt{1-x^2}}
$$

For integer $n\ge0$,

$$
(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}{2}\right)
\\
(\cos x)^{(n)}=\cos\left(x+\frac{n\pi}{2}\right)
$$

##### Mean value theorems

**Rolle's theorem**

If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and

$$
f(a)=f(b)
$$

then there exists $\xi\in(a,b)$ such that

$$
f'(\xi)=0
$$

**Lagrange mean value theorem**

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $\xi\in(a,b)$ such that

$$
f(a)-f(b)=f'(\xi)(a-b)
$$

Equivalently,

$$
f(b)-f(a)=f'(\xi)(b-a)
$$

**Cauchy mean value theorem**

If $f$ and $F$ are continuous on $[a,b]$, differentiable on $(a,b)$, and $F'(x)\ne0$ on $(a,b)$, then there exists $\xi\in(a,b)$ such that

$$
\frac{f(a)-f(b)}{F(a)-F(b)}
=
\frac{f'(\xi)}{F'(\xi)}
$$

##### Taylor formula

For $f$ sufficiently differentiable near $x_0$,

$$
f(x)=f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)
+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots
+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+R_n(x)
$$

Integral remainder
$$
R_n(x)=\int_{x_0}^{x}\frac{f^{(n+1)}(t)}{n!}(x-t)^n\,dt
$$

Using the integral mean value theorem, one obtains the Lagrange remainder.

Lagrange remainder
$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
$$

where $\xi$ lies between $x$ and $x_0$.

Peano remainder
$$
R_n(x)=o\left((x-x_0)^n\right)
$$

##### Maclaurin formula

At $x_0=0$,

$$
f(x)=f(0)+\frac{f'(0)}{1!}x+\frac{f''(0)}{2!}x^2+
\cdots+\frac{f^{(n)}(0)}{n!}x^n+R_n(x)
$$

With Lagrange remainder,

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1},
\xi=\theta x,
\theta\in(0,1)
$$

For $|x|<1$,

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n
=1+x+x^2+x^3+\cdots
$$

For $|x|<1$,

$$
\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^nx^n
=1-x+x^2-x^3+\cdots
$$

For small $x$,

$$
e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+o(x^n)
$$

$$
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
+\frac{(-1)^{k-1}x^{2k-1}}{(2k-1)!}+o(x^{2k-1})
$$

$$
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots
+\frac{(-1)^kx^{2k}}{(2k)!}+o(x^{2k})
$$

As $x\to0$,

$$
\ln(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
+\frac{(-1)^{n-1}}{n}x^n+o(x^n)
$$
For $-1<x\le1$,

$$
\ln(1+x)=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}x^k.
$$

##### Examples

**eg.**

**Problem.** Find the tangent line of $y=f(x)$ at $(1,f(1))$ under the given condition.

$$
f(1+x)-3f(1-x)=4+2x+o(x),
\qquad
\text{tangent line of }y=f(x)\text{ at }(1,f(1))
$$

**Solution.**

$$
f(1+x)=f(1)+f'(1)x+o(x),
f(1-x)=f(1)-f'(1)x+o(x)
$$

$$
f(1)+f'(1)x+o(x)-3\left[f(1)-f'(1)x+o(x)\right]=4+2x+o(x)
$$

$$
x\to0:
-2f(1)=4,
f(1)=-2
$$

$$
4f'(1)=2,
\qquad
f'(1)=\frac{1}{2}.
$$

$$
y=\frac{1}{2}x-\frac{5}{2}
$$

**eg.**

**Problem.** Find $f^{(n)}(-1)$ for the following function.

$$
f(x)=(x+1)^n e^{-x^2},
\qquad
f^{(n)}(-1)
$$

**Solution.**

$$
g(x)=f(x-1)=x^n e^{-(x-1)^2}
\\
g^{(n)}(0)=f^{(n)}(-1)
$$

Since $g(x)=x^ne^{-(x-1)^2}$, the value $g^{(n)}(0)$ is determined by the coefficient of $x^n$ in the Taylor expansion of $g(x)$ at $0$.

$$
e^{-(x-1)^2}=e^{-1}+O(x),
\qquad
g(x)=e^{-1}x^n+O(x^{n+1})
$$

$$
g^{(n)}(0)=\frac{n!}{e}
$$

$$
f^{(n)}(-1)=\frac{n!}{e}
$$

**eg.**

**Problem.** Find $f^{(n)}(0)$ for the following function.

$$
f(x)=\frac{1}{x^2-3x+2},
\qquad
f^{(n)}(0)
$$

**Solution.**

$$
f(x)=\frac{1}{x^2-3x+2}=\frac{1}{x-2}-\frac{1}{x-1}
$$

$$
f^{(n)}(x)=\frac{(-1)^n n!}{(x-2)^{n+1}}-\frac{(-1)^n n!}{(x-1)^{n+1}}
$$

$$
f^{(n)}(0)=n!\left(1-\frac{1}{2^{n+1}}\right)
$$

**eg.**

**Problem.** For $n\le2023$, find $f^{(n)}(0)$ for the following function.

$$
f(x)=e^{-x}\int_0^x\frac{t^{2023}}{1+t^2}\,dt,
\qquad
n\le2023,
\qquad
f^{(n)}(0)
$$

**Solution.**

$$
\begin{aligned}
f(x)
&=e^{-x}\int_0^x\frac{t^{2023}}{1+t^2}\,dt\\
&=
\left[\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}x^n\right]
\int_0^x t^{2023}\sum_{n=0}^{\infty}(-t^2)^n\,dt\\
&=
\left[\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}x^n\right]
\int_0^x\sum_{n=0}^{\infty}(-1)^n t^{2n+2023}\,dt\\
&=
\left[\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}x^n\right]
\left[\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+2024}}{2n+2024}\right]
=
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n
\end{aligned}
$$

$$
\min\deg_x=2024,
\qquad
n\le2023:
\quad
f^{(n)}(0)=0
$$

**eg.**

**Problem.** Given the following assumptions, evaluate the limit.

$$
\lim_{x\to0}f(x)=\lim_{x\to0}g(x)=a>0,
\qquad
f(x)\ne g(x)
$$

$$
\lim_{x\to0}\frac{[f(x)]^{g(x)}-[g(x)]^{g(x)}}{f(x)-g(x)}
$$

**Solution.**

$$
h(t)=t^{g(x)},
h'(\xi)=\frac{h(f(x))-h(g(x))}{f(x)-g(x)}
$$

$$
\text{original limit}
=
\lim_{x\to0}h'(\xi)
=
\lim_{x\to0}g(x)\xi^{g(x)-1}
=a\cdot a^{a-1}=a^a
$$

### Indefinite Integrals

$$
\int f(\varphi(x))\varphi'(x)\,dx
=\int f(\varphi(x))\,d\varphi(x)
=\int f(u)\,du
$$

$$
\int u\,dv=uv-\int v\,du
$$

##### Universal tangent half-angle substitution

Let

$$
u=\tan\frac{x}{2}
$$

Then

$$
\sin x=\frac{2u}{1+u^2}
\\
\cos x=\frac{1-u^2}{1+u^2}
\\
dx=\frac{2\,du}{1+u^2}
$$

##### Trigonometric identities

$$
\sin^2x+\cos^2x=1
\\
\sec^2x-\tan^2x=1
$$

$$
\arctan x+\arctan\frac{1}{x}=\frac{\pi}{2} (x>0)
$$

If $1+xy>0$, then

$$
\arctan x-\arctan y
=
\arctan\frac{x-y}{1+xy}
$$

In general, the right-hand side may differ by an integer multiple of $\pi$ because of the branch of $\arctan$.

Sum-to-product formulas

$$
\sin\alpha+\sin\beta
=2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}
$$

$$
\sin\alpha-\sin\beta
=2\cos\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}
$$

$$
\cos\alpha+\cos\beta
=2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}
$$

$$
\cos\alpha-\cos\beta
=-2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}
$$

Product-to-sum formulas

$$
\sin\alpha\cos\beta
=\frac{1}{2}\left[\sin(\alpha+\beta)+\sin(\alpha-\beta)\right]
$$

$$
\cos\alpha\sin\beta
=\frac{1}{2}\left[\sin(\alpha+\beta)-\sin(\alpha-\beta)\right]
$$

$$
\cos\alpha\cos\beta
=\frac{1}{2}\left[\cos(\alpha+\beta)+\cos(\alpha-\beta)\right]
$$

$$
\sin\alpha\sin\beta
=-\frac{1}{2}\left[\cos(\alpha+\beta)-\cos(\alpha-\beta)\right]
$$

##### Examples

**eg.**

**Problem.** Evaluate the following infinite series.

$$
\sum_{n=1}^{\infty}\arctan\frac{2}{4n^2+4n+1}
$$

**Solution.**

$$
\arctan\frac{2}{4n^2+4n+1}
=
\arctan\frac{(2n+2)-(2n)}{1+(2n+2)(2n)}
=
\arctan(2n+2)-\arctan(2n)
$$

$$
\text{original expression}
=
\sum_{n=1}^{\infty}\left[\arctan(2n+2)-\arctan(2n)\right]
=
\frac{\pi}{2}-\arctan2
=
\arctan\frac{1}{2}
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\tan x\,dx
$$

**Solution.**

$$
\int\tan x\,dx=-\ln|\cos x|+C
$$

$$
\int\tan x\,dx
=
\int\frac{\sin x}{\cos x}\,dx
=-\int\frac{d\cos x}{\cos x}
=-\ln|\cos x|+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\sec x\,dx
$$

**Solution.**

$$
\int\sec x\,dx=\ln|\sec x+\tan x|+C
$$

Method 1

$$
\begin{aligned}
\int\sec x\,dx
&=
\int\sec x\frac{\sec x+\tan x}{\sec x+\tan x}\,dx\\
&=
\int\frac{\sec^2x+\sec x\tan x}{\sec x+\tan x}\,dx\\
&=
\int\frac{d(\tan x+\sec x)}{\sec x+\tan x}
=
\ln|\sec x+\tan x|+C
\end{aligned}
$$

Method 2

$$
\begin{aligned}
\int\sec x\,dx
&=
\int\sec x\frac{\sec x-\tan x}{\sec x-\tan x}\,dx\\
&=
\int\frac{\sec^2x-\sec x\tan x}{\sec x-\tan x}\,dx\\
&=
\int\frac{d(\tan x-\sec x)}{\sec x-\tan x}
=-\ln|\sec x-\tan x|+C
\end{aligned}
$$

Method 3

$$
u=\tan\frac{x}{2},
\qquad
\sec x=\frac{1+u^2}{1-u^2},
\qquad
dx=\frac{2\,du}{1+u^2}.
$$

$$
\begin{aligned}
\int\sec x\,dx
&=\int\frac{1+u^2}{1-u^2}\frac{2\,du}{1+u^2}
=\int\frac{2\,du}{1-u^2}\\
&=\int\left(\frac{1}{1-u}+\frac{1}{1+u}\right)du
=\ln\left|\frac{1+u}{1-u}\right|+C\\
&=
\ln\left|\frac{1+\tan(x/2)}{1-\tan(x/2)}\right|+C
\end{aligned}
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{dx}{2^x(1+4^x)}
$$

**Solution.**

$$
\int\frac{dx}{2^x(1+4^x)}
=
\int\frac{2^x\,dx}{4^x(1+4^x)}
=
\frac{1}{\ln2}\int\left(\frac{1}{4^x}-\frac{1}{1+4^x}\right)d(2^x)
$$

$$
=
-\frac{1}{\ln2}\left(\frac{1}{2^x}+\arctan2^x\right)+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{x^2+1}{x^4+1}\,dx
$$

**Solution.**

$$
\begin{aligned}
\text{original expression}
&=
\int\frac{1+\dfrac{1}{x^2}}{x^2+\dfrac{1}{x^2}}\,dx
=
\int\frac{d\left(x-\dfrac{1}{x}\right)}{\left(x-\dfrac{1}{x}\right)^2+2}\\
&=
\frac{1}{\sqrt2}\int
\frac{d\left[\left(x-\dfrac{1}{x}\right)\dfrac{1}{\sqrt2}\right]}
{\left[\left(x-\dfrac{1}{x}\right)\dfrac{1}{\sqrt2}\right]^2+1}\\
&=
\frac{1}{\sqrt2}\arctan\frac{x^2-1}{\sqrt2x}+C
\end{aligned}
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{dx}{x^4(1+x^2)}
$$

**Solution.**

$$
t=\frac{1}{x}
$$

$$
\text{original expression}
=-\int\frac{t^4}{1+t^2}\,dt
=-\int\frac{t^4-1}{1+t^2}\,dt-\int\frac{dt}{1+t^2}
=-\frac{t^3}{3}+t-\arctan t+C
$$

$$
=
\frac{3x^2-1}{3x^3}-\arctan\frac{1}{x}+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{dx}{\sqrt{x(1-x)}}
$$

**Solution.**

$$
t=\sqrt{x}
\\
\text{original expression}
=
\int\frac{2\,dt}{\sqrt{1-t^2}}
=2\arcsin t+C
=2\arcsin\sqrt{x}+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{\cos x-2\sin x}{\sin x+2\cos x}\,dx
$$

**Solution.**

$$
\int\frac{\cos x-2\sin x}{\sin x+2\cos x}\,dx
=
\int\frac{d(\sin x+2\cos x)}{\sin x+2\cos x}
=
\ln|\sin x+2\cos x|+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{\sin2x}{1+\cos^2x}\,dx
$$

**Solution.**

$$
\begin{aligned}
\text{original expression}
&=
\int\frac{2\sin x\cos x}{1+\cos^2x}\,dx
=-\int\frac{2\cos x\,d\cos x}{1+\cos^2x}
\\
&=-\int\frac{d\cos^2x}{1+\cos^2x}
=-\ln(1+\cos^2x)+C
\end{aligned}
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{dx}{\sin^2x+2\cos^2x}
$$

**Solution.**

$$
\text{original expression}
=
\int\frac{dx}{\cos^2x(\tan^2x+2)}
=
\int\frac{d\tan x}{\tan^2x+2}
=
\frac{1}{\sqrt2}\arctan\frac{\tan x}{\sqrt2}+C
$$

**eg.**

**Problem.** Evaluate the following indefinite integral.

$$
\int\frac{\ln\left(x+\sqrt{1+x^2}\right)}{(1+x^2)^{3/2}}\,dx
$$

**Solution.**

$$
\left[\ln\left(x+\sqrt{1+x^2}\right)\right]'=\frac{1}{\sqrt{1+x^2}}
$$

$$
x=\tan t
\\
\int\frac{1}{(1+x^2)^{3/2}}\,dx
=
\int\frac{1}{\sec^3t}\sec^2t\,dt
=
\int\cos t\,dt
=
\frac{x}{\sqrt{1+x^2}}+C
$$

$$
\begin{aligned}
\int\frac{\ln\left(x+\sqrt{1+x^2}\right)}{(1+x^2)^{3/2}}\,dx
&=
\int\ln\left(x+\sqrt{1+x^2}\right)d\frac{x}{\sqrt{1+x^2}}\\
&=
\frac{x\ln\left(x+\sqrt{1+x^2}\right)}{\sqrt{1+x^2}}
-
\int\frac{x}{1+x^2}\,dx\\
&=
\frac{x\ln\left(x+\sqrt{1+x^2}\right)}{\sqrt{1+x^2}}
-\frac{1}{2}\ln|1+x^2|+C
\end{aligned}
$$

**eg.**

**Problem.** For the implicit function $y=y(x)$, evaluate the following integral.

$$
y=y(x),
\qquad
y^2(x-y)=x^2,
\qquad
\int\frac{dx}{y^2}
$$

**Solution.**

$$
t=\frac{y}{x}
\\
t^2(x-tx)=1
$$

$$
\begin{cases}
\displaystyle x=\frac{1}{t^2(1-t)}\\[6pt]
\displaystyle y=\frac{1}{t(1-t)}
\end{cases}
$$

$$
\int\frac{dx}{y^2}
=
\int t^2(1-t)^2\left[-\frac{2t-3t^2}{t^4(1-t)^2}\right]dt
=-\int\left(\frac{2}{t}-3\right)dt
=-2\ln|t|+3t+C
$$

$$
=-2\ln\left|\frac{y}{x}\right|+3\frac{y}{x}+C
$$

**eg.**

**Problem.** For a constant $a$, evaluate the following indefinite integral.

$$
a\text{ constant},
\qquad
a\ne0,
\qquad
\int\frac{a\,dy}{3a^2-2ay+3y^2}
$$

**Solution.**

$$
\int\frac{d(y/a)}{3(y/a)^2-2(y/a)+3}
=
\int\frac{dt}{3\left(t^2-\dfrac{2}{3}t+\dfrac{1}{9}\right)-\dfrac{1}{3}+3}
=
\frac{1}{3}\int\frac{dt}{\left(t-\dfrac{1}{3}\right)^2+\dfrac{8}{9}}
$$

$$
=
\frac{1}{2\sqrt2}\arctan\frac{3t-1}{2\sqrt2}+C
=
\frac{1}{2\sqrt2}\arctan\frac{3y-a}{2a\sqrt2}+C
$$

### Definite Integrals

If

$$
F(x)=\int_{a(x)}^{b(x)}f(t)\,dt
$$

then

$$
F'(x)=f(b(x))b'(x)-f(a(x))a'(x)
$$

##### Symmetry

For integrals over symmetric intervals,

$$
\int_{-a}^{a}f(x)\,dx
=
\begin{cases}
0 & f \text{ is odd}\\[4pt]
2\int_0^a f(x)\,dx & f \text{ is even}
\end{cases}
$$

For intervals symmetric with respect to the origin,

$$
\int_a^b f(x)\,dx
=
\begin{cases}
-\displaystyle\int_{-b}^{-a}f(x)\,dx & f \text{ is odd}\\[8pt]
\displaystyle\int_{-b}^{-a}f(x)\,dx & f \text{ is even}
\end{cases}
$$

$$
\int_0^\pi f(\sin x)\,dx
=2\int_0^{\pi/2}f(\sin x)\,dx
$$

$$
\int_0^\pi x f(\sin x)\,dx
=\frac{\pi}{2}\int_0^\pi f(\sin x)\,dx
$$

$$
\int_0^{\pi/2}f(\sin x)\,dx
=
\int_0^{\pi/2}f(\cos x)\,dx
$$

Basic values

$$
\int_0^\pi \sin x\,dx=2
\\
\int_0^\pi \cos x\,dx=0
$$

$$
\int_0^{\pi/2}\sin x\,dx=1
\\
\int_0^{\pi/2}\sin^2x\,dx=\frac{\pi}{4}
\\
\int_0^{\pi/2}\sin^3x\,dx=\frac{2}{3}
$$

For $n\ge1$,

$$
\int_0^{\pi/2}\sin^n x\,dx
=
\int_0^{\pi/2}\cos^n x\,dx
$$

Reduction formula

$$
\int_0^{\pi/2}\sin^n x\,dx
=
\begin{cases}
\dfrac{n-1}{n}\dfrac{n-3}{n-2}\cdots\dfrac{1}{2}\cdot\dfrac{\pi}{2} & n \text{ even}\\[10pt]
\dfrac{n-1}{n}\dfrac{n-3}{n-2}\cdots\dfrac{2}{3} & n \text{ odd}
\end{cases}
$$

##### Integral mean value theorem

If $f$ is continuous on $[a,b]$, then there exists $\xi\in(a,b)$ such that

$$
\int_a^b f(x)\,dx=f(\xi)(b-a)
$$

For $a<b$,

$$
\left|\int_a^b f(x)\,dx\right|
\le
\int_a^b |f(x)|\,dx
$$

If $m\le f(x)\le M$ on $[a,b]$, then

$$
m(b-a)\le\int_a^b f(x)\,dx\le M(b-a)
$$

##### Interval reproduction formula

For an integral over $[a,b]$,

$$
\int_a^b f(x)\,dx
=
\int_a^b f(a+b-x)\,dx
$$

Example:

$$
\int_0^{\pi/2}f(\sin x)\,dx
=
\int_0^{\pi/2}f(\cos x)\,dx
$$

##### Examples

**eg.**

**Problem.** Evaluate the following definite integral.

$$
\int_0^{\pi/2}\frac{\cos^2\theta\sin^2\theta}{(\cos^3\theta+\sin^3\theta)^2}\,d\theta
$$

**Solution.**

$$
\text{Divide by }\cos^6\theta
$$

$$
\text{original expression}
=
\int_0^{\pi/2}\frac{\tan^2\theta\sec^2\theta}{(1+\tan^3\theta)^2}\,d\theta
=
\int_0^{+\infty}\frac{t^2}{(1+t^3)^2}\,dt
=
\frac{1}{3}\int_0^{+\infty}\frac{d(t^3)}{(1+t^3)^2}
=\frac{1}{3}
$$

**eg.**

**Problem.** Given the Dirichlet integral, evaluate the following two definite integrals.

$$
\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac{\pi}{2}
\\
\int_0^{+\infty}\left(\frac{\sin x}{x}\right)^2dx
\\
\int_0^{+\infty}\left(\frac{\sin x}{x}\right)^3dx
$$

**Solution.**

$$
\int_0^{+\infty}\left(\frac{\sin x}{x}\right)^2dx
=
-\int_0^{+\infty}(\sin x)^2d\left(\frac{1}{x}\right)
=-\frac{1}{x}(\sin x)^2\Big|_0^{+\infty}
+
\int_0^{+\infty}\frac{2\sin x\cos x}{x}\,dx
$$

$$
=0+
\int_0^{+\infty}\frac{\sin2x}{2x}\,d(2x)
=\frac{\pi}{2}
$$

$$
\int_0^{+\infty}\left(\frac{\sin x}{x}\right)^3dx
=
-\int_0^{+\infty}\frac{(\sin x)^3}{x}\,d\left(\frac{1}{x}\right)
=
\frac{1}{x^2}(\sin x)^3\Big|_{+\infty}^{0}
+
\int_0^{+\infty}\frac{1}{x}d\left(\frac{(\sin x)^3}{x}\right)
$$

$$
=0+
\int_0^{+\infty}\frac{3x(\sin x)^2\cos x-(\sin x)^3}{x^3}\,dx
$$

$$
I=\int_0^{+\infty}\left(\frac{\sin x}{x}\right)^3dx
$$

$$
\begin{aligned}
I
&=
\frac{3}{2}\int_0^{+\infty}\frac{(\sin x)^2\cos x}{x^2}\,dx
=
\frac{3}{4}\int_0^{+\infty}\frac{\sin2x\sin x}{x^2}\,dx\\
&=
\frac{3}{8}\int_0^{+\infty}\frac{\cos x-\cos3x}{x^2}\,dx\\
&=
\frac{3}{8}\int_0^{+\infty}\frac{\left(1-2\sin^2\dfrac{x}{2}\right)-\left(1-2\sin^2\dfrac{3x}{2}\right)}{x^2}\,dx\\
&=
\frac{3}{8}\int_0^{+\infty}\frac{2\sin^2\dfrac{3x}{2}-2\sin^2\dfrac{x}{2}}{x^2}\,dx\\
&=
\frac{3}{8}\left[
\int_0^{+\infty}\frac{3\sin^2\dfrac{3x}{2}}{\left(\dfrac{3x}{2}\right)^2}d\left(\frac{3x}{2}\right)
-
\int_0^{+\infty}\frac{\sin^2\dfrac{x}{2}}{\left(\dfrac{x}{2}\right)^2}d\left(\frac{x}{2}\right)
\right]\\
&=
\frac{3}{8}\left(\frac{3\pi}{2}-\frac{\pi}{2}\right)
=\frac{3\pi}{8}
\end{aligned}
$$

**eg.**

**Problem.** For $a>1$, evaluate $\lim\limits_{n\to\infty}I_n$.

$$
I_n=n\int_1^a\frac{dx}{1+x^n},
\qquad
a>1,
\qquad
\lim_{n\to\infty}I_n
$$

**Solution.**

$$
\begin{aligned}
I_n
&=n\int_{1/a}^{1}\frac{t^{-2}\,dt}{1+t^{-n}}
=
\int_{1/a}^{1}\frac{nt^{n-2}}{1+t^n}\,dt
=
\int_{1/a}^{1}\frac{dt^n}{t(1+t^n)}\\
&=
\int_{1/a}^{1}\frac{d\ln(1+t^n)}{t}\\
&=
\frac{1}{t}\ln(1+t^n)\Big|_{1/a}^{1}
-
\int_{1/a}^{1}\ln(1+t^n)d\frac{1}{t}\\
&=
\ln2-a\ln\left(1+\frac{1}{a^n}\right)
+
\int_{1/a}^{1}\frac{\ln(1+t^n)}{t^2}\,dt
\end{aligned}
$$

$$
\lim_{n\to\infty}a\ln\left(1+\frac{1}{a^n}\right)=0
\\
\int_{1/a}^{1}\frac{\ln(1+t^n)}{t^2}\,dt
\le
\int_{1/a}^{1}\frac{t^n}{t^2}\,dt
\\
\lim_{n\to\infty}\int_{1/a}^{1}\frac{t^n}{t^2}\,dt=0
$$

$$
\lim_{n\to\infty}I_n=\ln2
$$

**eg.**

**Problem.** Find the volume bounded by the cone and the ellipsoid.

$$
\Sigma_1:\text{ cone with vertex }(0,4,0),
\qquad
\Sigma_2:\frac{x^2}{3}+\frac{y^2}{4}+\frac{z^2}{3}=1,
\quad y>0.
$$

$$
\text{Volume bounded by }\Sigma_1\text{ and }\Sigma_2
$$

**Solution.**

$$
(x_0,y_0,z_0):\text{ tangent point},
\qquad
\frac{x_0x}{3}+\frac{y_0y}{4}+\frac{z_0z}{3}=1
$$

$$
(0,4,0)\Rightarrow y_0=1,
\qquad
\text{tangent points lie in }y=1
$$

$$
V=V_{\text{cone}}-V_{\text{ellipsoid}}
=\frac{1}{3}\pi r^2h-
\left.\int_1^2\pi f^2(y)\,dy\right|_{x=0}
=\frac{1}{3}\pi\cdot\frac{9}{4}\cdot3
-
\int_1^2\pi\cdot3\left(1-\frac{y^2}{4}\right)dy
=\pi
$$

**eg.**

**Problem.** Prove the following inequality.

$$
\int_0^{\pi/4}\tan^n t\,dt<\frac{1}{2n}
$$

**Solution.**

$$
\tan t=u,
\qquad
u\in(0,1),
\qquad
t=\arctan u
$$

$$
\int_0^{\pi/4}\tan^n t\,dt
=
\int_0^1\frac{u^n}{1+u^2}\,du
<
\int_0^1\frac{u^n}{2u}\,du
=
\frac{1}{2}\int_0^1u^{n-1}\,du
=
\frac{1}{2n}u^n\Big|_0^1
=
\frac{1}{2n}
$$

**eg.**

**Problem.** Evaluate the following limit.

$$
\lim_{x\to\infty}\frac{\int_0^x t|\sin t|\,dt}{\pi x^2}
$$

**Solution.**

$$
\int_0^x t|\sin t|\,dt
=
\int_0^{n\pi}t|\sin t|\,dt+
\int_{n\pi}^{x}t|\sin t|\,dt
$$

$$
\int_{k\pi}^{(k+1)\pi}t|\sin t|\,dt,
\qquad
u=t-k\pi,
\qquad
u\in(0,\pi)
$$

$$
\int_0^{\pi}(u+k\pi)|\sin(u+k\pi)|\,du
=
\int_0^{\pi}(u+k\pi)\sin u\,du
=\pi+2k\pi
$$

$$
\int_0^{n\pi}t|\sin t|\,dt
=
\sum_{k=0}^{n-1}(1+2k)\pi
=n\pi+2\cdot\frac{(n-1)(1+n-1)}{2}\pi
=n^2\pi
$$

$$
n\pi\le x\le(n+1)\pi
\quad\Rightarrow\quad
n^2\pi\le\int_0^x t|\sin t|\,dt\le(n+1)^2\pi
$$

$$
\lim_{n\to\infty}\frac{n^2\pi}{\pi[(n+1)\pi]^2}
\le
\lim_{x\to\infty}\frac{\int_0^x t|\sin t|\,dt}{\pi x^2}
\le
\lim_{n\to\infty}\frac{(n+1)^2\pi}{\pi(n\pi)^2}
$$

$$
\lim_{x\to\infty}\frac{\int_0^x t|\sin t|\,dt}{\pi x^2}
=\frac{1}{\pi^2}
$$

**eg.**

**Problem.** Given the integral definition of $f(x)$ and $f(0)$, find $f(x)$.

$$
f(x)=\int_0^{+\infty}e^{-t^2}\cos2tx\,dt,
\qquad
f(0)=\frac{\sqrt\pi}{2},
\qquad
f(x)
$$

**Solution.**

$$
f'(x)
=
\int_0^{+\infty}\frac{\partial}{\partial x}\left(e^{-t^2}\cos2tx\right)dt
=
\int_0^{+\infty}-2te^{-t^2}\sin2tx\,dt
$$

$$
=
\int_0^{+\infty}\sin2tx\,d(e^{-t^2})
=
\sin2tx\,e^{-t^2}\Big|_0^{+\infty}
-
\int_0^{+\infty}e^{-t^2}d\sin2tx
$$

$$
=-2x\int_0^{+\infty}e^{-t^2}\cos2tx\,dt
=-2xf(x)
$$

$$
y'+2xy=0\\
y=Ce^{-x^2}\\
f(x)=\frac{\sqrt\pi}{2}e^{-x^2}.
$$

**eg.**

**Problem.** Evaluate the following definite integral.

$$
\int_0^{\pi/2}\frac{e^x(1+\sin x)}{1+\cos x}\,dx
$$

**Solution.**

$$
\int\frac{1}{1+\cos x}\,dx
=
\int\frac{1}{2\cos^2\dfrac{x}{2}}\,dx
=
\int\frac{1}{2}\sec^2\frac{x}{2}\,dx
=
\tan\frac{x}{2}+C
=
\frac{\sin x}{1+\cos x}
$$

$$
d\left(\frac{\sin x}{1+\cos x}\right)
=
\frac{1}{1+\cos x}\,dx
$$

$$
\begin{aligned}
\int_0^{\pi/2}\frac{e^x(1+\sin x)}{1+\cos x}\,dx
&=
\int_0^{\pi/2}e^x d\left(\frac{\sin x}{1+\cos x}\right)
+
\frac{\sin x}{1+\cos x}d(e^x)\\
&=
\left.e^x\frac{\sin x}{1+\cos x}\right|_0^{\pi/2}
=e^{\pi/2}
\end{aligned}
$$

### Differential Equations

##### First-order linear differential equation

For

$$
\frac{dy}{dx}+P(x)y=Q(x)
$$

the solution is

$$
y=e^{-\int P(x)\,dx}
\left[
\int Q(x)e^{\int P(x)\,dx}\,dx+C
\right]
$$

##### Bernoulli equation

For

$$
\frac{dy}{dx}+P(x)y=Q(x)y^k
$$

dividing by $y^k$ gives

$$
y^{-k}\frac{dy}{dx}+P(x)y^{1-k}=Q(x)
$$

Let

$$
z=y^{1-k}
$$

Then

$$
\frac{1}{1-k}\frac{dz}{dx}+P(x)z=Q(x)
$$

which is a first-order linear equation.

##### Reducible second-order equations

Case 1: $y$ does not appear explicitly

If

$$
y''=f(x,y')
$$

let

$$
p=y'
$$

Then

$$
y''=\frac{dp}{dx}=p'
$$

so the equation becomes

$$
p'=f(x,p)
$$

Case 2: $x$ does not appear explicitly

If

$$
y''=f(y,y')
$$

let

$$
p=y'
$$

Then

$$
y''=\frac{dp}{dy}\frac{dy}{dx}=p\frac{dp}{dy}
$$

so the equation becomes

$$
p\frac{dp}{dy}=f(y,p)
$$

##### Constant-coefficient nonhomogeneous linear equations

Consider

$$
y''+py'+qy=f(x)
$$

The characteristic equation is

$$
r^2+pr+q=0
$$

**Complementary solution**.

| Roots of the characteristic equation       | Complementary solution $y_h$                                 |
| ------------------------------------------ | ------------------------------------------------------------ |
| Distinct real roots $r_1\ne r_2$           | $y_h=C_1e^{r_1x}+C_2e^{r_2x}$                                |
| Repeated real root $r_1=r_2=r$             | $y_h=(C_1+C_2x)e^{rx}$                                       |
| Complex conjugate roots $\alpha\pm i\beta$ | $y_h=e^{\alpha x}\left(C_1\cos\beta x+C_2\sin\beta x\right)$ |

**Particular solution**.

If

$$
f(x)=e^{\lambda x}P_m(x)
$$

then a trial particular solution is

$$
y^*=x^s Q_m(x)e^{\lambda x}
$$

where

$$
s=
\begin{cases}
0 & \lambda \text{ is not a characteristic root}\\
1 & \lambda \text{ is a simple characteristic root}\\
2 & \lambda \text{ is a double characteristic root}
\end{cases}
$$

If

$$
f(x)=e^{\lambda x}\left[P_l^{(1)}(x)\cos\omega x+P_m^{(2)}(x)\sin\omega x\right]
$$

let

$$
n=\max\{l,m\}
$$

If $\lambda+i\omega$ is not a characteristic root, take

$$
y^*=e^{\lambda x}
\left[R_n^{(1)}(x)\cos\omega x+R_n^{(2)}(x)\sin\omega x\right]
$$

If $\lambda+i\omega$ is a characteristic root, take

$$
y^*=xe^{\lambda x}
\left[R_n^{(1)}(x)\cos\omega x+R_n^{(2)}(x)\sin\omega x\right]
$$

##### Examples

**eg.**

**Problem.** Solve the following initial value problem.

$$
\begin{cases}
y''-2y'-3y=1\\
y(0)=0\quad y'(0)=1
\end{cases}
$$

**Solution.**

$$
r^2-2r-3=0
\\
r_1=3,
r_2=-1
\\
y_h(x)=C_1e^{3x}+C_2e^{-x}
$$

$$
y_p=-\frac{1}{3},
\qquad
y(x)=C_1e^{3x}+C_2e^{-x}-\frac{1}{3}
$$

$$
y(0)=0,
\quad
y'(0)=1
\quad\Rightarrow\quad
 y(x)=\frac{1}{3}e^{3x}-\frac{1}{3}
$$

**eg.**

**Problem.** Solve the following differential equation.

$$
\frac{dy}{dx}x\ln x\sin y+\cos y(1-x\cos y)=0
$$

**Solution.**

$$
-\ln x\,d\cos y+\cos y(1-x\cos y)d\ln x=0
$$

$$
\cos y\,d\ln x-\ln x\,d\cos y=x\cos^2y\,d\ln x
$$

$$
x\,d\ln x=dx
=
\frac{\cos y\,d\ln x-\ln x\,d\cos y}{\cos^2y}
=d\frac{\ln x}{\cos y}
$$

$$
C+x=\frac{\ln x}{\cos y}
\\
\ln x=(C+x)\cos y
$$

**eg.**

**Problem.** Solve the following differential equation.

$$
(x^2+y^2+3)\frac{dy}{dx}=2x\left(2y-\frac{x^2}{y}\right)
$$

**Solution.**

$$
(x^2+y^2+3)dy^2=2dx^2(2y^2-x^2)
\qquad
u=x^2,
v=y^2
$$

$$
(u+v+3)dv=2du(2v-u)
$$

$$
\frac{dv}{du}=\frac{2(2v-u)}{u+v+3}
\qquad
p=u+m
\quad
q=v+n
\qquad
\frac{dv}{du}=\frac{dq}{dp}=\frac{2(2q-p)}{p+q}
$$

$$
\begin{cases}
2q-p=2v-u\\
p+q=u+v+3
\end{cases}
\qquad
\begin{cases}
2n-m=0\\
m+n=3
\end{cases}
\qquad
\begin{cases}
m=2\\
n=1
\end{cases}
$$

$$
p=u+2,
\qquad
q=v+1
$$

$$
\frac{dq}{dp}
=
\frac{2\left(2\dfrac{q}{p}-1\right)}{\dfrac{q}{p}+1},
\qquad
z=\frac{q}{p},
\qquad
\frac{d(zp)}{dp}=z+p\frac{dz}{dp}=\frac{2(2z-1)}{z+1}
$$

$$
\frac{p}{dp}
=
\left[\frac{2(2z-1)}{z+1}-z\right]\frac{1}{dz},
\qquad
\frac{dp}{p}
=-\frac{z+1}{(z-1)(z-2)}dz
=
\left(\frac{2}{z-1}-\frac{3}{z-2}\right)dz
$$

$$
\ln p=2\ln(z-1)-3\ln(z-2)+\ln C,
\qquad
p=x^2+2,
\quad
z=\frac{y^2+1}{x^2+2}
$$

$$
\ln(x^2+2)
=2\ln(y^2-x^2-1)-2\ln(x^2+2)-3\ln(y^2-2x^2-3)+3\ln(x^2+2)+\ln C
$$

$$
C(y^2-x^2-1)^2=(y^2-2x^2-3)^3
$$

$$
C(y^2-x^2-1)^2=(y^2-2x^2)^3
$$

