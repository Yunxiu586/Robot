# Vector Algebra and Analytic Geometry

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

Let $\boldsymbol{A}=A_x\boldsymbol{e}_x+A_y\boldsymbol{e}_y+A_z\boldsymbol{e}_z$ and $\boldsymbol{B}=B_x\boldsymbol{e}_x+B_y\boldsymbol{e}_y+B_z\boldsymbol{e}_z$. Then

$$
\boldsymbol{A}+\boldsymbol{B}
=(A_x+B_x)\boldsymbol{e}_x+(A_y+B_y)\boldsymbol{e}_y+(A_z+B_z)\boldsymbol{e}_z\qquad\boldsymbol{A}\cdot\boldsymbol{B}=A_xB_x+A_yB_y+A_zB_z
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
\boldsymbol{s}_2=P-A=(3t-3,2t,-t-3) \qquad \boldsymbol{s}_1\cdot\boldsymbol{s}_2=0\qquad 3(3t-3)+2\cdot 2t+(-1)(-t-3)=0 \qquad t=\frac{3}{7}
$$

$$
\boldsymbol{s}_2=\left(-\frac{12}{7},-\frac{6}{7},-\frac{24}{7}\right) =\frac{6}{7}(-2,-1,-4)\qquad L_2:\frac{x-2}{-2}=\frac{y-1}{-1}=\frac{z-3}{-4}
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
\boldsymbol{n}=(f_x,f_y,-1) \qquad f(tu,tv)=t^2f(u,v)\qquad u f_1(tu,tv)+v f_2(tu,tv)=2t f(u,v) \qquad tu=1 \quad tv=-1
$$

$$
f_1(1,-1)-f_2(1,-1)=2f(1,-1) \qquad 3-f_2(1,-1)=4 \\ f_2(1,-1)=-1\qquad 3(x-1)-(y+1)-(z-2)=0 \qquad 3x-y-z-2=0
$$

