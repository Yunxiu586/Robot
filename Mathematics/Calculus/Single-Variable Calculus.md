# Single-Variable Calculus

[toc]

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

