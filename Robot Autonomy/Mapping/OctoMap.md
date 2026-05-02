# OctoMap

[toc]

##### Overview

OctoMap is a 3D probabilistic occupancy mapping framework that stores **free**, **occupied**, and **unknown** space using an **octree**. Each **voxel** maintains an **occupancy probability**, which is updated through sensor-ray observations in log-odds form. 

The octree structure makes the map compact and multi-resolution, while probabilistic updates make it robust to noisy measurements.

##### Octree

An octree recursively divides a cubic region of 3D space into 8 smaller cubes. Each node in the tree corresponds to a cubic volume. If more detail is needed inside that region, the node is split into 8 child nodes. This process continues until the desired map resolution is reached.

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/e352cfa1ba9128201f5b1449aca5df43.jpg" alt="e352cfa1ba9128201f5b1449aca5df43" style="zoom:67%;" />

##### Probabilistic Occupancy Model

Each voxel maintains an **occupancy probability**. For a node $n$, the occupancy probability after receiving measurements $z_{1:t}$ is

$$
P(n \mid z_{1:t})
$$

where $z_{1:t}$ denotes all sensor observations from time $1$ to time $t$.

A voxel is usually classified by comparing its occupancy probability with a threshold

$$
P(n \mid z_{1:t}) > P_{\mathrm{occ}} \quad \Rightarrow \quad n \text{ is occupied}
$$

$$
P(n \mid z_{1:t}) \leq P_{\mathrm{occ}} \quad \Rightarrow \quad n \text{ is free}
$$

If a voxel has never been observed, it remains unknown.

##### Log-Odds Update

Bayesian probability updates can be computationally inconvenient because they involve repeated multiplication and normalization. OctoMap commonly uses the log-odds form of occupancy probability

$$
L(n) = \log \frac{P(n)}{1 - P(n)}
$$

The inverse transformation from log-odds back to probability is

$$
P(n) = 1 - \frac{1}{1 + \exp(L(n))}
$$

Using log-odds, the recursive occupancy update becomes an additive operation

$$
L(n \mid z_{1:t}) =
L(n \mid z_{1:t-1}) + L(n \mid z_t) - L(n)
$$

When the **prior occupancy probability** is $P(n)=0.5$, the **prior log-odds value** is $L(n)=0$. In that common case, the update is simplified to

$$
L(n \mid z_{1:t}) =
L(n \mid z_{1:t-1}) + L(n \mid z_t)
$$

To avoid overconfidence, OctoMap clamps the log-odds value within a fixed range

$$
L_{\mathrm{min}} \leq L(n) \leq L_{\mathrm{max}}
$$

or equivalently,

$$
L(n) =
\max\left(
L_{\mathrm{min}},
\min\left(
L_{\mathrm{max}},
L(n)
\right)
\right)
$$

Clamping prevents the map from becoming impossible to update. Without clamping, repeated observations could make the occupancy probability approach $0$ or $1$ too strongly, which would make it difficult to adapt when the environment changes.

##### Pruning and Map Compression

OctoMap can reduce memory usage through **pruning**. If all 8 child nodes of a parent node have the same stable occupancy state, the children can be merged into the parent node. The parent then represents the entire larger cubic region.

If future measurements require more detail, a node can be expanded again into child nodes. This allows OctoMap to maintain a compact representation while still supporting incremental updates.
