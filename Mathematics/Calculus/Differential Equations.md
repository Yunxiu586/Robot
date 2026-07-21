# Differential Equations

[toc]

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

