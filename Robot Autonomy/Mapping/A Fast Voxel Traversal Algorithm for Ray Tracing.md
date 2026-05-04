# A Fast Voxel Traversal Algorithm for Ray Tracing

The **Amanatides-Woo Algorithm**, a fast and simple voxel traversal algorithm through a 3D space partition, is introduced.

[toc]

##### Ray Intervals

The equation of the ray is

$$
\boldsymbol{p}(t)=\boldsymbol{u}+t\boldsymbol{v}, \qquad t\ge 0
$$

where $\boldsymbol{u}$ is the ray origin and $\boldsymbol{v}$ is the ray direction. The algorithm breaks down the ray into intervals of $t$, each of which spans one voxel. Starting from the ray origin, the voxels are visited in interval order.

##### Initialization

The initialization can be described clearly by using the $x$ axis as an example.

Let $G_x$ be the grid minimum coordinate in the $x$ direction, $h_x$ be the voxel width, $u_x$ be the $x$ component of $\boldsymbol{u}$, and $v_x$ be the $x$ component of $\boldsymbol{v}$.

First, the algorithm tests whether the ray origin is inside the grid. In the $x$ direction this means
$$
G_x^{min} \le u_x < G_x^{max}
$$

and the same test is applied in the $y$ and $z$ directions:

$$
G_y^{min} \le u_y < G_y^{max}, \qquad G_z^{min} \le u_z < G_z^{max}
$$

The starting voxel coordinate in the $x$ direction is

$$
\text{X}=\left\lfloor\frac{u_x-G_x}{h_x}\right\rfloor
$$

The step variable indicates whether `X` is incremented or decremented when the ray crosses an $x$ voxel boundary

$$
\text{stepX}=
\begin{cases}
1, & v_x>0 \\
-1, & v_x<0
\end{cases}
$$

Next, the algorithm determines the value of $t$ at which the ray crosses the first vertical voxel boundary. The first $x$ boundary is

$$
B_x=
\begin{cases}
G_x+(\text{X}+1)h_x, & \text{stepX}=1 \\
G_x+\text{X}h_x, & \text{stepX}=-1
\end{cases}
$$

Then

$$
\text{tMaxX}=\frac{B_x-u_x}{v_x}
$$

Thus, `tMaxX` stores the value of $t$ at which the ray first crosses the next $x$ voxel boundary.

Finally, the algorithm computes

$$
\text{tDeltaX}=\frac{h_x}{|v_x|}
$$

`tDeltaX` indicates how far along the ray one must move, in units of $t$, for the horizontal component of such a movement to equal the width of a voxel.

The same initialization is applied analogously in the $y$ and $z$ directions, giving

$$
\text{Y}, \text{Z}
$$

$$
\text{stepY}, \text{stepZ}
$$

$$
\text{tMaxY}, \text{tMaxZ}
$$

$$
\text{tDeltaY}, \text{tDeltaZ}
$$

| Initialization task                                          | Floating point operations |
| ------------------------------------------------------------ | :-----------------------: |
| Test whether the ray origin is inside the grid               |             6             |
| Compute the starting voxel coordinates $\text{X},\text{Y},\text{Z}$ |             6             |
| Determine the signs of the three components of $\boldsymbol{v}$ |             3             |
| Compute the first voxel boundary $B_x,B_y,B_z$               |             6             |
| Compute $\text{tMaxX},\text{tMaxY},\text{tMaxZ}$             |             6             |
| Compute $\text{tDeltaX},\text{tDeltaY},\text{tDeltaZ}$       |             6             |
| Total                                                        |            33             |

If the ray origin is outside the grid, the algorithm first finds the point at which the ray enters the grid and then takes the adjacent voxel.

For example, for an $x$ boundary,
$$
t_x^{min}=\frac{G_x^{min}-u_x}{v_x}
$$

$$
t_x^{max}=\frac{G_x^{max}-u_x}{v_x}
$$

$$
t_{entry}=\min(t_x^{min},t_x^{max})
$$

And the entry point is then
$$
\boldsymbol{p}_{entry}=\boldsymbol{u}+t_{entry}\boldsymbol{v}
$$

The adjacent voxel at this entry point is used as the starting voxel.

the entry-point computation increases the initialization cost by at most 7 floating point operations

$$
33+7=40
$$

##### Incremental Traversal

During traversal, the algorithm finds

$$
\min (\text{tMaxX}, \text{tMaxY}, \text{tMaxZ})
$$

at each iteration. The smallest value indicates which voxel boundary the ray crosses next.

If `tMaxX` is the smallest, the ray crosses an $x$ boundary first

```pseudocode
X = X + stepX
tMaxX = tMaxX + tDeltaX
```

Other two cases are analogous.

The loop continues until either a voxel with a non-empty object list is found or the ray falls out of the end of the grid.

```pseudocode
list = NIL;

do {
    if (tMaxX < tMaxY) {
        if (tMaxX < tMaxZ) {
            X = X + stepX;
            if (X == justOutX) 
            	return NIL;
            tMaxX = tMaxX + tDeltaX;
        } else {
            Z = Z + stepZ;
            if (Z == justOutZ) 
            	return NIL;
            tMaxZ = tMaxZ + tDeltaZ;
        }
    } else {
        if (tMaxY < tMaxZ) {
            Y = Y + stepY;
            if (Y == justOutY) 
            	return NIL;
            tMaxY = tMaxY + tDeltaY;
        } else {
            Z = Z + stepZ;
            if (Z == justOutZ) 
            	return NIL;
            tMaxZ = tMaxZ + tDeltaZ;
        }
    }

    list = ObjectList[X][Y][Z];

} while (list == NIL);

return list;
```

The loop requires

$$
2\ \text{floating point comparisons}
$$

for finding the minimum of `tMaxX`, `tMaxY`, and `tMaxZ`; and

$$
1\ \text{floating point addition}
$$

for updating the selected `tMax` value. It also requires two integer comparisons and one integer addition per iteration.

This algorithm can **find the nearest non-empty voxel** along the ray traversal order.

##### Correct Visibility

To correctly determine visibility, the closest intersection point must be in the current voxel. The first voxel with a non-empty object list may contain an object whose actual intersection lies farther away, in a later voxel.

Checking whether the intersection point is within the voxel require one floating point comparisons. Compare the value of $t$ at the intersection point with the maximum value of $t$ allowed in the current voxel.
$$
t_{hit} \le t_{current\ max}
$$

If the condition holds, the intersection point is in the current voxel. Otherwise, traversal continues until either the voxel containing that intersection is reached or a closer object is found.

The easiest way to perform this comparison is to include it in the incremental traversal code just after the minimum of `tMaxX`, `tMaxY`, and `tMaxZ` is determined.

##### Avoiding Multiple Intersections

Since objects may reside in more than one voxel, a ray may intersect the same object many times. 

To solve the multiple intersection problem, an integer variable called
$$
\text{rayID}
$$

 is added to each ray.

Each object stores the `rayID` of the ray that most recently performed an intersection test with it. Before an intersection test, the two identifiers are compared.

Thus, a ray intersection test need only be performed once for any object. This requires one extra integer comparison, but a full intersection test is typically several orders of magnitude more expensive.

```pseudocode
/* 
 * Ray has:
 *     rayID
 *     winner: the closest object intersected so far
 *     tHit
 *
 * Each object has:
 *     rayID
 */

winner = NIL;
tHit = INFINITY;

/* start from the initial voxel */
list = ObjectList[X][Y][Z];

while(TRUE) {
    if(list != NIL) {
        for(each object in list) {
            if(object.rayID == ray.rayID) {
                /* this object has previously been intersected by the same ray */
                continue;
            } else {
                object.rayID = ray.rayID;
                t = Intersect(ray, object);
                if(t != NIL) {
                    if(t < tHit) {
                        tHit = t;
                        winner = object;
                    }
                }
            }
        }
    }
    
	list = NIL;
    do {
        if(tMaxX < tMaxY) {
            if(tMaxX < tMaxZ) {
                if(winner != NIL) {
                    if(tHit <= tMaxX)
                        return(winner);
                }
                X = X + stepX;
                if(X == justOutX) {
                    if(winner != NIL)
                        return(winner);
                    else
                        return(NIL);
                }
                tMaxX = tMaxX + tDeltaX;
            } else {
                if(winner != NIL) {
                    if(tHit <= tMaxZ)
                        return(winner);
                }
                Z = Z + stepZ;
                if(Z == justOutZ) {
                    if(winner != NIL)
                        return(winner);
                    else
                        return(NIL);
                }
                tMaxZ = tMaxZ + tDeltaZ;
            }
        } else {
            if(tMaxY < tMaxZ) {
                if(winner != NIL) {
                    if(tHit <= tMaxY)
                        return(winner);
                }
                Y = Y + stepY;
                if(Y == justOutY) {
                    if(winner != NIL)
                        return(winner);
                    else
                        return(NIL);
                }
                tMaxY = tMaxY + tDeltaY;
            } else {
                if(winner != NIL) {
                    if(tHit <= tMaxZ)
                        return(winner);
                }
                Z = Z + stepZ;
                if(Z == justOutZ) {
                    if(winner != NIL)
                        return(winner);
                    else
                        return(NIL);
                }
                tMaxZ = tMaxZ + tDeltaZ;
            }
        }
        list = ObjectList[X][Y][Z];
    } while(list == NIL);
}
```

This algorithm traverses a 3D grid along a ray and finds the closest valid object intersection. 

It avoids repeated intersection tests for objects spanning multiple voxels by using `rayID`, and it returns the current `winner` only when its intersection point is confirmed to lie within the current voxel.
