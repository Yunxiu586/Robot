# Eigen

[toc]

##### Include Headers

For basic matrices and vectors

```cpp
#include <Eigen/Dense>
```

For rotations, quaternions, affine transforms, and rigid transforms

```cpp
#include <Eigen/Geometry>
```

For sparse matrices, useful in graph optimization and large linear systems

```cpp
#include <Eigen/Sparse>
```

##### Fixed-size vectors

```cpp
Eigen::Vector2d p2;      // 2D point or vector: [x, y]
Eigen::Vector3d p3;      // 3D point or vector: [x, y, z]
Eigen::Vector4d q;       // quaternion coefficients or homogeneous vectors
```

Methods

```cpp
v.norm();          // Euclidean norm
v.squaredNorm();   // squared Euclidean norm, faster if you only compare distances
v.normalized();    // returns a normalized copy
v.normalize();     // normalizes in place
v.dot(w);          // dot product
v.cross(w);        // cross product, mainly for 3D vectors
```

Example

```cpp
bool isCloser(const Eigen::Vector2d& a,
              const Eigen::Vector2d& b,
              const Eigen::Vector2d& query) {
    return (a - query).squaredNorm() < (b - query).squaredNorm();
}
```

This avoids computing unnecessary square roots.

##### Fixed-Size Matrices

```cpp
Eigen::Matrix2d R2;    // 2x2 double matrix
Eigen::Matrix3d R3;    // 3x3 double matrix
Eigen::Matrix4d T4;    // 4x4 double matrix
```

##### Dynamic-Size Matrices

Use dynamic-size matrices for data whose size is known only at runtime

```cpp
Eigen::MatrixXd A;     // dynamic rows and columns
Eigen::VectorXd x;     // dynamic vector
```

Example

```cpp
int n = 100;
Eigen::VectorXd costs(n);
costs.setZero();

Eigen::MatrixXd samples(n, 2);  // n sampled 2D states
```

Comma initialization is common

```cpp
Eigen::Matrix2d R;
R << 0.0, -1.0,
     1.0,  0.0;

Eigen::Vector3d p;
p << 1.0, 2.0, 3.0;
```

Factory methods

```cpp
Eigen::Matrix3d I = Eigen::Matrix3d::Identity();
Eigen::Vector3d z = Eigen::Vector3d::Zero();
Eigen::Vector3d o = Eigen::Vector3d::Ones();
```

Angle Normalization

```cpp
double normalize(double angle) {
    return std::atan2(std::sin(angle), std::cos(angle));
}
```

For 3D robotics, you will commonly use

```cpp
Eigen::Vector3d
Eigen::Matrix3d
Eigen::Quaterniond
Eigen::Isometry3d
Eigen::Affine3d
```

##### `Eigen::AngleAxisd`

`AngleAxisd` represents a rotation using the **axis-angle** form.

Rotation Matrix `R`

```cpp
Eigen::Matrix3d R = Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitZ())
                        .toRotationMatrix();
```

```cpp
Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitZ())
```

creates a 3D rotation object representing a 45-degree rotation about the z-axis.

##### `Eigen::Quaterniond`

```cpp
Eigen::Quaterniond q(Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitZ()));
Eigen::Vector3d p_rotated = q * Eigen::Vector3d(1.0, 0.0, 0.0);
```

The quaternion `q` is constructed from

```cpp
Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitZ())
```

```cpp
q * Eigen::Vector3d(1.0, 0.0, 0.0)
```

applies the rotation `q` to the vector

##### `Eigen::Isometry3d`

Rigid Transform with `Isometry3d`

```cpp
Eigen::Isometry3d T_world_base = Eigen::Isometry3d::Identity();
// the base frame origin is located at (1.0, 2.0, 0.0) in the world frame.
T_world_base.translation() = Eigen::Vector3d(1.0, 2.0, 0.0);
// set the rotation matrix
T_world_base.linear() = Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitZ())
                            .toRotationMatrix();

Eigen::Vector3d p_base(1.0, 0.0, 0.0);
Eigen::Vector3d p_world = T_world_base * p_base;
```

Inverse transform

```cpp
Eigen::Vector3d p_back = T_world_base.inverse() * p_world;
```

##### `Eigen::Map`

`Eigen::Map` does **not** copy data.

```cpp
double data[3] = {1.0, 2.0, 3.0};
Eigen::Map<Eigen::Vector3d> v(data);
```

```cpp
std::vector<double> data = {1, 2, 3};
Eigen::Map<Eigen::VectorXd> v(data.data(), data.size());
```

```cpp
double data[6] = {1, 2, 3, 4, 5, 6};
Eigen::Map<
    Eigen::Matrix<double, 3, 2>
> M(data);
```

By default, `Eigen` uses **column-major** storage, so the matrix is interpreted as

```
1 4
2 5
3 6
```

If your data is stored row by row

```cpp
Eigen::Map<
    Eigen::Matrix<double, 3, 2, Eigen::RowMajor>
> M(data);
```

Then the matrix is interpreted as

```
1 2
3 4
5 6
```

