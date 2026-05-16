[toc]

# Robotics

Robotics are split into 4 major subdisciplines: mechanical manipulation, locomotion, computer vision, and artificial intelligence.

# Spatial descriptions and transformations

In order to **describe the position and orientation** of a body in space, we attach a coordinate system, or **frame**, rigidly to the object. We often think of **transforming** the description of these attributes of a body from one frame to another.

### Descriptions

##### Position

$^AP$ represents a **position** vector written in coordinate system {$A$}.
$$
^AP=\left[ \begin{matrix}
   p_{x}  \\
   p_{y}  \\
   p_{z} \\
\end{matrix} \right]
$$

##### Orientation

In order to describe the **orientation** of a body, we will attach a coordinate system {$B$} to the body. Unit vectors ${X}_{B}$ , ${Y}_{B}$ and ${Z}_{B}$ are the principal directions of coordinate system {$B$}.
$$
{{R}_{B}}=\left[ \begin{matrix}
   {{X}_{B}} & {{Y}_{B}} & {{Z}_{B}}  \\
\end{matrix} \right]
$$
$^{A}{R}_{B}$ is a **rotation matrix** that describes {$B$} relative to {$A$}. 
$$
^{A}{{R}_{B}}=\left[ \begin{matrix}
   ^{A}{{X}_{B}} & ^{A}{{Y}_{B}} & ^{A}{{Z}_{B}}  \\
\end{matrix} \right]
$$

$$
{{R}_{A}}{{\cdot }^{A}}{{R}_{B}}={{R}_{B}}
$$

The components of any vector are simply the projections of that vector onto the unit directions of its reference frame. Hence, each component of $^{A}{{R}_{B}}$ can be written as the dot product of a pair of unit vectors.
$$
^{A}{{R}_{B}}=R_{A}^{-1}\cdot {{R}_{B}}=\left[ \begin{matrix}
   X_{A}^{\text{T}}  \\
   Y_{A}^{\text{T}}  \\
   Z_{A}^{\text{T}}  \\
\end{matrix} \right]\left[ \begin{matrix}
   {{X}_{B}} & {{Y}_{B}} & {{Z}_{B}}  \\
\end{matrix} \right]=\left[ \begin{matrix}
   {{X}_{B}}\cdot {{X}_{A}} & {{Y}_{B}}\cdot {{X}_{A}} & {{Z}_{B}}\cdot {{X}_{A}}  \\
   {{X}_{B}}\cdot {{Y}_{A}} & {{Y}_{B}}\cdot {{Y}_{A}} & {{Z}_{B}}\cdot {{Y}_{A}}  \\
   {{X}_{B}}\cdot {{Z}_{A}} & {{Y}_{B}}\cdot {{Z}_{A}} & {{Z}_{B}}\cdot {{Z}_{A}}  \\
\end{matrix} \right]
$$

The dot product of two unit vectors yields the cosine of the angle between them, so the elements on $^{A}{R}_{B}$ are called **direction cosine**.

The rows of the matrix ${^AR_B}$ are the unit vectors of {$A$} expressed in {$B$}.
$$
{^AR_B^\text{T}}={^AR_B}=\left[ \begin{matrix}
   ^BX_{A}^{\text{T}}  \\
   ^BY_{A}^{\text{T}}  \\
   ^BZ_{A}^{\text{T}}  \\
\end{matrix} \right]
$$

 This suggests that the inverse of a rotation matrix is equal to its transpose.
$$
^{A}{{R}_{B}^\text{T}}\cdot{^{A}{{R}_{B}}}=\left[ \begin{matrix}
   ^AX_{B}^{\text{T}}  \\
   ^AY_{B}^{\text{T}}  \\
   ^AZ_{B}^{\text{T}}  \\
\end{matrix} \right]\left[ \begin{matrix}
   {^A{X}_{B}} & {^A{Y}_{B}} & {^A{Z}_{B}}  \\
\end{matrix} \right]=I_3
$$

From linear algebra, the inverse of a matrix with orthonormal columns is equal to its transpose.
$$
^AR_B={^BR_A^{-1}}={^AR_B^\text{T}}
$$

##### Frame

**Frame** is a set of 4 vectors giving position and orientation information, used as a description of one coordinate system relative to another. One vector locates the position and 3 more describe its orientation.

The description of a frame can be thought of as a position vector and a rotation matrix. A frame
is a coordinate system where we give the orientation amd a position vector which locates its origin relative to some other embedding frame.

Positions could be represented by a frame whose rotation-matrix part is the identity matrix and whose position-vector part locates the point being described. Likewise, an orientation could be represented by a frame whose position-vector part was the zero vector.

For example, frame is described by $^AR_B$ and $^AP_{BORG}$  where $^AP_{BORG}$ is the vector that locates the origin of the frame {$B$}.
$$
\{B\}=\{^AR_B,{^AP_{BORG}}\}
$$

### Mappings

**Mapping** means changing descriptions from fame to frame.

##### Translated frames

Only in the special case of equivalent orientations may we add vectors that are defined in terms of different frames.
$$
^{A}P={^{B}P}+^{A}P_{BORG}
$$
##### Rotated frames

The columns of a rotation matrix $^{A}{R}_{B}$ all have unit magnitude, and are orthogonal. Therefore, the columns of $^{A}{R}_{B}$ represent the unit direction vectors of frame {$B$} expressed in frame {$A$}. The rows of $^{A}{R}_{B}$ ( .i.e the columns of $^{A}R_B^\text{T}$ ) represent the direction cosines of frame {$A$} expressed in frame {$B$}.

In the case of the coincident origins for two frames, we note that the components of position vector $^AP$ is the projection of $^AP$ onto the unit directions of its frame {$A$}.
$$
^{A}P={^{A}{{R}_B}}\cdot{^{B}P}=
\begin{bmatrix}
   ^A{X}_{B}\cdot{^{B}P}  \\
   ^A{Y}_{B}\cdot{^{B}P}  \\
   ^A{Z}_{B}\cdot{^{B}P}  \\
\end{bmatrix}
=\begin{bmatrix}
   ^Ap_{x}  \\
   ^Ap_{y}  \\
   ^Ap_{z} \\
\end{bmatrix}
$$

##### General frames

A general transformation mapping of a vector from its description in one frame to a description in a second frame.
$$
^{A}P={^{A}{{R}_B}}\cdot{^{B}P}+{^{A}P_{BORG}}
$$
We define a 4 x 4 matrix operator and use 4 x 1 position vectors:
$$
^{A}P={^{A}{{T}_B}}\cdot{^{B}P}
$$

$$
\begin{bmatrix}
{^{A}P} \\
1
\end{bmatrix}=
\begin{bmatrix}
{^{A}R_B} & {^{A}P_{BORG}} \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
{^{B}P} \\
1
\end{bmatrix}=
\begin{bmatrix}
{^{A}R_B}{^{B}P}+{^{A}P_{BORG}} \\
1
\end{bmatrix}
$$

The 4 x 4 matrix ${^{A}{{T}_B}}$ is called a **homogeneous transform**. For our purposes, it can be regarded as a construction used to cast the rotation and translation of the general transform into a single matrix form.

The description of frame {$B$} relative to {$A$} is ${^{A}{{T}_B}}$.

### Transformations

#### Operators

##### Translational operators

A vector ${^AP_1}$ is translated by a vector ${^AQ}$. The result of the operation is a new vector ${^AP_2}$, calculated as
$$
{^AP_2}={^AP_1}+{^AQ}
$$

$$
{^AP_2}={D_Q{(q)}}{^AP_1}
$$

where $q$ is the signed magnitude of the translation along the vector direction $Q$. The $D_Q$ operator may be thought of as a homogeneous transform of a special simple form:
$$
D_Q(q)=
\begin{bmatrix}
1 & 0 & 0 & q_x \\
0 & 1 & 0 & q_y \\
0 & 0 & 1 & q_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

##### Rotational operators

The rotation matrix that rotates vectors through some rotation, $R$ , is the same as the rotation matrix that describes a frame rotated by $R$ relative to the reference frame. We define notation ${R_K{(\theta)}}$ for a rotational operator.
$$
{^AP_2}={R_K{(\theta)}}{^AP_1}
$$
$$
R_{k1}(\alpha)\cdot R_{k2}(\beta)\neq R_{k1}(\alpha)\cdot R_{k2}(\beta) \qquad \text{except} \ k_1=k_2
$$

${R_K{(\theta)}}$ performs a rotation about the axis direction $K$ by $\theta$ degrees.
$$
R_x(\theta)=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \text{cos}\theta & -\text{sin}\theta & 0 \\
0 & \text{sin}\theta & \text{cos}\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
R_y(\theta)=
\begin{bmatrix}
\text{cos}\theta & 0 & \text{sin}\theta & 0 \\
0 & 1 & 0 & 0 \\
-\text{sin}\theta & 0 & \text{cos}\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
R_z(\theta)=
\begin{bmatrix}
\text{cos}\theta & -\text{sin}\theta & 0 & 0 \\
\text{sin}\theta & \text{cos}\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

##### Transformation operators

The operator $T$ rotates and translates a vector ${^AP_1}$ to compute a new vector:
$$
{^AP_2}=T{^AP_1}
$$
A transform is usually thought of as being in the form of a homogeneous transform with general rotation-matrix and position-vector parts.
$$
T=\begin{bmatrix}
n & o & a & p \\
0 & 0 & 0 & 1
\end{bmatrix}=\begin{bmatrix}
n_x & o_x & a_x & p_x \\
n_y & o_y & a_y & p_y \\
n_z & o_z & a_z & p_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
approach=\left[ \begin{matrix}
  	a_x  \\
   	a_y  \\
   	a_z  \\
\end{matrix} \right] \qquad
orientation=\left[ \begin{matrix}
  	o_x  \\
   	o_y  \\
   	o_z  \\
\end{matrix} \right] \qquad
normal=\left[ \begin{matrix}
  	n_x  \\
   	n_y  \\
   	n_z  \\
\end{matrix} \right]
$$

$$
T^{-1}=\begin{bmatrix}
n_x & n_y & n_z & -p \cdot n \\
o_x & o_y & o_z & -p \cdot o \\
a_x & a_y & a_z & -p \cdot a \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Three interpretations of this homogeneous transform:

+ It is **a description of a frame**. ${^AT_B}$ describes the frame {$B$} relative to the frame {$A$}. The columns of ${^AR_B}$ are unit vectors defining the directions of the principal axes of {$B$} , and $^AP_{BORG}$ locates the position of the origin of {$B$}.
+ It is **a transform mapping**. ${^AT_B}$ maps $^BP$ to $^AP$.
+ It is **a transform operator**. $T$ operates on $^AP_1$ to create $^AP_2$.

The frame and transform will both be used to refer to a position vector plus an orientation. Frame refers to pose as a description, and transform implies its function as a mapping or operator.

#### Transformation arithmetic

##### Compound transformations

A transformation $A$ by a second transformation $B$

Postmultiplying of $B$ relative to $A$ applies the transformation with respect to the frame of $A$.
$$
T=A\cdot B
$$
Premultiplying of $B$ relative to $A$ applies the transformation with respect to the base coordinate frame.
$$
T=B\cdot A
$$
Frame {$C$} is relative to frame {$B$}, and frame {$B$} is relative to frame ($A$}. We can transform $^CP$ into $^AP$ as
$$
{^AP}={^AT_B}{^BT_C}{^CP}
$$

$$
{^AT_C}=\begin{bmatrix}
{^{A}R_B}{^{B}R_C} & {^{A}R_B}{^{B}P_{CORG}}+{^{A}P_{BORG}} \\
0 & 1
\end{bmatrix}
$$

##### Inverting a transform

To find ${^BT_A}$, we must compute ${^BR_A}$ and ${^{B}P_{AORG}}$ from  ${^AR_B}$ and ${^{A}P_{BORG}}$
$$
{^{B}R_A}={^{A}R_B^\text{T}}
$$
Change the description of ${^AP_{BORG}}$ into {$B$}:
$$
^B({^AP_{BORG}})={^BR_A}{^AP_{BORG}}+{^BP_{AORG}}=0
$$

$$
{^BP_{AORG}}=-{^BR_A}{^AP_{BORG}}=-{^{A}R_B^\text{T}}{^{A}P_{BORG}}
$$

Notation ${^BT_A}$:

$$
{^BT_A}=
\begin{bmatrix}
{^{A}R_B^\text{T}} & -{^{A}R_B^\text{T}}{^{A}P_{BORG}} \\
0 & 1
\end{bmatrix}
$$

$$
{^BT_A}={^AT_B^{-1}}
$$

#### Transform equations

A frame {$D$} can be expressed as products of transformations in two different ways.
$$
{^UT_D}={^UT_A}{^AT_D}
$$

$$
{^UT_D}={^UT_B}{^BT_C}{^CT_D}
$$

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/59ad0532-7b5c-4e5d-bf3b-55f0d3a686e2.png" alt="59ad0532-7b5c-4e5d-bf3b-55f0d3a686e2" style="zoom:66%;" />

Construct a transform equation:
$$
{^UT_A}{^AT_D}={^UT_B}{^BT_C}{^CT_D}
$$
Transform equations can be used to solve for transforms in the case of $n$ unknown transforms and $n$ transform equations.
$$
{^BT_C}={^UT_B^{-1}}{^UT_A}{^AT_D}{^CT_D^{-1}}
$$
If an arrow points the opposite way in a chain of transforms, we simply compute its inverse first.
$$
{^UT_D}={^UT_B}{^BT_C}{^CT_D}
$$

$$
{^UT_D}={^UT_B}{^CT_B^{-1}}{^CT_D}
$$

### Three angle rotation

##### RPY angle

Start with the frame coincident with a known frame {$A$}. Rotate {$B$} first about $X_A$ by an angle $\gamma$, then about $Y_A$ by an angle $\beta$ , and about $Z_A$ by an angle $\alpha$. Each of the 3 rotations takes place about an axis in the fixed reference frame {$A$}.

This convention is referred to as X-Y-Z fixed angles, or **roll, pitch, yaw angles**.
$$
^AR_{BXYZ}(\gamma,\beta,\alpha)=R_{Z}(\alpha)R_{Y}(\beta)R_{X}(\gamma)
 \left.=\left[
\begin{array}
{ccc}{{\text {cos}}\alpha} & {-{\text {sin}}\alpha} & {0} \\
{{\text {sin}}\alpha} & {{\text {cos}}\alpha} & {0} \\
{0} & {0} & {1}
\end{array}\right.\right]
\begin{bmatrix}
{{\text {cos}}\beta} & {0} & {{\text {sin}}\beta} \\
{0} & {1} & {0} \\
{-{\text {sin}}\beta} & {0} & {{\text {cos}}\beta}
\end{bmatrix}
\begin{bmatrix}
{1} & {0} & {0} \\
{0} & {{\text {cos}}\gamma} & {-{\text {sin}}\gamma} \\
{0} & {{\text {sin}}\gamma} & {{\text {cos}}\gamma}
\end{bmatrix}
$$

$$
^AR_{BXYZ}(\gamma,\beta,\alpha)
 =
 \begin{bmatrix}
{\text {cos}}\alpha{\text {cos}}\beta & {\text {cos}}\alpha{\text {sin}}\beta{\text {sin}}\gamma-{\text {sin}}\alpha{\text {cos}}\gamma & {\text {cos}}\alpha{\text {sin}}\beta{\text {cos}}\gamma+{\text {sin}}\alpha{\text {sin}}\gamma \\
{\text {sin}}\alpha{\text {cos}}\beta & {\text {sin}}\alpha{\text {sin}}\beta{\text {sin}}\gamma+{\text {cos}}\alpha{\text {cos}}\gamma & {\text {sin}}\alpha{\text {sin}}\beta{\text {cos}}\gamma-{\text {cos}}\alpha{\text {sin}}\gamma \\
{-{\text {sin}}\beta} & {\text {cos}}\beta{\text {sin}}\gamma & {{\text {cos}}\beta}{\text {cos}}\gamma
\end{bmatrix}
$$



##### Z-Y-X Euler angle

Start with the frame coincident with a known frame {$A$}. Rotate {$B$} first about $Z_B$ by an angle $\alpha$, then about $Y_B$ by an angle $\beta$ , and about $X_B$ by an angle $\gamma$.

In this representation, each rotation is performed about an axis of the moving system {$B$} rather than one of the fixed reference {$A$}.
$$
^AR_{BZ^{\prime}Y^{\prime}X^{\prime}}(\alpha,\beta,\gamma)
=R_{Z}(\alpha)R_{Y}(\beta)R_{X}(\gamma)
 \left.=\left[
\begin{array}
{ccc}{{\text {cos}}\alpha} & {-{\text {sin}}\alpha} & {0} \\
{{\text {sin}}\alpha} & {{\text {cos}}\alpha} & {0} \\
{0} & {0} & {1}
\end{array}\right.\right]
\begin{bmatrix}
{{\text {cos}}\beta} & {0} & {{\text {sin}}\beta} \\
{0} & {1} & {0} \\
{-{\text {sin}}\beta} & {0} & {{\text {cos}}\beta}
\end{bmatrix}
\begin{bmatrix}
{1} & {0} & {0} \\
{0} & {{\text {cos}}\gamma} & {-{\text {sin}}\gamma} \\
{0} & {{\text {sin}}\gamma} & {{\text {cos}}\gamma}
\end{bmatrix}
$$

$$
^AR_{BZ^{\prime}Y^{\prime}X^{\prime}}(\alpha,\beta,\gamma)=
 \begin{bmatrix}
{\text {cos}}\alpha{\text {cos}}\beta & {\text {cos}}\alpha{\text {sin}}\beta{\text {sin}}\gamma-{\text {sin}}\alpha{\text {cos}}\gamma & {\text {cos}}\alpha{\text {sin}}\beta{\text {cos}}\gamma+{\text {sin}}\alpha{\text {sin}}\gamma \\
{\text {sin}}\alpha{\text {cos}}\beta & {\text {sin}}\alpha{\text {sin}}\beta{\text {sin}}\gamma+{\text {cos}}\alpha{\text {cos}}\gamma & {\text {sin}}\alpha{\text {sin}}\beta{\text {cos}}\gamma-{\text {cos}}\alpha{\text {sin}}\gamma \\
{-{\text {sin}}\beta} & {\text {cos}}\beta{\text {sin}}\gamma & {{\text {cos}}\beta}{\text {cos}}\gamma
\end{bmatrix}
$$

Three rotations taken about fixed axes yield the same final orientation as the same three rotations taken in opposite order about the axes of the moving frame.
$$
^AR_{BZ^{\prime}Y^{\prime}X^{\prime}}(\alpha,\beta,\gamma)=
\begin{bmatrix}
{r_{11}} & {r_{12}} & {r_{13}} \\
{r_{21}} & {r_{22}} & {r_{23}} \\
{r_{31}} & {r_{32}} & {r_{33}}
\end{bmatrix}
$$

$$
\beta=\text {atan2}(-r_{31},\sqrt{r^2_{11}+r^2_{21}})
$$

$$
\alpha=\text{atan2}({r_{21}/\text{cos}\beta},{r_{11}/\text{cos}\beta})
$$

$$
\gamma=\text{atan2}({r_{32}/\text{cos}\beta},{r_{33}/\text{cos}\beta})
$$

where $\text{atan2} (y,x)$ is a two-argument arc tangent function:
$$
\text{atan2}{(y, x)} = 
\left\{
\begin{array}{ll}
\arctan\left(\dfrac{y}{x}\right) & x > 0 \\
\arctan\left(\dfrac{y}{x}\right) + \pi & y \geq 0, \; x < 0 \\
\arctan\left(\dfrac{y}{x}\right) - \pi & y < 0, \; x < 0 \\
+\dfrac{\pi}{2} & y > 0, \; x = 0 \\
-\dfrac{\pi}{2} & y < 0, \; x = 0 \\
\text{undefined} & y = 0, \; x = 0
\end{array}
\right.
$$
$\text{atan2} (y,x)$ computes $\text{arctan}$ but uses the signs of both $x$ and $y$ to identify the **quadrant** in which
the resulting angle lies.

##### Z-Y-Z Euler angle

Start with the frame coincident with a known frame {$A$}. Rotate {$B$} first about $Z_B$ by an angle $\alpha$, then about $Y_B$ by an angle $\beta$ , and about $X_b$ by an angle $\gamma$.
$$
^AR_{BZ^{\prime}Y^{\prime}Z^{\prime}}(\alpha,\beta,\gamma)=
 \begin{bmatrix}
{\text {cos}}\alpha{\text {cos}}\beta{\text {cos}}\gamma-{\text {sin}}\alpha{\text {sin}}\gamma & -{\text {cos}}\alpha{\text {cos}}\beta{\text {sin}}\gamma-{\text {sin}}\alpha{\text {cos}}\gamma & {\text {cos}}\alpha{\text {sin}}\beta \\
{\text {sin}}\alpha{\text {cos}}\beta{\text {cos}}\gamma+{\text {cos}}\alpha{\text {sin}}\gamma & -{\text {sin}}\alpha{\text {cos}}\beta{\text {sin}}\gamma+{\text {cos}}\alpha{\text {cos}}\gamma & {\text {sin}}\alpha{\text {sin}}\beta \\
{-{\text {sin}}\beta}{\text {cos}}\gamma & {\text {sin}}\beta{\text {sin}}\gamma & {{\text {cos}}\beta}
\end{bmatrix}
$$

$$
^AR_{BZ^{\prime}Y^{\prime}Z^{\prime}}(\alpha,\beta,\gamma)=
\begin{bmatrix}
{r_{11}} & {r_{12}} & {r_{13}} \\
{r_{21}} & {r_{22}} & {r_{23}} \\
{r_{31}} & {r_{32}} & {r_{33}}
\end{bmatrix}
$$

$$
\beta=\text {atan2}({\sqrt{r^2_{31}+r^2_{32}}},{r_{33}})
$$

$$
\alpha=\text{atan2}({r_{23}/\text{sin}\beta},{r_{13}/\text{sin}\beta})
$$

$$
\gamma=\text{atan2}({r_{32}/\text{sin}\beta},-{r_{31}/\text{sin}\beta})
$$

##### Equivalent angle-axis representation

Given that the rotation matrix relative to the frame {$A$} is $C$. Vector $K$ is the $z$ axis direction vector of frame {$C$}, and an arbitrary vector in frame {$A$}.
$$
C=\begin{bmatrix}
{n_{x}} & {o_{x}} & {a_{x}} \\
{n_{y}} & {o_{y}} & {a_{y}} \\
{n_{z}} & {o_{z}} & {a_{z}}
\end{bmatrix}
$$

$$
K=\begin{bmatrix}
{k_x} \\
{k_y} \\
{k_z}
\end{bmatrix}=\begin{bmatrix}
{a_x} \\
{a_y} \\
{a_z}
\end{bmatrix}
$$

Given the frame $B$, then we find a frame $X$, s.t.
$$
B=CX
$$

$$
X=C^{-1}B
$$

Rotating $B$ about $K$ is equivalent to rotating $X$ about the $z$ axis of frame {$C$}. 
$$
R_K(\theta)B=CR_z(\theta)X=CR_z(\theta)C^{-1}B
$$

$$
R_K(\theta)=CR_z(\theta)C^{-1}
$$

$$
R_K(\theta)=\begin{bmatrix}
{n_{x}} & {o_{x}} & {a_{x}} \\
{n_{y}} & {o_{y}} & {a_{y}} \\
{n_{z}} & {o_{z}} & {a_{z}}
\end{bmatrix}\begin{bmatrix}
\text{cos}\theta & -\text{sin}\theta & 0 \\
\text{sin}\theta & \text{cos}\theta & 0 \\
0 & 0 & 1 \\
\end{bmatrix}\begin{bmatrix}
n_x & n_y & n_z \\
o_x & o_y & o_z \\
a_x & a_y & a_z 
\end{bmatrix}
$$

Unit direction vector $K$ is called the **equivalent axis** of a finite rotation. A general orientation of {$B$} relative to {$A$} may be written as $^AR_B(K,\theta)$ or $R_K(\theta)$, and will be called the equivalent angle-axis representation.

The **equivalent rotation matrix** is
$$
R_K(\theta)=\begin{bmatrix}
{k_xk_x\text{vers}\theta+\text{cos}\theta} & 
{k_xk_y\text{vers}\theta-k_z\text{sin}\theta} & 
{k_xk_z\text{vers}\theta+k_y\text{sin}\theta} \\
{k_xk_y\text{vers}\theta+k_z\text{sin}\theta} & 
{k_yk_y\text{vers}\theta+\text{cos}\theta} & 
{k_yk_z\text{vers}\theta-k_x\text{sin}\theta} \\
{k_xk_z\text{vers}\theta-k_y\text{sin}\theta} & 
{k_yk_z\text{vers}\theta+k_x\text{sin}\theta} & 
{k_zk_z\text{vers}\theta+\text{cos}\theta}
\end{bmatrix}
$$
where $\text{vers}\theta=1-\text{cos}\theta$. The sign of $\theta$ is determined by the right-hand rule, with the thumb pointing along the positive sense of $^AK$.

The equivalent rotation matrix converts from angle-axis representation to rotation-matrix representation.
$$
\theta=\text{arccos}(\frac{r_{11}+r_{22}+r_{33}-1}{2})
$$

$$
K=\frac{1}{2\text{sin}\theta}
\begin{bmatrix}
{r_{32}-r_{23}} \\
{r_{13}-r_{31}} \\
{r_{21}-r_{12}}
\end{bmatrix}
$$

##### Euler parameter

Another representation of orientation is by means of four numbers called the **Euler parameters**. In terms of the equivalent axis $K=\begin{bmatrix}k_x & k_y & k_z\end{bmatrix}^{\text{T}}$ and the equivalent angle $\theta$, the Euler parameters are given by
$$
\epsilon_1=k_x{\text{sin}{\frac{\theta}2}}
$$

$$
\epsilon_2=k_y{\text{sin}{\frac{\theta}2}}
$$

$$
\epsilon_3=k_z{\text{sin}{\frac{\theta}2}}
$$

$$
\epsilon_4={\text{cos}{\frac{\theta}2}}
$$

These four quantities are not independent
$$
\epsilon_1^2+\epsilon_2^2+\epsilon_3^2+\epsilon_4^2=1
$$
An orientation can be visualized as a point on a unit hypersphere in four-dimensional space.

Sometimes, the Euler parameters are viewed as a 3 x 1 vector plus a scalar. However, as a 4 x 1 vector, the Euler parameters are known as a **unit quaternion**.

The rotation matrix $R_\epsilon$ that is equivalent to a set of Euler parameters is
$$
R_\epsilon=\begin{bmatrix}
1-2\epsilon^2_2-2\epsilon^2_3 & 
2(\epsilon_1\epsilon_2-\epsilon_3\epsilon_4) & 
2(\epsilon_1\epsilon_3+\epsilon_2\epsilon_4) \\
2(\epsilon_1\epsilon_2+\epsilon_3\epsilon_4) & 
1-2\epsilon^2_1-2\epsilon^2_3 & 
2(\epsilon_2\epsilon_3-\epsilon_1\epsilon_4) \\
2(\epsilon_1\epsilon_3-\epsilon_2\epsilon_4) & 2(\epsilon_2\epsilon_3+\epsilon_1\epsilon_4) & 
1-2\epsilon^2_1-2\epsilon^2_2
\end{bmatrix}
$$
Given a rotation matrix, the equivalent Euler parameters are
$$
\epsilon_1=\frac{r_{32}-r_{23}}{4\epsilon_4}
$$

$$
\epsilon_2=\frac{r_{13}-r_{31}}{4\epsilon_4}
$$

$$
\epsilon_3=\frac{r_{21}-r_{12}}{4\epsilon_4}
$$

$$
\epsilon_4=\frac{1}{2}\sqrt{1+r_{11}+r_{22}+r_{33}}
$$

### Transformation of free vectors

Two vectors are equal if they have the same dimensions, magnitude, and direction. 

The **line vector** refers to a vector that is dependent on its **line of action**, along with direction and magnitude, for causing its effects. The effects of a **force vector** depend upon its line of action (or point of application), so it would then be considered a line vector. 

A **free vector** refers to a vector that may be positioned anywhere in space without loss or change of meaning, provided that magnitude and direction are preserved. 

In the case of a free vector, all counts is the **magnitude** and **direction**. Only the rotation matrix relating the two systems is used in transforming. The relative locations of the origins do not enter into the calculation.

For example, a pure **moment vector** is always a free vector. If we have a moment vector $^BN$ that is known in terms of {$B$}, then we calculate the same moment in terms of frame {$A$} as
$$
^AN={^AR_B}{^BN}
$$
The **velocity vector** is a free vector. A velocity vector written in {$B$}, $^BV$, is written in {$A$} as
$$
^AV={^AR_B}{^BV}
$$

