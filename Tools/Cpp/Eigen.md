# Eigen

[toc]

### Dense Matrices and Vectors

##### Include Headers

```cpp
#include <Eigen/Dense>		// Dense matrices, vectors, decompositions
#include <Eigen/Geometry>	// Rotations and transformations
#include <Eigen/Sparse>		// Sparse matrices and solvers
```

##### Matrix and Vector Types

Eigen dense matrices and vectors use the `Matrix` template. A vector is a matrix with one column.

```cpp
Eigen::Matrix<Scalar, Rows, Cols>
```

- fixed-size types use compile-time dimensions
- dynamic-size types use `Eigen::Dynamic`
- fixed-size types are preferred for small dimensions known at compile time

```cpp
Eigen::Vector2d p2;		// Matrix<double, 2, 1>
Eigen::Vector3d p3;		// Matrix<double, 3, 1>

Eigen::Matrix2d R2;		// Matrix<double, 2, 2>
Eigen::Matrix3d R3;		// Matrix<double, 3, 3>
Eigen::Matrix4d T4;		// Matrix<double, 4, 4>

Eigen::VectorXd x;						// Dynamic x 1
Eigen::MatrixXd A;						// Dynamic x Dynamic
Eigen::Matrix<double, 3, Eigen::Dynamic> points;	// 3 x Dynamic
```

A `3 x N` matrix is convenient for a runtime-sized set of 3D points.

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	const int point_count = 3;

	Eigen::Matrix<double, 3, Eigen::Dynamic> points(3, point_count);
	points << 0.0, 1.0, 2.0,
	          0.0, 0.5, 1.0,
	          1.0, 1.0, 1.0;

	std::cout << points.rows() << '\n';		// 3
	std::cout << points.cols() << '\n';		// 3
	std::cout << points.col(1).transpose() << '\n';	// 1 0.5 1
}
```

##### Construction and Initialization

Common initialization forms include:

- constructors for vectors and dynamic-size objects
- comma initialization with `<<`
- `Zero()`, `Ones()`, `Constant()`, and `Identity()`
- `setZero()`, `setOnes()`, `setConstant()`, and `setIdentity()`

```cpp
Eigen::Vector3d v(x, y, z);

Eigen::MatrixXd A(rows, cols);
Eigen::VectorXd b(size);

Eigen::Matrix3d::Zero();
Eigen::Matrix3d::Ones();
Eigen::Matrix3d::Constant(value);
Eigen::Matrix3d::Identity();

A.setZero();
A.setOnes();
A.setConstant(value);
A.setIdentity();
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Vector3d position(1.0, 2.0, 3.0);

	Eigen::Matrix3d rotation;
	rotation << 0.0, -1.0, 0.0,
	            1.0,  0.0, 0.0,
	            0.0,  0.0, 1.0;

	Eigen::Matrix3d identity = Eigen::Matrix3d::Identity();
	Eigen::Vector3d zero = Eigen::Vector3d::Zero();

	std::cout << position.transpose() << '\n';	// 1 2 3
	std::cout << rotation(0, 1) << '\n';		// -1
	std::cout << identity(2, 2) << '\n';		// 1
	std::cout << zero.norm() << '\n';			// 0
}
```

Dynamic-size objects can be resized. `resize()` does not initialize newly created coefficients.

```cpp
Eigen::MatrixXd measurements(2, 3);
measurements.resize(3, 4);
measurements.setZero();
```

##### Size and Access

- `rows()` returns the number of rows
- `cols()` returns the number of columns
- `size()` returns the number of coefficients
- `operator()(row, col)` accesses a matrix coefficient
- `operator()(index)` accesses a vector coefficient
- `x()`, `y()`, and `z()` provide named vector access

```cpp
matrix.rows();
matrix.cols();
matrix.size();

matrix(row, col);
vector(index);

vector.x();
vector.y();
vector.z();
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix2d A;
	A << 1.0, 2.0,
	     3.0, 4.0;

	Eigen::Vector3d p(1.0, 2.0, 3.0);

	std::cout << A.rows() << '\n';	// 2
	std::cout << A.cols() << '\n';	// 2
	std::cout << A.size() << '\n';	// 4
	std::cout << A(1, 0) << '\n';	// 3
	std::cout << p(2) << '\n';		// 3
	std::cout << p.z() << '\n';		// 3
}
```

##### Matrix Arithmetic

For `Matrix` objects, `operator*` performs matrix multiplication.

- `+` and `-` perform matrix addition and subtraction
- `*` between matrices performs matrix multiplication
- multiplication or division by a scalar scales all coefficients
- `transpose()` returns the transpose
- `determinant()` computes the determinant of a square matrix

```cpp
A + B;
A - B;
A * B;

scalar * A;
A / scalar;

A.transpose();
A.determinant();
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix2d A;
	A << 1.0, 2.0,
	     3.0, 4.0;

	const Eigen::Matrix2d B = Eigen::Matrix2d::Identity();

	const Eigen::Matrix2d sum = A + B;
	const Eigen::Matrix2d product = A * B;
	const Eigen::Matrix2d transpose = A.transpose();

	std::cout << sum(0, 0) << '\n';			// 2
	std::cout << product(1, 0) << '\n';		// 3
	std::cout << transpose(0, 1) << '\n';	// 3
	std::cout << A.determinant() << '\n';	// -2
}
```

For solving `Ax = b`, prefer a decomposition and `solve()` instead of explicitly computing `A.inverse() * b`.

##### Vector Operations

- `norm()` returns the Euclidean norm
- `squaredNorm()` returns the squared Euclidean norm
- `normalized()` returns a normalized copy
- `normalize()` normalizes in place
- `dot()` computes the dot product
- `cross()` computes the 3D cross product

```cpp
vector.norm();
vector.squaredNorm();

vector.normalized();
vector.normalize();

a.dot(b);
a.cross(b);
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Vector3d forward(1.0, 0.0, 0.0);
	Eigen::Vector3d left(0.0, 1.0, 0.0);
	Eigen::Vector3d velocity(3.0, 4.0, 0.0);

	std::cout << velocity.norm() << '\n';			// 5
	std::cout << velocity.squaredNorm() << '\n';	// 25
	std::cout << forward.dot(left) << '\n';		// 0

	const Eigen::Vector3d up = forward.cross(left);
	const Eigen::Vector3d direction = velocity.normalized();

	std::cout << up.transpose() << '\n';			// 0 0 1
	std::cout << direction.norm() << '\n';		// 1
}
```

`squaredNorm()` is useful when only relative distances are compared.

```cpp
bool isCloser(const Eigen::Vector2d& first,
              const Eigen::Vector2d& second,
              const Eigen::Vector2d& query) {
	return (first - query).squaredNorm() <
	       (second - query).squaredNorm();
}
```

##### Coefficient-Wise Operations

Use coefficient-wise operations when each coefficient should be processed independently.

- `cwiseProduct()` multiplies corresponding coefficients
- `cwiseMin()` and `cwiseMax()` compare corresponding coefficients
- `.array()` switches to coefficient-wise array expressions
- `.matrix()` converts back to a matrix expression

```cpp
a.cwiseProduct(b);
a.cwiseMin(b);
a.cwiseMax(b);

matrix.array();
array.matrix();
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Vector3d error(1.0, -2.0, 3.0);
	Eigen::Vector3d weight(2.0, 0.5, 1.0);

	const Eigen::Vector3d weighted = error.cwiseProduct(weight);
	const Eigen::Vector3d squared = error.array().square().matrix();
	const Eigen::Vector3d absolute = error.array().abs().matrix();

	std::cout << weighted.transpose() << '\n';	// 2 -1 3
	std::cout << squared.transpose() << '\n';	// 1 4 9
	std::cout << absolute.transpose() << '\n';	// 1 2 3
}
```

##### Blocks and Segments

Block expressions provide read-write access to parts of matrices and vectors.

- `block()` accesses a rectangular matrix region
- `row()` and `col()` access a row or column
- `head()`, `tail()`, and `segment()` access vector segments
- fixed-size forms encode the block size at compile time

```cpp
matrix.block(row, col, rows, cols);
matrix.block<Rows, Cols>(row, col);

matrix.row(index);
matrix.col(index);

vector.head(count);
vector.tail(count);
vector.segment(start, count);

vector.head<Count>();
vector.tail<Count>();
vector.segment<Count>(start);
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix4d transform = Eigen::Matrix4d::Identity();

	transform.block<3, 3>(0, 0) <<
		0.0, -1.0, 0.0,
		1.0,  0.0, 0.0,
		0.0,  0.0, 1.0;

	transform.block<3, 1>(0, 3) = Eigen::Vector3d(1.0, 2.0, 3.0);

	const Eigen::Matrix3d rotation = transform.topLeftCorner<3, 3>();
	const Eigen::Vector3d translation = transform.block<3, 1>(0, 3);

	Eigen::Matrix<double, 6, 1> state;
	state << 1.0, 2.0, 3.0,
	         0.1, 0.2, 0.3;

	const Eigen::Vector3d position = state.head<3>();
	const Eigen::Vector3d velocity = state.tail<3>();

	std::cout << rotation(1, 0) << '\n';			// 1
	std::cout << translation.transpose() << '\n';	// 1 2 3
	std::cout << position.transpose() << '\n';		// 1 2 3
	std::cout << velocity.transpose() << '\n';		// 0.1 0.2 0.3
}
```

##### Reductions and Comparisons

- `sum()` returns the sum of all coefficients
- `mean()` returns the arithmetic mean
- `minCoeff()` and `maxCoeff()` return minimum and maximum coefficients
- `isApprox()` performs an approximate floating-point comparison

```cpp
matrix.sum();
matrix.mean();
matrix.minCoeff();
matrix.maxCoeff();

first.isApprox(second);
```

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Vector4d residuals(0.2, -0.1, 0.4, 0.3);

	Eigen::Index index{};
	const double maximum = residuals.maxCoeff(&index);

	std::cout << residuals.sum() << '\n';	// 0.8
	std::cout << residuals.mean() << '\n';	// 0.2
	std::cout << maximum << '\n';			// 0.4
	std::cout << index << '\n';				// 2

	const Eigen::Matrix2d A = Eigen::Matrix2d::Identity();
	const Eigen::Matrix2d B = Eigen::Matrix2d::Identity();

	std::cout << std::boolalpha << A.isApprox(B) << '\n';	// true
}
```

##### Aliasing

An assignment can be unsafe when the destination also appears inside an expression.

```cpp
matrix = matrix.transpose();	// Unsafe
```

Use an in-place operation or force evaluation into a temporary.

```cpp
matrix.transposeInPlace();

matrix = matrix.transpose().eval();
```

### Linear Algebra

##### Solving Linear Systems

Use a decomposition appropriate for the matrix properties.

- `colPivHouseholderQr().solve()` handles general dense systems
- `ldlt().solve()` is useful for suitable self-adjoint systems
- SVD provides a robust least-squares solver

```cpp
A.colPivHouseholderQr().solve(b);
A.ldlt().solve(b);

A.bdcSvd(Eigen::ComputeThinU | Eigen::ComputeThinV).solve(b);
```

A small Hessian system is common in robotics optimization.

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix2d H;
	H << 4.0, 1.0,
	     1.0, 3.0;

	Eigen::Vector2d gradient(1.0, 2.0);

	const Eigen::Vector2d delta = H.ldlt().solve(-gradient);

	std::cout << delta.transpose() << '\n';	// approximately -0.0909 -0.6364
}
```

For an overdetermined system, QR or SVD can compute a least-squares solution.

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix<double, 3, 2> A;
	A << 1.0, 0.0,
	     1.0, 1.0,
	     1.0, 2.0;

	Eigen::Vector3d b(1.0, 2.0, 2.0);

	const Eigen::Vector2d x = A.colPivHouseholderQr().solve(b);

	std::cout << x.transpose() << '\n';	// approximately 1.1667 0.5
}
```

##### Eigenvalues

`SelfAdjointEigenSolver` is intended for self-adjoint matrices such as covariance matrices.

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	Eigen::Matrix2d covariance;
	covariance << 2.0, 1.0,
	              1.0, 2.0;

	Eigen::SelfAdjointEigenSolver<Eigen::Matrix2d> solver(covariance);

	std::cout << solver.eigenvalues().transpose() << '\n';	// 1 3
	std::cout << solver.eigenvectors() << '\n';
}
```

### Geometry

##### Rotation Types

Common 3D robotics types include:

```cpp
Eigen::Matrix3d
Eigen::AngleAxisd
Eigen::Quaterniond
Eigen::Isometry3d
Eigen::Affine3d
```

- `Matrix3d` is commonly used as a rotation matrix
- `AngleAxisd` represents a rotation by an angle about a normalized axis
- `Quaterniond` provides a compact 3D rotation representation
- `Isometry3d` represents a rigid transformation
- `Affine3d` additionally permits scaling and shear

##### `Eigen::AngleAxisd`

The axis passed to `AngleAxisd` must be normalized.

```cpp
Eigen::AngleAxisd(angle, normalized_axis);
```

```cpp
#include <Eigen/Geometry>
#include <iostream>

int main() {
	const double yaw = 0.5;	// rad

	const Eigen::AngleAxisd yaw_rotation(
		yaw,
		Eigen::Vector3d::UnitZ()
	);

	const Eigen::Matrix3d R = yaw_rotation.toRotationMatrix();

	std::cout << R << '\n';
}
```

`AngleAxisd` is mainly convenient for constructing other rotation representations.

##### `Eigen::Quaterniond`

Common operations include:

- construct from `AngleAxisd` or a rotation matrix
- `toRotationMatrix()` converts to a rotation matrix
- `operator*` composes rotations or rotates a vector
- `inverse()` returns the inverse rotation
- `slerp()` performs spherical interpolation
- `normalize()` and `normalized()` maintain unit length

```cpp
Eigen::Quaterniond quaternion(Eigen::AngleAxisd(angle, axis));
Eigen::Quaterniond quaternion(rotation_matrix);

quaternion.toRotationMatrix();
quaternion.inverse();
quaternion.slerp(t, other);
quaternion.normalize();
```

Operations that interpret a quaternion as a rotation require a normalized quaternion.

```cpp
#include <Eigen/Geometry>
#include <iostream>

int main() {
	const Eigen::Quaterniond q(
		Eigen::AngleAxisd(0.5, Eigen::Vector3d::UnitZ())
	);

	const Eigen::Vector3d point(1.0, 0.0, 0.0);
	const Eigen::Vector3d rotated = q * point;

	const Eigen::Quaterniond identity = Eigen::Quaterniond::Identity();
	const Eigen::Quaterniond halfway = identity.slerp(0.5, q);

	std::cout << rotated.transpose() << '\n';
	std::cout << halfway.norm() << '\n';	// 1
}
```

The scalar constructor uses `w, x, y, z`, while `coeffs()` uses `x, y, z, w`.

```cpp
#include <Eigen/Geometry>
#include <iostream>

int main() {
	Eigen::Quaterniond q(1.0, 0.1, 0.2, 0.3);

	std::cout << q.w() << '\n';					// 1
	std::cout << q.x() << '\n';					// 0.1
	std::cout << q.coeffs().transpose() << '\n';	// 0.1 0.2 0.3 1
}
```

##### `Eigen::Isometry3d`

`Isometry3d` represents a rigid transformation with rotation and translation.

- `Identity()` creates an identity transform
- `linear()` accesses the rotation/linear part
- `translation()` accesses the translation
- `matrix()` accesses the homogeneous matrix
- `inverse()` returns the inverse transform
- `operator*` composes transforms or transforms a point

```cpp
Eigen::Isometry3d::Identity();

transform.linear();
transform.translation();
transform.matrix();
transform.inverse();

first * second;
transform * point;
```

Frame-named transforms make composition direction explicit.

```cpp
#include <Eigen/Geometry>
#include <iostream>

int main() {
	Eigen::Isometry3d T_world_base = Eigen::Isometry3d::Identity();
	T_world_base.translation() = Eigen::Vector3d(1.0, 2.0, 0.0);
	T_world_base.linear() =
		Eigen::AngleAxisd(0.5, Eigen::Vector3d::UnitZ()).toRotationMatrix();

	Eigen::Isometry3d T_base_sensor = Eigen::Isometry3d::Identity();
	T_base_sensor.translation() = Eigen::Vector3d(0.2, 0.0, 0.1);

	const Eigen::Isometry3d T_world_sensor =
		T_world_base * T_base_sensor;

	const Eigen::Vector3d p_sensor(1.0, 0.0, 0.0);
	const Eigen::Vector3d p_world = T_world_sensor * p_sensor;
	const Eigen::Vector3d p_back = T_world_sensor.inverse() * p_world;

	std::cout << p_world.transpose() << '\n';
	std::cout << p_back.transpose() << '\n';	// 1 0 0
}
```

For a point, the full transform includes translation. For a direction vector, use only the linear part when translation must not be applied.

```cpp
Eigen::Vector3d transformed_point = T * point;
Eigen::Vector3d transformed_direction = T.linear() * direction;
```

### Existing Memory

##### `Eigen::Map`

`Eigen::Map` provides an Eigen view over existing memory without copying coefficients.

```cpp
Eigen::Map<PlainObjectType>
Eigen::Map<const PlainObjectType>
```

**Vector Mapping**

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	double data[3] = {1.0, 2.0, 3.0};

	Eigen::Map<Eigen::Vector3d> vector(data);
	vector.z() = 4.0;

	std::cout << vector.transpose() << '\n';	// 1 2 4
	std::cout << data[2] << '\n';				// 4
}
```

**Dynamic Mapping**

```cpp
#include <Eigen/Dense>
#include <iostream>
#include <vector>

int main() {
	std::vector<double> data{1.0, 2.0, 3.0, 4.0};

	Eigen::Map<Eigen::VectorXd> vector(
		data.data(),
		static_cast<Eigen::Index>(data.size())
	);

	vector *= 2.0;

	std::cout << vector.transpose() << '\n';	// 2 4 6 8
}
```

Use `Eigen::Map<const T>` for read-only memory.

##### Storage Order

Eigen matrices are column-major by default.

```cpp
#include <Eigen/Dense>
#include <iostream>

int main() {
	double data[6] = {1, 2, 3, 4, 5, 6};

	Eigen::Map<Eigen::Matrix<double, 3, 2>> column_major(data);

	std::cout << column_major << '\n';
	// 1 4
	// 2 5
	// 3 6
}
```

Use `Eigen::RowMajor` when the external buffer stores complete rows consecutively.

```cpp
Eigen::Map<
	Eigen::Matrix<double, 3, 2, Eigen::RowMajor>
> row_major(data);
```

### Sparse Matrices

##### `Eigen::SparseMatrix`

Use sparse matrices when most coefficients are zero and dense storage is inefficient.

```cpp
Eigen::SparseMatrix<double>
Eigen::Triplet<double>
```

Building triplets and calling `setFromTriplets()` is a common assembly pattern.

```cpp
#include <Eigen/Sparse>
#include <iostream>
#include <vector>

int main() {
	using SparseMatrix = Eigen::SparseMatrix<double>;
	using Triplet = Eigen::Triplet<double>;

	std::vector<Triplet> coefficients{
		{0, 0, 4.0},
		{0, 1, 1.0},
		{1, 0, 1.0},
		{1, 1, 3.0}
	};

	SparseMatrix H(2, 2);
	H.setFromTriplets(coefficients.begin(), coefficients.end());

	Eigen::Vector2d b(1.0, 2.0);

	Eigen::SimplicialLDLT<SparseMatrix> solver;
	solver.compute(H);

	const Eigen::Vector2d x = solver.solve(b);

	std::cout << x.transpose() << '\n';	// approximately 0.0909 0.6364
}
```
