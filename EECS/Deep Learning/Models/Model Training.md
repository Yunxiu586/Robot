# Model Training

[toc]

### Gradient Descent

##### Gradient Descent

The objective function $J(\boldsymbol{\theta})$ is usually a loss function. Given a training set with $m$ samples, each sample $\boldsymbol{x}_i$ has $d$ features. The goal is to find parameters $\boldsymbol{\theta}$ that make $J(\boldsymbol{\theta})$ sufficiently small.

For one sample, the loss can be written as

$$
\ell(\boldsymbol{\theta}; \boldsymbol{x}_i, y_i)
$$

Around the current parameters $\boldsymbol{\theta}^{(k)}$, the first-order Taylor approximation is

$$
J(\boldsymbol{\theta}) \approx J(\boldsymbol{\theta}^{(k)}) +
\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}^{(k)})^T
(\boldsymbol{\theta} - \boldsymbol{\theta}^{(k)})
$$

Let

$$
\Delta \boldsymbol{\theta}
=
\boldsymbol{\theta} - \boldsymbol{\theta}^{(k)}
$$

To decrease $J(\boldsymbol{\theta})$ as much as possible under a fixed step size, the update direction should be the negative gradient direction

$$
\Delta \boldsymbol{\theta}
=
-\eta \nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}^{(k)})
$$

Thus the gradient descent update is

$$
\boldsymbol{\theta}^{(k+1)}
=
\boldsymbol{\theta}^{(k)}
-
\eta \nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}^{(k)})
$$

Here $\eta$ is the learning rate, commonly chosen as a small value such as $0.01$ or $0.001$.

##### BGD

Batch Gradient Descent uses the average gradient over the whole training set at each update.

$$
J(\boldsymbol{\theta})
=
\frac{1}{m}
\sum_{i=1}^{m}
\ell(\boldsymbol{\theta}; \boldsymbol{x}_i, y_i)
$$

$$
\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta})
=
\begin{bmatrix}
\frac{\partial J}{\partial \theta_1}
&
\frac{\partial J}{\partial \theta_2}
&
\cdots
&
\frac{\partial J}{\partial \theta_p}
\end{bmatrix}^T
$$

$$
\boldsymbol{\theta}^{(k+1)}
=
\boldsymbol{\theta}^{(k)}
-
\eta
\frac{1}{m}
\sum_{i=1}^{m}
\nabla_{\boldsymbol{\theta}}
\ell(\boldsymbol{\theta}^{(k)}; \boldsymbol{x}_i, y_i)
$$

The update direction is stable, but each iteration is expensive for large datasets.

##### SGD

Stochastic Gradient Descent uses one randomly selected sample at each update.

$$
\boldsymbol{\theta}^{(k+1)}
=
\boldsymbol{\theta}^{(k)}
-
\eta
\nabla_{\boldsymbol{\theta}}
\ell(\boldsymbol{\theta}^{(k)}; \boldsymbol{x}_{i_k}, y_{i_k})
$$

Each update is fast, but the direction has high variance, so the loss curve may oscillate heavily.

##### MBGD

Mini-batch Gradient Descent uses a small batch of samples at each update.  
Common batch sizes include $64$, $128$, and $256$.
$$
\boldsymbol{\theta}^{(k+1)}
=
\boldsymbol{\theta}^{(k)}
-
\eta
\frac{1}{|\mathcal{B}_k|}
\sum_{i\in\mathcal{B}_k}
\nabla_{\boldsymbol{\theta}}
\ell(\boldsymbol{\theta}^{(k)}; \boldsymbol{x}_i, y_i)
$$

Mini-batch gradient descent is the standard choice in deep learning because it balances computational efficiency and gradient stability.

### Matrix Derivatives

All vectors in this section are column vectors.

$$
\boldsymbol{x}
=
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n
\end{bmatrix}^T
$$

A derivative layout describes how partial derivatives are arranged. It does not change the scalar partial derivatives themselves. The same derivation should use only one layout.

##### Numerator Layout

The numerator layout is also called the Jacobian formulation. The numerator dimensions are placed before the denominator dimensions. For a scalar function $y=f(\boldsymbol{x})$, the derivative with respect to a column vector is a row vector.

$$
\frac{\partial y}{\partial \boldsymbol{x}}
=
\begin{bmatrix}
\frac{\partial y}{\partial x_1}
&
\frac{\partial y}{\partial x_2}
&
\cdots
&
\frac{\partial y}{\partial x_n}
\end{bmatrix}
$$

For the sum of vector components,

$$
\operatorname{sum}(\boldsymbol{x})
=
\sum_{i=1}^{n}x_i
$$

$$
\frac{\partial \operatorname{sum}(\boldsymbol{x})}{\partial \boldsymbol{x}}
=
\mathbf{1}^T
$$

Let

$$
y
=
\boldsymbol{u}^T\boldsymbol{v}
$$

where $\boldsymbol{u}$ and $\boldsymbol{v}$ depend on $\boldsymbol{x}$. Under the numerator layout,

$$
\frac{\partial y}{\partial \boldsymbol{x}}
=
\boldsymbol{u}^T
\frac{\partial \boldsymbol{v}}{\partial \boldsymbol{x}}
+
\boldsymbol{v}^T
\frac{\partial \boldsymbol{u}}{\partial \boldsymbol{x}}
$$

In particular,

$$
\frac{\partial \boldsymbol{u}^T\boldsymbol{v}}{\partial \boldsymbol{v}}
=
\boldsymbol{u}^T
$$

For a vector-valued function

$$
\boldsymbol{y}
=
\begin{bmatrix}
y_1 & y_2 & \cdots & y_m
\end{bmatrix}^T
$$

the derivative with respect to $\boldsymbol{x}$ is

$$
\frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}}
=
\begin{bmatrix}
\frac{\partial y_1}{\partial \boldsymbol{x}}\\
\frac{\partial y_2}{\partial \boldsymbol{x}}\\
\vdots\\
\frac{\partial y_m}{\partial \boldsymbol{x}}
\end{bmatrix}
=
\begin{bmatrix}
\frac{\partial y_1}{\partial x_1}
&
\frac{\partial y_1}{\partial x_2}
&
\cdots
&
\frac{\partial y_1}{\partial x_n}\\
\frac{\partial y_2}{\partial x_1}
&
\frac{\partial y_2}{\partial x_2}
&
\cdots
&
\frac{\partial y_2}{\partial x_n}\\
\vdots
&
\vdots
&
\ddots
&
\vdots\\
\frac{\partial y_m}{\partial x_1}
&
\frac{\partial y_m}{\partial x_2}
&
\cdots
&
\frac{\partial y_m}{\partial x_n}
\end{bmatrix}
\in
\mathbb{R}^{m\times n}
$$

For a mapping from $\mathbb{R}^n$ to $\mathbb{R}^m$,

$$
\mathbf{F}(\boldsymbol{x})
=
\begin{bmatrix}
f_1(\boldsymbol{x})\\
f_2(\boldsymbol{x})\\
\vdots\\
f_m(\boldsymbol{x})
\end{bmatrix}
$$

the **Jacobian matrix** in numerator layout is

$$
\mathbf{J}
=
\frac{\partial \mathbf{F}}{\partial \boldsymbol{x}}
=
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1}
&
\frac{\partial f_1}{\partial x_2}
&
\cdots
&
\frac{\partial f_1}{\partial x_n}\\
\frac{\partial f_2}{\partial x_1}
&
\frac{\partial f_2}{\partial x_2}
&
\cdots
&
\frac{\partial f_2}{\partial x_n}\\
\vdots
&
\vdots
&
\ddots
&
\vdots\\
\frac{\partial f_m}{\partial x_1}
&
\frac{\partial f_m}{\partial x_2}
&
\cdots
&
\frac{\partial f_m}{\partial x_n}
\end{bmatrix}
\in
\mathbb{R}^{m\times n}
$$

If $\mathbf{A}$ is constant and the dimensions are compatible, then

$$
\frac{\partial \boldsymbol{x}}{\partial \boldsymbol{x}}
=
\mathbf{I}
$$

$$
\frac{\partial \mathbf{A}\boldsymbol{x}}{\partial \boldsymbol{x}}
=
\mathbf{A}
$$

$$
\frac{\partial \boldsymbol{x}^T\mathbf{A}}{\partial \boldsymbol{x}}
=
\mathbf{A}^T
$$

$$
\frac{\partial \mathbf{A}\boldsymbol{u}}{\partial \boldsymbol{x}}
=
\mathbf{A}
\frac{\partial \boldsymbol{u}}{\partial \boldsymbol{x}}
$$

For matrix derivatives, the derivative is generally a tensor. In the numerator-layout convention used here, the denominator matrix dimensions appear in transposed order.

If $\mathbf{X}\in\mathbb{R}^{n\times k}$ and $y$ is scalar, then

$$
\frac{\partial y}{\partial \mathbf{X}}
\in
\mathbb{R}^{k\times n}
$$

If $\mathbf{Y}\in\mathbb{R}^{m\times l}$ and $x$ is scalar, then

$$
\frac{\partial \mathbf{Y}}{\partial x}
\in
\mathbb{R}^{m\times l}
$$

If $\mathbf{X}\in\mathbb{R}^{n\times k}$ and $\boldsymbol{y}\in\mathbb{R}^{m\times 1}$, then

$$
\frac{\partial \boldsymbol{y}}{\partial \mathbf{X}}
\in
\mathbb{R}^{m\times k\times n}
$$

If $\mathbf{Y}\in\mathbb{R}^{m\times l}$ and $\boldsymbol{x}\in\mathbb{R}^{n\times 1}$, then

$$
\frac{\partial \mathbf{Y}}{\partial \boldsymbol{x}}
\in
\mathbb{R}^{m\times l\times n}
$$

If $\mathbf{X}\in\mathbb{R}^{n\times k}$ and $\mathbf{Y}\in\mathbb{R}^{m\times l}$, then

$$
\frac{\partial \mathbf{Y}}{\partial \mathbf{X}}
\in
\mathbb{R}^{m\times l\times k\times n}
$$

##### Denominator Layout

The denominator layout is also called the gradient formulation. The denominator dimensions are placed before the numerator dimensions. For a scalar function $y=f(\boldsymbol{x})$, the derivative with respect to a column vector is a column vector.

$$
\frac{\partial y}{\partial \boldsymbol{x}}
=
\begin{bmatrix}
\frac{\partial y}{\partial x_1}\\
\frac{\partial y}{\partial x_2}\\
\vdots\\
\frac{\partial y}{\partial x_n}
\end{bmatrix}
$$

For the sum of vector components,

$$
\frac{\partial \operatorname{sum}(\boldsymbol{x})}{\partial \boldsymbol{x}}
=
\mathbf{1}
$$

Let

$$
y
=
\boldsymbol{u}^T\boldsymbol{v}
$$

where $\boldsymbol{u}$ and $\boldsymbol{v}$ depend on $\boldsymbol{x}$. Under the denominator layout,

$$
\frac{\partial \boldsymbol{u}}{\partial \boldsymbol{x}}
\in
\mathbb{R}^{n\times m}
$$

$$
\frac{\partial \boldsymbol{v}}{\partial \boldsymbol{x}}
\in
\mathbb{R}^{n\times m}
$$

Therefore the dimensionally consistent product rule is

$$
\frac{\partial y}{\partial \boldsymbol{x}}
=
\frac{\partial \boldsymbol{u}}{\partial \boldsymbol{x}}
\boldsymbol{v}
+
\frac{\partial \boldsymbol{v}}{\partial \boldsymbol{x}}
\boldsymbol{u}
$$

In particular,

$$
\frac{\partial \boldsymbol{u}^T\boldsymbol{v}}{\partial \boldsymbol{v}}
=
\boldsymbol{u}
$$

For a vector-valued function $\boldsymbol{y}\in\mathbb{R}^{m}$,

$$
\frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}}
=
\begin{bmatrix}
\frac{\partial y_1}{\partial x_1}
&
\frac{\partial y_2}{\partial x_1}
&
\cdots
&
\frac{\partial y_m}{\partial x_1}\\
\frac{\partial y_1}{\partial x_2}
&
\frac{\partial y_2}{\partial x_2}
&
\cdots
&
\frac{\partial y_m}{\partial x_2}\\
\vdots
&
\vdots
&
\ddots
&
\vdots\\
\frac{\partial y_1}{\partial x_n}
&
\frac{\partial y_2}{\partial x_n}
&
\cdots
&
\frac{\partial y_m}{\partial x_n}
\end{bmatrix}
\in
\mathbb{R}^{n\times m}
$$

For a vector-to-vector derivative, the denominator-layout result is the transpose of the numerator-layout result.

$$
\left(
\frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}}
\right)_{\mathrm{den}}
=
\left(
\frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}}
\right)_{\mathrm{num}}^T
$$

If $\mathbf{A}$ is constant and the dimensions are compatible, then

$$
\frac{\partial \mathbf{A}\boldsymbol{u}}{\partial \boldsymbol{x}}
=
\frac{\partial \boldsymbol{u}}{\partial \boldsymbol{x}}
\mathbf{A}^T
$$

$$
\frac{\partial \mathbf{A}\boldsymbol{x}}{\partial \boldsymbol{x}}
=
\mathbf{A}^T
$$

$$
\frac{\partial \boldsymbol{x}^T\mathbf{A}}{\partial \boldsymbol{x}}
=
\mathbf{A}
$$

### Automatic Differentiation

Automatic differentiation applies the chain rule to compute derivatives efficiently.

For a computational chain

$$
x \rightarrow u_1 \rightarrow u_2 \rightarrow \cdots \rightarrow u_n \rightarrow y
$$

the derivative is

$$
\frac{\partial y}{\partial x}
=
\frac{\partial y}{\partial u_n}
\frac{\partial u_n}{\partial u_{n-1}}
\cdots
\frac{\partial u_1}{\partial x}
$$

##### Forward Accumulation

Forward accumulation computes derivatives from input to output.

$$
\frac{\partial y}{\partial x}
=
\frac{\partial y}{\partial u_n}
\left(
\frac{\partial u_n}{\partial u_{n-1}}
\left(
\cdots
\left(
\frac{\partial u_1}{\partial x}
\right)
\right)
\right)
$$

It follows the same direction as forward propagation. The time complexity is $O(n)$ and the space complexity is $O(n)$.

##### Reverse Accumulation

Reverse accumulation computes derivatives from output to input.

$$
\frac{\partial y}{\partial x}
=
\left(
\left(
\left(
\frac{\partial y}{\partial u_n}
\right)
\frac{\partial u_n}{\partial u_{n-1}}
\right)
\cdots
\right)
\frac{\partial u_1}{\partial x}
$$

This is the principle behind back propagation. The derivative of the output with respect to each intermediate variable is called an adjoint.

### Back Propagation

Consider a neural network with $L$ layer. Layer $l$ has $n_l$ neurons. The weight matrix of layer $l$ is
$$
\mathbf{W}^{(l)}
\in
\mathbb{R}^{n_l \times (n_{l-1}+1)}
$$

The last column corresponds to the bias weights. The output of layer $l-1$ is written as $\boldsymbol{a}^{(l-1)}$. The augmented output is

$$
\tilde{\boldsymbol{a}}^{(l-1)}
=
\begin{bmatrix}
\boldsymbol{a}^{(l-1)}\\
1
\end{bmatrix}
$$

The pre-activation value of layer $l$ is

$$
\boldsymbol{z}^{(l)}
=
\mathbf{W}^{(l)}
\tilde{\boldsymbol{a}}^{(l-1)}
$$

The activation value is

$$
\boldsymbol{a}^{(l)}
=
f(\boldsymbol{z}^{(l)})
$$

The loss function is

$$
J(\mathbf{W})
$$

##### Forward Pass

For each sample $\boldsymbol{x}$, compute layer by layer
$$
\boldsymbol{z}^{(1)}
=
\mathbf{W}^{(1)}
\tilde{\boldsymbol{a}}^{(0)}
$$

$$
\boldsymbol{a}^{(1)}
=
f(\boldsymbol{z}^{(1)})
$$

$$
\boldsymbol{z}^{(L)}
=
\mathbf{W}^{(L)}
\tilde{\boldsymbol{a}}^{(L-1)}
$$

$$
\hat{\boldsymbol{y}}
=
\boldsymbol{a}^{(L)}
=
f(\boldsymbol{z}^{(L)})
$$

Then compute the sample loss

$$
\ell(\hat{\boldsymbol{y}}, \boldsymbol{y})
$$

##### Error Term

Define the error term of layer $l$ as

$$
\boldsymbol{\delta}^{(l)}
=
\frac{\partial \ell}{\partial \boldsymbol{z}^{(l)}}
$$

For the output layer,

$$
\delta_i^{(L)}
=
\frac{\partial \ell}{\partial z_i^{(L)}}
=
\frac{\partial \ell}{\partial \hat{y}_i}
\frac{\partial \hat{y}_i}{\partial z_i^{(L)}}
=
\frac{\partial \ell}{\partial \hat{y}_i}
f'(z_i^{(L)})
$$

This formula assumes that the output activation is applied element-wise. For softmax output, cross terms in the Jacobian must be considered. For softmax with cross-entropy loss, the output-layer error is usually simplified as

$$
\boldsymbol{\delta}^{(L)}
=
\hat{\boldsymbol{y}}
-
\boldsymbol{y}
$$

For a hidden layer, the error is propagated backward from the next layer.

$$
\delta_i^{(l)}
=
f'(z_i^{(l)})
\sum_{j=1}^{n_{l+1}}
\delta_j^{(l+1)}
w_{ji}^{(l+1)}
$$

In vector form,

$$
\boldsymbol{\delta}^{(l)}
=
\left[
\left(
\mathbf{W}^{(l+1)}_{:,1:n_l}
\right)^T
\boldsymbol{\delta}^{(l+1)}
\right]
\odot
f'(\boldsymbol{z}^{(l)})
$$

Here $\odot$ denotes element-wise multiplication.

##### Gradient of Weights

For layer $l$, the gradient of the loss with respect to the weight matrix is

$$
\frac{\partial \ell}{\partial \mathbf{W}^{(l)}}
=
\boldsymbol{\delta}^{(l)}
\left(
\tilde{\boldsymbol{a}}^{(l-1)}
\right)^T
$$

For each weight,

$$
\frac{\partial \ell}{\partial w_{ji}^{(l)}}
=
\delta_j^{(l)}
\tilde{a}_i^{(l-1)}
$$

For batch training, the gradients are averaged over all samples.

$$
\frac{\partial J}{\partial \mathbf{W}^{(l)}}
=
\frac{1}{m}
\sum_{i=1}^{m}
\boldsymbol{\delta}_i^{(l)}
\left(
\tilde{\boldsymbol{a}}_i^{(l-1)}
\right)^T
$$

##### Parameter Update

The weights are updated by gradient descent.

$$
\mathbf{W}_{k+1}^{(l)}
=
\mathbf{W}_{k}^{(l)}
-
\eta
\frac{\partial J}{\partial \mathbf{W}^{(l)}}
$$

### Numerical Stability

For a deep neural network with $L$ layers, let the output of layer $l$ be

$$
\boldsymbol{h}^{(l)}
=
f_l(\boldsymbol{h}^{(l-1)})
$$

The gradient of the loss $\ell$ with respect to the weights of layer $l$ involves repeated matrix multiplication.

$$
\frac{\partial \ell}{\partial \mathbf{W}^{(l)}}
=
\frac{\partial \ell}{\partial \boldsymbol{h}^{(L)}}
\frac{\partial \boldsymbol{h}^{(L)}}{\partial \boldsymbol{h}^{(L-1)}}
\cdots
\frac{\partial \boldsymbol{h}^{(l+1)}}{\partial \boldsymbol{h}^{(l)}}
\frac{\partial \boldsymbol{h}^{(l)}}{\partial \mathbf{W}^{(l)}}
$$

When the multiplicative terms produced by the chain rule have magnitudes consistently less than one, the gradient norm may decay exponentially as it is propagated from deeper layers to earlier layers. This phenomenon is referred to as **vanishing gradients**.

Conversely, when these multiplicative terms have magnitudes consistently greater than one, the gradient norm may grow exponentially during back propagation. This phenomenon is referred to as **exploding gradients**.

For an MLP layer,

$$
\boldsymbol{h}^{(l)}
=
\sigma(\mathbf{W}^{(l)} \boldsymbol{h}^{(l-1)} + \boldsymbol{b}^{(l)})
$$

In this section, the bias term is written separately, so

$$
\mathbf{W}^{(l)}
\in
\mathbb{R}^{n_l\times n_{l-1}}
$$

The local Jacobian is

$$
\frac{\partial \boldsymbol{h}^{(l)}}{\partial \boldsymbol{h}^{(l-1)}}
=
\operatorname{diag}
\left(
\sigma'(\mathbf{W}^{(l)} \boldsymbol{h}^{(l-1)} + \boldsymbol{b}^{(l)})
\right)
\mathbf{W}^{(l)}
$$

Thus the gradient propagation from layer $l$ to layer $L$ contains

$$
\mathbf{M}^{(r)}
=
\operatorname{diag}
\left(
\sigma'(\mathbf{W}^{(r)} \boldsymbol{h}^{(r-1)} + \boldsymbol{b}^{(r)})
\right)
\mathbf{W}^{(r)}
$$

$$
\frac{\partial \boldsymbol{h}^{(L)}}{\partial \boldsymbol{h}^{(l)}}
=
\mathbf{M}^{(L)}
\mathbf{M}^{(L-1)}
\cdots
\mathbf{M}^{(l+1)}
=
\prod_{r=l+1}^{L}
\operatorname{diag}
\left(
\sigma'(\mathbf{W}^{(r)} \boldsymbol{h}^{(r-1)} + \boldsymbol{b}^{(r)})
\right)
\mathbf{W}^{(r)}
$$
