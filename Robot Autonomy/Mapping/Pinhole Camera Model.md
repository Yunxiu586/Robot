# Pinhole Camera Model

[toc]

##### Pixel, Depth, and Camera Intrinsics

A depth image stores a depth value for each pixel location. A pixel is usually written as

$$
(u, v)
$$

where $u$ is the horizontal pixel coordinate and $v$ is the vertical pixel coordinate.

The camera intrinsic parameters are

$$
f_x, f_y, c_x, c_y
$$

where $f_x$ and $f_y$ are the focal lengths measured in pixels, and $c_x, c_y$ define the principal point of the camera.

The raw depth image stores depth as an unsigned integer. The real metric depth is obtained by dividing by a depth scaling factor

$$
z_c = \frac{D(u,v)}{s}
$$

where $D(u,v)$ is the raw depth value and $s$ is the depth scaling factor.

The important point is that this **depth** is treated as the **$z$-coordinate** in the camera frame, not as the Euclidean distance from the camera center.

##### Pinhole Camera Projection Model

The pinhole camera model describes how a 3D point in the camera frame projects onto the image plane.

Let a 3D point in the camera frame be

$$
\boldsymbol{p}_c =
\begin{bmatrix}
x_c \\
y_c \\
z_c
\end{bmatrix}
$$

The projection from camera coordinates to pixel coordinates is

$$
u = f_x \frac{x_c}{z_c} + c_x
$$

$$
v = f_y \frac{y_c}{z_c} + c_y
$$

This means that a 3D point farther away from the camera has a larger $z_c$, and its image-plane coordinates are obtained by perspective division.

##### Back-Projecting a Depth Pixel to a Camera-Frame Point

We already know the pixel coordinate $(u,v)$ and its depth value $z_c$. Then, we invert the pinhole projection model to recover the 3D point in the camera frame.

$$
x_c = \frac{(u - c_x)z_c}{f_x}
$$

$$
y_c = \frac{(v - c_y)z_c}{f_y}
$$

The camera-frame 3D point is therefore

$$
\boldsymbol{p}_c =
\begin{bmatrix}
\frac{(u - c_x)z_c}{f_x} \\
\frac{(v - c_y)z_c}{f_y} \\
z_c
\end{bmatrix}
$$

##### Camera Coordinate Convention

The formula used in the function assumes the common depth-camera coordinate convention

$$
x_c \text{ points to the right}
$$

$$
y_c \text{ points downward}
$$

$$
z_c \text{ points forward}
$$

So, if a pixel is exactly at the principal point

$$
u = c_x,\quad v = c_y
$$

then

$$
x_c = 0,\quad y_c = 0
$$

and the point lies directly in front of the camera

$$
\boldsymbol{p}_c =
\begin{bmatrix}
0 \\
0 \\
z_c
\end{bmatrix}
$$

If $u > c_x$, then $x_c > 0$, meaning the point is to the right of the optical axis.

If $v > c_y$, then $y_c > 0$, meaning the point is below the optical axis.

##### From Camera Frame to World Frame

After obtaining the 3D point in the camera frame, the function transforms it into the world frame.

The homogeneous transformation matrix is

$$
{}^{world}\boldsymbol{T}_{camera} =
\begin{bmatrix}
{}^{world}\boldsymbol{R}_{camera} & {}^{world}\boldsymbol{t}_{camera} \\
\boldsymbol{0} & 1
\end{bmatrix}
$$

where ${}^{world}\boldsymbol{R}_{camera}$ is the rotation from the camera frame to the world frame, and ${}^{world}\boldsymbol{t}_{camera}$ is the position of the camera origin expressed in the world frame.

For a 3D point expressed in the camera frame,

$$
{}^{camera}\boldsymbol{p} =
\begin{bmatrix}
x_c \\
y_c \\
z_c
\end{bmatrix}
$$

its homogeneous coordinate is

$$
{}^{camera}\tilde{\boldsymbol{p}} =
\begin{bmatrix}
{}^{camera}\boldsymbol{p} \\
1
\end{bmatrix}
$$

The transformation from the camera frame to the world frame is

$$
{}^{world}\tilde{\boldsymbol{p}} =
{}^{world}\boldsymbol{T}_{camera}
{}^{camera}\tilde{\boldsymbol{p}}
$$

Equivalently, in non-homogeneous form,

$$
{}^{world}\boldsymbol{p} =
{}^{world}\boldsymbol{R}_{camera}
{}^{camera}\boldsymbol{p}
+
{}^{world}\boldsymbol{t}_{camera}
$$

Therefore, the transformation from one depth pixel to one world point is
$$
{}^{world}\boldsymbol{p} =
{}^{world}\boldsymbol{R}_{camera}
\begin{bmatrix}
\frac{(u - c_x)z_c}{f_x} \\
\frac{(v - c_y)z_c}{f_y} \\
z_c
\end{bmatrix}
+
{}^{world}\boldsymbol{t}_{camera}
$$
