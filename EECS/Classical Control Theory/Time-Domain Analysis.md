# Time-Domain Analysis

[toc]

### Standard Test Inputs

Standard test inputs are used because the actual input is often unknown. They provide a common basis for comparing transient response, steady-state response, and stability.

| input | time function | Laplace transform |
|---|---|---|
| unit impulse | $\delta(t)$ | $1$ |
| step | $A u(t)$ | $\dfrac{A}{s}$ |
| ramp | $A t u(t)$ | $\dfrac{A}{s^2}$ |
| parabolic | $\dfrac{A}{2}t^2u(t)$ | $\dfrac{A}{s^3}$ |
| common | $A t^n u(t)$ | $A\dfrac{n!}{s^{n+1}}$ |

The unit impulse has unit area $\int_{-\infty}^{\infty}\delta(t)\,dt=1$.

### Time Response

The time response of a control system consists of the transient response and the steady-state response. For a stable system, the transient response is the part that goes to zero as time becomes large, and the steady-state response is the part that remains after the transient has died out.

##### Transient Response

For a unit-step response $y(t)$, the main transient-response specifications are rise time, peak time, settling time, and maximum overshoot.

| specification | meaning |
|---|---|
| rise time $t_r$ | time required for the response to rise from a low percentage to a high percentage of the final value, or to reach the final value for the first time in an underdamped response |
| peak time $t_p$ | time required for the response to reach the first peak |
| settling time $t_s$ | time required for the response to enter and remain within a specified error band |
| maximum overshoot $M_p$ | largest peak value measured from the final value |

$$
M_p=\frac{y(t_p)-y(\infty)}{y(\infty)}\times100\%
$$

##### Steady-State Response

Steady-state error measures the accuracy of the system after the transient response has disappeared.

$$
e_{ss}=\lim_{t\to\infty}e(t)
$$

For stable systems, the final value theorem gives

$$
e_{ss}=\lim_{s\to0}sE(s)
$$

### Stability

Stability is the most important requirement of a control system. A linear time-invariant system is Bounded-Input Bounded-Output(BIBO)  stable if every bounded input produces a bounded output.

A proper rational continuous-time LTI transfer function is BIBO stable if and only if all poles of the reduced transfer function lie in the open left-half $s$-plane, $\operatorname{Re}(s_i)<0$. A finite-dimensional closed-loop realization is internally asymptotically stable if and only if all roots of its characteristic equation lie in the open left-half $s$-plane. Pole–zero cancellation can hide unstable internal modes, so BIBO stability of the reduced transfer function does not by itself guarantee internal stability.

For a pole $s_i=\sigma_i+j\omega_i$, the corresponding time-domain mode is $t^k e^{s_i t}=t^k e^{\sigma_i t}e^{j\omega_i t}$, where $k\geq 0$ accounts for repeated poles, and its magnitude is $\left|t^k e^{s_i t}\right|=t^k e^{\sigma_i t}$. If $\sigma_i<0$, the exponential decay dominates any finite power of $t$, so
$$
\lim_{t\to\infty}t^k e^{\sigma_i t}=0
$$
Thus, every natural mode decays to zero. For a proper rational transfer function, the impulse response is a finite sum of these modes, so $\int_0^\infty |h(t)|\,dt<\infty$.

For any bounded input satisfying $|u(t)|\leq M$,

$$
|y(t)|
=
\left|\int_0^t h(\tau)u(t-\tau)\,d\tau\right|
\leq
M\int_0^\infty |h(\tau)|\,d\tau
<\infty
$$

Hence, the system is BIBO stable. Conversely, a pole with $\operatorname{Re}(s_i)\geq 0$ produces a non-decaying or growing mode, so the impulse response is not absolutely integrable and the system is not BIBO stable.

A necessary condition for stability is that all coefficients of the characteristic polynomial have the same sign and that no coefficient is missing.

### Routh-Hurwitz Criterion

Let the characteristic equation be

$$
D(s)=a_0s^n+a_1s^{n-1}+\cdots+a_{n-1}s+a_n=0
$$

The Routh array is formed from the coefficients of $D(s)$.

$$
\begin{array}{c|ccccc}
s^n & a_0 & a_2 & a_4 & a_6 & \cdots \\[2pt]
s^{n-1} & a_1 & a_3 & a_5 & a_7 & \cdots \\[2pt]
s^{n-2} & b_1 & b_2 & b_3 & b_4 & \cdots \\[2pt]
s^{n-3} & c_1 & c_2 & c_3 & c_4 & \cdots \\[2pt]
\vdots & \vdots & \vdots & \vdots & \vdots & \cdots \\[2pt]
s^2 & d_1 & d_2 & d_3 & 0 & \\[2pt]
s^1 & e_1 & e_2 & 0 & & \\[2pt]
s^0 & f_1 & 0 & & &
\end{array}
$$

The lower rows are computed in the determinant form used in the Routh array.

$$
b_1=-\frac{\begin{vmatrix}a_0&a_2\\a_1&a_3\end{vmatrix}}{a_1}=\frac{a_1a_2-a_0a_3}{a_1}
$$

$$
b_2=-\frac{\begin{vmatrix}a_0&a_4\\a_1&a_5\end{vmatrix}}{a_1}=\frac{a_1a_4-a_0a_5}{a_1}
$$

$$
b_3=-\frac{\begin{vmatrix}a_0&a_6\\a_1&a_7\end{vmatrix}}{a_1}=\frac{a_1a_6-a_0a_7}{a_1}
$$

$$
c_1=-\frac{\begin{vmatrix}a_1&a_3\\b_1&b_2\end{vmatrix}}{b_1}=\frac{b_1a_3-a_1b_2}{b_1}
$$

$$
c_2=-\frac{\begin{vmatrix}a_1&a_5\\b_1&b_3\end{vmatrix}}{b_1}=\frac{b_1a_5-a_1b_3}{b_1}
$$

$$
c_3=-\frac{\begin{vmatrix}a_1&a_7\\b_1&b_4\end{vmatrix}}{b_1}=\frac{b_1a_7-a_1b_4}{b_1}
$$

The number of roots in the right-half $s$-plane is equal to the number of sign changes in the first column of the Routh array. The system is stable if all elements in the first column have the same sign.

##### Special Cases

If the first element of a row is zero, replace it by a small positive number $\varepsilon$ and then let $\varepsilon\to0^+$.

If an entire row is zero, form an auxiliary polynomial from the row immediately above the zero row. Replace the zero row by the coefficients of the derivative of the auxiliary polynomial.

### First-Order Systems

A standard first-order closed-loop transfer function is

$$
G(s)=\frac{K}{Ts+1}
$$

For a unit-step input, the response is

$$
y(t)=K\left(1-e^{-t/T}\right)u(t)
$$

The time constant $T$ determines the speed of response. At $t=T$, the response reaches $63.2\%$ of its final value, $y(T)=0.632K$. For a stable first-order system with $K>0$ and $T>0$, the unit-step response is monotonic, so $M_p=0$. Common settling-time approximations are $t_s\approx3T\quad \text{for the }5\%\text{ criterion}$ and $t_s\approx4T\quad \text{for the }2\%\text{ criterion}$.

The unit-impulse response is

$$
g(t)=\frac{K}{T}e^{-t/T}u(t)
$$

### Second-Order Systems

A standard second-order closed-loop transfer function is

$$
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}
$$

The characteristic equation is

$$
s^2+2\zeta\omega_ns+\omega_n^2=0
$$

The closed-loop poles are

$$
s_{1,2}=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}
$$

For the underdamped case $0<\zeta<1$, the poles are

$$
s_{1,2}=-\zeta\omega_n\pm j\omega_d
$$

$$
\omega_d=\omega_n\sqrt{1-\zeta^2}
$$

Here $\zeta$ is the damping ratio, $\omega_n$ is the undamped natural frequency, and $\omega_d$ is the damped natural frequency.

| damping ratio | response type |
|---|---|
| $\zeta>1$ | overdamped |
| $\zeta=1$ | critically damped |
| $0<\zeta<1$ | underdamped |
| $\zeta=0$ | undamped |

##### Underdamped Step Response

For $0<\zeta<1$, the unit-step response is

$$
y(t)=1-\frac{e^{-\zeta\omega_nt}}{\sqrt{1-\zeta^2}}\sin(\omega_dt+\phi)
$$

$$
\phi=\arccos\zeta
$$

The response is oscillatory, and the oscillation amplitude decays according to $e^{-\zeta\omega_nt}$.

##### Second-Order Specifications

For the underdamped unit-step response,

$$
t_r=\frac{\pi-\phi}{\omega_d}
$$

$$
t_p=\frac{\pi}{\omega_d}
$$

$$
M_p=e^{-\zeta\pi/\sqrt{1-\zeta^2}}\times100\%
$$

$$
t_s\approx\frac{3}{\zeta\omega_n}\quad \text{for the }5\%\text{ criterion}
$$

$$
t_s\approx\frac{4}{\zeta\omega_n}\quad \text{for the }2\%\text{ criterion}
$$

Increasing $\zeta$ reduces overshoot. Increasing $\omega_n$ generally increases the speed of response.

### Steady-State Error

For a standard negative-feedback system with forward-path transfer function $G(s)$ and feedback transfer function $H(s)$,

$$
E(s)=R(s)-H(s)Y(s)
$$

$$
E(s)=\frac{R(s)}{1+G(s)H(s)}
$$

For non-unity feedback, this steady-state error is the actuating error

$$
e(t)=r(t)-y_m(t)=r(t)-h(t)\ast y(t)
$$

It is not necessarily the same as the output tracking error $r(t)-y(t)$.

If the closed-loop system is stable, the steady-state error due to the reference input is

$$
e_{ss}=\lim_{s\to0}\frac{sR(s)}{1+G(s)H(s)}
$$

##### Error Constants

Let the open-loop transfer function be

$$
L(s)=G(s)H(s)
$$

The system type is the number of pure integrations in $L(s)$.

$$
L(s)=\frac{K\prod_i(\tau_i s+1)}{s^\nu\prod_j(T_js+1)}
$$

The static error constants are

$$
K_p=\lim_{s\to0}L(s)=\lim_{s\to0}G(s)H(s)
$$

$$
K_v=\lim_{s\to0}sL(s)=\lim_{s\to0}sG(s)H(s)
$$

$$
K_a=\lim_{s\to0}s^2L(s)=\lim_{s\to0}s^2G(s)H(s)
$$

For a unit-step input

$$
R(s)=\frac{1}{s}
$$

$$
e_{ss}
=
\lim_{s\to0}\frac{1}{1+G(s)H(s)}
=
\frac{1}{1+K_p}
$$

For a unit-ramp input

$$
R(s)=\frac{1}{s^2}
$$

$$
e_{ss}
=
\lim_{s\to0}\frac{1}{s\left[1+G(s)H(s)\right]}
=
\frac{1}{K_v}
$$

For a unit-parabolic input
$$
R(s)=\frac{1}{s^3}
$$

$$
e_{ss}
=
\lim_{s\to0}\frac{1}{s^2\left[1+G(s)H(s)\right]}
=
\frac{1}{K_a}
$$

| input | error constant | steady-state error |
|---|---|---|
| unit step | $K_p$ | $e_{ss}=\dfrac{1}{1+K_p}$ |
| unit ramp | $K_v$ | $e_{ss}=\dfrac{1}{K_v}$ |
| unit parabolic | $K_a$ | $e_{ss}=\dfrac{1}{K_a}$ |

Near $s=0$ a Type $N$ system has the form

$$
L(s)\sim\frac{K}{s^N}
$$

where $K$ is finite and nonzero

Therefore

$$
K_p
=
\lim_{s\to0}\frac{K}{s^N}
$$

$$
K_v
=
\lim_{s\to0}\frac{K}{s^{N-1}}
$$

$$
K_a
=
\lim_{s\to0}\frac{K}{s^{N-2}}
$$

For a finite nonzero gain $K$, the common results are

| system type | step input | ramp input | parabolic input |
|---|---|---|---|
| Type 0 | $\dfrac{1}{1+K}$ | $\infty$ | $\infty$ |
| Type I | $0$ | $\dfrac{1}{K}$ | $\infty$ |
| Type II | $0$ | $0$ | $\dfrac{1}{K}$ |

These formulas apply only when the closed-loop system is stable.
