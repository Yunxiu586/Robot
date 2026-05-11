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
\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}^{(k)})^{\top}
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
\left[
\frac{\partial J}{\partial \theta_1}
\frac{\partial J}{\partial \theta_2}
\cdots
\frac{\partial J}{\partial \theta_p}
\right]^{\top}
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

The last column corresponds to the bias weights. The output of layer $l-1$ is written as $\boldsymbol{a}^{(l-1)}$, where the last component is fixed to $1$ for the bias term.

The pre-activation value of layer $l$ is

$$
\boldsymbol{z}^{(l)}
=
\mathbf{W}^{(l)}
\boldsymbol{a}^{(l-1)}
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
\boldsymbol{a}^{(0)}
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
\boldsymbol{a}^{(L-1)}
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
\right)^{\top}
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
\boldsymbol{a}^{(l-1)}
\right)^{\top}
$$

For each weight,

$$
\frac{\partial \ell}{\partial w_{ji}^{(l)}}
=
\delta_j^{(l)}
a_i^{(l-1)}
$$

For batch training, the gradients are averaged over all samples.

$$
\frac{\partial J}{\partial \mathbf{W}^{(l)}}
=
\frac{1}{m}
\sum_{i=1}^{m}
\boldsymbol{\delta}_i^{(l)}
\left(
\boldsymbol{a}_i^{(l-1)}
\right)^{\top}
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
\frac{\partial \boldsymbol{h}^{(L)}}{\partial \boldsymbol{h}^{(l)}}
=
\prod_{r=l+1}^{L}
\operatorname{diag}
\left(
\sigma'(\mathbf{W}^{(r)} \boldsymbol{h}^{(r-1)} + \boldsymbol{b}^{(r)})
\right)
\mathbf{W}^{(r)}
$$
