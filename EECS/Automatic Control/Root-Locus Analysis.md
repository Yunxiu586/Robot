# Root-Locus Analysis

[toc]

### Root Locus

The root locus is the locus of the closed-loop poles as a system parameter is varied. In classical control design, the parameter is usually the open-loop gain or the root-locus gain $k$.

For a standard negative-feedback system,

$$
T(s)=\frac{G(s)}{1+G(s)H(s)}
$$

The closed-loop poles are the roots of the characteristic equation

$$
D(s)=1+G(s)H(s)=0
$$

Let the open-loop transfer function be written in pole-zero form

$$
L(s)=G(s)H(s)=k\frac{\prod_{j=1}^{m}(s-z_j)}{\prod_{i=1}^{n}(s-p_i)}
$$

Then the root-locus equation is

$$
1+L(s)=0
$$

or

$$
L(s)=-1
$$

### Conditions

A point $s$ is on the negative-feedback root locus if it satisfies both the magnitude condition and the angle condition.

$$
|L(s)|=1
$$

$$
\angle L(s)=(2\ell+1)\pi,\qquad \ell=0,\pm1,\pm2,\ldots
$$

Equivalently,

$$
k=\frac{\prod_{i=1}^{n}|s-p_i|}{\prod_{j=1}^{m}|s-z_j|}
$$

$$
\sum_{j=1}^{m}\angle(s-z_j)-\sum_{i=1}^{n}\angle(s-p_i)=(2\ell+1)\pi
$$

For positive feedback, the characteristic equation is

$$
1-L(s)=0
$$

and the angle condition becomes

$$
\angle L(s)=2\ell\pi
$$

### Construction Rules

##### Branches and Symmetry

For a proper open-loop transfer function, the number of root-locus branches is equal to the number of open-loop poles.

$$
\text{number of branches}=n
$$

The root locus is symmetric about the real axis because complex roots occur in conjugate pairs.

Each branch starts at an open-loop pole when $k=0$ and ends at an open-loop zero as $k\to\infty$. If $n>m$, then $n-m$ branches go to zeros at infinity.

##### Real-Axis Segments

A point on the real axis belongs to the negative-feedback root locus if the number of real open-loop poles and zeros to the right of the point is odd.

Complex-conjugate poles and zeros do not change this real-axis rule because their angle contributions cancel on the real axis.

##### Breakaway and Break-In Points

Breakaway and break-in points occur when multiple closed-loop poles meet at the same point. Let

$$
M(s)=\prod_{j=1}^{m}(s-z_j)
$$

$$
N(s)=\prod_{i=1}^{n}(s-p_i)
$$

Since

$$
L(s)=k\frac{M(s)}{N(s)}
$$

the characteristic equation gives

$$
k=-\frac{N(s)}{M(s)}
$$

Possible breakaway or break-in points satisfy

$$
\frac{dk}{ds}=0
$$

or

$$
N'(s)M(s)-N(s)M'(s)=0
$$

Equivalently,

$$
\sum_{i=1}^{n}\frac{1}{s-p_i}=\sum_{j=1}^{m}\frac{1}{s-z_j}
$$

Only the solutions that lie on the root locus and give $k>0$ are valid.

If $r$ branches meet at the same point, the angles of departure from the point are

$$
\theta_q=\frac{(2q+1)\pi}{r},\qquad q=0,1,\ldots,r-1
$$

For $r=2$, the branches leave or enter at right angles.

##### Asymptotes

If $n>m$, then $n-m$ branches go to infinity. The asymptote angles are

$$
\phi_q=\frac{(2q+1)\pi}{n-m},\qquad q=0,1,\ldots,n-m-1
$$

The asymptotes intersect the real axis at the centroid

$$
\sigma_a=\frac{\sum_{i=1}^{n}p_i-\sum_{j=1}^{m}z_j}{n-m}
$$

Only the real parts of complex-conjugate poles and zeros affect the centroid.

##### Departure and Arrival Angles

For a complex open-loop pole $p_k$, the departure angle is found from the angle condition by letting $s$ approach $p_k$.

$$
\theta_{d,k}=(2\ell+1)\pi+\sum_{\substack{i=1\\i\ne k}}^{n}\angle(p_k-p_i)-\sum_{j=1}^{m}\angle(p_k-z_j)
$$

For a complex open-loop zero $z_k$, the arrival angle is

$$
\theta_{a,k}=(2\ell+1)\pi-\sum_{\substack{j=1\\j\ne k}}^{m}\angle(z_k-z_j)+\sum_{i=1}^{n}\angle(z_k-p_i)
$$

##### Imaginary-Axis Crossings

Imaginary-axis crossings are used to find the limiting value of gain for stability. The usual methods are the Routh criterion or direct substitution.

$$
D(s)=0
$$

$$
s=j\omega
$$

Then

$$
\operatorname{Re}D(j\omega)=0,\qquad \operatorname{Im}D(j\omega)=0
$$

At the crossing, the closed-loop system is marginally stable.

### Design Use

The root locus shows how gain changes the location of closed-loop poles. Closed-loop poles in the left-half plane give a stable continuous-time system. Poles farther to the left usually give faster decay.

For a dominant complex pole pair,

$$
s=-\sigma\pm j\omega_d
$$

The damping ratio is related to the angle $\beta$ measured from the negative real axis.

$$
\zeta=\cos\beta
$$

The maximum percent overshoot is approximately

$$
M_p=e^{-\zeta\pi/\sqrt{1-\zeta^2}}\times100\%
$$

Increasing gain may improve steady-state accuracy, but it can also reduce relative stability or increase oscillation.

### Typical Example

Consider the open-loop transfer function

$$
L(s)=\frac{k}{s(s+4)(s+6)}
$$

The open-loop poles are

$$
p_1=0,\qquad p_2=-4,\qquad p_3=-6
$$

There are no finite open-loop zeros. Therefore, there are three branches and all three branches end at infinity.

The real-axis segments are

$$
(-\infty,-6),\qquad (-4,0)
$$

From the characteristic equation,

$$
1+\frac{k}{s(s+4)(s+6)}=0
$$

so

$$
k=-s(s+4)(s+6)
$$

The breakaway points satisfy

$$
\frac{dk}{ds}=-(3s^2+20s+24)=0
$$

Thus,

$$
s=\frac{-10\pm2\sqrt{7}}{3}
$$

The valid breakaway point is

$$
s\approx-1.57,\qquad k\approx16.9
$$

The asymptote centroid is

$$
\sigma_a=\frac{0-4-6}{3}=-\frac{10}{3}
$$

The asymptote angles are

$$
\phi_q=\frac{(2q+1)\pi}{3},\qquad q=0,1,2
$$

Hence,

$$
\phi_q=60^\circ,\ 180^\circ,\ 300^\circ
$$

The closed-loop characteristic equation is

$$
D(s)=s^3+10s^2+24s+k
$$

The Routh array is

$$
\begin{array}{c|cc}
s^3 & 1 & 24 \\
s^2 & 10 & k \\
s^1 & \dfrac{240-k}{10} & 0 \\
s^0 & k & 0
\end{array}
$$

The system is stable when the first column is positive.

$$
0<k<240
$$

At the stability boundary,

$$
k=240
$$

The auxiliary equation is

$$
10s^2+240=0
$$

so the imaginary-axis crossing is

$$
s=\pm j2\sqrt{6}
$$

For a unit-step overshoot requirement $M_p\le16.3\%$, the damping ratio requirement is approximately

$$
\zeta\ge0.5
$$

The corresponding root-locus gain range is

$$
0<k\le44
$$

The velocity error constant is

$$
K_v=\lim_{s\to0}sL(s)=\frac{k}{24}
$$

Within the stable range,

$$
0<K_v<10
$$

Thus the requirement $K_v\ge15$ cannot be satisfied by changing only $k$.
