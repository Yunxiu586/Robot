# Local Model Predictive Contouring Control

[toc]

### Abstract

This paper presents a method for local motion planning in unstructured environments with static and moving obstacles, such as humans. Given a reference path and speed, our optimization-based receding-horizon approach computes a local trajectory that minimizes the tracking error while avoiding obstacles.

We build on nonlinear model-predictive contouring control (MPCC) and extend it to incorporate a static map by computing, online, a set of convex regions in free space. We model moving obstacles as ellipsoids and provide a correct bound to approximate the collision region, given by the Minkowsky sum of an ellipse and a circle. Our framework is agnostic to the robot model.

We present experimental results with a mobile robot navigating in indoor environments populated with humans. Our method is executed fully onboard without the need of external support and can be applied to other robot morphologies such as autonomous cars.

### Preliminaries

##### Robot description

An autonomous ground vehicle (AGV) is a ground robot that navigates without continuous human control. Let $\mathcal{B}$ denote an AGV on the plane $\mathcal{W}=\mathbb{R}^2$. Its dynamics are described by the discrete-time nonlinear system

$$
\boldsymbol{z}(t+1)=f\left(\boldsymbol{z}(t),\boldsymbol{u}(t)\right)
$$

where $\boldsymbol{z}(t)$ and $\boldsymbol{u}(t)$ are the robot state and input. For the mobile robot, the state equals the configuration $\boldsymbol{z}(t)\in\mathcal{C}=\mathbb{R}^2\times\mathbb{S}$; for the car, the state also includes speed. The occupied area $\mathcal{B}(\boldsymbol{z})$ is approximated by a union of $n_c$ circles

$$
\mathcal{B}(\boldsymbol{z})\subseteq\bigcup_{c=1}^{n_c}\mathcal{B}_c(\boldsymbol{z})\subset\mathcal{W}
$$

The center of circle $c$ in the inertial frame is

$$
\boldsymbol{p}+\boldsymbol{R}^{\mathcal{W}}_{\mathcal{B}}(\boldsymbol{z})\boldsymbol{p}^{\mathcal{B}}_c
$$

where $\boldsymbol{p}$ is the robot position, $\boldsymbol{R}^{\mathcal{W}}_{\mathcal{B}}$ is the rotation matrix given by its orientation, and $\boldsymbol{p}^{\mathcal{B}}_c$ is the circle center in the body frame. This representation makes the framework agnostic to the robot model.

##### Static obstacles

The static obstacle environment is captured in an occupancy grid map, with occupied area $\mathcal{O}^{\mathrm{static}}\subset\mathcal{W}$. A global map built a priori is used primarily for localization, while a local map from current sensor readings is continuously updated. Recognized and tracked dynamic obstacles are removed from the static map and considered as moving obstacles.

##### Dynamic obstacles

Each moving obstacle $i$ is represented by an ellipse $\mathcal{A}_i\subset\mathcal{W}$ with semi-major axis $a_i$, semi-minor axis $b_i$, and rotation matrix $\boldsymbol{R}_i(\psi_i)$. For a time-varying set $\mathcal{I}=\{1,\ldots,n\}$, the occupied area is

$$
\mathcal{O}^{\mathrm{dyn}}_t=\bigcup_{i=1}^{n}\mathcal{A}_i\left(\boldsymbol{z}_i(t)\right)
$$

A constant-velocity model with Gaussian acceleration noise is assumed

$$
\ddot{\boldsymbol{p}}_i(t)=\boldsymbol{\omega}_i(t)
\qquad
\boldsymbol{\omega}_i(t)\sim\mathcal{N}\left(\boldsymbol{0},\boldsymbol{Q}_o(t)\right)
$$

Given measured positions, future positions and uncertainties are estimated with a linear Kalman filter.

##### Global Reference Path

The reference may be a straight line to the goal, a line in the preferred direction of motion, or a path supplied by a global planner. The global reference path $\mathcal{P}$ consists of $M$ path segments connecting waypoints $\boldsymbol{p}^{r}_m=[x^p_m\ y^p_m]^{\mathsf{T}}\in\mathcal{W}$. For smoothness, every segment $\varsigma_m(\theta)$ is a cubic polynomial. The variable $\theta$ approximately represents traveled distance along the path. The reference is not required to be collision free, so the robot may deviate from it to avoid collisions.

##### Problem Formulation

The objective is to generate collision-free motion for $N$ future time steps while minimizing a cost that penalizes deviation from the reference path

$$
\begin{aligned}
J^*=\min_{\boldsymbol{z}_{0:N}\ \boldsymbol{u}_{0:N-1}\ \theta_{0:N-1}}
&\sum_{k=0}^{N-1}J\left(\boldsymbol{z}_k,\boldsymbol{u}_k,\theta_k\right)
+J\left(\boldsymbol{z}_N,\theta_N\right)\\
\mathrm{s.t.}\quad
&\boldsymbol{z}_{k+1}=f\left(\boldsymbol{z}_k,\boldsymbol{u}_k\right)\\
&\theta_{k+1}=\theta_k+v_k\tau\\
&\mathcal{B}(\boldsymbol{z}_k)\cap\left(\mathcal{O}^{\mathrm{static}}\cup\mathcal{O}^{\mathrm{dyn}}_k\right)=\varnothing\\
&\boldsymbol{u}_k\in\mathcal{U}\quad\boldsymbol{z}_k\in\mathcal{Z}
\end{aligned}
$$

Here $v_k$ is the forward velocity, $\tau$ is the time step, and $\mathcal{Z}$ and $\mathcal{U}$ are the admissible state and input sets. Solving the problem yields a locally optimal command sequence that follows the reference while avoiding static and moving obstacles.

### Method

The method is executed in every planning loop. It searches for collision-free regions in the updated static map and constrains the robot to remain inside them, predicts future dynamic-obstacle positions and applies a corrected collision bound, then solves a modified Model Predictive Contouring Control formulation and applies the first optimal input.

##### Static collision avoidance

Given the static map, the method computes convex four-sided polygons in free space. These regions can be larger than approximations such as safety bubbles. At time $t$, the optimal trajectory from $t-1$ is shifted

$$
\boldsymbol{q}_{0:N}=\left[\boldsymbol{p}^{*}_{1:N\mid t-1}\ \boldsymbol{q}_N\right]
\qquad
\boldsymbol{q}_N=2\boldsymbol{p}^{*}_{N\mid t-1}-\boldsymbol{p}^{*}_{N-1\mid t-1}
$$

For each $\boldsymbol{q}_k$, a convex region is defined by four linear constraints. The implementation uses a rectangular region aligned with the trajectory orientation at $\boldsymbol{q}_k$; every side is obtained by a search routine and reduced by the robot-circle radius $r_{\mathrm{disc}}$. For circle $j$ and polygon side $l$,

$$
c^{\mathrm{stat},l,j}_k(\boldsymbol{z})
=h^l-\boldsymbol{n}^{l\mathsf{T}}
\left(\boldsymbol{p}-\boldsymbol{R}^{\mathcal{W}}_{\mathcal{B}}(\boldsymbol{z})\boldsymbol{p}^{\mathcal{B}}_j\right)>0
$$

where $h^l$ and $\boldsymbol{n}^l$ define the polygon side. The predicted robot positions are therefore explicitly constrained to a polyhedral approximation of the collision-free area.

##### Dynamic collision avoidance

For every obstacle $i$, prediction step $k$, and robot circle $j$, the circle must not intersect the obstacle ellipse. Omitting $i$ for compactness, the constraint is

$$
\begin{bmatrix}
\Delta x^j_k\\
\Delta y^j_k
\end{bmatrix}^{\mathsf{T}}
\boldsymbol{R}(\psi)^{\mathsf{T}}
\begin{bmatrix}
\alpha^{-2} & 0\\
0 & \beta^{-2}
\end{bmatrix}
\boldsymbol{R}(\psi)
\begin{bmatrix}
\Delta x^j_k\\
\Delta y^j_k
\end{bmatrix}>1
$$

The parameters $\alpha$ and $\beta$ define an enlarged ellipse containing the Minkowski sum of the obstacle ellipse and the robot circle. The usual approximation $\alpha=a+r_{\mathrm{disc}}$ and $\beta=b+r_{\mathrm{disc}}$ is not correct and collisions can still occur.

The paper instead considers the original ellipse $\boldsymbol{E}_1=\operatorname{Diag}(a^{-2},b^{-2})$ and an ellipse $\boldsymbol{E}_2=\operatorname{Diag}((a+\delta)^{-2},(b+\delta)^{-2})$. The minimum enlargement $\delta$ makes the minimum distance between them equal to the circle radius $r$. The relevant root is

$$
\lambda_1(\delta)=
\frac{2a(r+\delta)^3+2b(r+\delta)^3+4ab(r+\delta)^2}
{a^2+2ab+2ra+b^2+2rb}
$$

and $\delta$ is obtained from

$$
\lambda_1(\delta)=r^2
$$

The semi-axes

$$
\alpha=a+\delta
\qquad
\beta=b+\delta
$$

guarantee that the constraint ellipse entirely bounds the collision space. This closed-form conservative bound is the key correction used for safe avoidance of ellipsoidal moving obstacles.

##### Model Predictive Contouring Control

Model Predictive Contouring Control is specially tailored to path-following problems. LMPCC modifies the baseline formulation for mobile robots navigating in unstructured environments with on-board perception.

**Progress on reference path.** At every planning stage, $\theta_0$ is initialized by finding the closest path segment $m$ and performing a line search in the neighborhood of the previously predicted path parameter.

**Selecting the number of path segments.** Only $\eta\le M$ segments are used to build the local reference and lower the computational load. A conservative $\eta$ must cover the distance reachable over the prediction horizon

$$
\tau\sum_{j=0}^{N-1}v_j
\le\tau Nv_{\max}
\le\sum_{i=m+1}^{m+\eta}\left\lVert\boldsymbol{p}^{r}_{i+1}-\boldsymbol{p}^{r}_i\right\rVert
\le\sum_{i=m+1}^{m+\eta}s_i
$$

where $s_i$ is the length of path segment $i$.

**Maintaining continuity over the local reference path.** The selected cubic segments are concatenated into a differentiable local reference

$$
\bar{\boldsymbol{p}}^{r}(\theta_k)=
\sum_{i=m}^{m+\eta}
\sigma_{i,+}(\theta_k)\sigma_{i,-}(\theta_k)\boldsymbol{\varsigma}_i(\theta_k)
$$

with

$$
\sigma_{i,-}(\theta_k)=
\frac{1}{1+\exp\left(\dfrac{\theta_k-\sum_{j=m}^{i}s_j}{\epsilon}\right)}
\qquad
\sigma_{i,+}(\theta_k)=
\frac{1}{1+\exp\left(\dfrac{-\theta_k+\sum_{j=m}^{i-1}s_j}{\epsilon}\right)}
$$

The sigmoid activation functions provide a continuous local reference needed to compute solver gradients.

**Cost function.** The contour and lag errors are combined in

$$
\boldsymbol{e}_k=
\begin{bmatrix}
\sin\phi(\theta_k) & -\cos\phi(\theta_k)\\
-\cos\phi(\theta_k) & -\sin\phi(\theta_k)
\end{bmatrix}
\left(\boldsymbol{p}_k-\bar{\boldsymbol{p}}^{r}(\theta_k)\right)
$$

where $\phi(\theta_k)=\arctan\left(\partial y^r(\theta_k)/\partial x^r(\theta_k)\right)$ is the path direction. The tracking term is

$$
J_{\mathrm{tracking}}(\boldsymbol{z}_k,\theta_k)=
\boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{Q}_{\epsilon}\boldsymbol{e}_k
$$

Progress, dynamic-obstacle clearance, and smooth inputs are introduced by

$$
J_{\mathrm{speed}}(\boldsymbol{z}_k,\boldsymbol{u}_k)=Q_v(v_{\mathrm{ref}}-v_k)^2
$$

$$
J_{\mathrm{repulsive}}(\boldsymbol{z}_k)=
Q_R\sum_{i=1}^{n}
\frac{1}{(\Delta x^i_k)^2+(\Delta y^i_k)^2+\gamma}
$$

$$
J_{\mathrm{input}}(\boldsymbol{u}_k)=
\boldsymbol{u}_k^{\mathsf{T}}\boldsymbol{Q}_u\boldsymbol{u}_k
$$

The repulsive term increases clearance and improves robustness to localization uncertainties. The stage cost is

$$
J=J_{\mathrm{tracking}}+J_{\mathrm{speed}}+J_{\mathrm{repulsive}}+J_{\mathrm{input}}
$$

and the terminal cost contains $J_{\mathrm{tracking}}+J_{\mathrm{repulsive}}$.

The complete LMPCC problem is a receding-horizon nonconvex optimization

$$
\begin{aligned}
J^*=\min_{\boldsymbol{z}_{0:N}\ \boldsymbol{u}_{0:N-1}\ \theta_{0:N}}
&\sum_{k=0}^{N-1}J\left(\boldsymbol{z}_k,\boldsymbol{u}_k,\theta_k\right)
+J\left(\boldsymbol{z}_N,\theta_N\right)\\
\mathrm{s.t.}\quad
&\boldsymbol{z}_{k+1}=f\left(\boldsymbol{z}_k,\boldsymbol{u}_k\right)\\
&\theta_{k+1}=\theta_k+v_k\tau\\
&\boldsymbol{u}_k\in\mathcal{U}\quad\boldsymbol{z}_k\in\mathcal{Z}\\
&c^{\mathrm{stat},l,j}_k(\boldsymbol{z}_k)>0\\
&c^{\mathrm{obst},i,j}_k(\boldsymbol{z}_k)>1
\end{aligned}
$$

At each control iteration, the method estimates $\theta_0$, selects $\eta$, builds $\bar{\boldsymbol{p}}^r$, computes the static regions, obtains predicted dynamic-obstacle poses, solves the optimization problem, and applies only $\boldsymbol{u}^{*}_0$. The problem is solved until a Karush-Kuhn-Tucker condition or the maximum number of iterations is reached, after which the horizon is shifted and the procedure repeats.

### Conclusions & Future Work

The local MPCC combines motion planning and control in one optimization module. Its main innovations are the polyhedral free-space constraints for static obstacles and the corrected upper bound of the Minkowski sum of a circle and an ellipse for dynamic obstacles. The implementation runs in real time on-board, showed lower failure rates and safer predictive behavior than the tested baselines, scaled to six pedestrians, and was also applied to a simulated autonomous car. Future work targets crowded scenarios by accounting for interaction effects between the robot and other agents.
