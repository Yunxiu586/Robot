# Functions of a Complex Variable

[toc]

### Complex Numbers

##### Algebraic and polar forms

For

$$
z=x+iy=re^{i\theta}
$$

we have

$$
z^2=x^2-y^2+2ixy=r^2e^{2i\theta}
$$

$$
z\overline z=|z|^2=x^2+y^2=r^2
$$

$$
z+\overline z=2\operatorname{Re}z
\qquad
z-\overline z=2i\operatorname{Im}z
$$

For two complex numbers

$$
|z_1+z_2|^2=|z_1|^2+|z_2|^2+2|z_1||z_2|\cos\angle(z_1,z_2)
$$

##### Argument

The principal argument is written in these notes as

$$
\theta=\arg z\in(-\pi,\pi]
$$

For $z=x+iy$

$$
\arg z=
\begin{cases}
\arctan\dfrac{y}{x} & x>0\\[8pt]
\dfrac{\pi}{2} & x=0,\ y>0\\[8pt]
-\dfrac{\pi}{2} & x=0,\ y<0\\[8pt]
\arctan\dfrac{y}{x}+\pi & x<0,\ y\ge0\\[8pt]
\arctan\dfrac{y}{x}-\pi & x<0,\ y<0
\end{cases}
$$

$$
\operatorname{Arg}\overline z=-\operatorname{Arg}z\pmod{2\pi}
$$

For the principal argument this identity holds away from the negative real axis

At $z=0$ the argument is undefined

The full set of arguments is

$$
\operatorname{Arg}z=\arg z+2k\pi
\qquad k\in\mathbb Z
$$

##### De Moivre's formula

For real $\theta$ and integer $n$

$$
z^n=r^n(\cos\theta+i\sin\theta)^n
=r^n(\cos n\theta+i\sin n\theta)
$$

The $n$ roots are

$$
z_k=\sqrt[n]{r}\left[
\cos\frac{\theta+2k\pi}{n}
+i\sin\frac{\theta+2k\pi}{n}
\right]
\qquad k=0,1,\ldots,n-1
$$

De Moivre's formula follows from Euler's formula

$$
(e^{i\theta})^n=e^{in\theta}=\cos n\theta+i\sin n\theta
$$

##### Rotation factors

Multiplication by $i$ rotates by $\pi/2$

$$
ire^{i\theta}=re^{i(\theta+\pi/2)}
$$

Multiplication by $-1$ rotates by $\pi$

$$
-re^{i\theta}=re^{i(\theta\pm\pi)}
$$

**eg.**

**Problem.**

Prove that

$$
\lim_{\Delta z\to0}\frac{\Delta\overline z}{\Delta z}
$$

does not exist

**Solution.**

$$
\frac{\Delta\overline z}{\Delta z}
=\frac{\Delta x-i\Delta y}{\Delta x+i\Delta y}
$$

Along the $x$-axis

$$
\Delta y=0
\qquad
\lim_{\Delta x\to0}\frac{\Delta x-i\Delta y}{\Delta x+i\Delta y}=1
$$

Along the $y$-axis

$$
\Delta x=0
\qquad
\lim_{\Delta y\to0}\frac{\Delta x-i\Delta y}{\Delta x+i\Delta y}=-1
$$

$$
\therefore
\lim_{\Delta z\to0}\frac{\Delta\overline z}{\Delta z}
\text{ does not exist}
$$

### Holomorphic Functions

##### Complex derivative

The derivative of $f(z)$ at $z_0$ is

$$
f'(z_0)=\lim_{\Delta z\to0}
\frac{f(z_0+
\Delta z)-f(z_0)}{\Delta z}
$$

The limit must be independent of the path by which $\Delta z\to0$

##### Holomorphicity

If $f$ is differentiable in a neighborhood of $z_0$ then $f$ is holomorphic at $z_0$

If $f$ is not holomorphic at $z_0$ then $z_0$ is a singular point of $f$

If $f$ is holomorphic at every point of a domain $D$ then $f$ is holomorphic in $D$

In common terminology

$$
\text{holomorphic}\approx\text{complex differentiable on a domain}
$$

$$
\text{analytic}\approx\text{locally expandable as a power series}
$$

##### Cauchy-Riemann equations

Let

$$
f(z)=u(x,y)+iv(x,y)
$$

The Cauchy-Riemann equations are

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}
\qquad
\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}
$$

If $u,v$ are differentiable in $D$ then

$$
f\text{ satisfies the Cauchy-Riemann equations}
\iff
f\text{ is complex differentiable}
$$

If $u,v$ have continuous first partial derivatives in $D$ then

$$
f\text{ satisfies the Cauchy-Riemann equations}
\iff
f\text{ is holomorphic in }D
$$

The derivative can be written as

$$
f'(z)=u_x+iv_x=u_x-iu_y=v_y+iv_x=v_y-iu_y
$$

##### Harmonic functions

A real-valued function $u(x,y)$ is harmonic if

$$
\Delta u=u_{xx}+u_{yy}=0
$$

If $f(z)=u+iv$ is holomorphic then $u$ and $v$ are conjugate harmonic functions

##### Elementary holomorphic functions

The exponential function is

$$
e^z=e^{x+iy}=e^x(\cos y+i\sin y)
$$

$$
|e^z|=e^x
\qquad
\operatorname{Arg}(e^z)=y+2k\pi
$$

$$
e^{z+2k\pi i}=e^z
\qquad
(e^z)'=e^z
\qquad
0\ne e^z
$$

$$
e^{z_1+z_2}=e^{z_1}e^{z_2}
$$

The logarithm is

$$
\operatorname{Ln}z=\ln|z|+i\operatorname{Arg}z
$$

The principal branch is

$$
\log z=\ln|z|+i\arg z
$$

It is holomorphic in the slit plane excluding the origin and the negative real axis

$$
(\operatorname{Ln}z)'=\frac{1}{z}
$$

$$
\operatorname{Ln}(z_1z_2)=\operatorname{Ln}z_1+\operatorname{Ln}z_2
$$

$$
\operatorname{Ln}\frac{z_1}{z_2}=\operatorname{Ln}z_1-\operatorname{Ln}z_2
\qquad z_1z_2\ne0
$$

Complex powers are defined by

$$
z^b=e^{b\operatorname{Ln}z}
$$

$$
(z^b)'=bz^{b-1}
$$

If $b=n\in\mathbb Z$ then $z^b$ is single-valued

If $b=p/q$ with $(p,q)=1$ then $z^b$ has $q$ values

If $b$ is irrational or complex non-real then $z^b$ has infinitely many values

The trigonometric functions are

$$
\cos z=\frac{e^{iz}+e^{-iz}}{2}
\qquad
\sin z=\frac{e^{iz}-e^{-iz}}{2i}
$$

They are entire functions with period $2\pi$

$$
(\sin z)'=\cos z
\qquad
(\cos z)'=-\sin z
$$

**eg.**

**Problem.**

Prove that as $|y|\to\infty$

$$
|\cos z|\to\infty
\qquad
|\sin z|\to\infty
$$

where $z=x+iy$

**Solution.**

$$
\cos z=\frac{e^{iz}+e^{-iz}}{2}
=\frac{e^{-y+ix}+e^{y-ix}}{2}
$$

$$
\cos z=\frac{e^y+e^{-y}}{2}\cos x
+i\frac{e^{-y}-e^y}{2}\sin x
$$

$$
|\cos z|^2
=\left(\frac{e^y+e^{-y}}{2}\right)^2\cos^2x
+\left(\frac{e^y-e^{-y}}{2}\right)^2\sin^2x
$$

$$
|\cos z|^2=\cos^2x+\sinh^2y
$$

$$
|\sin z|^2=\sin^2x+\sinh^2y
$$

$$
|y|\to\infty
\quad\Longrightarrow\quad
\sinh^2y\to\infty
$$

$$
|\cos z|\to\infty
\qquad
|\sin z|\to\infty
$$

**eg.**

**Problem.**

Let

$$
u(x,y)=x^3-3xy^2
$$

Find a holomorphic function

$$
f(z)=u+iv
$$

such that

$$
f(i)=-i
$$

**Solution.**

Method 1

$$
v_y=u_x=3x^2-3y^2
$$

$$
v=\int(3x^2-3y^2)dy=3x^2y-y^3+\varphi(x)
$$

$$
v_x=-u_y=6xy
$$

$$
6xy+\varphi'(x)=6xy
\qquad
\varphi'(x)=0
\qquad
\varphi(x)=C
$$

$$
f(z)=x^3-3xy^2+i(3x^2y-y^3+C)
$$

Method 2

$$
dv=v_xdx+v_ydy=-u_y dx+u_xdy
$$

$$
v=\int_{(0,0)}^{(x,y)}6xy\,dx+(3x^2-3y^2)dy
$$

$$
v=3x^2y-y^3+C
$$

$$
f(z)=x^3-3xy^2+i(3x^2y-y^3+C)
$$

$$
f(i)=-i
\quad\Longrightarrow\quad
C=0
$$

$$
f(z)=z^3
$$

### Complex Integrals

##### Real integral form

Let

$$
f(z)=u(x,y)+iv(x,y)
\qquad
z=x+iy
$$

Then

$$
\int_C f(z)\,dz
=\int_C (u+iv)(dx+i\,dy)
$$

$$
\int_C f(z)\,dz
=\int_C u\,dx-v\,dy
+i\int_C v\,dx+u\,dy
$$

##### Parametric form

If

$$
C:z=z(t)
\qquad
\alpha\le t\le\beta
$$

then

$$
\int_C f(z)\,dz
=\int_\alpha^\beta f(z(t))z'(t)\,dt
$$

##### Domains

A simple closed curve is a continuous closed curve without self-intersections

A domain is a connected open set

A domain is simply connected if every simple closed curve in it has its interior contained in the domain

A multiply connected domain has holes or removed subregions

##### Cauchy's integral theorem

If $f$ is holomorphic in a simply connected domain $D$ then

$$
\oint_C f(z)\,dz=0
$$

for every simple closed curve $C\subset D$

##### Path independence

If $f$ is holomorphic in a simply connected domain $D$ then the integral depends only on the endpoints

Define

$$
F(z)=\int_{z_0}^{z}f(\zeta)\,d\zeta
$$

Then

$$
F'(z)=f(z)
$$

If $G'(z)=f(z)$ then

$$
\int_{z_1}^{z_2}f(\zeta)\,d\zeta=G(z_2)-G(z_1)
$$

##### Composite path theorem

Let $D$ be a multiply connected domain bounded by an outer boundary $C$ and inner boundaries $C_k^{-}$

The positive direction keeps $D$ on the left side

$$
\oint_C f(z)\,dz+
\sum_{k=1}^{n}\oint_{C_k^{-}}f(z)\,dz=0
$$

Equivalently, if all $C_k$ are counterclockwise

$$
\oint_C f(z)\,dz=
\sum_{k=1}^{n}\oint_{C_k}f(z)\,dz
$$

##### Path deformation

For a doubly connected domain with outer boundary $C_1$ and inner boundary $C_2^{-}$

$$
\oint_{C_1}f(z)\,dz=
\oint_{C_2}f(z)\,dz
$$

##### Cauchy's integral formula

If $f$ is holomorphic in $D$ and continuous on $D\cup C$ then for $z_0\in D$

$$
\oint_C\frac{f(z)}{z-z_0}\,dz=2\pi i f(z_0)
$$

$$
f(z_0)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz
$$

##### Cauchy's differentiation formula

For $n\ge0$

$$
\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz
=\frac{2\pi i}{n!}f^{(n)}(z_0)
$$

$$
f^{(n)}(z_0)
=\frac{n!}{2\pi i}
\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz
$$

**eg.**

**Problem.**

Evaluate

$$
\oint_C\frac{dz}{(z-z_0)^{n+1}}
$$

where $C$ is the counterclockwise circle centered at $z_0$ with radius $r$ and $n\in\mathbb Z$

**Solution.**

$$
z=z_0+re^{i\theta}
\qquad
 dz=ire^{i\theta}\,d\theta
$$

$$
\oint_C\frac{dz}{(z-z_0)^{n+1}}
=\int_0^{2\pi}\frac{ire^{i\theta}}{r^{n+1}e^{i(n+1)\theta}}\,d\theta
=\frac{i}{r^n}\int_0^{2\pi}e^{-in\theta}\,d\theta
$$

$$
n=0
\quad\Longrightarrow\quad
\oint_C\frac{dz}{z-z_0}=2\pi i
$$

$$
n\ne0
\quad\Longrightarrow\quad
\oint_C\frac{dz}{(z-z_0)^{n+1}}=0
$$

$$
\oint_C\frac{dz}{(z-z_0)^{n+1}}
=
\begin{cases}
2\pi i & n=0\\
0 & n\ne0
\end{cases}
$$

**eg.**

**Problem.**

Let

$$
F(z)=\int_{z_0}^{z}f(\zeta)\,d\zeta
$$

Prove that if $f$ is continuous then

$$
F'(z)=f(z)
$$

**Solution.**

$$
\frac{F(z+\Delta z)-F(z)}{\Delta z}-f(z)
=\frac{1}{\Delta z}\int_z^{z+\Delta z}f(\zeta)\,d\zeta-f(z)
$$

$$
=\frac{1}{\Delta z}\int_z^{z+\Delta z}[f(\zeta)-f(z)]\,d\zeta
$$

For $|\zeta-z|<\delta$

$$
|f(\zeta)-f(z)|<\varepsilon
$$

Hence

$$
\left|
\frac{F(z+\Delta z)-F(z)}{\Delta z}-f(z)
\right|
\le
\frac{1}{|\Delta z|}\int_z^{z+\Delta z}\varepsilon |d\zeta|
=\varepsilon
$$

$$
F'(z)=f(z)
$$

### Complex Series

##### Complex sequences

For

$$
\alpha_n=a_n+ib_n
$$

we have

$$
\alpha_n\to a+ib
\iff
a_n\to a
\quad\text{and}\quad
b_n\to b
$$

##### Complex series

Let

$$
S_n=\sum_{k=1}^{n}\alpha_k
$$

If $S_n$ converges then

$$
\sum_{n=1}^{\infty}\alpha_n
$$

converges

If

$$
\sum_{n=1}^{\infty}\alpha_n
$$

converges then

$$
\lim_{n\to\infty}\alpha_n=0
$$

For $\alpha_n=a_n+ib_n$

$$
\sum_{n=1}^{\infty}\alpha_n\text{ converges}
\iff
\sum_{n=1}^{\infty}a_n\text{ and }\sum_{n=1}^{\infty}b_n\text{ converge}
$$

If either real series diverges then the complex series diverges

If

$$
\sum_{n=1}^{\infty}|\alpha_n|
$$

converges then

$$
\sum_{n=1}^{\infty}\alpha_n
$$

converges absolutely and

$$
\left|\sum_{n=1}^{\infty}\alpha_n\right|
\le
\sum_{n=1}^{\infty}|\alpha_n|
$$

##### Power series

For

$$
f(z)=\sum_{n=0}^{\infty}c_nz^n
$$

if the series converges at $z_0\ne0$ then it converges absolutely for

$$
|z|<|z_0|
$$

If the series diverges at $z_0\ne0$ then it diverges for

$$
|z|>|z_0|
$$

The series always converges at $z=0$

If the power series converges absolutely at one point on its circle of convergence then it converges absolutely inside the circle

If it converges conditionally at $z_0$ then the radius of convergence is $|z_0|$

##### Radius of convergence

If

$$
\lim_{n\to\infty}\left|\frac{c_{n+1}}{c_n}\right|=\lambda\ne0
$$

or

$$
\lim_{n\to\infty}\sqrt[n]{|c_n|}=\lambda\ne0
$$

then

$$
R=\frac{1}{\lambda}
$$

##### Products of power series

If

$$
f(z)=\sum_{n=0}^{\infty}a_nz^n
\qquad
|z|<r_1
$$

and

$$
g(z)=\sum_{n=0}^{\infty}b_nz^n
\qquad
|z|<r_2
$$

then

$$
f(z)g(z)=\sum_{n=0}^{\infty}c_nz^n
$$

where

$$
c_n=\sum_{k=0}^{n}a_kb_{n-k}
$$

##### Common power series

$$
\frac{1}{1-z}=1+z+z^2+\cdots+z^n+\cdots
\qquad
|z|<1
$$

$$
\frac{1}{1-az}=\sum_{n=0}^{\infty}a^nz^n
\qquad
|az|<1
$$

Equivalently

$$
\frac{1}{z-a}
=-\frac{1}{a}\frac{1}{1-z/a}
=-\sum_{n=0}^{\infty}\frac{z^n}{a^{n+1}}
\qquad
|z|<|a|
$$

$$
\frac{1}{(z-a)^2}
=\sum_{n=0}^{\infty}\frac{(n+1)z^n}{a^{n+2}}
\qquad
|z|<|a|
$$

$$
\ln(1+z)=\int_0^z\frac{d\zeta}{1+\zeta}
$$

**eg.**

**Problem.**

Find the power series of $\sin z$ at $z=1$

**Solution.**

$$
\sin z=\sin[(z-1)+1]
$$

$$
\sin z=\sin(z-1)\cos1+\cos(z-1)\sin1
$$

$$
\sin z
=\cos1\sum_{n=0}^{\infty}(-1)^n\frac{(z-1)^{2n+1}}{(2n+1)!}
+
\sin1\sum_{n=0}^{\infty}(-1)^n\frac{(z-1)^{2n}}{(2n)!}
$$

$$
|z-1|<\infty
$$

**eg.**

**Problem.**

Find the power series of

$$
\frac{1}{(1-z)^2}
$$

at $z=i$

**Solution.**

$$
\frac{1}{1-z}
=\frac{1}{1-i-(z-i)}
$$

$$
=\frac{1}{1-i}\frac{1}{1-\dfrac{z-i}{1-i}}
=
\sum_{n=0}^{\infty}\frac{(z-i)^n}{(1-i)^{n+1}}
$$

$$
\left|\frac{z-i}{1-i}\right|<1
$$

$$
\frac{1}{(1-z)^2}
=\left(\frac{1}{1-z}\right)'
=
\sum_{n=1}^{\infty}\frac{n(z-i)^{n-1}}{(1-i)^{n+1}}
$$

$$
|z-i|<|1-i|
$$

### Taylor and Laurent Series

##### Taylor series

If $f$ is holomorphic in

$$
|z-z_0|<R
$$

then

$$
f(z)=\sum_{n=0}^{\infty}c_n(z-z_0)^n
$$

where

$$
c_n=\frac{f^{(n)}(z_0)}{n!}
=\frac{1}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz
$$

If the radius of convergence is finite, then at least one singularity of $f$ lies on the circle of convergence

##### Laurent series

If $f$ is holomorphic in the annulus

$$
R_1<|z-z_0|<R_2
$$

then

$$
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-z_0)^n
$$

where

$$
c_n=\frac{1}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz
$$

The analytic part is

$$
\sum_{n=0}^{\infty}c_n(z-z_0)^n
$$

The principal part is

$$
\sum_{n=-\infty}^{-1}c_n(z-z_0)^n
$$

**eg.**

**Problem.**

Find the Taylor expansion of

$$
f(z)=\frac{1}{(z+1)(z-3)}
$$

at $z=0$

**Solution.**

$$
\frac{1}{(z+1)(z-3)}
=\frac{1}{4}\left(\frac{1}{z-3}-\frac{1}{z+1}\right)
$$

$$
=-\frac{1}{4}\left(
\frac{1}{3}\frac{1}{1-z/3}+\frac{1}{1+z}
\right)
$$

$$
=-\frac{1}{4}\left(
\sum_{n=0}^{\infty}\frac{z^n}{3^{n+1}}
+
\sum_{n=0}^{\infty}(-1)^nz^n
\right)
$$

$$
|z|<1
$$

**eg.**

**Problem.**

Find the Taylor expansion of

$$
f(z)=\ln(1+z)
$$

at $z=1$

**Solution.**

$$
\ln(1+z)=\ln2+\int_1^z\frac{d\zeta}{1+\zeta}
$$

$$
\frac{1}{1+\zeta}
=\frac{1}{2+\zeta-1}
=\frac{1}{2}\frac{1}{1+(\zeta-1)/2}
$$

$$
=\frac{1}{2}\sum_{n=0}^{\infty}(-1)^n\left(\frac{\zeta-1}{2}\right)^n
$$

$$
\ln(1+z)
=\ln2+
\sum_{n=0}^{\infty}
\frac{(-1)^n(z-1)^{n+1}}{2^{n+1}(n+1)}
$$

$$
|z-1|<2
$$

**eg.**

**Problem.**

Find the Laurent expansion of

$$
\frac{1}{1-z}
$$

in

$$
1<|z|<\infty
$$

**Solution.**

$$
\frac{1}{1-z}
=-\frac{1}{z}\frac{1}{1-1/z}
$$

$$
=-\frac{1}{z}\sum_{n=0}^{\infty}\left(\frac{1}{z}\right)^n
$$

$$
=-\sum_{n=0}^{\infty}\frac{1}{z^{n+1}}
=-\sum_{n=-\infty}^{-1}z^n
$$

$$
|z|>1
$$

### Residues

##### Isolated singularities

If $f$ is not holomorphic at $z_0$ but is holomorphic in

$$
0<|z-z_0|<\delta
$$

then $z_0$ is an isolated singularity

##### Removable singularity

If the Laurent series has no negative powers then $z_0$ is removable

Equivalently

$$
\lim_{z\to z_0}f(z)=C
$$

##### Poles

If the principal part has finitely many terms and the highest negative power is $-m$ then $z_0$ is a pole of order $m$

Equivalently

$$
f(z)=\frac{g(z)}{(z-z_0)^m}
$$

where $g$ is holomorphic at $z_0$ and

$$
g(z_0)\ne0
$$

For a pole

$$
\lim_{z\to z_0}f(z)=\infty
$$

A pole of order $1$ is a simple pole

##### Essential singularity

If the principal part has infinitely many terms then $z_0$ is an essential singularity

Equivalently

$$
\lim_{z\to z_0}f(z)
$$

does not exist and is not infinite

##### Zeros and poles

If $f$ is holomorphic and not identically zero near $z_0$ then

$$
f(z)=(z-z_0)^m\varphi(z)
$$

where

$$
\varphi(z_0)\ne0
$$

Then $z_0$ is a zero of order $m$

Equivalently

$$
f^{(n)}(z_0)=0
\qquad n=0,1,\ldots,m-1
$$

$$
f^{(m)}(z_0)\ne0
$$

If

$$
f(z)=\frac{(z-z_0)^m\varphi(z)}{(z-z_0)^n\psi(z)}
$$

where $\varphi(z_0)\psi(z_0)\ne0$ then

$$
\begin{cases}
\text{removable singularity} & m\ge n\\
\text{pole of order }n-m & m<n
\end{cases}
$$

Examples

$$
f(z)=\cos\frac{1}{z}
$$

has an essential singularity at $z=0$

$$
f(z)=\cos\left(\frac{e^z-1}{z}\right)
$$

has a removable singularity at $z=0$ since

$$
\lim_{z\to0}\frac{e^z-1}{z}=1
$$

##### Residue

The residue of $f$ at $z_0$ is the coefficient of $(z-z_0)^{-1}$ in the Laurent series

$$
\operatorname{Res}(f,z_0)=c_{-1}
$$

$$
\operatorname{Res}(f,z_0)
=\frac{1}{2\pi i}\oint_C f(z)\,dz
$$

At infinity

$$
\operatorname{Res}(f,\infty)=-c_{-1}
$$

##### Residue theorem

If $f$ is holomorphic in $D$ except for finitely many isolated singularities $z_k$ inside $C$ then

$$
\oint_C f(z)\,dz
=2\pi i\sum_{k=1}^{n}\operatorname{Res}(f,z_k)
$$

##### Residue formulas

For a removable singularity

$$
\operatorname{Res}(f,z_0)=0
$$

For a pole of order $m$

$$
\operatorname{Res}(f,z_0)
=\frac{1}{(m-1)!}
\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}
\left[(z-z_0)^mf(z)\right]
$$

For a simple pole

$$
\operatorname{Res}(f,z_0)
=\lim_{z\to z_0}(z-z_0)f(z)
$$

If

$$
f(z)=\frac{P(z)}{Q(z)}
$$

and

$$
P(z_0)\ne0
\qquad
Q(z_0)=0
\qquad
Q'(z_0)\ne0
$$

then

$$
\operatorname{Res}(f,z_0)=\frac{P(z_0)}{Q'(z_0)}
$$

For a pole of order $2$

$$
\operatorname{Res}(f,z_0)
=\lim_{z\to z_0}\frac{d}{dz}\left[(z-z_0)^2f(z)\right]
$$

For finitely many isolated singularities

$$
\sum_{k=1}^{n}\operatorname{Res}(f,z_k)
=-\operatorname{Res}(f,\infty)
$$

$$
\operatorname{Res}(f,\infty)
=-\operatorname{Res}\left(\frac{1}{z^2}f\left(\frac{1}{z}\right),0\right)
$$

##### Definite integrals

For rational trigonometric integrals on $[0,2\pi]$

$$
z=e^{i\theta}
\qquad
\cos\theta=\frac{1}{2}\left(z+\frac{1}{z}\right)
\qquad
\sin\theta=\frac{1}{2i}\left(z-\frac{1}{z}\right)
\qquad
 d\theta=\frac{dz}{iz}
$$

Then residues inside $|z|=1$ are used

For Fourier-type integrals

$$
\int_{-\infty}^{+\infty}R(x)e^{iax}\,dx
=2\pi i\sum\operatorname{Res}\left(R(z)e^{iaz},z_k\right)
$$

where $a>0$ and $z_k$ are singularities in the upper half-plane

For rational integrals with no real poles

$$
\int_{-\infty}^{+\infty}R(x)\,dx
=2\pi i\sum\operatorname{Res}(R,z_k)
$$

If there are simple poles on the real axis then the principal value contains half-residue terms on the real axis

**eg.**

**Problem.**

Evaluate

$$
I=\oint_C\frac{z^3}{z^4-1}\,dz
$$

where

$$
C:|z|=2
$$

**Solution.**

$$
f(z)=\frac{z^3}{z^4-1}
$$

Inside $|z|<2$ there are four simple poles

$$
z_k=e^{k\pi i/2}
\qquad k=0,1,2,3
$$

$$
I=2\pi i\sum_{k=0}^{3}\operatorname{Res}(f,z_k)
$$

Using the residue at infinity

$$
I=-2\pi i\operatorname{Res}(f,\infty)
$$

$$
\operatorname{Res}(f,\infty)
=-\operatorname{Res}\left(\frac{1}{z^2}f\left(\frac{1}{z}\right),0\right)
$$

$$
\frac{1}{z^2}f\left(\frac{1}{z}\right)
=\frac{1}{z^2}\frac{z}{1-z^4}
=\frac{1}{z(1-z^4)}
$$

$$
\operatorname{Res}\left(\frac{1}{z(1-z^4)},0\right)=1
$$

$$
I=2\pi i
$$

**eg.**

**Problem.**

Evaluate

$$
I=\int_0^{2\pi}\frac{\cos2\theta}{1-2p\cos\theta+p^2}\,d\theta
\qquad
|p|<1
$$

**Solution.**

$$
z=e^{i\theta}
\qquad
\cos n\theta=\frac{1}{2}\left(z^n+z^{-n}\right)
\qquad
 d\theta=\frac{dz}{iz}
$$

$$
I=\oint_{|z|=1}
\frac{z^2+z^{-2}}{2}
\frac{1}{1-p(z+z^{-1})+p^2}
\frac{dz}{iz}
$$

$$
I=\frac{1}{i}\oint_{|z|=1}
\frac{z^4+1}{2z^2(1-pz)(z-p)}\,dz
$$

Let

$$
f(z)=\frac{z^4+1}{2z^2(1-pz)(z-p)}
$$

The poles inside $|z|=1$ are

$$
z=0
\qquad
z=p
$$

$$
I=2\pi\left[
\operatorname{Res}(f,0)+\operatorname{Res}(f,p)
\right]
$$

$$
\operatorname{Res}(f,0)=-\frac{1}{2}-\frac{1}{2p^2}
$$

$$
\operatorname{Res}(f,p)=\frac{1+p^4}{2p^2(1-p^2)}
$$

$$
\operatorname{Res}(f,0)+\operatorname{Res}(f,p)=\frac{p^2}{1-p^2}
$$

$$
I=\frac{2\pi p^2}{1-p^2}
$$

**eg.**

**Problem.**

Evaluate

$$
I=\int_0^{\pi}\frac{\cos3\theta}{5-4\cos\theta}\,d\theta
$$

**Solution.**

$$
I=\frac{1}{2}\int_0^{2\pi}\frac{\cos3\theta}{5-4\cos\theta}\,d\theta
$$

$$
z=e^{i\theta}
\qquad
\cos3\theta=\frac{1}{2}(z^3+z^{-3})
\qquad
 d\theta=\frac{dz}{iz}
$$

$$
I=\frac{1}{2}\oint_{|z|=1}
\frac{z^3+z^{-3}}{5-2(z+z^{-1})}\frac{dz}{iz}
$$

$$
=\frac{1}{4i}\oint_{|z|=1}\frac{z^6+1}{z^3(-2z^2+5z-2)}\,dz
$$

$$
-2z^2+5z-2=-(2z-1)(z-2)
$$

The poles inside $|z|=1$ are $z=0$ and $z=1/2$

Let

$$
G(z)=\frac{z^6+1}{z^3(-2z^2+5z-2)}
$$

Then

$$
\operatorname{Res}(G,0)=-\frac{21}{8}
\qquad
\operatorname{Res}\left(G,\frac{1}{2}\right)=\frac{65}{24}
$$

$$
\operatorname{Res}(G,0)+\operatorname{Res}\left(G,\frac{1}{2}\right)=\frac{1}{12}
$$

$$
I=\frac{1}{4i}\cdot2\pi i\cdot\frac{1}{12}=\frac{\pi}{24}
$$

**eg.**

**Problem.**

Evaluate

$$
I=\int_{-\infty}^{+\infty}\frac{x\cos x}{x^2-2x+10}\,dx
$$

**Solution.**

$$
x^2-2x+10=(x-1-3i)(x-1+3i)
$$

$$
\int_{-\infty}^{+\infty}\frac{xe^{ix}}{x^2-2x+10}\,dx
=2\pi i\operatorname{Res}\left(\frac{ze^{iz}}{(z-1-3i)(z-1+3i)},1+3i\right)
$$

$$
=2\pi i\lim_{z\to1+3i}
\frac{ze^{iz}}{z-1+3i}
$$

$$
=2\pi i\frac{(1+3i)e^{i(1+3i)}}{6i}
$$

$$
=\frac{\pi}{3}e^{-3}(1+3i)(\cos1+i\sin1)
$$

$$
I=\operatorname{Re}\left[\frac{\pi}{3}e^{-3}(1+3i)(\cos1+i\sin1)\right]
$$

$$
I=\frac{\pi e^{-3}}{3}(\cos1-3\sin1)
$$

**eg.**

**Problem.**

Evaluate

$$
I=\int_0^{+\infty}\frac{\sin x}{x}\,dx
$$

**Solution.**

$$
I=\frac{1}{2}\int_{-\infty}^{+\infty}\frac{\sin x}{x}\,dx=\frac{1}{2}\operatorname{Im}\int_{-\infty}^{+\infty}\frac{e^{ix}}{x}\,dx
$$

Using the indentation contour at $z=0$. Here `PV` denotes the Cauchy principal value

$$
\operatorname{PV}\int_{-\infty}^{+\infty}\frac{e^{ix}}{x}\,dx
=
\lim_{\varepsilon\to0^+}
\left(
\int_{-\infty}^{-\varepsilon}\frac{e^{ix}}{x}\,dx
+
\int_{\varepsilon}^{+\infty}\frac{e^{ix}}{x}\,dx
\right)
=i\pi
$$

$$
I=\frac{1}{2}\operatorname{Im}(i\pi)
$$

$$
I=\frac{\pi}{2}
$$
