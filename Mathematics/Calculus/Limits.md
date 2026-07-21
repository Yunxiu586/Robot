# Limits

[toc]

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

