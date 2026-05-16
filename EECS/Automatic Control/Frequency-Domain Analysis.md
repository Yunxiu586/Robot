# Frequency-Domain Analysis

[toc]

### Frequency Response

##### Sinusoidal Steady-State Response

Frequency response is the steady-state response of a stable linear time-invariant system to a sinusoidal input. If

$$
r(t)=R\sin \omega t
$$

then

$$
R(s)=\frac{R\omega}{s^2+\omega^2}
$$

For a stable system with transfer function $G(s)$, the steady-state output is a sinusoid at the same frequency

$$
y_{ss}(t)=R\left|G(j\omega)\right|\sin\left[\omega t+\angle G(j\omega)\right]
$$

The magnitude changes the amplitude, and the phase changes the time position of the sinusoid.

##### Frequency Characteristics

The frequency transfer function is obtained by setting $s=j\omega$ in the transfer function

$$
G(j\omega)=G(s)\big|_{s=j\omega}
$$

It can be written as

$$
G(j\omega)=\frac{Y(j\omega)}{R(j\omega)}=A(\omega)e^{j\varphi(\omega)}
$$

where

$$
A(\omega)=\left|G(j\omega)\right|
$$

$$
\varphi(\omega)=\angle G(j\omega)
$$

Equivalent forms are

$$
G(j\omega)=\operatorname{Re}\left[G(j\omega)\right]+j\operatorname{Im}\left[G(j\omega)\right]
$$

$$
G(j\omega)=\left|G(j\omega)\right|e^{j\angle G(j\omega)}
$$

$$
G(j\omega)=\left|G(j\omega)\right|\cos\angle G(j\omega)+j\left|G(j\omega)\right|\sin\angle G(j\omega)
$$

##### Frequency-Response Plots

| plot | main idea |
|---|---|
| polar plot | plot $G(j\omega)$ in the complex plane as $\omega$ varies from $0$ to $\infty$ |
| Bode plot | plot logarithmic magnitude and phase against logarithmic frequency |
| Nichols plot | plot logarithmic magnitude against phase with $\omega$ as a parameter |

The Bode magnitude is

$$
L(\omega)=20\log_{10}A(\omega)\ \mathrm{dB}
$$

The horizontal axis is logarithmic in $\omega$, usually in rad/s. A decade means a tenfold change in frequency. A slope in Bode magnitude is measured in dB/dec.

### Elementary Factors

##### Proportional Factor

For

$$
G(s)=K
$$

$$
G(j\omega)=K=Ke^{j0}
$$

$$
A(\omega)=K
$$

$$
\varphi(\omega)=0
$$

$$
L(\omega)=20\log_{10}K
$$

##### Integral and Derivative Factors

For an integral factor,

$$
G(s)=\frac{1}{s}
$$

$$
G(j\omega)=\frac{1}{j\omega}=\frac{1}{\omega}e^{-j90^\circ}
$$

$$
A(\omega)=\frac{1}{\omega}
$$

$$
\varphi(\omega)=-90^\circ
$$

$$
L(\omega)=-20\log_{10}\omega
$$

For a derivative factor,

$$
G(s)=s
$$

$$
G(j\omega)=j\omega=\omega e^{j90^\circ}
$$

$$
A(\omega)=\omega
$$

$$
\varphi(\omega)=90^\circ
$$

$$
L(\omega)=20\log_{10}\omega
$$

The integral factor has slope $-20\ \mathrm{dB/dec}$ and constant phase $-90^\circ$. The derivative factor has slope $20\ \mathrm{dB/dec}$ and constant phase $90^\circ$.

##### First-Order Lag Factor

For

$$
G(s)=\frac{1}{Ts+1}
$$

$$
G(j\omega)=\frac{1}{1+j\omega T}
$$

$$
A(\omega)=\frac{1}{\sqrt{1+(\omega T)^2}}
$$

$$
\varphi(\omega)=-\tan^{-1}(\omega T)
$$

$$
L(\omega)=-20\log_{10}\sqrt{1+(\omega T)^2}
$$

The real and imaginary parts are

$$
\operatorname{Re}[G(j\omega)]=\frac{1}{1+(\omega T)^2}
$$

$$
\operatorname{Im}[G(j\omega)]=-\frac{\omega T}{1+(\omega T)^2}
$$

The polar plot lies on the circle

$$
\left(\operatorname{Re}[G(j\omega)]-\frac{1}{2}\right)^2+\left(\operatorname{Im}[G(j\omega)]\right)^2=\left(\frac{1}{2}\right)^2
$$

The corner frequency is

$$
\omega_c=\frac{1}{T}
$$

The low-frequency asymptote is $0\ \mathrm{dB}$, and the high-frequency asymptote has slope $-20\ \mathrm{dB/dec}$. At the corner frequency, the exact curve is about $3\ \mathrm{dB}$ below the asymptotes.

##### First-Order Lead Factor

For

$$
G(s)=Ts+1
$$

$$
G(j\omega)=1+j\omega T
$$

$$
A(\omega)=\sqrt{1+(\omega T)^2}
$$

$$
\varphi(\omega)=\tan^{-1}(\omega T)
$$

$$
L(\omega)=20\log_{10}\sqrt{1+(\omega T)^2}
$$

The first-order lead factor is the inverse of the first-order lag factor. Its high-frequency asymptote has slope $20\ \mathrm{dB/dec}$.

##### Second-Order Factor

A standard second-order factor is

$$
G(s)=\frac{1}{T^2s^2+2\zeta Ts+1}
$$

With $\omega_n=1/T$,

$$
G(j\omega)=\frac{1}{1-(\omega T)^2+j2\zeta\omega T}
$$

$$
A(\omega)=\frac{1}{\sqrt{[1-(\omega T)^2]^2+(2\zeta\omega T)^2}}
$$

$$
L(\omega)=-20\log_{10}\sqrt{[1-(\omega T)^2]^2+(2\zeta\omega T)^2}
$$

The phase is

$$
\varphi(\omega)=
\begin{cases}
-\tan^{-1}\dfrac{2\zeta\omega T}{1-(\omega T)^2}, & \omega T\le 1 \\
-180^\circ+\tan^{-1}\dfrac{2\zeta\omega T}{(\omega T)^2-1}, & \omega T>1
\end{cases}
$$

The low-frequency asymptote is $0\ \mathrm{dB}$, and the high-frequency asymptote has slope $-40\ \mathrm{dB/dec}$. The corner frequency is

$$
\omega_c=\omega_n=\frac{1}{T}
$$

For $0<\zeta<1/\sqrt{2}$, the resonant frequency and resonant peak are

$$
\omega_r=\omega_n\sqrt{1-2\zeta^2}
$$

$$
M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}
$$

Smaller $\zeta$ gives a larger resonant peak and a sharper phase transition.

##### Time Delay

For a pure time delay,

$$
G(s)=e^{-\tau s}
$$

$$
G(j\omega)=e^{-j\tau\omega}
$$

$$
A(\omega)=1
$$

$$
\varphi(\omega)=-\tau\omega
$$

$$
L(\omega)=0\ \mathrm{dB}
$$

A time delay changes only the phase. For small $\tau\omega$,

$$
e^{-j\tau\omega}\approx 1-j\tau\omega\approx\frac{1}{1+j\tau\omega}
$$

### Bode Plot Construction

##### Magnitude Plot

For an open-loop transfer function

$$
G_o(s)=G(s)H(s)=\frac{K\prod_{j=1}^{m}(\tau_js+1)}{s^\nu\prod_{i=1}^{n-\nu}(T_is+1)}
$$

The low-frequency asymptote is

$$
L_{\mathrm{low}}(\omega)=20\log_{10}K-20\nu\log_{10}\omega
$$

The initial slope is

$$
-20\nu\ \mathrm{dB/dec}
$$

At $\omega=1$,

$$
L_{\mathrm{low}}(1)=20\log_{10}K
$$

For $\nu>0$, the low-frequency asymptote crosses $0\ \mathrm{dB}$ at

$$
\omega=K^{1/\nu}
$$

Each factor changes the slope after its corner frequency.

| factor | slope change |
|---|:---|
| $Ts+1$ | $+20\ \mathrm{dB/dec}$ |
| $\dfrac{1}{Ts+1}$ | $-20\ \mathrm{dB/dec}$ |
| second-order zero factor | $+40\ \mathrm{dB/dec}$ |
| second-order pole factor | $-40\ \mathrm{dB/dec}$ |

At high frequency, if the open-loop transfer function has $n$ poles and $m$ zeros, the final slope is

$$
-20(n-m)\ \mathrm{dB/dec}
$$

The gain crossover frequency is defined by

$$
L(\omega_c)=0\ \mathrm{dB}
$$

##### Phase Plot

The phase curve is obtained by adding the phase contribution of each factor.

| factor | phase change |
|---|---|
| first-order zero $Ts+1$ | $0^\circ$ to $90^\circ$ |
| first-order pole $1/(Ts+1)$ | $0^\circ$ to $-90^\circ$ |
| second-order zero factor | $0^\circ$ to $180^\circ$ |
| second-order pole factor | $0^\circ$ to $-180^\circ$ |

For a first-order factor, the phase is $\pm45^\circ$ at the corner frequency. For a second-order factor, the phase is $\pm90^\circ$ at the corner frequency.

### Open-Loop Frequency Characteristics

##### Nyquist Plot

For

$$
G_o(s)=G(s)H(s)
$$

The Nyquist plot is the polar plot of $G_o(j\omega)$ as $\omega$ varies. If

$$
G_o(s)=\frac{K\prod_{j=1}^{m}(\tau_js+1)}{s^\nu\prod_{i=1}^{n-\nu}(T_is+1)}
$$

then at low frequency

$$
G_o(j\omega)\approx\frac{K}{(j\omega)^\nu}=\frac{K}{\omega^\nu}\angle(-90^\circ\nu)
$$

Thus the starting behavior is

| type $\nu$ | low-frequency behavior |
|:---|---|
| $0$ | starts at $K$ on the positive real axis |
| $1$ | starts at infinity along the negative imaginary axis |
| $2$ | starts at infinity along the negative real axis |
| $3$ | starts at infinity along the positive imaginary axis |

If $n>m$, then at high frequency

$$
G_o(j\omega)\to 0\angle[-90^\circ(n-m)]
$$

| $n-m$ | approach to the origin |
|:---|---|
| $1$ | tangent to the negative imaginary axis |
| $2$ | tangent to the negative real axis |
| $3$ | tangent to the positive imaginary axis |
| $4$ | tangent to the positive real axis |

For the middle-frequency part, axis crossings can be found from

$$
\operatorname{Re}[G_o(j\omega)]=0
$$

$$
\operatorname{Im}[G_o(j\omega)]=0
$$

A local peak in magnitude satisfies

$$
\frac{dA(\omega)}{d\omega}=0
$$

##### Open-Loop Bode Plot

The open-loop Bode plot gives useful information about the closed-loop system. Low-frequency gain is related to steady-state accuracy. Crossover behavior and phase lag are related to relative stability and transient response.

For a type-$\nu$ system, the low-frequency Bode magnitude slope is $-20\nu\ \mathrm{dB/dec}$. Type $0$ begins with a horizontal line, type I begins with slope $-20\ \mathrm{dB/dec}$, and type II begins with slope $-40\ \mathrm{dB/dec}$.

### Minimum-Phase Systems

A minimum-phase transfer function has no zeros or poles in the right-half $s$-plane and has no pure time delay. A system with such a transfer function is called a minimum-phase system.

A nonminimum-phase transfer function has at least one right-half-plane zero, right-half-plane pole, or time-delay factor. Nonminimum-phase factors can have the same magnitude curve as corresponding minimum-phase factors, but they introduce additional phase lag.

### Nyquist Stability Criterion

##### Mapping Relation

For a negative-feedback system,

$$
T(s)=\frac{G(s)}{1+G(s)H(s)}
$$

Let

$$
G_o(s)=G(s)H(s)=\frac{M(s)}{N(s)}
$$

The closed-loop characteristic function is

$$
F(s)=1+G_o(s)=\frac{N(s)+M(s)}{N(s)}
$$

The zeros of $F(s)$ are the closed-loop poles. The poles of $F(s)$ are the open-loop poles.

##### Criterion

Let $P$ be the number of open-loop poles of $G_o(s)$ in the right-half $s$-plane. Let $N$ be the number of counterclockwise encirclements of $(-1,j0)$ by the Nyquist plot of $G_o(j\omega)$.

Then the number of closed-loop poles in the right-half plane is

$$
Z=P-N
$$

The closed-loop system is stable if and only if

$$
Z=0
$$

Equivalently, the Nyquist plot must encircle $(-1,j0)$ counterclockwise exactly $P$ times.

If the open-loop system is stable, then $P=0$. The closed-loop system is stable if the Nyquist plot does not encircle $(-1,j0)$. If the plot passes through $(-1,j0)$, the closed-loop system is marginally stable.

##### Imaginary-Axis Poles

If $G_o(s)$ has poles on the imaginary axis, the Nyquist contour is indented to the right of those poles. Integral poles at the origin are handled by the modified contour, and the same encirclement relation is then applied.
