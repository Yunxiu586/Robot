# Proofs

**eg.**

**Problem.**

Let $f(x)$ be a nonnegative function with continuous derivative on $\mathbb{R}$

Suppose there exists $M>0$ such that for all $x,y\in\mathbb{R}$

$$
\lvert f'(x)-f'(y)\rvert\le M\lvert x-y\rvert
$$

Prove that for every real $x$

$$
\bigl(f'(x)\bigr)^2\le 2Mf(x)
$$

**Solution.**

If $f(x)=0$, then $x$ is a local minimum point of $f$, so

$$
f'(x)=0
$$

Assume $f(x)>0$ and $f'(x)\ne0$.

Let

$$
\varepsilon=\operatorname{sgn}f'(x)
$$

For $h>0$,

$$
0\le f(x-\varepsilon h)
$$

$$
\begin{aligned}
f(x-\varepsilon h)
&=f(x)-h\lvert f'(x)\rvert
+\int_x^{x-\varepsilon h}\bigl[f'(t)-f'(x)\bigr]dt
\end{aligned}
$$

Therefore

$$
h\lvert f'(x)\rvert
\le
f(x)+\left|\int_x^{x-\varepsilon h}\bigl[f'(t)-f'(x)\bigr]dt\right|
$$

$$
\left|\int_x^{x-\varepsilon h}\bigl[f'(t)-f'(x)\bigr]dt\right|
\le
M\int_0^h s\,ds
=
\frac{M}{2}h^2
$$

Thus

$$
\lvert f'(x)\rvert
\le
\frac{f(x)}{h}+\frac{M}{2}h
$$

Take

$$
h=\sqrt{\frac{2f(x)}{M}}
$$

Then

$$
\lvert f'(x)\rvert\le\sqrt{2Mf(x)}
$$

$$
\bigl(f'(x)\bigr)^2\le 2Mf(x)
$$

---

**eg.**

**Problem.**

Let $f$ be twice differentiable on $(-1,1)$ with

$$
f(0)=1
$$

For $x\ge0$ assume

$$
f(x)\ge0
\qquad
f'(x)\le0
\qquad
f''(x)\le f(x)
$$

Prove that

$$
f'(0)\ge-\sqrt2
$$

**Solution.**

Let

$$
F(x)=f^2(x)-\bigl(f'(x)\bigr)^2
$$

Then

$$
F'(x)=2f(x)f'(x)-2f'(x)f''(x)
=2f'(x)\bigl[f(x)-f''(x)\bigr]
\le0
$$

Hence $F$ is decreasing on $(0,1)$.

For any $a\in(0,1)$, by the Lagrange mean value theorem, there exists $\xi_a\in(0,a)$ such that

$$
f'(\xi_a)=\frac{f(a)-f(0)}{a}
$$

Since

$$
f'(x)\le0
\qquad
f(0)=1
\qquad
f(x)\ge0
$$

we have

$$
0\le f(a)\le1
$$

Thus

$$
\lvert f'(\xi_a)\rvert\le\frac1a
$$

Since $F$ is decreasing,

$$
F(0)\ge F(\xi_a)
$$

Also

$$
F(\xi_a)=f^2(\xi_a)-\bigl(f'(\xi_a)\bigr)^2
\ge
-\frac1{a^2}
$$

Therefore

$$
1-\bigl(f'(0)\bigr)^2\ge -\frac1{a^2}
$$

$$
\bigl(f'(0)\bigr)^2\le 1+\frac1{a^2}
$$

Let $a\to1^-$.

$$
\bigl(f'(0)\bigr)^2\le2
$$

Since $f'(0)\le0$,

$$
f'(0)\ge-\sqrt2
$$

---

**eg.**

**Problem.**

Let $f$ have a continuous derivative on $[0,1]$ and let

$$
f(0)=0
$$

Prove that

$$
\int_0^1 f^2(x)\,dx
\le
4\int_0^1(1-x^2)\lvert f'(x)\rvert^2\,dx
$$

Find all functions for which equality holds

**Solution.**

$$
\begin{aligned}
\int_0^1 f^2(x)\,dx
&=\int_0^1 f^2(x)d(x-1)\\
&=(x-1)f^2(x)\Big|_0^1-
\int_0^1 2(x-1)f(x)f'(x)\,dx\\
&=\int_0^1 2(1-x)f(x)f'(x)\,dx
\end{aligned}
$$

By the Cauchy-Schwarz inequality,

$$
\left[\int_0^1 f^2(x)\,dx\right]^2
\le
\int_0^1 4(1-x)^2\bigl[f'(x)\bigr]^2\,dx
\int_0^1 f^2(x)\,dx
$$

If

$$
\int_0^1 f^2(x)\,dx=0
$$

then

$$
f(x)\equiv0
$$

Otherwise,

$$
\int_0^1 f^2(x)\,dx
\le
4\int_0^1(1-x)^2\bigl[f'(x)\bigr]^2\,dx
$$

Since

$$
(1-x)^2\le1-x^2
\qquad
0\le x\le1
$$

we get

$$
\int_0^1 f^2(x)\,dx
\le
4\int_0^1(1-x^2)\bigl[f'(x)\bigr]^2\,dx
$$

For equality, both inequalities must be equalities.

Since

$$
(1-x)^2<1-x^2
\qquad
0<x<1
$$

we must have

$$
f'(x)=0
\qquad
0<x<1
$$

Together with $f(0)=0$,

$$
f(x)\equiv0
$$

Thus equality holds only for

$$
\boxed{f(x)\equiv0}
$$

---

**eg.**

**Problem.**

Let $f$ be continuous on $[0,1]$ and suppose

$$
1\le f(x)\le3
$$

Prove that

$$
1\le
\int_0^1 f(x)\,dx\int_0^1\frac1{f(x)}\,dx
\le\frac43
$$

**Solution.**

By the Cauchy-Schwarz inequality,

$$
\int_0^1 f(x)\,dx\int_0^1\frac1{f(x)}\,dx
\ge
\left[\int_0^1\sqrt{f(x)\frac1{f(x)}}\,dx\right]^2
=1
$$

Let

$$
A=\int_0^1 f(x)\,dx
\qquad
B=\int_0^1\frac1{f(x)}\,dx
$$

Then

$$
AB=\frac13A(3B)
\le
\frac1{12}(A+3B)^2
$$

$$
A+3B
=
\int_0^1\left(f(x)+\frac3{f(x)}\right)dx
$$

Since $1\le f(x)\le3$,

$$
f(x)+\frac3{f(x)}\le4
$$

Therefore

$$
\begin{aligned}
AB
&\le
\frac1{12}
\left[\int_0^1\left(f(x)+\frac3{f(x)}\right)dx\right]^2\\
&\le
\frac1{12}
\int_0^1\left(f(x)+\frac3{f(x)}\right)^2dx\\
&\le
\frac1{12}\cdot4^2
=\frac43
\end{aligned}
$$

Thus

$$
1\le
\int_0^1 f(x)\,dx\int_0^1\frac1{f(x)}\,dx
\le\frac43
$$

---

**eg.**

**Problem.**

Let $f$ be differentiable on $[0,1]$ and suppose

$$
f(0)>0
\qquad
f(1)>0
\qquad
\int_0^1f(x)\,dx=0
$$

Prove that

$$
f(x)\text{ has at least two zeros on }[0,1]
$$

and that there exists $\xi\in(0,1)$ such that

$$
f'(\xi)+3f^3(\xi)=0
$$

**Solution.**

If $f(x)\ge0$ for all $x\in[0,1]$, then

$$
\int_0^1 f(x)\,dx>0
$$

This contradicts

$$
\int_0^1f(x)\,dx=0
$$

Hence there exists $x_0\in(0,1)$ such that

$$
f(x_0)<0
$$

Since

$$
f(0)>0
\qquad
f(1)>0
$$

there exist

$$
x_1\in(0,x_0)
\qquad
x_2\in(x_0,1)
$$

such that

$$
f(x_1)=f(x_2)=0
$$

Construct

$$
F(x)=f(x)e^{\int_0^x3f^2(t)\,dt}
$$

Then

$$
F'(x)=\bigl[f'(x)+3f^3(x)\bigr]e^{\int_0^x3f^2(t)\,dt}
$$

Since

$$
F(x_1)=F(x_2)=0
$$

by Rolle's theorem, there exists $\xi\in(x_1,x_2)$ such that

$$
F'(\xi)=0
$$

Therefore

$$
f'(\xi)+3f^3(\xi)=0
$$

---

**eg.**

**Problem.**

Let

$$
f(x)=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}\lvert x-t\rvert e^{-t^2}\,dt
$$

Prove that $f(x)$ has exactly two real roots in $(-1,1)$

**Solution.**

$$
\begin{aligned}
f(-1)
&=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}(t+1)e^{-t^2}\,dt\\
&=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}e^{-t^2}\,dt\\
&>-\frac12\left(1+\frac1e\right)+\frac2e
=\frac{3-e}{2e}>0
\end{aligned}
$$

$$
\begin{aligned}
f(1)
&=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}(1-t)e^{-t^2}\,dt\\
&=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}e^{-t^2}\,dt\\
&>-\frac12\left(1+\frac1e\right)+\frac2e
=\frac{3-e}{2e}>0
\end{aligned}
$$

$$
\begin{aligned}
f(0)
&=-\frac12\left(1+\frac1e\right)+\int_{-1}^{1}\lvert t\rvert e^{-t^2}\,dt\\
&=-\frac12\left(1+\frac1e\right)+2\int_0^1te^{-t^2}\,dt\\
&=-\frac12\left(1+\frac1e\right)+1-\frac1e\\
&=\frac{e-3}{2e}<0
\end{aligned}
$$

Therefore $f$ has at least two roots in $(-1,1)$.

For $-1<x<1$,

$$
\begin{aligned}
f(x)
&=-\frac12\left(1+\frac1e\right)
+\int_{-1}^{x}(x-t)e^{-t^2}\,dt
+\int_x^1(t-x)e^{-t^2}\,dt
\end{aligned}
$$

Thus

$$
\begin{aligned}
f'(x)
&=\int_{-1}^x e^{-t^2}\,dt-
\int_x^1e^{-t^2}\,dt\\
&=\int_{-x}^x e^{-t^2}\,dt
\end{aligned}
$$

Hence

$$
-1<x<0\Rightarrow f'(x)<0
\qquad
0<x<1\Rightarrow f'(x)>0
$$

So $f$ is strictly decreasing on $(-1,0)$ and strictly increasing on $(0,1)$.

Therefore $f$ has exactly two real roots in $(-1,1)$.

---

**eg.**

**Problem.**

Let $f$ be differentiable on $[0,+\infty)$ with

$$
f(0)=0
$$

Suppose there exists $A>0$ such that on $[0,+\infty)$

$$
\lvert f'(x)\rvert\le A\lvert f(x)\rvert
$$

Prove that

$$
f(x)\equiv0
$$

**Solution.**

For $x\ge0$,

$$
f(x)=\int_0^x f'(t)\,dt
$$

Thus

$$
\lvert f(x)\rvert
\le
A\int_0^x\lvert f(t)\rvert\,dt
$$

Let $x_0>0$ and let

$$
M(x_0)=\max_{0\le x\le x_0}\lvert f(x)\rvert
$$

For $0\le x\le x_0$,

$$
\lvert f(x)\rvert\le AM(x_0)x
$$

Substituting this estimate repeatedly gives

$$
\lvert f(x)\rvert
\le
M(x_0)\frac{(Ax)^n}{n!}
\qquad
n=1,2,3,\ldots
$$

Let $n\to\infty$.

$$
\lvert f(x)\rvert=0
\qquad
0\le x\le x_0
$$

Since $x_0>0$ is arbitrary,

$$
f(x)\equiv0
$$

---

**eg.**

**Problem.**

Let $f(x)$ be bounded and continuous on $[0,+\infty)$

Prove that every solution of

$$
y''+14y'+13y=f(x)
$$

is bounded on $[0,+\infty)$

**Solution.**

$$
y''+14y'+13y=(y'+y)'+13(y'+y)
$$

Let

$$
u=y'+y
$$

Then

$$
u'+13u=f(x)
$$

Since $f$ is bounded, there exists $M>0$ such that

$$
\lvert f(x)\rvert\le M
$$

Solving the linear equation,

$$
u(x)=e^{-13x}\left[u(0)+\int_0^x f(t)e^{13t}\,dt\right]
$$

Hence

$$
\begin{aligned}
\lvert u(x)\rvert
&\le
\lvert u(0)\rvert e^{-13x}
+e^{-13x}\int_0^x Me^{13t}\,dt\\
&\le
\lvert u(0)\rvert+\frac{M}{13}
\end{aligned}
$$

Thus $u$ is bounded.

Since

$$
y'+y=u
$$

we have

$$
y(x)=e^{-x}\left[y(0)+\int_0^x u(t)e^t\,dt\right]
$$

If $\lvert u(x)\rvert\le M_1$, then

$$
\begin{aligned}
\lvert y(x)\rvert
&\le
\lvert y(0)\rvert e^{-x}
+e^{-x}\int_0^x M_1e^t\,dt\\
&\le
\lvert y(0)\rvert+M_1
\end{aligned}
$$

Therefore every solution $y$ is bounded on $[0,+\infty)$.

---

**eg.**

**Problem.**

For a continuous function $f(x)>0$ prove that

$$
\ln\int_0^1 f(x)\,dx\ge\int_0^1\ln f(x)\,dx
$$

**Solution.**

It is enough to prove

$$
\int_0^1\left[\ln f(x)-\ln\int_0^1 f(x)\,dx\right]dx\le0
$$

Since

$$
\ln u\le u-1
\qquad
u>0
$$

we have

$$
\begin{aligned}
\int_0^1\left[\ln f(x)-\ln\int_0^1 f(x)\,dx\right]dx
&=\int_0^1\ln\frac{f(x)}{\int_0^1f(x)\,dx}\,dx\\
&\le
\int_0^1\left(\frac{f(x)}{\int_0^1f(x)\,dx}-1\right)dx\\
&=0
\end{aligned}
$$

---

**eg.**

**Problem.**

Let $f$ be continuous on $[0,1]$ and differentiable on $(0,1)$ with

$$
f(0)=0
\qquad
f(1)=1
$$

Prove that

$$
\exists x_0\in(0,1)
\qquad
f(x_0)=2-3x_0
$$

and that there exist $\xi,\eta\in(0,1)$ with $\xi\ne\eta$ such that

$$
\bigl[1+f'(\xi)\bigr]\bigl[1+f'(\eta)\bigr]=4
$$

**Solution.**

Let

$$
g(x)=f(x)+3x-2
$$

Then

$$
g(0)=-2
\qquad
 g(1)=2
$$

By the intermediate value theorem, there exists $x_0\in(0,1)$ such that

$$
g(x_0)=0
$$

Thus

$$
f(x_0)=2-3x_0
$$

Let

$$
c=x_0
$$

By the Lagrange mean value theorem, there exist

$$
\xi\in(0,c)
\qquad
\eta\in(c,1)
$$

such that

$$
f'(\xi)=\frac{f(c)-f(0)}{c}
=\frac{f(c)}{c}
$$

$$
f'(\eta)=\frac{f(1)-f(c)}{1-c}
=\frac{1-f(c)}{1-c}
$$

Therefore

$$
\begin{aligned}
\bigl[1+f'(\xi)\bigr]\bigl[1+f'(\eta)\bigr]
&=
\frac{c+f(c)}{c}\cdot\frac{2-c-f(c)}{1-c}
\end{aligned}
$$

Since

$$
f(c)=2-3c
$$

we get

$$
\frac{c+2-3c}{c}\cdot\frac{2-c-2+3c}{1-c}
=
\frac{2(1-c)}{c}\cdot\frac{2c}{1-c}
=4
$$

---

**eg.**

**Problem.**

Let $f$ be continuous on $[0,1]$ and differentiable on $(0,1)$ with

$$
f(0)=0
\qquad
f(1)=2
$$

Prove that there exist pairwise distinct points

$$
\xi_1,\xi_2,\xi_3\in(0,1)
$$

such that

$$
f'(\xi_1)f'(\xi_2)\sqrt{1-\xi_3}\ge2
$$

**Solution.**

Let

$$
h(x)=f(x)+x-1
$$

Then

$$
h(0)=-1
\qquad
h(1)=2
$$

By the intermediate value theorem, there exists $a\in(0,1)$ such that

$$
h(a)=0
$$

Thus

$$
f(a)=1-a
$$

By the Lagrange mean value theorem, there exist

$$
\xi_1\in(0,a)
\qquad
\xi_2\in(a,1)
$$

such that

$$
f'(\xi_1)=\frac{f(a)-f(0)}{a}
=\frac{1-a}{a}
$$

$$
f'(\xi_2)=\frac{f(1)-f(a)}{1-a}
=\frac{1+a}{1-a}
$$

Therefore

$$
f'(\xi_1)f'(\xi_2)
=
\frac{1+a}{a}
>2
$$

Choose $\xi_3\in(0,1)$, distinct from $\xi_1$ and $\xi_2$, such that

$$
\sqrt{1-\xi_3}
\ge
\frac{2}{f'(\xi_1)f'(\xi_2)}
$$

Then

$$
f'(\xi_1)f'(\xi_2)\sqrt{1-\xi_3}\ge2
$$

---

**eg.**

**Problem.**

Prove that for every positive integer $n$

$$
\int_0^{\pi/2}x\left(\frac{\sin nx}{\sin x}\right)^4dx
\le
\left(\frac{n^2}{4}-\frac18\right)\pi^2
$$

**Solution.**

For $0\le x\le\pi/2$,

$$
\lvert\sin nx\rvert\le n\sin x
$$

and

$$
\sin x\ge\frac{2x}{\pi}
$$

For $0<t\le\pi/2$,

$$
\begin{aligned}
\int_0^{\pi/2}x\left(\frac{\sin nx}{\sin x}\right)^4dx
&=\int_0^t x\left(\frac{\sin nx}{\sin x}\right)^4dx
+\int_t^{\pi/2}x\left(\frac{\sin nx}{\sin x}\right)^4dx\\
&\le
\int_0^t xn^4\,dx+
\int_t^{\pi/2}x\left(\frac{\pi}{2x}\right)^4dx\\
&=\frac12t^2n^4+\frac{\pi^4}{32t^2}-\frac{\pi^2}{8}
\end{aligned}
$$

Take

$$
t=\frac{\pi}{2n}
$$

Then

$$
\frac12t^2n^4+\frac{\pi^4}{32t^2}-\frac{\pi^2}{8}
=
\left(\frac{n^2}{4}-\frac18\right)\pi^2
$$

Therefore

$$
\int_0^{\pi/2}x\left(\frac{\sin nx}{\sin x}\right)^4dx
\le
\left(\frac{n^2}{4}-\frac18\right)\pi^2
$$

---

**eg.**

**Problem.**

Let

$$
f(x)=\int_0^x\left(1-\frac{[u]}{u}\right)du
$$

where $[x]$ denotes the greatest integer not exceeding $x$

Discuss the convergence of

$$
\int_1^{+\infty}\frac{e^{f(x)}}{x^p}\cos\left(x^2-\frac1{x^2}\right)dx
\qquad
p>0
$$

**Solution.**

Let

$$
N=[x]
\qquad
N\le x<N+1
$$

Then

$$
\begin{aligned}
f(x)
&=\int_0^N\left(1-\frac{[u]}u\right)du+
\int_N^x\left(1-\frac{N}{u}\right)du\\
&=N-\sum_{k=1}^{N-1}k\ln\frac{k+1}{k}
+x-N-N\ln\frac{x}{N}\\
&=x+\ln(N!)-N\ln x
\end{aligned}
$$

Thus

$$
e^{f(x)}=\frac{N!e^x}{x^N}
$$

By Stirling's formula,

$$
N!\sim\sqrt{2\pi N}\left(\frac Ne\right)^N
$$

Hence

$$
e^{f(x)}
\sim
\sqrt{2\pi N}\left(\frac Nx\right)^Ne^{x-N}
$$

Since $N\le x<N+1$,

$$
1\le
\left(\frac Nx\right)^Ne^{x-N}
\le e
$$

Therefore

$$
e^{f(x)}\asymp\sqrt N\asymp\sqrt x
$$

After the substitution

$$
y=x^2
$$

we get

$$
\int_1^{+\infty}\frac{e^{f(x)}}{x^p}\cos\left(x^2-\frac1{x^2}\right)dx
=
\frac12\int_1^{+\infty}e^{f(\sqrt y)}y^{-\frac p2-\frac12}\cos\left(y-\frac1y\right)dy
$$

The amplitude satisfies

$$
e^{f(\sqrt y)}y^{-\frac p2-\frac12}
\asymp
y^{-\frac14-\frac p2}
$$

For $p>0$,

$$
y^{-\frac14-\frac p2}\to0
$$

Moreover, on $N\le x<N+1$,

$$
\frac{d}{dx}\left(e^{f(x)}x^{-p-1}\right)
=
e^{f(x)}x^{-p-1}\left(f'(x)-\frac{p+1}{x}\right)
<0
$$

so the amplitude after $y=x^2$ is decreasing.

Also

$$
\int_1^Y\cos\left(y-\frac1y\right)dy
$$

is bounded on $[1,+\infty)$.

By Dirichlet's test, the improper integral converges for every $p>0$.

For absolute convergence, consider

$$
\int_1^{+\infty}
 y^{-\frac14-\frac p2}
\left|\cos\left(y-\frac1y\right)\right|dy
$$

It converges if and only if

$$
\frac14+\frac p2>1
$$

Therefore

$$
p>\frac32
$$

Conclusion:

$$
\begin{cases}
\text{absolutely convergent}, & p>\dfrac32\\[6pt]
\text{conditionally convergent}, & 0<p\le\dfrac32
\end{cases}
$$
