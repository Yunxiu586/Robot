# EGO-Swarm

[toc]

### Abstract

This paper presents a decentralized and asynchronous systematic solution for multi-robot autonomous navigation in unknown obstacle-rich scenes using merely onboard resources. The planning system is formulated under gradient-based local planning framework, where collision avoidance is achieved by formulating the collision risk as a penalty of a nonlinear optimization problem.

In order to improve robustness and escape local minima, we incorporate a lightweight topological trajectory generation method. Then agents generate safe, smooth, and dynamically feasible trajectories in only several milliseconds using an unreliable trajectory sharing network. Relative localization drift among agents is corrected by using agent detection in depth images.

Our method is demonstrated in both simulation and real-world experiments. The source code is released for the reference of the community.

### implicit topological trajectory generation of gradient-based local planning

##### an ESDF-free gradient-based local planner

EGO-Planner formulates trajectory generation as a non-linear optimization problem that trades off smoothness, collision, dynamic feasibility, and terminal progress.

The decision variables are the control points $\boldsymbol{Q}$ of a uniform B-spline $\boldsymbol{\Phi}$ used to parameterize the trajectory.

$$
\min_{\boldsymbol{Q}} J_{\mathrm{EGO}}
=
\sum_r \lambda_r J_r
$$

$$
r=\{s,c,d,t\}
$$

Here $J_s$, $J_c$, $J_d$, and $J_t$ denote smoothness, collision, dynamic feasibility, and terminal progress costs.

The terms of $J$ are divided into two categories: minimum error and soft barrier constraint.

Minimum error terms $J_s$ and $J_t$ minimize the total error between a linear transformation of decision variables $L(\boldsymbol{Q})$ and a desired value $\boldsymbol{D}$.

$$
J_r
=
\sum_{\boldsymbol{Q}\in\boldsymbol{\Phi}}
\left\|L(\boldsymbol{Q})-\boldsymbol{D}\right\|_n^n
$$

Soft barrier constraint terms $J_c$ and $J_d$ penalize decision variables exceeding a specific threshold $T$.

$$
J_r
=
\sum_{\boldsymbol{Q}\in\boldsymbol{\Phi}}
\begin{cases}
\left(\dfrac{L(\boldsymbol{Q})-(T-\epsilon)}{S}\right)^n & L(\boldsymbol{Q})>T-\epsilon \\
0 & L(\boldsymbol{Q})\le T-\epsilon
\end{cases}
$$

EGO-Planner estimates obstacle distance from environment information possessed by each control point independently.

The information is parameterized by several $\{\boldsymbol{p},\boldsymbol{v}\}$ pairs.

- $\boldsymbol{p}$ denotes an anchor point at the obstacle surface
- $\boldsymbol{v}$ represents a safe direction pointing from inside to outside of that obstacle

The obstacle distance $d_{ij}$ of the $i$-th control point $\boldsymbol{Q}_i$ to the $j$-th obstacle is defined as

$$
d_{ij}
=
(\boldsymbol{Q}_i-\boldsymbol{p}_{ij})^T\boldsymbol{v}_{ij}
$$

The basic procedure is as follows.

A naive initial trajectory $\boldsymbol{\Phi}$ is given regardless of collision. A safe path $\boldsymbol{\Gamma}$ connecting two ends of the colliding segment of $\boldsymbol{\Phi}$ is searched. Then $\boldsymbol{v}$ is generated from $\boldsymbol{\Phi}$ to $\boldsymbol{\Gamma}$, and $\boldsymbol{p}$ is defined at the obstacle surface. With generated $\{\boldsymbol{p},\boldsymbol{v}\}$ pairs, the planner maximizes $d_{ij}$ and returns an optimized trajectory.

##### implicit topological trajectory generation

The widely used homotopy concept is insufficient to capture candidate trajectories in 3-D cases. The paper follows the term topological planning, while using the visibility deformation idea for useful 3-D trajectory distinction.

Uniform visibility deformation is defined as follows.

Two trajectories $\boldsymbol{\tau}_1(s)$ and $\boldsymbol{\tau}_2(s)$, parameterized by $s\in[0,1]$, satisfy

$$
\boldsymbol{\tau}_1(0)=\boldsymbol{\tau}_2(0)
$$

$$
\boldsymbol{\tau}_1(1)=\boldsymbol{\tau}_2(1)
$$

They belong to the same UVD class if, for all $s$, the line segment between $\boldsymbol{\tau}_1(s)$ and $\boldsymbol{\tau}_2(s)$ is collision-free.

Traditional topological planning methods consist of topologically distinct path search and back-end optimization. They mainly focus on finding multiple initial paths in distinct homotopy.

The proposed method constructs distance fields in different directions by inverting the safe direction.

$$
\boldsymbol{v}_{\mathrm{new}}
:=
-\boldsymbol{v}
$$

A search process determines a new anchor point $\boldsymbol{p}_{\mathrm{new}}$ at the obstacle surface along $\boldsymbol{v}_{\mathrm{new}}$.

The new pair is

$$
\{\boldsymbol{p}_{\mathrm{new}},\boldsymbol{v}_{\mathrm{new}}\}
$$

This pair leads to a different local minimum. No explicit path search is adopted. Any pair of paths through $\boldsymbol{p}$ and $\boldsymbol{p}_{\mathrm{new}}$ naturally violates the UVD definition at these two points.

Distinctive trajectories are optimized in parallel in different threads. The trajectory with the lowest cost is executed.

### drone swarm navigation

##### reciprocal collision avoidance

Let $\boldsymbol{x}_k(t)\in\mathcal{X}\subset\mathbb{R}^3$ be the position state of agent $k$ among $K$ agents at time $t$.

$\mathcal{X}^{\mathrm{free}}_k(t)$ is the free region in the state space of agent $k$ considering the existence of other agents.

The valid trajectory $\boldsymbol{\Phi}_k$ satisfies

$$
\boldsymbol{\Phi}_k(t)
\in
\mathcal{X}^{\mathrm{free}}_k(t)
$$

The paper ignores obstacles and dynamic constraints in this term because they have already been tackled in the ESDF-free gradient-based local planner.

Similar to the penalty on obstacle collision and dynamical infeasibility, the swarm collision avoidance penalty $J_{w,k}$ for agent $k$ is formulated as a soft barrier constraint.

$$
J_{w,k}
=
\sum_i
\int_{t_s}^{t_e}
\begin{cases}
d_{k,i}^2(t) & d_{k,i}(t)<0 \\
0 & d_{k,i}(t)\ge 0
\end{cases}
dt
$$

$$
d_{k,i}(t)
=
\left\|
\boldsymbol{E}^{1/2}
\left[
\boldsymbol{\Phi}_k(t)-\boldsymbol{\Phi}_i(t)
\right]
\right\|
-
(C+\epsilon)
$$

$$
\boldsymbol{E}
=
\operatorname{diag}(1,1,1/c)
$$

Here $C$ is the user-defined agent clearance. $\boldsymbol{E}$ transforms Euclidean distance into ellipsoidal distance with a shorter principal axis at the $z$-axis to relieve downwash risk.

Adding the weighted $J_w$ to the EGO-Planner objective yields the total optimization problem for each agent.

$$
\min_{\boldsymbol{Q}} J
=
J_{\mathrm{EGO}}+
\lambda_w J_w
$$

The paper parameterizes trajectory using a $p_b$-degree uniform B-spline. The position evaluation has a matrix representation.

$$
\boldsymbol{\Phi}(t)
=
\boldsymbol{s}^T(t)\boldsymbol{M}_{p_b+1}\boldsymbol{q}_m
$$

$$
\boldsymbol{s}(t)
=
\begin{bmatrix}
1 & s(t) & s^2(t) & \cdots & s^{p_b}(t)
\end{bmatrix}^T
$$

$$
\boldsymbol{q}_m
=
\begin{bmatrix}
\boldsymbol{Q}_{m-p_b} &
\boldsymbol{Q}_{m-p_b+1} &
\boldsymbol{Q}_{m-p_b+2} &
\cdots &
\boldsymbol{Q}_m
\end{bmatrix}^T
$$

$$
s(t)
=
\dfrac{t-t_m}{\Delta t}
$$

$\boldsymbol{M}_{p_b+1}$ is a constant matrix determined by $p_b$, and $s(t)$ is defined when $t$ belongs to the knot span $(t_m,t_{m+1}]$.

##### localization drift compensation

Individual localization in unknown environments accumulates drift during the flight because there is no reliable and high-frequency loop-closure.

The paper proposes a simplified and lightweight relative drift estimation method by comparing

- the predicted position evaluated from received agents' trajectories
- the measured positions from depth images of witnessed agents

This strategy works when trajectory tracking error is negligible and at least one of any two agents that might collide can see the other.

After evaluating the current position $\boldsymbol{\Phi}_i(t_{\mathrm{now}})$ of agent $i$, a spherical trust region $\mathcal{S}\subset\mathbb{R}^3$ centered at $\boldsymbol{\Phi}_i(t_{\mathrm{now}})$ with radius $R$ is determined.

$R$ is an empirical parameter indicating the upper bound of typical drift estimated from experiments.

The trust region is mapped to the currently captured depth image.

$$
z
\begin{bmatrix}
\boldsymbol{s}'^T & 1
\end{bmatrix}^T
=
\boldsymbol{K}\boldsymbol{T}_w^c
\begin{bmatrix}
\boldsymbol{s}^T & 1
\end{bmatrix}^T
$$

Here $\boldsymbol{s}'\in\mathcal{S}'$, $\boldsymbol{s}\in\mathcal{S}$, $\boldsymbol{K}$ and $\boldsymbol{T}_w^c$ are camera intrinsic and extrinsic matrices, and $z$ is the deviation of $\boldsymbol{s}$ along the main optical axis from the optical center.

The exact $\mathcal{S}'$ is an elliptical conic section. The paper adopts an approximate axis-aligned ellipse $\bar{\mathcal{S}}'$ because the trust region is empirical.

Each point within $\bar{\mathcal{S}}'$ is projected into the world frame. Points belonging to $\mathcal{S}$ are collected as a point cluster $\mathcal{P}\subset\mathcal{S}$.

The observed position of the agent is regarded as the center, namely the first raw moment of $\mathcal{P}$.

$$
\boldsymbol{P}
=
\mu_1^0(\mathcal{P})
$$

Additional criteria are added to improve the robustness of agent detection, such as the number of pixels, the second central moment of $\mathcal{P}$, and the deviation of the current measurement to previous ones.

The error between $\boldsymbol{\Phi}_i(t_{\mathrm{now}})$ and $\boldsymbol{P}$ is fed to a filter, from where the estimated drift is acquired.

##### agent removal from depth images

The system uses occupancy grid map to store static obstacles and depth images for map fusion.

Moving agents are handled by reciprocal collision avoidance, so recording moving agents and treating them as obstacles in map building is not necessary and can be harmful.

The pixels of detected agents are masked and removed from the depth images. Agents on gray-scale images are removed using the same mask for the corresponding depth images because moving objects covering the majority of the view are interference to VIO.

The criterion for agent detection used here is less strict since false positives are more harmful than false negatives.

### system architecture

The system architecture contains the detailed architecture for a single agent and the multi-agent communication system.

##### navigation system of a single agent

The single-agent system is based on EGO-Planner, with an extra module that compensates VIO drift and removes witnessed agents on images.

For trajectory generation in unknown environments, the local planner is used.

Planning is activated when the current trajectory collides with newly discovered obstacles, or when the agent is getting close to the end of the current trajectory.

##### communication framework

Two networks connect the system.

- a broadcast network sharing trajectories
- a chain network to synchronize timestamps and manage sequential startup

##### broadcast network

Once an agent generates a new collision-free trajectory, it is broadcast immediately to all agents.

Other agents receive and store this trajectory. The stored trajectory is used to generate safe trajectories for themselves when necessary.

The closed-loop strategy works in ideal situations where the connection is stable and latency is negligible. Since this is not guaranteed in practice, the paper uses two methods to reduce collision possibility.

First, one trajectory is broadcast at a given frequency under network capacity. A typical trajectory containing 3-D waypoints and other parameters is less than 0.5KB.

Second, each agent checks collision as soon as a trajectory is received from the broadcast network. If potential collisions are detected, a new collision-free trajectory is generated.

Before planning, each agent compares its current position with received surrounding agents' trajectories. Any trajectory outside the planning range is ignored.

##### chain network

A connection-based stable chain network is used for timestamp synchronization and system startup management.

At system startup, agents generate trajectories in a predefined order. Each agent generates its initial trajectory after receiving trajectories from agents with higher priority through the chain network.

This strategy avoids chaos caused by simultaneous trajectory generation during system startup, when agents have no information about other trajectories.

### benchmark

##### topological planning

The paper compares the proposed EGO-Swarm with Fast-Planner in candidate trajectory number and computation time for front-end topological path search.

EGO-Swarm finds fewer candidate trajectories, which means a lower probability of finding the global optimum, but it is faster than Fast-Planner by two orders of magnitude.

Fast-Planner finds topologically distinct paths by PRM graph search, path shortening, and path pruning. These operations are time-consuming but have a higher degree of freedom compared with the proposed implicit topological path search method.

##### swarm planning

In empty space, the paper compares the proposed method with DMPC, ORCA, and RBP in flight distance, flight time, collision times per agent, and computation time.

+ RBP tends to generate safe but conservative trajectories because the construction of convex relative safe flight corridor significantly compresses the solution space.

+ DMPC is designed for distributed deployment, but it requires accurate and high-frequency pose communication, which cannot be guaranteed in real-world applications.

+ ORCA updates fast because of efficient rules, but using speed as control commands makes it incompatible with third-order systems such as quadrotors. The risk of collision also limits its application.

The proposed method generates short collision-free and non-conservative trajectories with fast computation, enabling real-time applications for quadrotors.

In obstacle-rich environments, ten drones fly from one side of the map to the other. Each agent senses the environment independently, and local maps are constructed independently.

An inverse point-to-point transition is designed to make reciprocal collision avoidance inevitable around the map center. Each agent manages to plan smooth and safe trajectories.

##### scalability analysis

The computation performance is evaluated in a scenario where agents arranged in a straight line fly to random target points 50 meters away.

Due to the on-demand collision check strategy, time complexity gradually flattens out with the increase in the number of agents.

### real-world experiments

##### indoor

Indoor experiments are presented at a speed limit of 1.5m/s.

The quadrotors perform a circle swap with reciprocal collision avoidance. They also pass through a narrow door one after another. In a more cluttered environment, three quadrotors navigate across the environment.

##### outdoor

Outdoor experiments are performed in a forest where trees are spaced about 2 meters apart.

Three quadrotors start in the forest together and reach the target position outside the forest. The velocity limit is set to 1.5m/s.

To emphasize reciprocal avoidance, the order of the goal positions is reversed relative to the start positions, making reciprocal avoidance unavoidable.
