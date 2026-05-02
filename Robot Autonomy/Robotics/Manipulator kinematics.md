[toc]

# Manipulator kinematics

### Forward kinematics

Kinematics studies motion geometry, such as position, velocity, acceleration, without considering forces. 

A manipulator consists of rigid **links** connected by **joints** with position sensors. **Revolute** joints, where displacement is measured as **joint angles**, and **prismatic joints**, where displacement is a linear translation called **joint offset**.

A manipulator’s **degrees of freedom (DOF)** equal the number of independent position variables required to fully locate all its parts. In typical industrial robots, because a manipulator are open kinematic chains with each joint defined by a single variable, the number of joints directly equals the number of DOF.

The **end-effector** (e.g., gripper, tool) at the chain’s end is described via a **tool frame** relative to a **base frame**. **Forward kinematics** solves the static geometric problem of computing the end-effector’s position and orientation from given joint angles, transforming motion representation from **joint space** to **Cartesian space**. 

Given the position and orientation of the end-effector of the manipulator, **inverse kinematics** calculates all possible sets of joint angles that could be used to attain this given position and orientation.

### Link connection

##### Denavit-Hartenberg notation

Any robot can be described kinematically by giving the values of 4 quantities for each link. Two describe the link itself, and two describe the link's connection to a neighboring link. 

+ $a_i$  **link length**: This distance along a line that is mutually perpendicular to both axis $i$ and axis $i+1$.
+ $\alpha_i$  **link twist**: Imagine a plane whose normal is the mutually perpendicular line. Project the axes $i$ and $i+1$ onto this plane and measure the angle from axis $i$ to axis $i+1$ in the right-hand sense.
+ $d_i$ **link offset**: The distance along the common axis from one link to the next, i.e., the distance between two normals.
+ $\theta_i$: **joint angle**: The angle between one link and its neighbor.

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/436994b1-10e0-4fe8-89fb-2c007e7949d6.png" alt="436994b1-10e0-4fe8-89fb-2c007e7949d6" style="zoom:60%;" />

**Tip**: The mutual perpendicular always exists; it is unique except when both axes are parallel, in which case there are many mutual perpendiculars of equal length.

##### Convention for affixing frames to links

+ The origin of frame {$i$} is located where the perpendicular intersects the joint $i$ axis. 
+ The $z$ axis of frame {$i$}, called $Z_i$, is coincident with the joint axis $i$. 
+ $X_i$ points along $a_i$ in the direction from joint $i$ to joint $i+1$. In the case of $a_i=0$, $X_i$ is normal to the plane of $Z_i$ and $Z_{i+1}$. 
+ $Y_i$ is formed by the right-hand rule to complete the $i$th frame.

$$
X_i=Z_{i-1}\times Z_{i}\quad or \quad X_i=Z_{i}\times Z_{i-1}
$$

If the link frames have been attached to the links according to our convention, the following definitions of the link parameters are valid:
$$
a_i=the \; distance \; from \; Z_i \; to \; Z_{i+1} \; measured \; along \; X_i
$$

$$
\alpha_i= the \; angle \; from \; Z_i \; to \; Z_{i+1} \; measured \; about \; X_i
$$

$$
d_i= the \; distance \; from \; X_{i-1} \; to \; X_i \; measured \; along \; Z_i
$$

$$
\theta_i=the \; angle \; from \; X_{i-1} \; to \; X_i \; measured \; about \; Z_i
$$

Find transformation between coordinate frames {$i-1$} and {$i$}.

+ Translate along $Z_{i-1}$ a distance $d_i$.
+ Rotate around $Z_{i-1}$ an angle $\theta_i$ to align the  $x$ axes parallel.
+ Translate along $X_{i}$ a distance $a_{i-1}$ to to align the origins to coincide.
+ Rotate around $X_{i}$ an angle $\alpha_{i-1}$ to align the $z$ axes to coincide.

 ##### Manipulator kinematics

In general, the transformation ${^{i-1}T_i}$ that defines frame {$i$} relative to the frame {$i-1$}, will be a function of the 4 link parameters. For any given robot, this transformation will be a function of only 1 variable, the other 3 parameters being fixed by mechanical design.
$$
{^{i-1}T_i}=R_X(\alpha_{i-1})D_X(a_{i-1})R_Z(\theta_i)D_Z(d_i)
$$
or
$$
{^{i-1}T_i}=\text{Screw}_X(a_{i-1},\alpha_{i-1})\text{Screw}_Z(d_{i},\theta_{i})
$$
The general form of ${^{i-1}T_i}$
$$
{^{i-1}T_i}=\begin{bmatrix}
\text{cos}\theta_i & -\text{sin}\theta_i & 0 & a_{i-1} \\
\text{sin}\theta_i\text{cos}\alpha_{i-1} & \text{cos}\theta_i\text{cos}\alpha_{i-1} &
-\text{sin}\alpha_{i-1} & -d_i\text{sin}\alpha_{i-1} \\
\text{sin}\theta_i\text{sin}\alpha_{i-1} & \text{cos}\theta_i\text{sin}\alpha_{i-1} & 
\text{cos}\alpha_{i-1} & d_i\text{cos}\alpha_{i-1} \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
The link transformations can be multiplied together to find the single transformation that relates frame {$N$} to frame {$0$}:
$$
^0T_N={^0T_1}{^1T_2}{^2T_3}...{^{N-1}T_N}
$$
If the robot's joint-position sensors are queried, the Cartesian position and orientation of the last
link can be computed by $^0T_N$.

+ For revolute joint, $\theta$ is joint variable.
+ For prismatic joint, $d$ is a joint variable.
+ In the case of prismatic joint, the length $a_n$ has no meaning and is set to 0.
+ The origin of the frame for a prismatic join is coincident with the next defined link origin. The zero position is defined when $d_n=0$.

##### Actual space, joint space and Cartesian space

+ **Joint Space**: The position of all links is specified by a set of $n$ joint variables, forming an $n\times1$ joint vector. The collection of all possible joint vectors is called joint space.
+ **Cartesian Space **(Task-Oriented/Operational Space): Position is measured along orthogonal axes and orientation is measured by established conventions.
+ **Actuator Space**: In many robots, joints are not directly actuated. Actuators may work in differential pairs or through linkages. Sensors are often at the actuators, so computation is needed to derive the joint vector from an actuator vector.

The forward kinematics focuses on the forward mappings from actuator space to joint space, and from joint space to Cartesian space. The forward kinematics addresses the inverse mappings.

The connection between actuators and joints varies. For any robot, the specific relationship between actuator positions and joint positions must be determined.

##### Frames with standard names

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/1b4c4502-19e8-4330-a270-9be4bb545680.png" alt="1b4c4502-19e8-4330-a270-9be4bb545680" style="zoom:60%;" />

The **base frame**, {$B$} is located at the base of the manipulator. It is merely another name for frame
{0}. It is affixed to a non-moving part of the robot, sometimes called link 0.

The **station frame** {$S$} is placed at a task-relevant location, such as a table corner. As far as the user of this robot system is concerned, {$S$} is the universe frame, and all robot actions are performed relative to it. It is also called the task  frame, world frame, or universe frame. The station frame is always specified with respect to the base frame ${^BT_S}$.

The **wrist frame** {$W$} is affixed to the last link of the manipulator. Very often, {$W$} has its origin fixed
at a point called the wrist of the manipulator, and {$W$} moves with the last link of the manipulator.

The **tool frame** {$T$} is affixed to the end of any tool the robot happens to be holding. When the
hand is empty, {$T$} is usually located with its origin between the fingertips of the robot. The tool frame is always specified with respect to the wrist frame.

The **goal frame** {$G$} is a description of the location to which the robot is to move the tool. At the end of the motion, the tool frame should be brought to coincidence with the goal frame. {$G$} is always specified relative to the station frame.

To calculate {$T$} relative to {$S$}, implement **WHERE** function. The output of **WHERE** would be the position and orientation of the tool relative to the station.
$$
{^ST_T}={^BT_S^{-1}}{^BT_W}{^WT_T}
$$
<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/e5a3ca9b-eb0f-4446-87e0-f06692ca6ec7.png" alt="e5a3ca9b-eb0f-4446-87e0-f06692ca6ec7" style="zoom:70%;" />

### PUMA 560

The Unimation PUMA 560 is a robot with six degrees of freedom and all rotational joints.

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/1be6963a-e3ec-4eec-abda-7efcbe83167c.png" alt="1be6963a-e3ec-4eec-abda-7efcbe83167c" style="zoom:70%;" />

Link parameters of the PUMA 560:

|      | $\alpha_{i-1}$ | $a_{i-1}$ | $d_i$ | $\theta_i$ |
| :--: | :------------: | :-------: | :---: | :--------: |
|  1   |       0        |     0     |   0   | $\theta_1$ |
|  2   |  $-90\degree$  |     0     |   0   | $\theta_2$ |
|  3   |       0        |   $a_2$   | $d_3$ | $\theta_3$ |
|  4   |  $-90\degree$  |   $a_3$   | $d_4$ | $\theta_4$ |
|  5   |  $90\degree$   |     0     |   0   | $\theta_5$ |
|  6   |  $-90\degree$  |     0     |   0   | $\theta_6$ |

Each of the link transformations:
$$
\begin{array}{l}
^{0}T_{1} = \left[\begin{array}{cccc}
\cos\theta_{1} & -\sin\theta_{1} & 0 & 0 \\
\sin\theta_{1} &  \cos\theta_{1} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
^{1}T_{2} = \left[\begin{array}{cccc}
\cos\theta_{2} & -\sin\theta_{2} & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\sin\theta_{2} & -\cos\theta_{2} & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
^{3}T_{2} = \left[\begin{array}{cccc}
\cos\theta_{3} & -\sin\theta_{3} & 0 & a_{2} \\
\sin\theta_{3} &  \cos\theta_{3} & 0 & 0 \\
0 & 0 & 1 & d_{3} \\
0 & 0 & 0 & 1
\end{array}\right] \\
^{4}T_{3} = \left[\begin{array}{cccc}
\cos\theta_{4} & -\sin\theta_{4} & 0 & a_{3} \\
0 & 0 & 1 & d_{4} \\
-\sin\theta_{4} & -\cos\theta_{4} & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
^{5}T_{4} = \left[\begin{array}{cccc}
\cos\theta_{5} & -\sin\theta_{5} & 0 & 0 \\
0 & 0 & -1 & 0 \\
\sin\theta_{5} &  \cos\theta_{5} & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
^{6}T_{5} = \left[\begin{array}{cccc}
\cos\theta_{6} & -\sin\theta_{6} & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\sin\theta_{6} & -\cos\theta_{6} & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right]
\end{array}
$$
The product of all six link transforms:
$$
^{0}{T}_{6} = 
{^{0}{T}_{1}}{^{1}{T}_{2}}{^{2}{T}_{3}}{^{3}{T}_{4}}{^{4}{T}_{5}}{^{5}{T}_{6}} = 
{^{0}{T}_{1}} {^{1}{T}_{3}}{^{3}{T}_{6}}=
{^{0}{T}_{1}}{^{1}{T}_{6}}=
\left[ \begin{array}{cccc}
r_{11} & r_{12} & r_{13} & p_x \\
r_{21} & r_{22} & r_{23} & p_y \\
r_{31} & r_{32} & r_{33} & p_z \\
0 & 0 & 0 & 1
\end{array} \right]
$$
The equations specify how to compute the position and orientation of frame {6} relative to frame {0} of the robot.

### Inverse kinematics

Solving the problem of finding the required joint angles to place the tool frame, {$T$}, relative to the station frame, {$S$}, is split into two parts. First, frame transformations are performed to find the wrist frame, {$W$}, relative to the base frame, {$B$}, and then the inverse kinematics are used to solve for the joint angles.

##### Solvability

Given the numerical value of $^0T_N$, we attempt to find values of $\theta_1$, $\theta_2$, ..., $\theta_N$.

The inverse kinematics for a 6-DOF robotic arm involves solving for 6 joint angles $\theta_1$ through $\theta_6$. This is because the 6 degrees of freedom yield 6 independent equations, 3 rotation-matrix portion of $^0T_6$ and 3 from the position-vector portion of $^0T_6$. These 6 equations are nonlinear, transcendental equations, which can be quite difficult to solve.

##### Existence of solutions

+ **Workspace** is that volume of space that the end-effector of the manipulator can reach. 
+ Dextrous workspace is that volume of space that the robot end-effector can reach with all orientations.
+ Reachable workspace is that volume of space that the robot can reach in at least one orientation. The dextrous workspace is a subset of the reachable workspace.

If the desired position and orientation of the wrist frame is in the workspace, then at least one solution exists.

##### Multiple solutions

A position may be reached with several different **configurations**.

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/6f86d1712d164814f7467a6a3e1e8cd2.jpg" alt="6f86d1712d164814f7467a6a3e1e8cd2" style="zoom:9%;" />

The number of solutions depends upon the number of joints in the manipulator, but is also a function of the link parameters ($\alpha_i$, $a_i$ and $d_i$ for a rotary joint manipulator) and the allowable ranges of motion of the joints.

##### Method of solution

A manipulator is solvable if the joint variables can be determined by an algorithm that allows one to determine all the sets of joint variables associated with a given position and orientation.

Within the class of **closed-form solutions**, we distinguish two methods of obtaining the solution: **algebraic** and **geometric**.

All systems with revolute and prismatic joints having a total of six DOF in a single series chain are solvable. A sufficient condition that a manipulator with 6 revolute joints have a closed- form solution is that three neighboring joint axes intersect at a point.

##### Manipulator subspace

The reachable workspace of an $n$ DOF manipulator (where $n<6$) is a portion of an $n$ DOF subspace. The workspace of a simpler manipulator is a subset of its subspace. 

One way to specify the subspace is to describe the wrist or tool frame as a function of $n$ free variables. As these variables vary, the subspace is generated.

##### Algebraic solution

 Consider the three-link planar manipulator:

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/846b93ee4623efb7ee9202abc6c68290.jpg" alt="846b93ee4623efb7ee9202abc6c68290" style="zoom:8%;" />

|      | $\alpha_{i-1}$ | $a_{i-1}$ | $d_i$ | $\theta_i$ |
| :--: | :------------: | :-------: | :---: | :--------: |
|  1   |       0        |     0     |   0   | $\theta_1$ |
|  2   |       0        |   $l_1$   |   0   | $\theta_2$ |
|  3   |       0        |   $l_2$   |   0   | $\theta_3$ |

$$
^{B}T_{W} = {^{0}T_{3}} = \left[\begin{array}{cccc}
\cos(\theta_{1}+\theta_{2}+\theta_{3}) & -\sin(\theta_{1}+\theta_{2}+\theta_{3}) & 
0 & l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2) \\
\sin(\theta_{1}+\theta_{2}+\theta_{3}) &  \cos(\theta_{1}+\theta_{2}+\theta_{3}) & 
0 & l_1\sin\theta_1+l_2\sin(\theta_1+\theta_2) \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
$$

To focus our discussion on inverse kinematics, we assume that the transformations have been performed so that the goal point is a specification of the wrist frame relative to the base frame, $^BT_W$. Because we are working with three-link planar manipulator, specification of these goal points can be accomplished by specifying $x$, $y$, and $\phi$, where $\phi$ is the orientation of link 3 in the plane.
$$
^{B}T_{W} = \left[\begin{array}{cccc}
\cos\phi & -\sin\phi & 0 & x \\
\sin\phi &  \cos\phi & 0 & y \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \\
$$
We arrive at a set of 4 nonlinear equations that must be solved for $\theta_1$, $\theta_2$ and $\theta_3$.
$$
\cos\phi =  \cos(\theta_{1}+\theta_{2}+\theta_{3}) \\
\sin\phi = \sin(\theta_{1}+\theta_{2}+\theta_{3}) \\
x = l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2)\\  
y = l_1\sin\theta_1+l_2\sin(\theta_1+\theta_2)\\
$$
We now begin our algebraic solution
$$
x^2+y^2=l^2_1+l^2_2+2l_1l_2\cos\theta_2
$$

$$
\cos\theta_2 = \frac{x^2+y^2-l^2_1-l^2_2}{2l_1l_2}
$$

The right-hand side of the above equation must have a value between -1 and 1. This constraint would be checked at this time to find out whether a solution exists. Physically, if this constraint is not satisfied, then the goal point is too far away for the manipulator to reach.

Assuming the goal is in the workspace:
$$
\sin\theta_2=\pm \sqrt{1 - \cos^2\theta_2}
$$

$$
\theta_2=\text{atan2}({\sin\theta_2},{\cos\theta_2})
$$

Having found $\theta_2$, we can solve for $\theta_1$
$$
x = k_1\cos\theta_1-k_2\sin\theta_1\\  
y = k_1\sin\theta_1+k_2\cos\theta_1\\
$$
  where
$$
k_1=l_1+l_2\cos\theta_2	\\
k_2=l_2\sin\theta_2
$$
If
$$
r = + \sqrt{k^2_1+k^2_2} \\
\gamma = \text{atan2}({k_2},{k_1})
$$
then
$$
k_1=r\cos\gamma	\\
k_2=r\sin\gamma
$$
Equations now can be written as
$$
\frac{x}{r} = \cos\gamma \cos\theta_{1} - \sin\gamma \sin\theta_{1} \\
\frac{y}{r} = \cos\gamma \sin\theta_{1} + \sin\gamma \cos\theta_{1}
$$
so
$$
\cos(\gamma + \theta_{1}) = \frac{x}{r} \\
\sin(\gamma + \theta_{1}) = \frac{y}{r}
$$
Using the two-argument arctangent
$$
\gamma + \theta_{1} = \text{atan2}(\frac{y}{r},\frac{x}{r}) =  \text{atan2}({y},{x}) \\
\theta_{1} = \text{atan2}({y},{x})-\text{atan2}({k_2},{k_1})
$$
Note that, when a choice of sign is made in the solution of $\theta_2$ above, it will cause a sign change in $k_2$, thus affecting $\theta_1$. Note also that, if $x = y = 0$, then $\text{atan2}({y},{x})$ becomes undefined, in this case, $\theta_1$ is arbitrary.

Finally, we can solve for $\theta_3$
$$
\theta_{1}+\theta_{2}+\theta_{3}=\text{atan2}({\sin\phi},{\cos\phi})=\phi
$$
In summary, an algebraic approach to solving kinematic equations is basically one of manipulating the given equations into a form for which a solution is known.

##### Algebraic solution by reduction to polynomial

Making the following substitutions, yields an expression in terms of a single variable, $u$:
$$
\begin{aligned}
u &= \tan\frac{\theta}{2},\\
\cos\theta &= \frac{1 - u^2}{1 + u^2},\\
\sin\theta &= \frac{2u}{1 + u^2}.
\end{aligned}
$$
These substitutions convert transcendental equations into polynomial equations in $u$.

##### Geometric solution

Considering the solid triangle, we can apply the law of cosines to solve for $\theta_2$
$$
x^2+y^2=l^2_1+l^2_2-2l_1l_2\cos(180+\theta_2) 
$$

$$
\cos(180+\theta_2)=-\cos(\theta_2)
$$

$$
\cos\theta_2 = \frac{x^2+y^2-l^2_1-l^2_2}{2l_1l_2}
$$

Assuming a solution exists, this equation is solved for that value of $\theta_2$ that lies between 0 and -180 degrees, because only for these values does the triangle exist.

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/2a2193707792e954491d1c890251c59f.jpg" alt="2a2193707792e954491d1c890251c59f" style="zoom:16%;" />

To solve for $\theta_1$, we find expressions for angle $\psi$ and $\beta$ as indicated in the figure above. $\beta$ may be in any quadrant, depending on the signs of $x$ and $y$.
$$
\beta=\text{atan2}(y,x)
$$
We again apply the law of cosines to find $\psi$:
$$
\cos\psi = \frac{x^2+y^2+l^2_1-l^2_2}{2l_1\sqrt{x^2+y^2}}
$$
Here, the arccosine must be solved so that $0\le\psi\le180\degree$. Then we have
$$
\theta_1=\beta\pm\psi
$$
where the plus sign is used if $\theta_2<0$ and the minus sign if $\theta_2>0$.

We know that angles in a plane add, so the sum of the three joint angles must be the orientation of the last link:
$$
\theta_1+\theta_2+\theta_3=\phi
$$
This equation is solved for $\theta_3$ to complete our solution.

##### Pieper's solution when 3 axes intersect

Although a completely general robot with 6 DOF does not have a closed-form solution, manipulators with 6 DOF in which 3 consecutive axes intersect at a point can be solved.

When the last 3 axes intersect, the origins of link frames {4}, {5}, and {6} are all located at this point of intersection. This point is given in base coordinates as
$$
^0P_{4ORG}={^0T_1}{^1T_2}{^2T_3}{^3P_{4ORG}}
=
\left[\begin{array}{cccc}
x \\
y \\
z \\
1
\end{array}\right]
$$
The ${^{i-1}T_i}$ is
$$
{^{i-1}T_i}=\begin{bmatrix}
\text{cos}\theta_i & -\text{sin}\theta_i & 0 & a_{i-1} \\
\text{sin}\theta_i\text{cos}\alpha_{i-1} & \text{cos}\theta_i\text{cos}\alpha_{i-1} &
-\text{sin}\alpha_{i-1} & -d_i\text{sin}\alpha_{i-1} \\
\text{sin}\theta_i\text{sin}\alpha_{i-1} & \text{cos}\theta_i\text{sin}\alpha_{i-1} & 
\text{cos}\alpha_{i-1} & d_i\text{cos}\alpha_{i-1} \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
Using the 4th column of  $^{i-1}T_i$ for $i=4$
$$
{}^{0} P_{4ORG} 
= {^0T_1}{^1T_2}{^2T_3}
\left[\begin{array}{c}
a_{3} \\
-d_{4} {\sin\alpha_{3}} \\
d_{4} {\cos\alpha_{3}} \\
1
\end{array}\right]
= {}^{0}_{1}T \, {}^{1}_{2}T
\left[\begin{array}{c}
f_{1}(\theta_{3}) \\
f_{2}(\theta_{3}) \\
f_{3}(\theta_{3}) \\
1
\end{array}\right]
$$
where
$$
\left[\begin{array}{c}
f_{1} \\
f_{2} \\
f_{3} \\
1
\end{array}\right] = {}^{2}T_{3}
\left[\begin{array}{c}
a_{3} \\
-d_{4} {\sin\alpha_{3}} \\
d_{4} {\cos\alpha_{3}} \\
1
\end{array}\right]
$$

$$
\begin{aligned}
f_1 &= a_3 \cos\theta_3 + d_4 \sin\alpha_3 \sin\theta_3 + a_2 \\
f_2 &= a_3 \cos\alpha_2 \sin\theta_3 - d_4 \sin\alpha_3 \cos\alpha_2 \cos\theta_3 - d_4 \sin\alpha_2 \cos\alpha_3 - d_3 \sin\alpha_2 \\
f_3 &= a_3 \sin\alpha_2 \sin\theta_3 - d_4 \sin\alpha_3 \sin\alpha_2 \cos\theta_3 + d_4 \cos\alpha_2 \cos\alpha_3 + d_3 \cos\alpha_2
\end{aligned}
$$

Using the $^{0}T_1$ and $^{1}T_2$
$$
{}^{0} P_{4ORG} =
\left[\begin{array}{c}
g_1\cos\theta_1-g_2\sin\theta_1 \\
g_1\sin\theta_1+g_2\cos\theta_1 \\
g_3 \\
1
\end{array}\right]
$$
where
$$
\begin{align*}
g_1 &= \cos\theta_2 \, f_1 - \sin\theta_2 \, f_2 + a_1 \\
g_2 &= \sin\theta_2 \cos\alpha_1 \, f_1 + \cos\theta_2 \cos\alpha_1 \, f_2 - \sin\alpha_1 \, f_3 - d_2 \sin\alpha_1 \\
g_3 &= \sin\theta_2 \sin\alpha_1 \, f_1 + \cos\theta_2 \sin\alpha_1 \, f_2 + \cos\alpha_1 \, f_3 + d_2 \cos\alpha_1
\end{align*}
$$
Now we write an expression for the squared magnitude of $^0P_{4ORG}$
$$
r=x^2+y^2+z^2
$$

$$
r=g^2_1 + g^2_2 + g^2_3
$$

We have
$$
r = f_{1}^{2} + f_{2}^{2} + f_{3}^{2} + a_{1}^{2} + d_{2}^{2} + 2d_{2}f_{3} + 2a_{1}\left(\cos\theta_2 f_{1} - \sin\theta_2 f_{2}\right).
$$
We now write this equation, along with the Z-component equation, as a system of 2 equations in the form
$$
\begin{aligned}
r &= (k_1 \cos\theta_2 + k_2 \sin\theta_2) 2 a_1 + k_3 \\
z &= (k_1 \sin\theta_2 - k_2 \cos\theta_2) \sin\alpha_1 + k_4 \\
\end{aligned}
$$
where
$$
\begin{aligned}
k_1 &= f_1 \\
k_2 &= -f_2 \\
k_3 &= f_1^2 + f_2^2 + f_3^2 + a_1^2 + d_2^2 + 2 d_2 f_3 \\
k_4 &= f_3 \cos\alpha_1 + d_2 \cos\alpha_1
\end{aligned}
$$
Equation above is useful because dependence on $\theta_1$ has been eliminated and because dependence on $\theta_2$ takes a simple form.

We consider the solution for $\theta_3$ in 3 cases

+ If $a_1=0$, then $r=k_3$, where $r$ is known.
+ If $\sin\alpha_1$, then $z=k_4$, where $z$ is known.
+ Otherwise, eliminate $\sin\theta_2$ and $\cos\theta_2$ to obtain

$$
\frac{(r - k_3)^2}{4 a_1^2} + \frac{(z - k_4)^2}{\sin^2\alpha_1} = k_1^2 + k_2^2
$$

Having solved for $\theta_3$, we can solve
$$
\begin{aligned}
r &= (k_1 \cos\theta_2 + k_2 \sin\theta_2) 2 a_1 + k_3 \\
z &= (k_1 \sin\theta_2 - k_2 \cos\theta_2) \sin\alpha_1 + k_4 \\
\end{aligned}
$$
for $\theta_2$ and
$$
x = g_1\cos\theta_1-g_2\sin\theta_1 \\
y = g_1\sin\theta_1+g_2\cos\theta_1
$$
for $\theta_1$.

Having obtained $\theta_1$, $\theta_2$ and $\theta_3$, we can compute $^{0}R_{4}^{-1}|_{\theta_{4}=0}$, by which notation we mean the orientation of link frame {4} relative to the base frame when $\theta_4=0$. Because the problem was specified as given ${^{0}R_{6}}$, we can compute
$$
\left.^{4}R_{6}\right|_{\theta_{4}=0}=\left.^{0}R_{4}^{-1}\right|_{\theta_{4}=0}{^{0}R_{6}}
$$
For many manipulators, these last 3 angles can be solved for by using exactly the Z-Y-Z Euler angle solution, applied to $^{4}R_{6}|_{\theta_{4}=0}$.

There are always two solutions for these last three joints, so the total number of solutions for the manipulator will be twice the number found for the first three joints.

##### Repeatability and accuracy

Industrial robots often use **taught points**, where the manipulator is physically moved to a location and the joint angles are stored. Returning to these points relies on replaying the stored joint values, so inverse kinematics is unnecessary. The precision in returning to a taught point is defined as the **repeatability** of the manipulator.

When a goal is specified in Cartesian coordinates,  the inverse kinematics must be computed to solve for the joint angles. Such goals are called **computed points**. The precision with which a computed point can be attained is called the **accuracy** of the manipulator.

**Accuracy** is bounded by **repeatability**. It is affected by errors in the kinematic parameters (such as  Denavit–Hartenberg parameters), which cause inaccuracies in the  calculated joint angles. While repeatability is often quite good, accuracy is usually worse and varies between manipulators. Calibration  techniques can improve accuracy by estimating the specific manipulator’s kinematic parameters.

### Inverse kinematics of PUMA 560

We wish to solve
$$
\begin{aligned}
{}^{0}T_{6} &= \begin{bmatrix}
r_{11} & r_{12} & r_{13} & p_{x} \\
r_{21} & r_{22} & r_{23} & p_{y} \\
r_{31} & r_{32} & r_{33} & p_{z} \\
0 & 0 & 0 & 1
\end{bmatrix} = {}^{0}T_{1}(\theta_{1}) \; {}^{1}T_{2}(\theta_{2}) \; {}^{2}T_{3}(\theta_{3}) \; {}^{3}T_{4}(\theta_{4}) \; {}^{4}T_{5}(\theta_{5}) \; {}^{5}T_{6}(\theta_{6})
\end{aligned}
$$
Inverting $^0T_1$
$$
{[{}^{0}T_{1}(\theta_1)]}^{-1}{}^{0}T_{6}=
\begin{bmatrix}
\cos\theta_1 & \sin\theta_1 & 0 & 0 \\
-\sin\theta_1 & \cos\theta_1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
r_{11} & r_{12} & r_{13} & p_x \\
r_{21} & r_{22} & r_{23} & p_y \\
r_{31} & r_{32} & r_{33} & p_z \\
0 & 0 & 0 & 1
\end{bmatrix}
= {}^{1}T_{6}
$$
where $^1T_6$ is given by equation
$$
^{1}T_{6} = {}^{1}T_{3} \, {}^{3}T_{6} = 
\begin{bmatrix}
{}^{1}r_{11} & {}^{1}r_{12} & {}^{1}r_{13} & {}^{1}p_{x} \\
{}^{1}r_{21} & {}^{1}r_{22} & {}^{1}r_{23} & {}^{1}p_{y} \\
{}^{1}r_{31} & {}^{1}r_{32} & {}^{1}r_{33} & {}^{1}p_{z} \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
where
$$
\begin{align*}
{}^{1}r_{11} &= \cos(\theta_2+\theta_3) \bigl[ \cos\theta_4 \cos\theta_5 \cos\theta_6 - \sin\theta_4 \sin\theta_6 \bigr] - \sin(\theta_2+\theta_3) \sin\theta_5 \cos\theta_6 \\
{}^{1}r_{21} &= -\sin\theta_4 \cos\theta_5 \cos\theta_6 - \cos\theta_4 \sin\theta_6 \\
{}^{1}r_{31} &= -\sin(\theta_2+\theta_3) \bigl[ \cos\theta_4 \cos\theta_5 \cos\theta_6 - \sin\theta_4 \sin\theta_6 \bigr] - \cos(\theta_2+\theta_3) \sin\theta_5 \cos\theta_6 \\
{}^{1}r_{12} &= -\cos(\theta_2+\theta_3) \bigl[ \cos\theta_4 \cos\theta_5 \sin\theta_6 + \sin\theta_4 \cos\theta_6 \bigr] + \sin(\theta_2+\theta_3) \sin\theta_5 \sin\theta_6 \\
{}^{1}r_{22} &= \sin\theta_4 \cos\theta_5 \sin\theta_6 - \cos\theta_4 \cos\theta_6 \\
{}^{1}r_{32} &= \sin(\theta_2+\theta_3) \bigl[ \cos\theta_4 \cos\theta_5 \sin\theta_6 + \sin\theta_4 \cos\theta_6 \bigr] + \cos(\theta_2+\theta_3) \sin\theta_5 \sin\theta_6 \\
{}^{1}r_{13} &= -\cos(\theta_2+\theta_3) \cos\theta_4 \sin\theta_5 - \sin(\theta_2+\theta_3) \cos\theta_5 \\
{}^{1}r_{23} &= \sin\theta_4 \sin\theta_5 \\
{}^{1}r_{33} &= \sin(\theta_2+\theta_3) \cos\theta_4 \sin\theta_5 - \cos(\theta_2+\theta_3) \cos\theta_5 \\
{}^{1}p_{x} &= a_{2} \cos\theta_2 + a_{3} \cos(\theta_2+\theta_3) - d_{4} \sin(\theta_2+\theta_3) \\
{}^{1}p_{y} &= d_{3} \\
{}^{1}p_{z} &= -a_{3} \sin(\theta_2+\theta_3) - a_{2} \sin\theta_2 - d_{4} \cos(\theta_2+\theta_3)
\end{align*}
$$
This technique of multiplying each side of a transform equation by an inverse is often used to advantage in separating out variables in the search for a solvable equation.

Equating the (2, 4) elements from both sides of equation ${[{}^{0}T_{1}(\theta_1)]}^{-1}{}^{0}T_{6}={^{1}T_{6}}$ above
$$
^{1}p_{y} = d_{3}
$$
i.e.
$$
-\sin\theta_1 p_x + \cos\theta_1 p_y = d_3
$$
To solve an equation of this form, we make the trigonometric substitutions
$$
p_x=\rho\cos\phi \\
p_y=\rho\sin\phi
$$
where
$$
\rho = \sqrt{p^2_x+p^2_y} \\
\phi = \text {atan2} (p_y,p_x)
$$
Make substitutions
$$
\cos\theta_1 \sin\phi - \sin\theta_1 \cos\phi  = \frac{d_3}{\rho}
$$
i.e.
$$
\sin(\phi-\theta_1) = \frac{d_3}{\rho}
$$
Hence,
$$
\cos(\phi-\theta_1) = \pm \sqrt{1 - \frac{d_3^2}{\rho^2}}
$$
and so
$$
\phi-\theta_1 = \text {atan2} (\frac{d_3}{\rho}, \pm \sqrt{1 - \frac{d_3^2}{\rho^2}})
$$
Finally, the solution for $\theta_1$ may be written as
$$
\theta_1 = \text {atan2} (p_y,p_x) - 
\text {atan2} ({d_3}, \pm \sqrt{p_x^2 + p_y^2 - {d_3^2}})
$$
Now that $\theta_1$ is known, the ${[{}^{0}T_{1}(\theta_1)]}^{-1}{}^{0}T_{6}$ is known. 

If we equate both the (1,4) elements and the (3,4) elements from the two sides of ${[{}^{0}T_{1}(\theta_1)]}^{-1}{}^{0}T_{6}={^{1}T_{6}}$.
$$
\begin{align*}
{}^{1}p_{x} &= a_{2} \cos\theta_2 + a_{3} \cos(\theta_2+\theta_3) - d_{4} \sin(\theta_2+\theta_3) \\
{}^{1}p_{z} &= -a_{3} \sin(\theta_2+\theta_3) - a_{2} \sin\theta_2 - d_{4} \cos(\theta_2+\theta_3)
\end{align*}
$$
i.e.
$$
\begin{align*}
\cos\theta_1 p_x + \sin\theta_1 p_y &= a_{3}  \cos(\theta_2+\theta_3) +  a_{2} \cos\theta_2 - d_{4} \sin(\theta_2+\theta_3) \\
-p_x &= a_{3} \sin(\theta_2+\theta_3) + a_{2} \sin\theta_2 + d_{4} \cos(\theta_2+\theta_3)
\end{align*}
$$
If we square equations above and add the resulting equations, we obtain the equation that is of the same form as $-\sin\theta_1 p_x + \cos\theta_1 p_y = d_3$.
$$
a_3 \cos\theta_3 - d_4 \sin\theta_3 = K
$$
where
$$
K = \frac{p_x^2 + p_y^2 + p_z^2 - a_2^2 - a_3^2 - d_3^2 - d_4^2}{2 a_2}.
$$
Note that dependence on $\theta_1$ has been removed.
$$
\theta_3 = \text {atan2} (a_3,d_4) - 
\text {atan2} ({K}, \pm \sqrt{a_3^2 + d_4^2 - {K^2}})
$$
We can now rewrite $^{0}T_{6}={}^{0}T_{1}(\theta_{1}) \; {}^{1}T_{2}(\theta_{2}) \; {}^{2}T_{3}(\theta_{3}) \; {}^{3}T_{4}(\theta_{4}) \; {}^{4}T_{5}(\theta_{5}) \; {}^{5}T_{6}(\theta_{6})$ so that all the left-hand side is a function of only knowns and $\theta_2$:
$$
\left[{ }^{0}T_{3}(\theta_{2})\right]^{-1}{ }^{0}T_{6} = { }^{3}T_{4}(\theta_{4}){ }^{4}T_{5}(\theta_{5}){ }^{5}T_{6}(\theta_{6})
$$

$$
\begin{bmatrix}
\cos\theta_1 \cos(\theta_2+\theta_3) & \sin\theta_1 \cos(\theta_2+\theta_3) & -\sin(\theta_2+\theta_3) & -a_2 \cos\theta_3 \\
-\cos\theta_1 \sin(\theta_2+\theta_3) & -\sin\theta_1 \sin(\theta_2+\theta_3) & -\cos(\theta_2+\theta_3) & a_2 \sin\theta_3 \\
-\sin\theta_1 & \cos\theta_1 & 0 & -d_3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
r_{11} & r_{12} & r_{13} & p_x \\
r_{21} & r_{22} & r_{23} & p_y \\
r_{31} & r_{32} & r_{33} & p_z \\
0 & 0 & 0 & 1
\end{bmatrix}
= {}^{3}T_{6}
$$

where $^{3}T_{6}$ is given by the equation
$$
^{3}T_{6} =
\begin{bmatrix}
\cos\theta_4 \cos\theta_5 \cos\theta_6 - \sin\theta_4 \sin\theta_6 & 
-\cos\theta_4 \cos\theta_5 \sin\theta_6 - \sin\theta_4 \cos\theta_6 & 
-\cos\theta_4 \sin\theta_5 & 
a_{3} \\
\sin\theta_5 \cos\theta_6 & 
-\sin\theta_5 \sin\theta_6 & 
\cos\theta_5 & 
d_{4} \\
-\sin\theta_4 \cos\theta_5 \cos\theta_6 - \cos\theta_4 \sin\theta_6 & 
\sin\theta_4 \cos\theta_5 \sin\theta_6 - \cos\theta_4 \cos\theta_6 & 
\sin\theta_4 \sin\theta_5 & 
0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
Equating both the (1,4) elements and the (2,4) elements from the two sides of $\left[{ }^{0}T_{3}(\theta_{2})\right]^{-1}{ }^{0}T_{6} = { }^{3}T_{6}$
$$
\begin{align*}
\cos\theta_1 \cos(\theta_2+\theta_3) p_x + \sin\theta_1 \cos(\theta_2+\theta_3) p_y - \sin(\theta_2+\theta_3) p_z - a_2 \cos\theta_3 &= a_3 \\
-\cos\theta_1 \sin(\theta_2+\theta_3) p_x - \sin\theta_1 \sin(\theta_2+\theta_3) p_y - \cos(\theta_2+\theta_3) p_z + a_2 \sin\theta_3 &= d_4
\end{align*}
$$
These equations can be solved simultaneously for $\sin(\theta_2+\theta_3)$ and $\cos(\theta_2+\theta_3)$
$$
\begin{align*}
\sin(\theta_2+\theta_3) &= \frac{\left(-a_{3}-a_{2} \cos\theta_3\right) p_{z} + \left(\cos\theta_1 p_{x}+\sin\theta_1 p_{y}\right)\left(a_{2} \sin\theta_3 - d_{4}\right)}{p_{z}^{2}+\left(\cos\theta_1 p_{x}+\sin\theta_1 p_{y}\right)^{2}} \\
\cos(\theta_2+\theta_3) &= \frac{\left(a_{2} \sin\theta_3 - d_{4}\right) p_{z} - \left(a_{3}+a_{2} \cos\theta_3\right)\left(\cos\theta_1 p_{x}+\sin\theta_1 p_{y}\right)}{p_{z}^{2}+\left(\cos\theta_1 p_{x}+\sin\theta_1 p_{y}\right)^{2}}
\end{align*}
$$
The denominators are equal and positive, so we solve for $\theta_2+\theta_3$. 
$$
\begin{aligned}
\theta_2+\theta_3 = \operatorname{atan2}[& \left(-a_3 - a_2 \cos\theta_3\right) p_z - \left(\cos\theta_1 p_x + \sin\theta_1 p_y\right)\left(d_4 - a_2 \sin\theta_3\right), \\
& \left(a_2 \sin\theta_3 - d_4\right) p_z - \left(a_3 + a_2 \cos\theta_3\right)\left(\cos\theta_1 p_x + \sin\theta_1 p_y\right) ]
\end{aligned}
$$
According to the 4 possible combinations of solutions for $\theta_1$ and $\theta_3$, then, 4 possible solutions for are computed as
$$
\theta_2=(\theta_2+\theta_3)-\theta_3
$$
Now the entire left side of $\left[{ }^{0}T_{3}(\theta_{2})\right]^{-1}{ }^{0}T_{6} = { }^{3}T_{6}$ is known. 

Equating both the (1,3) elements and the (3,3) elements from $\left[{ }^{0}T_{3}(\theta_{2})\right]^{-1}{ }^{0}T_{6} = { }^{3}T_{6}$.
$$
\begin{aligned}
r_{13} \cos\theta_1 \cos(\theta_2+\theta_3) + r_{23} \sin\theta_1 \cos(\theta_2+\theta_3) - r_{33} \sin(\theta_2+\theta_3) &= -\cos\theta_4 \sin\theta_5, \\
-r_{13} \sin\theta_1 + r_{23} \cos\theta_1 &= \sin\theta_4 \sin\theta_5.
\end{aligned}
$$
As long as $\sin\theta_5 \neq 0$, we can solve for $\theta_4$ as
$$
\theta_4=\text{atan2}(-r_{13} \sin\theta_1 + r_{23} \cos\theta_1, -r_{13} \cos\theta_1 \cos(\theta_2+\theta_3) - r_{23} \sin\theta_1 \cos(\theta_2+\theta_3) + r_{33} \sin(\theta_2+\theta_3))
$$
When $\sin\theta_5 = 0$, the manipulator is in a singular configuration in which joint axes 4 and 6 line up and cause the same motion of the last link of the robot. If so, $\theta_4$ is chosen arbitrarily, and when $\theta_6$ is computed later, it will be computed accordingly.

We can now rewrite  $^{0}T_{6}={}^{0}T_{1}(\theta_{1}) \; {}^{1}T_{2}(\theta_{2}) \; {}^{2}T_{3}(\theta_{3}) \; {}^{3}T_{4}(\theta_{4}) \; {}^{4}T_{5}(\theta_{5}) \; {}^{5}T_{6}(\theta_{6})$ so that all the left-hand side is a function of only knowns and $\theta_4$:
$$
\left[{ }^{0}T_{4}(\theta_{4})\right]^{-1}{ }^{0}T_{6} = { }^{4}T_{5}(\theta_{5}){ }^{5}T_{6}(\theta_{6})
$$
where $^{4}T_{6}$ is given by
$$
^{4}T_{6} =
\begin{bmatrix}
\cos\theta_5 \cos\theta_6 & -\cos\theta_5 \sin\theta_6 & -\sin\theta_5 & 0 \\
\sin\theta_6 & \cos\theta_6 & 0 & 0 \\
\sin\theta_5 \cos\theta_6 & -\sin\theta_5 \sin\theta_6 & \cos\theta_5 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$
Equating both the (1,3) elements and the (3,3) elements from the two sides of $\left[{ }^{0}T_{4}(\theta_{2})\right]^{-1}{ }^{0}T_{6} = { }^{4}T_{6}$
$$
\begin{aligned}
r_{13}\left(\cos\theta_1 \cos(\theta_2+\theta_3)\cos\theta_4+\sin\theta_1\sin\theta_4\right) 
    + \\ r_{23}\left(\sin\theta_1 \cos(\theta_2+\theta_3)\cos\theta_4
    -\cos\theta_1\sin\theta_4\right) 
    - r_{33}\left(\sin(\theta_2+\theta_3) \cos\theta_4\right) 
    &= -\sin\theta_5 \\
r_{13}\left(-\cos\theta_1 \sin(\theta_2+\theta_3)\right)
    + r_{23}\left(-\sin\theta_1 \sin(\theta_2+\theta_3)\right) 
    + r_{33}\left(-\cos(\theta_2+\theta_3)\right) 
    &= \cos\theta_5
\end{aligned}
$$
Hence, we can solve for $\theta_5$ as
$$
\theta_5 = \text{atan2}(\sin\theta_5,\cos\theta_5)
$$
Applying the same method one more time 
$$
\left({ }^{0}T_{5}\right)^{-1}{ }^{0}T_{6} = {^{5}T_{6}(\theta_{6})}
$$
Equating both the (3,1) elements and the (1,1) elements from the two sides of $\left[{ }^{0}T_{4}(\theta_{4})\right]^{-1}{ }^{0}T_{6} = { }^{4}T_{6}$
$$
\theta_6 = \text{atan2}(\sin\theta_6,\cos\theta_6)
$$
For each of the 4 solutions computed above, we obtain the flipped solution by
$$
\begin{array}{l}
\theta_{4}^{\prime} = \theta_{4} + 180^{\circ} \\
\theta_{5}^{\prime} = -\theta_{5} \\
\theta_{6}^{\prime} = \theta_{6} + 180^{\circ}
\end{array}
$$
After all eight solutions have been computed, some (or even all) of them might have to be discarded because of joint-limit violations. Of any remaining valid solutions, usually the one closest to the present manipulator configuration is chosen.

