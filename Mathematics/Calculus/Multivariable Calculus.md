# Multivariable Calculus

[toc]

### Vector Algebra and Coordinate Systems

##### Basic vector identities

$$
\boldsymbol{A}\times \boldsymbol{B}=-\boldsymbol{B}\times \boldsymbol{A}
$$

The scalar triple product is invariant under cyclic permutation

$$
\boldsymbol{A}\cdot(\boldsymbol{B}\times \boldsymbol{C})
=\boldsymbol{B}\cdot(\boldsymbol{C}\times \boldsymbol{A})
=\boldsymbol{C}\cdot(\boldsymbol{A}\times \boldsymbol{B})
=
\begin{vmatrix}
 a_1&a_2&a_3\\
 b_1&b_2&b_3\\
 c_1&c_2&c_3
\end{vmatrix}
$$

Vector triple products

$$
(\boldsymbol{A}\times\boldsymbol{B})\times\boldsymbol{C}
=(\boldsymbol{A}\cdot\boldsymbol{C})\boldsymbol{B}-(\boldsymbol{B}\cdot\boldsymbol{C})\boldsymbol{A}
$$

$$
\boldsymbol{A}\times(\boldsymbol{B}\times\boldsymbol{C})
=(\boldsymbol{A}\cdot\boldsymbol{C})\boldsymbol{B}-(\boldsymbol{A}\cdot\boldsymbol{B})\boldsymbol{C}
$$

Let

$$
\boldsymbol{A}=A_x\boldsymbol{e}_x+A_y\boldsymbol{e}_y+A_z\boldsymbol{e}_z
\qquad
\boldsymbol{B}=B_x\boldsymbol{e}_x+B_y\boldsymbol{e}_y+B_z\boldsymbol{e}_z
$$

Then

$$
\boldsymbol{A}+\boldsymbol{B}
=(A_x+B_x)\boldsymbol{e}_x+(A_y+B_y)\boldsymbol{e}_y+(A_z+B_z)\boldsymbol{e}_z
$$

$$
\boldsymbol{A}\cdot\boldsymbol{B}=A_xB_x+A_yB_y+A_zB_z
$$

$$
\boldsymbol{A}\times\boldsymbol{B}=
\begin{vmatrix}
\boldsymbol{e}_x&\boldsymbol{e}_y&\boldsymbol{e}_z\\
A_x&A_y&A_z\\
B_x&B_y&B_z
\end{vmatrix}
=(A_yB_z-A_zB_y)\boldsymbol{e}_x+(A_zB_x-A_xB_z)\boldsymbol{e}_y+(A_xB_y-A_yB_x)\boldsymbol{e}_z
$$

##### Basis cross products

| Cartesian | Cylindrical | Spherical |
|---|---|---|
| $\boldsymbol{e}_x\times\boldsymbol{e}_y=\boldsymbol{e}_z$ | $\boldsymbol{e}_\rho\times\boldsymbol{e}_\varphi=\boldsymbol{e}_z$ | $\boldsymbol{e}_r\times\boldsymbol{e}_\varphi=\boldsymbol{e}_\theta$ |
| $\boldsymbol{e}_y\times\boldsymbol{e}_z=\boldsymbol{e}_x$ | $\boldsymbol{e}_\varphi\times\boldsymbol{e}_z=\boldsymbol{e}_\rho$ | $\boldsymbol{e}_\varphi\times\boldsymbol{e}_\theta=\boldsymbol{e}_r$ |
| $\boldsymbol{e}_z\times\boldsymbol{e}_x=\boldsymbol{e}_y$ | $\boldsymbol{e}_z\times\boldsymbol{e}_\rho=\boldsymbol{e}_\varphi$ | $\boldsymbol{e}_\theta\times\boldsymbol{e}_r=\boldsymbol{e}_\varphi$ |

##### Scale factors and differential elements

For spherical coordinates, this file uses $\varphi$ as the polar angle and $\theta$ as the azimuthal angle.

| Coordinate system | Scale factors | Position vector | Differential displacement |
|---|---|---|---|
| Cartesian $(x,y,z)$ | $h_x=1,\ h_y=1,\ h_z=1$ | $\boldsymbol{r}=x\boldsymbol{e}_x+y\boldsymbol{e}_y+z\boldsymbol{e}_z$ | $d\boldsymbol{r}=\boldsymbol{e}_x\,dx+\boldsymbol{e}_y\,dy+\boldsymbol{e}_z\,dz$ |
| Cylindrical $(\rho,\varphi,z)$ | $h_\rho=1,\ h_\varphi=\rho,\ h_z=1$ | $\boldsymbol{r}=\rho\boldsymbol{e}_\rho+z\boldsymbol{e}_z$ | $d\boldsymbol{r}=\boldsymbol{e}_\rho\,d\rho+\boldsymbol{e}_\varphi\,\rho d\varphi+\boldsymbol{e}_z\,dz$ |
| Spherical $(r,\varphi,\theta)$ | $h_r=1,\ h_\varphi=r,\ h_\theta=r\sin\varphi$ | $\boldsymbol{r}=r\boldsymbol{e}_r$ | $d\boldsymbol{r}=\boldsymbol{e}_r\,dr+\boldsymbol{e}_\varphi\,r d\varphi+\boldsymbol{e}_\theta\,r\sin\varphi\,d\theta$ |

| Coordinate system | Surface elements | Volume element |
|---|---|---|
| Cartesian | $dS_x=dy\,dz$<br>$dS_y=dx\,dz$<br>$dS_z=dx\,dy$ | $dV=dx\,dy\,dz$ |
| Cylindrical | $dS_\rho=\rho\,d\varphi\,dz$<br>$dS_\varphi=d\rho\,dz$<br>$dS_z=\rho\,d\rho\,d\varphi$ | $dV=\rho\,d\rho\,d\varphi\,dz$ |
| Spherical | $dS_r=r^2\sin\varphi\,d\varphi\,d\theta$<br>$dS_\varphi=r\sin\varphi\,dr\,d\theta$<br>$dS_\theta=r\,dr\,d\varphi$ | $dV=r^2\sin\varphi\,dr\,d\varphi\,d\theta$ |

### Analytic Geometry in Space

##### Lines and planes

Equations of lines

| Form | Equation | Data |
|---|---|---|
| Parametric form | $\begin{cases}x=x_0+lt\\y=y_0+mt\\z=z_0+nt\end{cases}$ | $t\in(-\infty,+\infty)$<br>$\boldsymbol{s}=(l,m,n)$ |
| Symmetric form | $\dfrac{x-x_0}{l}=\dfrac{y-y_0}{m}=\dfrac{z-z_0}{n}$ | point $M_0(x_0,y_0,z_0)$<br>$\boldsymbol{s}=(l,m,n)$ |
| Intersection of two planes | $\begin{cases}A_1x+B_1y+C_1z+D_1=0\\A_2x+B_2y+C_2z+D_2=0\end{cases}$ | $\boldsymbol{s}=(A_1,B_1,C_1)\times(A_2,B_2,C_2)$ |
| Two-point form | $\dfrac{x-x_1}{x_1-x_2}=\dfrac{y-y_1}{y_1-y_2}=\dfrac{z-z_1}{z_1-z_2}$ | $\boldsymbol{s}=(x_1-x_2,y_1-y_2,z_1-z_2)$ |

Equations of planes

| Form              | Equation                                   | Data                                           |
| ----------------- | ------------------------------------------ | ---------------------------------------------- |
| Point-normal form | $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$             | $M_0(x_0,y_0,z_0)$<br>$\boldsymbol{n}=(A,B,C)$ |
| General form      | $Ax+By+Cz+D=0$                             | $\boldsymbol{n}=(A,B,C)$                       |
| Intercept form    | $\dfrac{x}{a}+\dfrac{y}{b}+\dfrac{z}{c}=1$ | intercepts $a,b,c$                             |

**Distance**

Distance from $P(x_1,y_1,z_1)$ to the plane $Ax+By+Cz+D=0$

$$
d=\frac{|Ax_1+By_1+Cz_1+D|}{\sqrt{A^2+B^2+C^2}}
$$

Distance from $P$ to the line

$$
\frac{x-x_0}{l}=\frac{y-y_0}{m}=\frac{z-z_0}{n}
$$

is

$$
d=\lVert\overrightarrow{QP}\rVert\sin\theta
=\frac{\lVert\overrightarrow{QP}\times\boldsymbol{s}\rVert}{\lVert\boldsymbol{s}\rVert}
$$

where $Q(x_0,y_0,z_0)$ is a point on the line and $\boldsymbol{s}=(l,m,n)$.

**Angles**

| Angle | Formula | Range |
|---|---|---|
| Between normal vectors | $\displaystyle \cos\theta=\frac{\boldsymbol{n}_1\cdot\boldsymbol{n}_2}{\lVert\boldsymbol{n}_1\rVert\lVert\boldsymbol{n}_2\rVert}$ | $\theta\in[0,\pi]$ |
| Between line and plane | $\displaystyle \sin\theta=\frac{\left\lvert\boldsymbol{s}\cdot\boldsymbol{n}\right\rvert}{\lVert\boldsymbol{s}\rVert\lVert\boldsymbol{n}\rVert}$ | $\theta\in\left[0,\frac{\pi}{2}\right]$ |
| Between lines | $\displaystyle \cos\theta=\frac{\left\lvert\boldsymbol{s}_1\cdot\boldsymbol{s}_2\right\rvert}{\lVert\boldsymbol{s}_1\rVert\lVert\boldsymbol{s}_2\rVert}$ | $\theta\in\left[0,\frac{\pi}{2}\right]$ |

The unit vector in the direction of $\boldsymbol{v}$ is

$$
\boldsymbol{e}_v=\frac{\boldsymbol{v}}{\lVert\boldsymbol{v}\rVert}
$$

##### Pencil of planes

If a line $L$ is given by

$$
\begin{cases}
A_1x+B_1y+C_1z+D_1=0,\\
A_2x+B_2y+C_2z+D_2=0
\end{cases}
$$

then all planes through $L$ can be written as

$$
A_1x+B_1y+C_1z+D_1
+\lambda(A_2x+B_2y+C_2z+D_2)=0
$$

This family is called a pencil of planes.

##### Space curves and surfaces

| Object | Equation | Tangent or normal |
|---|---|---|
| Parametric space curve | $\Gamma:\begin{cases}x=x(t)\\y=y(t)\\z=z(t)\end{cases}$ | $\boldsymbol{T}=(x'(t_0),y'(t_0),z'(t_0))$ |
| Normal plane of a parametric space curve | point $(x_0,y_0,z_0)$ at $t=t_0$ | $x'(t_0)(x-x_0)+y'(t_0)(y-y_0)+z'(t_0)(z-z_0)=0$ |
| Implicit space curve | $\Gamma:\begin{cases}F(x,y,z)=0\\G(x,y,z)=0\end{cases}$ | $\boldsymbol{T}=\nabla F\times\nabla G=\left(\dfrac{\partial(F,G)}{\partial(y,z)},\dfrac{\partial(F,G)}{\partial(z,x)},\dfrac{\partial(F,G)}{\partial(x,y)}\right)$ |
| Implicit surface | $\Sigma:F(x,y,z)=0$ | $\boldsymbol{n}=\pm(F_x,F_y,F_z)$ |
| Graph surface | $\Sigma:z=f(x,y)$ | $\boldsymbol{n}=(f_x,f_y,-1)$ |

##### Examples

**eg.**

**Problem.**

Find the equation of the line $L_2$ passing through $A(2,1,3)$ and intersecting the line $L_1$ perpendicularly

$$
L_1:\frac{x+1}{3}=\frac{y-1}{2}=\frac{z}{-1}
$$

**Solution.**

$$
\boldsymbol{s}_1=(3,2,-1)
\qquad
\frac{x+1}{3}=\frac{y-1}{2}=\frac{z}{-1}=t
\qquad
P(3t-1,2t+1,-t)
$$

$$
\boldsymbol{s}_2=P-A=(3t-3,2t,-t-3)
\qquad
\boldsymbol{s}_1\cdot\boldsymbol{s}_2=0
$$

$$
3(3t-3)+2\cdot 2t+(-1)(-t-3)=0
\qquad
t=\frac{3}{7}
$$

$$
\boldsymbol{s}_2=\left(-\frac{12}{7},-\frac{6}{7},-\frac{24}{7}\right)
=\frac{6}{7}(-2,-1,-4)
$$

$$
L_2:\frac{x-2}{-2}=\frac{y-1}{-1}=\frac{z-3}{-4}
$$

**eg.**

**Problem.**

Let $f(x,y)$ be differentiable and satisfy

$$
f(tu,tv)=t^2f(u,v)
$$

The point $P(1,-1,2)$ lies on the surface $z=f(x,y)$ and

$$
f_x(1,-1)=3
$$

Find the tangent plane of the surface at $P$

**Solution.**

$$
\boldsymbol{n}=(f_x,f_y,-1)
\qquad
f(tu,tv)=t^2f(u,v)
$$

$$
u f_1(tu,tv)+v f_2(tu,tv)=2t f(u,v)
\qquad
tu=1
\quad
tv=-1
$$

$$
f_1(1,-1)-f_2(1,-1)=2f(1,-1)
\qquad
3-f_2(1,-1)=4
\qquad
f_2(1,-1)=-1
$$

$$
3(x-1)-(y+1)-(z-2)=0
\qquad
3x-y-z-2=0
$$

### Multivariable Differential Calculus

$$
\text{continuous partial derivatives}
\Longrightarrow
\text{differentiability}
\Longrightarrow
\text{continuity}
\Longrightarrow
\text{existence of the limit}
$$

Also
$$
\text{differentiability}\Longrightarrow\text{existence of partial derivatives}
$$

Remarks:

- Continuity does not necessarily imply the existence of partial derivatives.
- Existence of partial derivatives does not necessarily imply continuity.

##### Implicit differentiation

For $F(x,y)=0$ and $F_y\ne0$
$$
\frac{dy}{dx}=-\frac{F_x}{F_y}
$$

For $F(x,y,z)=0$ and $F_z\ne0$
$$
\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}
\qquad
\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}
$$

For a system

$$
\begin{cases}
F(x,y,u,v)=0,\\
G(x,y,u,v)=0
\end{cases}
\qquad
u=u(x,y),\quad v=v(x,y)
$$

use the Jacobian

$$
J=\frac{\partial(F,G)}{\partial(u,v)}
=
\begin{vmatrix}
F_u&F_v\\
G_u&G_v
\end{vmatrix}
$$

Partial derivatives of $u$ and $v$ are found by differentiating the system directly.

##### Extrema of functions

| Item | Statement |
|---|---|
| Necessary condition | If $f$ has a local extremum at an interior point $(x_0,y_0)$ and the partial derivatives exist, then $f_x(x_0,y_0)=0,\ f_y(x_0,y_0)=0$ |
| Second derivative notation | $A=f_{xx}(x_0,y_0),\ B=f_{xy}(x_0,y_0),\ C=f_{yy}(x_0,y_0),\ D=AC-B^2$ |

| Condition | Conclusion |
|---|---|
| $D>0,\ A>0$ | local minimum |
| $D>0,\ A<0$ | local maximum |
| $D<0$ | not an extremum |
| $D=0$ | inconclusive |

##### Constrained extrema 

**Lagrange multipliers**

To find extrema of

$$
z=f(x,y)
$$

subject to

$$
\varphi(x,y)=0
$$

At a regular constrained extremum, assume

$$
\nabla\varphi(x_0,y_0)\ne\boldsymbol{0}.
$$

Construct

$$
L(x,y,\lambda)=f(x,y)+\lambda\varphi(x,y)
$$

Solve

$$
\begin{cases}
f_x+\lambda\varphi_x=0\\
f_y+\lambda\varphi_y=0\\
\varphi=0
\end{cases}
$$

For absolute extrema, compare the values at stationary points with boundary values.

##### Vector differential operators

**Nabla and Laplace operators**
$$
\nabla=\left(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}\right)
$$

$$
\Delta=\nabla^2
=\frac{\partial^2}{\partial x^2}
+\frac{\partial^2}{\partial y^2}
+\frac{\partial^2}{\partial z^2}
$$

**Gradient**

For a scalar field $u$
$$
\operatorname{grad}u=\nabla u
=\frac{\partial u}{\partial x}\boldsymbol{e}_x
+\frac{\partial u}{\partial y}\boldsymbol{e}_y
+\frac{\partial u}{\partial z}\boldsymbol{e}_z
$$

In an orthogonal coordinate system $(q_1,q_2,q_3)$ with scale factors $(h_1,h_2,h_3)$
$$
\nabla u=
\frac{1}{h_1}\frac{\partial u}{\partial q_1}\boldsymbol{e}_1
+\frac{1}{h_2}\frac{\partial u}{\partial q_2}\boldsymbol{e}_2
+\frac{1}{h_3}\frac{\partial u}{\partial q_3}\boldsymbol{e}_3
$$

The directional derivative in the direction $\boldsymbol{e}_l$ is

$$
\frac{\partial u}{\partial l}=\boldsymbol{e}_l\cdot\nabla u
$$

The gradient is normal to a level surface and points in the direction of fastest increase.

Useful identities

$$
\nabla(Cu)=C\nabla u
\qquad
\nabla(u+v)=\nabla u+\nabla v
$$

$$
\nabla(uv)=v\nabla u+u\nabla v
$$

$$
\nabla\left(\frac{u}{v}\right)
=\frac{v\nabla u-u\nabla v}{v^2}
$$

$$
\nabla f(u)=f'(u)\nabla u
$$

Let

$$
\boldsymbol{R}=\boldsymbol{r}-\boldsymbol{r}',
\qquad
R=\lVert\boldsymbol{R}\rVert
\qquad
\boldsymbol{e}_R=\frac{\boldsymbol{R}}{R}
$$

Then

$$
\nabla R=\boldsymbol{e}_R
\qquad
\nabla\left(\frac{1}{R}\right)=-\frac{\boldsymbol{e}_R}{R^2}
\qquad
\nabla'\left(\frac{1}{R}\right)=\frac{\boldsymbol{e}_R}{R^2}
$$

**Divergence**

For

$$
\boldsymbol{F}=F_x\boldsymbol{e}_x+F_y\boldsymbol{e}_y+F_z\boldsymbol{e}_z
$$

$$
\operatorname{div}\boldsymbol{F}=\nabla\cdot\boldsymbol{F}
=\frac{\partial F_x}{\partial x}
+\frac{\partial F_y}{\partial y}
+\frac{\partial F_z}{\partial z}
$$

In orthogonal coordinates
$$
\nabla\cdot\boldsymbol{F}
=\frac{1}{h_1h_2h_3}
\left[
\frac{\partial}{\partial q_1}(h_2h_3F_1)
+\frac{\partial}{\partial q_2}(h_1h_3F_2)
+\frac{\partial}{\partial q_3}(h_1h_2F_3)
\right]
$$

Flux through a surface $S$

$$
\Phi=\iint_S\boldsymbol{F}\cdot d\boldsymbol{S}
$$

Divergence theorem

$$
\iiint_V\nabla\cdot\boldsymbol{F}\,dV
=
\iint_{\partial V}\boldsymbol{F}\cdot d\boldsymbol{S}
$$

Useful identities

$$
\nabla\cdot(C\boldsymbol{F})=C\nabla\cdot\boldsymbol{F}
\qquad
\nabla\cdot(\boldsymbol{F}+\boldsymbol{G})=\nabla\cdot\boldsymbol{F}+\nabla\cdot\boldsymbol{G}
$$

$$
\nabla\cdot(u\boldsymbol{F})=\nabla u\cdot\boldsymbol{F}+u\nabla\cdot\boldsymbol{F}
$$

For $R=|\boldsymbol{r}-\boldsymbol{r}'|$
$$
\Delta\left(\frac{1}{R}\right)
=\nabla\cdot\nabla\left(\frac{1}{R}\right)
=
\begin{cases}
0, & \boldsymbol{r}\ne\boldsymbol{r}',\\
-4\pi\delta(\boldsymbol{R}), & \boldsymbol{r}=\boldsymbol{r}'.
\end{cases}
$$

**Curl**
$$
\operatorname{curl}\boldsymbol{F}=\nabla\times\boldsymbol{F}
=
\begin{vmatrix}
\boldsymbol{e}_x&\boldsymbol{e}_y&\boldsymbol{e}_z\\
\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\
F_x&F_y&F_z
\end{vmatrix}
$$

In orthogonal coordinates
$$
\nabla\times\boldsymbol{F}
=
\frac{1}{h_1h_2h_3}
\begin{vmatrix}
h_1\boldsymbol{e}_1&h_2\boldsymbol{e}_2&h_3\boldsymbol{e}_3\\
\dfrac{\partial}{\partial q_1}&\dfrac{\partial}{\partial q_2}&\dfrac{\partial}{\partial q_3}\\
h_1F_1&h_2F_2&h_3F_3
\end{vmatrix}
$$

Circulation around a closed curve $C$

$$
\Gamma=\oint_C\boldsymbol{F}\cdot d\boldsymbol{l}
$$

Stokes' theorem

$$
\iint_S(\nabla\times\boldsymbol{F})\cdot d\boldsymbol{S}
=
\oint_C\boldsymbol{F}\cdot d\boldsymbol{l}
$$

Useful identities

$$
\nabla\times(C\boldsymbol{F})=C\nabla\times\boldsymbol{F}
\qquad
\nabla\times(\boldsymbol{F}+\boldsymbol{G})=\nabla\times\boldsymbol{F}+\nabla\times\boldsymbol{G}
$$

$$
\nabla\times(u\boldsymbol{F})
=\nabla u\times\boldsymbol{F}+u\nabla\times\boldsymbol{F}
$$

Solenoidal and irrotational fields

The following representations hold locally, or on a domain where the corresponding potential exists.

| Type | Condition | Representation | Identity |
|---|---|---|---|
| Solenoidal field | $\nabla\cdot\boldsymbol{F}\equiv0$ | $\boldsymbol{F}=\nabla\times\boldsymbol{A}$ | $\nabla\cdot(\nabla\times\boldsymbol{A})\equiv0$ |
| Irrotational field | $\nabla\times\boldsymbol{F}\equiv0$ | $\boldsymbol{F}=-\nabla u$ | $\nabla\times\nabla u\equiv0$ |

For a solenoidal field with $\boldsymbol{F}=\nabla\times\boldsymbol{A}$ and $\partial S=C$,
$$
\Phi=\iint_S\boldsymbol{F}\cdot d\boldsymbol{S}
=\oint_C\boldsymbol{A}\cdot d\boldsymbol{l}
$$

For an irrotational field on a simply connected domain,
$$
\Gamma=\oint_C\boldsymbol{F}\cdot d\boldsymbol{l}=0
$$

##### Maxwell equations

| Integral form | Differential form |
|---|---|
| $\displaystyle \oint_C\boldsymbol{H}\cdot d\boldsymbol{l}=\iint_S\boldsymbol{J}\cdot d\boldsymbol{S}+\frac{\partial}{\partial t}\iint_S\boldsymbol{D}\cdot d\boldsymbol{S}$ | $\displaystyle \nabla\times\boldsymbol{H}=\boldsymbol{J}+\frac{\partial\boldsymbol{D}}{\partial t}$ |
| $\displaystyle \oint_C\boldsymbol{E}\cdot d\boldsymbol{l}=-\frac{\partial}{\partial t}\iint_S\boldsymbol{B}\cdot d\boldsymbol{S}$ | $\displaystyle \nabla\times\boldsymbol{E}=-\frac{\partial\boldsymbol{B}}{\partial t}$ |
| $\displaystyle \iint_{\partial V}\boldsymbol{B}\cdot d\boldsymbol{S}=0$ | $\displaystyle \nabla\cdot\boldsymbol{B}=0$ |
| $\displaystyle \iint_{\partial V}\boldsymbol{D}\cdot d\boldsymbol{S}=\iiint_V\rho\,dV$ | $\displaystyle \nabla\cdot\boldsymbol{D}=\rho$ |

For a linear, isotropic, stationary medium

$$
\boldsymbol{D}=\varepsilon\boldsymbol{E}=\varepsilon_r\varepsilon_0\boldsymbol{E}
\qquad
\boldsymbol{B}=\mu\boldsymbol{H}=\mu_r\mu_0\boldsymbol{H}
\qquad
\boldsymbol{J}=\sigma\boldsymbol{E}
$$

### Multiple Integrals

**Double integrals**

In Cartesian coordinates, a double integral can be evaluated by integrating first with respect to $x$ or first with respect to $y$.

In polar coordinates
$$
x=\rho\cos\theta
\qquad
y=\rho\sin\theta
\qquad
dx\,dy=\rho\,d\rho\,d\theta
$$

Hence

$$
\iint_D f(x,y)\,dx\,dy
=
\int_\alpha^\beta\int_{r_1(\theta)}^{r_2(\theta)}
f(\rho\cos\theta,\rho\sin\theta)\rho\,d\rho\,d\theta
$$

**Change of variables**

Let

$$
T:
\begin{cases}
x=x(u,v),\\
y=y(u,v)
\end{cases}
\qquad
J(u,v)=\frac{\partial(x,y)}{\partial(u,v)}\ne0
$$

Then

$$
\iint_D f(x,y)\,dx\,dy
=
\iint_{D'} f(x(u,v),y(u,v))\,|J(u,v)|\,du\,dv
$$

**Triple integrals**

Cylindrical coordinates.

Use cylindrical coordinates especially for expressions involving $x^2+y^2$

$$
x=\rho\cos\theta
\qquad
y=\rho\sin\theta
\qquad
z=z
$$

$$
dV=\rho\,d\rho\,d\theta\,dz
$$

Thus

$$
\iiint_\Omega f(x,y,z)\,dV
=
\int_\alpha^\beta\int_{r_1}^{r_2}\int_{z_1}^{z_2}
f(\rho\cos\theta,\rho\sin\theta,z)\rho\,dz\,d\rho\,d\theta
$$

Spherical coordinates.

Use spherical coordinates especially for expressions involving $x^2+y^2+z^2$.
Here $\varphi$ is the polar angle and $\theta$ is the azimuthal angle

$$
x=r\sin\varphi\cos\theta
\qquad
y=r\sin\varphi\sin\theta
\qquad
z=r\cos\varphi
$$

$$
dV=r^2\sin\varphi\,dr\,d\varphi\,d\theta
$$

**Direction cosines**

For $\boldsymbol{v}=(v_x,v_y,v_z)$
$$
\cos\alpha=\frac{v_x}{\lVert\boldsymbol{v}\rVert}
\qquad
\cos\beta=\frac{v_y}{\lVert\boldsymbol{v}\rVert}
\qquad
\cos\gamma=\frac{v_z}{\lVert\boldsymbol{v}\rVert}
$$

Differentiation of iterated integrals

Let

$$
G(x)=\int_{a(x)}^{b(x)}\int_{c(x,s)}^{d(x,s)} f(s,t,x)\,dt\,ds
$$

Then

$$
\begin{aligned}
G'(x)
=&\int_{a(x)}^{b(x)}\int_{c(x,s)}^{d(x,s)}\frac{\partial f}{\partial x}(s,t,x)\,dt\,ds +b'(x)\int_{c(x,b(x))}^{d(x,b(x))}f(b(x),t,x)\,dt \\
&-a'(x)\int_{c(x,a(x))}^{d(x,a(x))}f(a(x),t,x)\,dt +\int_{a(x)}^{b(x)}f(s,d(x,s),x)\frac{\partial d}{\partial x}(x,s)\,ds \\
&-\int_{a(x)}^{b(x)}f(s,c(x,s),x)\frac{\partial c}{\partial x}(x,s)\,ds
\end{aligned}
$$

##### Symmetry

If $D$ is symmetric about the $x$-axis, and $D_1$ and $D_2$ are mirror images with respect to the $x$-axis, then

$$
\iint_D f(x,y)\,d\sigma
=\iint_D f(x,-y)\,d\sigma
$$

Therefore
$$
\iint_D f(x,y)\,d\sigma
=
\begin{cases}
2\displaystyle\iint_{D_1}f(x,y)\,d\sigma, & f(x,y)\text{ is even in }y,\\[6pt]
0, & f(x,y)\text{ is odd in }y
\end{cases}
$$

##### Line integrals

**First kind** : with respect to arc length

For a plane curve $L$
$$
\int_L f(x,y)\,ds
$$

If $L$ is given by $y=y(x)$
$$
\int_L f(x,y)\,ds
=\int_a^b f(x,y(x))\sqrt{1+[y'(x)]^2}\,dx
$$

If $L$ is given in polar form $r=r(\theta)$
$$
\int_L f(x,y)\,ds
=\int_\alpha^\beta f(r\cos\theta,r\sin\theta)
\sqrt{r^2+[r'(\theta)]^2}\,d\theta
$$

**Second kind** : with respect to coordinates
$$
\int_L P(x,y)\,dx+Q(x,y)\,dy
$$

If $x=x(t),y=y(t)$, then

$$
\int_L P\,dx+Q\,dy
=\int_\alpha^\beta \left[P(x(t),y(t))x'(t)+Q(x(t),y(t))y'(t)\right]dt
$$

With direction cosines $\cos\alpha,\cos\beta$
$$
\int_L P\,dx+Q\,dy
=
\int_L(P\cos\alpha+Q\cos\beta)\,ds
$$

**Green's theorem**

For a positively oriented simple closed curve $L=\partial D$
$$
\oint_L P(x,y)\,dx+Q(x,y)\,dy
=
\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dx\,dy
$$

The integral is path independent in a simply connected domain $G$ if and only if

$$
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=0
\qquad\text{in }G
$$

**Stokes' theorem** in coordinate form
$$
\oint_L P\,dx+Q\,dy+R\,dz
=
\iint_S
\begin{vmatrix}
dy\,dz&dz\,dx&dx\,dy\\
\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\
P&Q&R
\end{vmatrix}
$$

For a parametric curve $x=x(t),y=y(t),z=z(t)$
$$
\oint_L P\,dx+Q\,dy+R\,dz
=
\int_\alpha^\beta [Px'(t)+Qy'(t)+Rz'(t)]\,dt
$$

##### Surface integrals

**First kind** : with respect to area

For $z=z(x,y)$
$$
\iint_\Sigma f(x,y,z)\,dS
=
\iint_{D_{xy}} f(x,y,z(x,y))|\sec\gamma|\,dx\,dy
$$

where $\gamma$ is the angle between the normal and the positive $z$-axis. Equivalently,
$$
dS=\sqrt{1+z_x^2+z_y^2}\,dx\,dy
$$

**Second kind** : with respect to coordinates
$$
\iint_\Sigma P\,dy\,dz+Q\,dz\,dx+R\,dx\,dy
$$

If $\Sigma$ is written as $z=z(x,y)$, then

$$
\iint_\Sigma P\,dy\,dz+Q\,dz\,dx+R\,dx\,dy
=
\pm\iint_{D_{xy}}(-Pz_x-Qz_y+R)\,dx\,dy
$$

Use $+$ for the upper side and $-$ for the lower side.

**Gauss' theorem**
$$
\iint_{\partial\Omega}P\,dy\,dz+Q\,dz\,dx+R\,dx\,dy
=
\iiint_\Omega
\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)dV
$$

In direction-cosine form
$$
\iint_\Sigma P\,dy\,dz+Q\,dz\,dx+R\,dx\,dy
=
\iint_\Sigma (P\cos\alpha+Q\cos\beta+R\cos\gamma)\,dS
$$


##### Examples

**eg.**

**Problem.**

Let $z=z(x,y)$ satisfy

$$
x^2\frac{\partial z}{\partial x}+y^2\frac{\partial z}{\partial y}=2z^2
$$

Set

$$
u=x,\qquad v=\frac{1}{y}-\frac{1}{x},\qquad w=\frac{1}{z}-\frac{1}{x}
$$

For $w=w(u,v)$, find

$$
\left.\frac{\partial w}{\partial u}\right|_{u=2,v=1}
$$

**Solution.**

$$
w_x=-\frac{z_x}{z^2}+\frac{1}{x^2}=w_u u_x+w_v v_x
=w_u+\frac{1}{x^2}w_v
$$

$$
w_y=-\frac{z_y}{z^2}=w_u u_y+w_v v_y
=-\frac{1}{y^2}w_v
$$

$$
\frac{x^2z_x+y^2z_y}{z^2}=2
\qquad
-x^2\left(w_x-\frac{1}{x^2}\right)-y^2w_y=2
$$

$$
-x^2w_u=1
\qquad
w_u=-\frac{1}{x^2}
\qquad
\left.w_u\right|_{u=2,v=1}=-\frac{1}{4}
$$

**eg.**

**Problem.**

Given

$$
z=xf\left(\frac{y}{x}\right)+2y\varphi\left(\frac{x}{y}\right)
$$

where $f$ and $\varphi$ are twice differentiable

Find

$$
\frac{\partial z}{\partial x},\qquad \frac{\partial^2 z}{\partial x\partial y}
$$

If $f=\varphi$ and

$$
\left.\frac{\partial^2 z}{\partial x\partial y}\right|_{x=a}=-by^2
$$

find $f(y)$

**Solution.**

$$
\frac{\partial z}{\partial x}
=f\left(\frac{y}{x}\right)
+x f'\left(\frac{y}{x}\right)\left(-\frac{y}{x^2}\right)
+2y\varphi'\left(\frac{x}{y}\right)\frac{1}{y}
$$

$$
\frac{\partial z}{\partial x}
=f\left(\frac{y}{x}\right)-\frac{y}{x}f'\left(\frac{y}{x}\right)+2\varphi'\left(\frac{x}{y}\right)
$$

$$
\frac{\partial^2 z}{\partial x\partial y}
=-\frac{y}{x^2}f''\left(\frac{y}{x}\right)-\frac{2x}{y^2}\varphi''\left(\frac{x}{y}\right)
$$

$$
x=a
\qquad
-\frac{y}{a^2}f''\left(\frac{y}{a}\right)-\frac{2a}{y^2}f''\left(\frac{a}{y}\right)=-by^2
$$

$$
\frac{y}{a^2}f''\left(\frac{y}{a}\right)+\frac{2a}{y^2}f''\left(\frac{a}{y}\right)=by^2
$$

Let
$$
s=\frac{y}{a}.
$$

Then
$$
f''(s)+\frac{2}{s^3}f''\left(\frac{1}{s}\right)=a^3bs.
$$

Replacing $s$ by $1/s$ gives
$$
f''\left(\frac{1}{s}\right)+2s^3f''(s)=\frac{a^3b}{s}.
$$

Solving the two equations,
$$
f''(s)=\frac{a^3b}{3}\left(\frac{2}{s^4}-s\right).
$$

Thus
$$
f''(y)=\frac{a^3b}{3}\left(\frac{2}{y^4}-y\right).
$$

$$
f'(y)=\frac{a^3b}{3}\left(-\frac{2}{3y^3}-\frac{y^2}{2}\right)+C_1
\qquad
f(y)=\frac{a^3b}{3}\left(\frac{1}{3y^2}-\frac{y^3}{6}\right)+C_1y+C_2
$$

**eg.**

**Problem.**

Evaluate

$$
\int_0^1 dx\int_x^{\sqrt{x}}\frac{\cos y}{y}\,dy
$$

**Solution.**

$$
0\le y\le1
\qquad
y^2\le x\le y
$$

$$
\int_0^1 dx\int_x^{\sqrt{x}}\frac{\cos y}{y}\,dy
=
\int_0^1\frac{\cos y}{y}\int_{y^2}^{y}dx\,dy
=
\int_0^1(1-y)\cos y\,dy
=1-\cos1
$$

**eg.**

**Problem.**

Let

$$
D=\left\{(x,y)\mid 0\le x+y\le\frac{\pi}{2},\quad 0\le x-y\le\frac{\pi}{2}\right\}
$$

Evaluate

$$
I=\iint_D y\sin(x+y)\,dx\,dy
$$

**Solution.**

$$
u=x+y
\qquad
v=x-y
\qquad
x=\frac{u+v}{2}
\qquad
y=\frac{u-v}{2}
\qquad
|J|=\frac{1}{2}
$$

$$
I=\frac{1}{4}\int_0^{\pi/2}\sin u\,du\int_0^{\pi/2}(u-v)\,dv
=\frac{\pi}{8}\left(1-\frac{\pi}{4}\right)
$$

**eg.**

**Problem.**

Find the arc length of the first-quadrant curve

$$
x^{2/3}+y^{2/3}=a^{2/3}
$$

**Solution.**

$$
x=a\cos^3t
\qquad
y=a\sin^3t
\qquad
0\le t\le\frac{\pi}{2}
$$

$$
ds=\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}\,dt
=3a\sin t\cos t\,dt
$$

$$
L=\int_0^{\pi/2}3a\sin t\cos t\,dt
=\frac{3a}{2}
$$

**eg.**

**Problem.**

Let $L$ be the circle $x^2+y^2=9$ with counterclockwise orientation

Evaluate

$$
\oint_L \frac{-y}{4x^2+y^2}\,dx+\frac{x}{4x^2+y^2}\,dy
$$

**Solution.**

$$
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=0
\qquad
L':4x^2+y^2=r^2
$$

$$
x=\frac{r}{2}\cos\theta
\qquad
y=r\sin\theta
$$

$$
\oint_L \frac{-y}{4x^2+y^2}\,dx+\frac{x}{4x^2+y^2}\,dy
=\int_0^{2\pi}\left(\frac{1}{2}\sin^2\theta+\frac{1}{2}\cos^2\theta\right)d\theta
=\pi
$$

**eg.**

**Problem.**

Let $f(x)$ be even and let $L$ be the positively oriented circle

$$
x^2+y^2=-2y
$$

Evaluate

$$
I=\oint_L f(x)\,dy
$$

**Solution.**

$$
I=\iint_S f'(x)\,dx\,dy
=\int_{-2}^{0}dy\int_{-\sqrt{-y^2-2y}}^{\sqrt{-y^2-2y}}f'(x)\,dx
$$

$$
=\int_{-2}^{0}\left[f\left(\sqrt{-y^2-2y}\right)-f\left(-\sqrt{-y^2-2y}\right)\right]dy
=0
$$

**eg.**

**Problem.**

Evaluate

$$
I=\oint_\Gamma (y^2+z^2)\,dx+(z^2+x^2)\,dy+(x^2+y^2)\,dz
$$

where

$$
\Gamma:
\begin{cases}
x^2+y^2+z^2=2Rx\\
x^2+y^2=2rx
\end{cases}
\qquad r<R\qquad z\ge0
$$

The direction is consistent with the right-hand rule along the positive $z$-axis

**Solution.**

Let $S$ be the upper part of the sphere and let $D$ be its projection onto the $xy$-plane:

$$
D:x^2+y^2\le2rx.
$$

For
$$
\boldsymbol{F}=(y^2+z^2,\ z^2+x^2,\ x^2+y^2),
$$

$$
\nabla\times\boldsymbol{F}
=2(y-z)\boldsymbol{e}_x+2(z-x)\boldsymbol{e}_y+2(x-y)\boldsymbol{e}_z.
$$

On the upper sphere
$$
z=\sqrt{2Rx-x^2-y^2},
\qquad
 d\boldsymbol{S}=(-z_x,-z_y,1)\,dx\,dy.
$$

Since
$$
z_x=\frac{R-x}{z},
\qquad
z_y=-\frac{y}{z},
$$

$$
(\nabla\times\boldsymbol{F})\cdot d\boldsymbol{S}
=\frac{2R(z-y)}{z}\,dx\,dy
=2R\,dx\,dy-\frac{2Ry}{z}\,dx\,dy.
$$

The domain $D$ is symmetric about the $x$-axis, and $y/z$ is odd in $y$. Therefore,
$$
I=2R\iint_D dx\,dy
=2R\cdot\pi r^2
=2\pi Rr^2.
$$

**eg.**

**Problem.**

Evaluate

$$
I=\oint_\Gamma |\sqrt3y-x|\,dx-5z\,dz
$$

where

$$
\Gamma:
\begin{cases}
x^2+y^2+z^2=8\\
x^2+y^2=2z
\end{cases}
$$

The curve is oriented counterclockwise when viewed from the positive $z$-axis toward the origin

**Solution.**

$$
z^2+2z-8=0
\qquad
(z+4)(z-2)=0
\qquad
z=2
$$

$$
\Gamma:\begin{cases}
x^2+y^2=4\\
z=2
\end{cases}
\qquad
x=2\cos\theta
\quad
y=2\sin\theta
$$

$$
I=\int_0^{2\pi}\left|2\sqrt3\sin\theta-2\cos\theta\right|(-2\sin\theta)d\theta
=-8\int_0^{2\pi}\left|\sin\left(\theta-\frac{\pi}{6}\right)\right|\sin\theta\,d\theta
$$

Let $u=\theta-\dfrac{\pi}{6}$. Then
$$
I=-8\int_0^{2\pi}|\sin u|\sin\left(u+\frac{\pi}{6}\right)du
$$

$$
=-8\int_0^{2\pi}|\sin u|
\left(\frac{\sqrt3}{2}\sin u+\frac{1}{2}\cos u\right)du
=0
$$

**eg.**

**Problem.**

Let $z=f(x,y)$ be differentiable on

$$
D=\{(x,y)\mid 0\le x\le1,\quad0\le y\le1\}
$$

Suppose

$$
f(0,0)=0
$$

and

$$
dz|_{(0,0)}=3dx+2dy
$$

Evaluate

$$
\lim_{x\to0^+}
\frac{\displaystyle\int_0^{x^2}dt\int_x^{\sqrt t}f(t,u)\,du}
{1-\sqrt[4]{1-x^4}}
$$

**Solution.**

$$
f_x(0,0)=3
\qquad
f_y(0,0)=2
\qquad
1-\sqrt[4]{1-x^4}\sim\frac{x^4}{4}
$$

For $0<x<1$ and $0<t<x^2$,
$$
0\le\sqrt t\le x.
$$

Hence
$$
\int_0^{x^2}dt\int_x^{\sqrt t}f(t,u)\,du
=-\int_0^xdu\int_0^{u^2}f(t,u)\,dt.
$$

Since $f$ is differentiable at $(0,0)$,
$$
f(t,u)=3t+2u+o(u),
\qquad 0\le t\le u^2.
$$

Therefore
$$
\int_0^{x^2}dt\int_x^{\sqrt t}f(t,u)\,du
=-\int_0^xdu\int_0^{u^2}\left[3t+2u+o(u)\right]dt
=-\frac{x^4}{2}+o(x^4).
$$

Since
$$
1-\sqrt[4]{1-x^4}\sim\frac{x^4}{4},
$$

$$
\text{original expression}=-2.
$$

**eg.**

**Problem.**

Let $z=f(x,y)$ have continuous second-order partial derivatives on

$$
D=\{(x,y)\mid x^2+y^2\le1\}
$$

Suppose

$$
f_{xx}+f_{yy}=x^2+y^2
$$

Evaluate

$$
\lim_{r\to0}
\frac{\displaystyle\iint_{x^2+y^2\le r^2}\left(xf_x+yf_y\right)dx\,dy}
{(\tan r-\sin r)^2}
$$

**Solution.**

$$
(\tan r-\sin r)^2\sim\frac{r^6}{4}
$$

$$
\iint_{x^2+y^2\le r^2}(xf_x+yf_y)dx\,dy
=\int_0^r\rho^2d\rho\int_0^{2\pi}\left(f_x\cos\theta+f_y\sin\theta\right)d\theta
$$

On $C_\rho:x^2+y^2=\rho^2$,
$$
\oint_{C_\rho} f_xdy-f_ydx
=\rho\int_0^{2\pi}\left(f_x\cos\theta+f_y\sin\theta\right)d\theta.
$$

Thus
$$
\iint_{x^2+y^2\le r^2}(xf_x+yf_y)dx\,dy
=\int_0^r\rho\,d\rho\oint_{C_\rho} f_xdy-f_ydx
$$

$$
=\int_0^r\rho\,d\rho\iint_{x^2+y^2\le\rho^2}(f_{xx}+f_{yy})dx\,dy
$$

$$
=\int_0^r\rho\,d\rho\iint_{x^2+y^2\le\rho^2}(x^2+y^2)dx\,dy
=\int_0^r\rho\cdot\frac{\pi\rho^4}{2}d\rho
=\frac{\pi r^6}{12}
$$

$$
\text{original expression}=\frac{\pi}{3}
$$

**eg.**

**Problem.**

Let

$$
D=\{(x,y)\mid x^2+y^2\le\pi\}
$$

Evaluate

$$
\iint_D\left(\sin x^2\cos y^2+x\sqrt{x^2+y^2}\right)dx\,dy
$$

**Solution.**

$$
\iint_D x\sqrt{x^2+y^2}\,dx\,dy=0
$$

$$
\sin x^2\cos y^2
=\frac{1}{2}\left[\sin(x^2+y^2)+\sin(x^2-y^2)\right]
\qquad
\iint_D\sin(x^2-y^2)dx\,dy=0
$$

$$
\frac{1}{2}\iint_D\sin(x^2+y^2)dx\,dy
=\frac{1}{2}\int_0^{2\pi}\int_0^{\sqrt\pi}\sin(\rho^2)\rho\,d\rho\,d\theta
=\frac{\pi}{2}\int_0^\pi\sin u\,du
=\pi
$$

**eg.**

**Problem.**

Compute

$$
I=\iiint_\Omega\frac{xyz}{x^2+y^2}\,dx\,dy\,dz
$$

where $\Omega$ is the first-octant part enclosed by

$$
(x^2+y^2+z^2)^2=2xy
$$

**Solution.**

$$
x=r\sin\varphi\cos\theta
\qquad
y=r\sin\varphi\sin\theta
\qquad
z=r\cos\varphi
$$

$$
\Omega:r^2\le\sin^2\varphi\sin2\theta
$$

$$
I=\int_0^{\pi/2}\int_0^{\pi/2}\int_0^{\sin\varphi\sqrt{\sin2\theta}}
r^3\sin\varphi\cos\varphi\cos\theta\sin\theta
\,dr\,d\varphi\,d\theta
$$

$$
=\frac{1}{4}\int_0^{\pi/2}\cos\theta\sin\theta\sin^2 2\theta\,d\theta
\int_0^{\pi/2}\sin^5\varphi\cos\varphi\,d\varphi
=\frac{1}{72}
$$

**eg.**

**Problem.**

Evaluate

$$
I=\int_0^{2\pi}\int_0^\pi e^{\sin\varphi(\cos\theta-\sin\theta)}\sin\varphi\,d\varphi\,d\theta
$$

**Solution.**

$$
x=\sin\varphi\cos\theta
\qquad
y=\sin\varphi\sin\theta
\qquad
z=\cos\varphi
$$

$$
\Sigma:x^2+y^2+z^2=1
\qquad
I=\iint_\Sigma e^{x-y}\,dS
$$

$$
t=\frac{x-y}{\sqrt2}
\qquad
-1\le t\le1
\qquad
dS=2\pi\sqrt{1-t^2}\frac{1}{\sqrt{1-t^2}}dt
$$

$$
I=\int_{-1}^{1}e^{\sqrt2t}2\pi\,dt
=\sqrt2\pi\left(e^{\sqrt2}-e^{-\sqrt2}\right)
$$

**eg.**

**Problem.**

Given

$$
\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac{\pi}{2}
$$

Evaluate

$$
\int_0^{+\infty}\int_0^{+\infty}
\frac{\sin x\sin(x+y)}{x(x+y)}\,dx\,dy
$$

**Solution.**

$$
y=u-x
$$

$$
\int_0^{+\infty}\int_0^{+\infty}\frac{\sin x\sin(x+y)}{x(x+y)}dx\,dy
=\int_0^{+\infty}\int_x^{+\infty}\frac{\sin x\sin u}{xu}du\,dx
$$

$$
F(x)=\int_x^{+\infty}\frac{\sin y}{y}\,dy
\qquad
F'(x)=-\frac{\sin x}{x}
$$

$$
\text{original expression}
=-\int_0^{+\infty}F'(x)F(x)\,dx
=-\frac{1}{2}F^2(x)\Big|_0^{+\infty}
=\frac{1}{2}\left(\frac{\pi}{2}\right)^2
=\frac{\pi^2}{8}
$$

**eg.**

**Problem.**

For any oriented smooth closed surface $S$ in the half-space $x>0$

$$
\iint_S
xf'(x)\,dy\,dz
+y\bigl(xf(x)-f'(x)\bigr)\,dz\,dx
-xz\bigl(\sin x+f'(x)\bigr)\,dx\,dy
=0
$$

where $f(x)$ has continuous second-order derivatives on $(0,+\infty)$ and

$$
\lim_{x\to0^+}f(x)=0
\qquad
\lim_{x\to0^+}f'(x)=0
$$

Find $f(x)$

**Solution.**

$$
f'(x)+xf''(x)+xf(x)-f'(x)-x\sin x-xf'(x)=0
$$

$$
f(x)-f'(x)+f''(x)=\sin x
$$

$$
r^2-r+1=0
\qquad
r=\frac{1}{2}\pm\frac{\sqrt3}{2}i
$$

$$
f_h(x)=e^{x/2}\left(C_1\cos\frac{\sqrt3}{2}x+C_2\sin\frac{\sqrt3}{2}x\right)
\qquad
f_p(x)=\cos x
$$

$$
f(x)=e^{x/2}\left(C_1\cos\frac{\sqrt3}{2}x+C_2\sin\frac{\sqrt3}{2}x\right)+\cos x
$$

$$
\lim_{x\to0^+}f(x)=0
\quad
C_1=-1
\qquad
\lim_{x\to0^+}f'(x)=0
\quad
C_2=\frac{\sqrt3}{3}
$$

$$
f(x)=e^{x/2}
\left(
\frac{\sqrt3}{3}\sin\frac{\sqrt3}{2}x
-
\cos\frac{\sqrt3}{2}x
\right)
+\cos x
$$
