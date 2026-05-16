# Automatic Control Principles

### Feedback Control System

A control system is an interconnection of components that forms a desired system response.

| Symbol | Textbook meaning |
|---|---|
| $r(t)$ | reference input, or desired value |
| $y(t)$ | controlled variable, or output |
| $n(t)$ | disturbance input |
| $y_m(t)$ | measured output, or feedback signal |
| $e(t)$ | error signal |

$$
e(t)=r(t)-y_m(t)
$$

The forward path carries the signal from the input side to the output side. The feedback path returns information about the output to the input side.

| Component | Function |
|---|---|
| Controller | generates the control action |
| Actuator | drives the plant |
| Plant | process to be controlled |
| Sensor | measures the output |

### Open-Loop and Closed-Loop Control

In an open-loop system, the control action is independent of the output.

In a closed-loop system, the output is measured and compared with the reference input. Feedback uses the error signal to reduce the difference between the desired response and the actual response.

For unity feedback,

$$
e(t)=r(t)-y(t)
$$

### Control-System Types

| Type | Essential idea |
|---|---|
| Regulator | the reference input is constant |
| Servomechanism | the output follows a changing input |
| Program control | the input follows a prescribed program |
| Linear system | superposition applies |
| Nonlinear system | at least one element is nonlinear |
| Time-invariant system | parameters do not vary with time |
| Time-varying system | at least one parameter varies with time |
| Continuous-time system | signals are functions of continuous time |
| Discrete-time system | signals are sampled or digital |

For a SISO system,

$$
Y(s)=G(s)R(s)
$$

For a MIMO system,

$$
\boldsymbol{\mathit{Y}}(s)=\mathbf{G}(s)\boldsymbol{\mathit{R}}(s)
$$

### Performance Specifications

A control system must be stable and must have acceptable transient response and steady-state accuracy.

| Requirement | Meaning |
|---|---|
| Stability | the response returns to equilibrium after a disturbance |
| Transient response | the response before steady state is reached |
| Steady-state accuracy | the final error after the transient has died out |

Common time-domain specifications are rise time, maximum overshoot, and settling time.

$$
e_{ss}=\lim_{t\to\infty}e(t)
$$

### Classical Analysis Methods

Classical control commonly uses time-domain analysis, root-locus analysis, and frequency-response analysis.

### Mathematical Models

A mathematical model describes the input-output relation of a dynamic system. Different physical systems may have the same mathematical model.

##### Differential Equation Model

For an RLC circuit,

$$
u_i(t)=Ri(t)+L\frac{di(t)}{dt}+u_o(t)
$$

$$
i(t)=C\frac{du_o(t)}{dt}
$$

Eliminating $i(t)$ gives

$$
LC\frac{d^2u_o(t)}{dt^2}+RC\frac{du_o(t)}{dt}+u_o(t)=u_i(t)
$$

If $L=0$,

$$
RC\frac{du_o(t)}{dt}+u_o(t)=u_i(t)
$$

##### Transfer Function

The transfer function of an LTI system is the ratio of the Laplace transform of the output to the Laplace transform of the input under zero initial conditions.

$$
G(s)=\frac{Y(s)}{R(s)}
$$

The transfer function is a property of the system, independent of the input signal. It is also the Laplace transform of the impulse response.

$$
G(s)=\mathcal{L}\{g(t)\}
$$

##### Polynomial Form

A proper rational transfer function has the form

$$
G(s)=\frac{b_0s^m+b_1s^{m-1}+\cdots+b_m}{a_0s^n+a_1s^{n-1}+\cdots+a_n}
$$

$$
n\ge m
$$

The order of the system is the degree of the denominator. If

$$
G(s)=\frac{N(s)}{D(s)}
$$

then $D(s)$ is the characteristic polynomial, and

$$
D(s)=0
$$

##### Pole-Zero Form

Zeros are roots of $N(s)$. Poles are roots of $D(s)$.

$$
G(s)=K\frac{\prod_{j=1}^{m}(s-z_j)}{\prod_{i=1}^{n}(s-p_i)}
$$

Closed-loop poles determine stability and the natural modes of the response.

##### Time-Constant Form

Each factor is often normalized so that its constant term is one.

$$
G(s)=\frac{K\prod_j(\tau_js+1)\prod_k(\tau_k^2s^2+2\zeta_k\tau_ks+1)}{s^\nu\prod_i(\tau_is+1)\prod_l(\tau_l^2s^2+2\zeta_l\tau_ls+1)}
$$

Here $K$ is gain, $\tau$ is a time constant, $\zeta$ is damping ratio, and $\nu$ is the number of poles at the origin.

### Standard Dynamic Elements

| Element | Differential relation | Transfer function |
|---|---|---|
| Proportional | $y(t)=Kr(t)$ | $G(s)=K$ |
| Integrator | $y(t)=\int r(t)\,dt$ | $G(s)=\dfrac{1}{s}$ |
| First-order lag | $T\dfrac{dy(t)}{dt}+y(t)=r(t)$ | $G(s)=\dfrac{1}{Ts+1}$ |
| Second-order factor | $T^2\dfrac{d^2y(t)}{dt^2}+2\zeta T\dfrac{dy(t)}{dt}+y(t)=r(t)$ | $G(s)=\dfrac{1}{T^2s^2+2\zeta Ts+1}$ |
| Differentiator | $y(t)=\dfrac{dr(t)}{dt}$ | $G(s)=s$ |
| Time delay | $y(t)=r(t-\tau)$ | $G(s)=e^{-\tau s}$ |

The standard second-order form is

$$
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}
$$

For $0<\zeta<1$, the response is underdamped. For $\zeta\ge1$, the response is nonoscillatory.

### Block Diagrams

A block diagram shows the functional relation between system variables.

| Connection | Equivalent transfer function |
|---|---|
| Series | $G(s)=G_1(s)G_2(s)$ |
| Parallel | $G(s)=G_1(s)+G_2(s)$ |
| Open loop | $G_{OL}(s)=G(s)H(s)$ |

For negative feedback,

$$
\frac{Y(s)}{R(s)}=\frac{G(s)}{1+G(s)H(s)}
$$

For positive feedback,

$$
\frac{Y(s)}{R(s)}=\frac{G(s)}{1-G(s)H(s)}
$$

The negative-feedback characteristic equation is

$$
1+G(s)H(s)=0
$$

Block-diagram reduction combines series, parallel, and feedback blocks. Inner loops are usually reduced before outer loops.

### Signal Flow Graphs

A signal flow graph represents a set of linear algebraic equations by nodes and directed branches.

| Term | Meaning |
|---|---|
| Source node | node with only outgoing branches |
| Sink node | node with only incoming branches |
| Mixed node | node with both incoming and outgoing branches |
| Forward path | path from input to output without repeated nodes |
| Loop | closed path without repeated nodes |
| Non-touching loops | loops with no common nodes |

##### Mason's Gain Formula

For $N$ forward paths,

$$
\frac{Y(s)}{R(s)}=\frac{1}{\Delta}\sum_{k=1}^{N}P_k\Delta_k
$$

$P_k$ is the gain of the $k$th forward path. $\Delta_k$ is found by removing all loops that touch the $k$th forward path.

$$
\Delta=1-\sum_iL_i+\sum_{i,j}L_iL_j-\sum_{i,j,l}L_iL_jL_l+\cdots
$$

The second sum contains all pairs of non-touching loops. The third sum contains all triples of mutually non-touching loops.
