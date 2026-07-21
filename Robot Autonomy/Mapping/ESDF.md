[toc]

# EDF

##### Definition

**Euclidean Distance Field** (EDF) is a scalar field that stores the Euclidean distance from each point to the nearest obstacle. EDF is usually computed from an occupancy grid by Euclidean Distance Transform (EDT)

For a continuous point $\boldsymbol{x} \in \mathbb{R}^{3}$, EDF is defined as

$$
D(\boldsymbol{x})
=
\min_{\boldsymbol{o} \in \mathcal{O}}
\left\|
\boldsymbol{x} - \boldsymbol{o}
\right\|_2
$$

where $\mathcal{O}$ denotes the obstacle set.

For a voxel grid, if $\boldsymbol{x}_{\boldsymbol{i}}$ is the center of voxel $\boldsymbol{i}$, then

$$
D(\boldsymbol{i})
=
\min_{\boldsymbol{j} \in \mathcal{I}_{\mathrm{occ}}}
\left\|
\boldsymbol{x}_{\boldsymbol{i}}
-
\boldsymbol{x}_{\boldsymbol{j}}
\right\|_2
$$

where $\mathcal{I}_{\mathrm{occ}}$ is the set of occupied voxel indices.

$D(\boldsymbol{x}) = 0$ means on obstacle surfaces.

# ESDF

##### Definition

**Euclidean Signed Distance Field ** (ESDF) is a spatial map in which every voxel stores the signed Euclidean distance to the nearest obstacle surface.

In practice, an ESDF map is usually stored on a voxel grid. Let $r$ be the **voxel resolution**, $\boldsymbol{i} \in \mathbb{Z}^3$ be a **voxel index**, and $\boldsymbol{x}_{\boldsymbol{i}}$ be the **center position** of that voxel

$$
\boldsymbol{x}_{\boldsymbol{i}} = r\boldsymbol{i}
$$

Let $\mathcal{I}_{\mathrm{occ}}$ be the set of occupied voxel indices. The unsigned Euclidean distance at voxel $\boldsymbol{i}$ can be written as

$$
d(\boldsymbol{i}) = \min_{\boldsymbol{j} \in \mathcal{I}_{\mathrm{occ}}}
\left\| \boldsymbol{x}_{\boldsymbol{i}} - \boldsymbol{x}_{\boldsymbol{j}} \right\|_2
$$

The **signed voxel distance** is then

$$
\phi(\boldsymbol{i}) = \sigma(\boldsymbol{i}) d(\boldsymbol{i})
$$

where

$$
\sigma(\boldsymbol{i}) =
\begin{cases}
+1, & \boldsymbol{i} \in \mathcal{I}_{\mathrm{free}} \\
-1, & \boldsymbol{i} \in \mathcal{I}_{\mathrm{occ}}
\end{cases}
$$

##### Closest Obstacle

For efficient updates and gradient computation, an ESDF map may store not only the distance value but also the nearest obstacle index

$$
\boldsymbol{b}(\boldsymbol{i}) = \arg\min_{\boldsymbol{j} \in \mathcal{I}_{\mathrm{occ}}}
\left\| \boldsymbol{x}_{\boldsymbol{i}} - \boldsymbol{x}_{\boldsymbol{j}} \right\|_2
$$

Then the distance can be computed by

$$
d(\boldsymbol{i}) =
\left\| \boldsymbol{x}_{\boldsymbol{i}} - \boldsymbol{x}_{\boldsymbol{b}(\boldsymbol{i})} \right\|_2
$$

Here $\boldsymbol{b}(\boldsymbol{i})$ is a vector-valued index, while $d(\boldsymbol{i})$ and $\phi(\boldsymbol{i})$ are scalar fields.

##### Gradient of the ESDF

The ESDF gradient points approximately away from the nearest obstacle in free space. If the nearest obstacle point of $\boldsymbol{x}$ is $\boldsymbol{o}^{\ast}$, then for a smooth region where the nearest obstacle is unique,

$$
\nabla \phi(\boldsymbol{x}) \approx
\frac{\boldsymbol{x} - \boldsymbol{o}^{\ast}}
{\left\| \boldsymbol{x} - \boldsymbol{o}^{\ast} \right\|_2}
$$

On a voxel grid, the gradient can be approximated by finite differences. For example, along the $x$ direction,

$$
\frac{\partial \phi}{\partial x}(\boldsymbol{i})
\approx
\frac{\phi(\boldsymbol{i} + \boldsymbol{e}_x) - \phi(\boldsymbol{i} - \boldsymbol{e}_x)}{2r}
$$

where $\boldsymbol{e}_x = [1,0,0]^\mathsf{T}$. Similar expressions are used for the $y$ and $z$ directions.

##### Interpolation

The interpolation allows the planner to query smooth approximate distance and gradient values along a continuous trajectory. Therefore, the ESDF value at an arbitrary point $\boldsymbol{x}$ is commonly obtained by trilinear interpolation from the neighboring voxel values. 

Let the query point be
$$
\boldsymbol{x} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
and let the lower-left-back grid sample of the voxel cell containing $\boldsymbol{x}$ be
$$
\boldsymbol{x}_{000} = \begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix}
$$
The local normalized coordinates of $\boldsymbol{x}$ inside this voxel cell are defined as
$$
u = \frac{x - x_0}{r}	\\

v = \frac{y - y_0}{r}	\\

w = \frac{z - z_0}{r}	\\
$$
Here,
$$
u, v, w \in [0,1]
$$
the query point $\boldsymbol{x}$ is surrounded by 8 neighboring ESDF samples. The trilinear interpolation result is written as
$$
\phi(\boldsymbol{x}) = \sum_{i=0}^{1} \sum_{j=0}^{1} \sum_{k=0}^{1} \omega_{ijk} \phi_{ijk}
$$
where $\phi_{ijk}$ is the index of the 8 neighboring voxel and $\omega_{ijk}$ is the interpolation weight of the corresponding voxel corner.
$$
\omega_{0}^{x}=1-u,\quad\omega_{1}^{x}=u\\

\omega_{0}^{y}=1-v,\quad\omega_{1}^{y}=v\\

\omega_{0}^{z}=1-w,\quad\omega_{1}^{z}=w
$$
Therefore,
$$
\omega_{ijk} = \omega_i^x \omega_j^y \omega_k^z
$$

$$
\sum_{i=0}^{1} \sum_{j=0}^{1} \sum_{k=0}^{1} \omega_{ijk}=1
$$
