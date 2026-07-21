# Hyperparameters

[toc]

### Loss Functions

##### Entropy

The information content of an event $x$ is defined as the negative logarithm of its probability.

$$
I(x)=-\log p(x)
$$

**Entropy** measures the average uncertainty of a probability distribution. For a discrete random variable $X$ with probability mass function $p(x_i)=P(X=x_i)$,
$$
H(X)
=
\mathbb{E}[I(x)]
=
-\sum_{i=1}^{N}p(x_i)\log p(x_i)
$$

Among all distributions on the same finite support, the uniform distribution has the maximum entropy. A sharp distribution has low entropy because one outcome dominates.

For a Bernoulli distribution,

$$
H(X)
=
-p\log p-(1-p)\log(1-p)
$$

**Joint entropy** measures the uncertainty of two random variables considered together.

For random variables $X$ and $Y$ with joint distribution $p(x_i,y_j)$,

$$
H(X,Y)
=
-\sum_{i=1}^{N_1}
\sum_{j=1}^{N_2}
p(x_i,y_j)\log p(x_i,y_j)
$$

It can also be decomposed as

$$
H(X,Y)=H(Y)+H(X|Y)
$$

The joint entropy satisfies

$$
H(X,Y)\le H(X)+H(Y)
$$

The equality holds when $X$ and $Y$ are independent.

**Conditional entropy** measures the remaining uncertainty of one random variable after another random variable is known.
$$
H(X|Y)
=
-\sum_{i=1}^{N_1}
\sum_{j=1}^{N_2}
p(x_i,y_j)\log p(x_i|y_j)
$$

It is related to joint entropy by

$$
H(X|Y)=H(X,Y)-H(Y)
$$

For discrete random variables,

$$
H(X|Y)\le H(X)
$$

The reduction in uncertainty is the information that $Y$ provides about $X$.

**Mutual information** measures how much information two random variables share.
$$
I(X;Y)
=
H(X)+H(Y)-H(X,Y)
$$

Equivalently,

$$
I(X;Y)
=
H(X)-H(X|Y)
=
H(Y)-H(Y|X)
$$

Using the joint and marginal distributions,

$$
I(X;Y)
=
\sum_{i=1}^{N_1}
\sum_{j=1}^{N_2}
p(x_i,y_j)
\log
\frac{p(x_i,y_j)}{p(x_i)p(y_j)}
$$

Mutual information is always non-negative.

$$
I(X;Y)\ge 0
$$

When $X$ and $Y$ are independent,

$$
I(X;Y)=0
$$

Mutual information can capture both linear and nonlinear dependence between variables.

##### Cross-Entropy

**Cross-entropy** measures the average coding cost when the true distribution is $p$, but another distribution $q$ is used for encoding.
$$
H(p,q)
=
-\sum_{i=1}^{N}p(x_i)\log q(x_i)
$$

Equivalently,

$$
H(p,q)
=
\mathbb{E}_{x\sim p}
[-\log q(x)]
$$

If $q$ is close to $p$, the cross-entropy is small. If $q$ assigns low probability to events that often occur under $p$, the cross-entropy becomes large.

**KL divergence** measures the information loss caused by using $q$ to approximate the true distribution $p$.
$$
D_{\mathrm{KL}}(p\|q)
=
\sum_{i=1}^{N}
p(x_i)
\log
\frac{p(x_i)}{q(x_i)}
$$

Cross-entropy can be decomposed into entropy and KL divergence.

$$
H(p,q)=H(p)+D_{\mathrm{KL}}(p\|q)
$$

Since $H(p)$ is fixed for a given true distribution, minimizing cross-entropy is equivalent to minimizing KL divergence.

KL divergence is non-negative.

$$
D_{\mathrm{KL}}(p\|q)\ge 0
$$

However, KL divergence is not symmetric.

$$
D_{\mathrm{KL}}(p\|q)\ne D_{\mathrm{KL}}(q\|p)
$$

Therefore, it should not be directly treated as a distance metric.

**JS divergence** is a symmetric and smoothed version of KL divergence.

First define the average distribution

$$
m(x_i)=\frac{1}{2}\left[p(x_i)+q(x_i)\right]
$$

Then the JS divergence is

$$
D_{\mathrm{JS}}(p\|q)
=
\frac{1}{2}
\left[
D_{\mathrm{KL}}(p\|m)
+
D_{\mathrm{KL}}(q\|m)
\right]
$$

JS divergence is symmetric.

$$
D_{\mathrm{JS}}(p\|q)=D_{\mathrm{JS}}(q\|p)
$$

With natural logarithms, it is bounded by

$$
0\le D_{\mathrm{JS}}(p\|q)\le \log 2
$$

With base-2 logarithms, the upper bound is $1$. A smaller JS divergence means that the two distributions are more similar.

##### Cross-Entropy Loss

In classification tasks, cross-entropy loss measures the difference between the true label distribution and the predicted probability distribution.

Let the model output be

$$
\hat{\boldsymbol{p}}
=
\begin{bmatrix}
\hat{p}_1 & \hat{p}_2 & \cdots & \hat{p}_K
\end{bmatrix}^{T}
$$

For one sample, the categorical cross-entropy loss is

$$
L
=
-\sum_{j=1}^{K}
y_j\log \hat{p}_j
$$

Since the true label is one-hot, only the true class $k$ contributes to the loss.

$$
L=-\log \hat{p}_k
$$

Here, $\hat{p}_k$ is the predicted probability assigned to the true class.

For a dataset with $m$ samples, the average cross-entropy loss is

$$
J(\boldsymbol{\theta})
=
-\frac{1}{m}
\sum_{i=1}^{m}
\sum_{j=1}^{K}
y_{ij}\log \hat{p}_{ij}
$$

The optimization objective is

$$
\boldsymbol{\theta}^{*}
=
\arg\min_{\boldsymbol{\theta}}
J(\boldsymbol{\theta})
$$

Cross-entropy strongly penalizes confident wrong predictions. If the model assigns a very small probability to the true class, the loss becomes large.

For binary classification, the label is

$$
y\in\{0,1\}
$$

Let $\hat{p}$ be the predicted probability of class $1$. The binary cross-entropy loss is

$$
L_{\mathrm{BCE}}
=
-y\log \hat{p}
-(1-y)\log(1-\hat{p})
$$

If $y=1$, the loss becomes

$$
L_{\mathrm{BCE}}=-\log \hat{p}
$$

If $y=0$, the loss becomes

$$
L_{\mathrm{BCE}}=-\log(1-\hat{p})
$$

##### MSE Loss

**Mean squared error loss** measures the average squared difference between the predicted value and the true value. It is commonly used in regression tasks.

For a dataset with $m$ samples,

$$
J(\boldsymbol{\theta})
=
\frac{1}{m}
\sum_{i=1}^{m}
(\hat{y}^{(i)}-y^{(i)})^2
$$

For vector-valued outputs, let the prediction and target be

$$
\hat{\boldsymbol{y}},
\boldsymbol{y}
\in \mathbb{R}^{K}
$$

Then the MSE loss for one sample can be written as

$$
L_{\mathrm{MSE}}
=
\frac{1}{K}
\sum_{j=1}^{K}
(\hat{y}_j-y_j)^2
=
\frac{1}{K}
\|\hat{\boldsymbol{y}}-\boldsymbol{y}\|_2^2
$$

MSE gives a larger penalty to large prediction errors because the error is squared.

For the averaged vector form,

$$
L_{\mathrm{MSE}}
=
\frac{1}{K}
\|\hat{\boldsymbol{y}}-\boldsymbol{y}\|_2^2
$$

the gradient is

$$
\nabla_{\hat{\boldsymbol{y}}}L_{\mathrm{MSE}}
=
\frac{2}{K}
(\hat{\boldsymbol{y}}-\boldsymbol{y})
$$

For the half squared error,

$$
L=\frac{1}{2}(\hat{y}-y)^2
$$

the derivative is

$$
\frac{\partial L}{\partial \hat{y}}
=
\hat{y}-y
$$

MSE is sensitive to outliers because very large errors dominate the loss.

### Regularization

##### Vector Norms

For a vector $\boldsymbol{x} \in \mathbb{R}^{n}$, a norm is a mapping

$$
\|\cdot\|:\mathbb{R}^{n}\rightarrow \mathbb{R}_{\ge 0}
$$

that measures the magnitude of a vector. A valid vector norm should satisfy 3 basic properties.

+ For any $\boldsymbol{x}\in\mathbb{R}^{n}$, the norm is **non-negative**, and it is 0 only when the vector itself is the zero vector

$$
\|\boldsymbol{x}\|\ge 0
$$

+ For any scalar $a\in\mathbb{R}$, scaling the vector scales its norm by the absolute value of the scalar

$$
\|a\boldsymbol{x}\|=|a|\|\boldsymbol{x}\|
$$

+ For any $\boldsymbol{x},\boldsymbol{y}\in\mathbb{R}^{n}$, the norm satisfies the triangle inequality

$$
\|\boldsymbol{x}+\boldsymbol{y}\|\le \|\boldsymbol{x}\|+\|\boldsymbol{y}\|
$$

The $L_{1}$ norm, also called the Manhattan norm, sums the absolute values of all vector components

$$
\|\boldsymbol{x}\|_{1}=\sum_{i=1}^{n}|x_i|
$$

The $L_{2}$ norm, also called the Euclidean norm, corresponds to the ordinary straight-line distance in Euclidean space

$$
\|\boldsymbol{x}\|_{2}=\sqrt{\sum_{i=1}^{n}x_i^2}
$$

The $L_{\infty}$ norm, also called the Chebyshev norm, measures the largest absolute component of the vector

$$
\|\boldsymbol{x}\|_{\infty}=\max_{1\le i\le n}|x_i|
$$

The general $L_{p}$ norm is defined as

$$
\|\boldsymbol{x}\|_{p}=\left(\sum_{i=1}^{n}|x_i|^p\right)^{\frac{1}{p}}
$$

where $p\ge 1$. The $L_{1}$, $L_{2}$, and $L_{\infty}$ norms can be viewed as special cases or limiting cases of the $L_{p}$ family.

##### Regularization Methods

Regularization reduces overfitting by limiting model complexity or making the training process more robust.

A common regularized objective has the form

$$
J_{\mathrm{reg}}(\boldsymbol{\theta})
=
J(\boldsymbol{\theta})
+
\lambda \Omega(\boldsymbol{\theta})
$$

where $J(\boldsymbol{\theta})$ is the original training loss, $\Omega(\boldsymbol{\theta})$ is the regularization term, and $\lambda$ controls the strength of regularization.

##### $L_2$ regularization

$L_2$ regularization penalizes large parameters by adding the squared $L_2$ norm to the original training loss.

$$
J_{\mathrm{reg}}(\boldsymbol{\theta})
=
J(\boldsymbol{\theta})
+
\frac{\lambda}{2}
\|\boldsymbol{\theta}\|_2^2
$$

The gradient is

$$
\nabla_{\boldsymbol{\theta}}J_{\mathrm{reg}}(\boldsymbol{\theta})
=
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
+
\lambda \boldsymbol{\theta}
$$

Thus the gradient descent update becomes

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_{t}
-
\eta
\left(
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta}_{t})
+
\lambda \boldsymbol{\theta}_{t}
\right)
$$

Equivalently,

$$
\boldsymbol{\theta}_{t+1}
=
(1-\eta\lambda)\boldsymbol{\theta}_{t}
-
\eta
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta}_{t})
$$

Since usually $\eta\lambda<1$, the parameter vector is slightly shrunk at each update. This shrinkage helps prevent very large weights and usually improves generalization.

##### Weight decay

Weight decay is closely related to $L_2$ regularization. For standard gradient descent or SGD, they have the same update form. For adaptive optimizers, classical $L_2$ regularization and decoupled weight decay are generally not equivalent.
$$
\boldsymbol{\theta}_{t+1}
=
(1-\eta\lambda)\boldsymbol{\theta}_{t}
-
\eta
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta}_{t})
$$

The factor $(1-\eta\lambda)$ directly decays the parameters before applying the ordinary gradient update, so the method is called weight decay. Here $\lambda$ is the weight decay coefficient. A larger $\lambda$ gives stronger shrinkage.

##### $L_1$ regularization

$L_1$ regularization penalizes the absolute values of parameters.
$$
J_{\mathrm{reg}}(\boldsymbol{\theta})
=
J(\boldsymbol{\theta})
+
\lambda \|\boldsymbol{\theta}\|_1
$$

It encourages sparsity, meaning that some parameters may become exactly or nearly zero.

##### Dropout

Dropout randomly sets part of the hidden activations to zero during training.

Let the activation vector be

$$
\boldsymbol{h}
\in \mathbb{R}^{d}
$$

A binary mask is sampled componentwise as

$$
m_j\sim \operatorname{Bernoulli}(p),
\qquad j=1,\dots,d
$$

where $p$ is the keep probability. The dropped activation is

$$
\tilde{\boldsymbol{h}}
=
\frac{\boldsymbol{m}\odot \boldsymbol{h}}{p}
$$

Dropout prevents neurons from relying too strongly on specific other neurons, which reduces co-adaptation.

During inference, dropout is disabled, and the full network is used without additional scaling.

##### Early stopping

Early stopping stops training when the validation loss no longer improves.

Let the training loss and validation loss be

$$
J_{\mathrm{train}},
J_{\mathrm{val}}
$$

If $J_{\mathrm{train}}$ keeps decreasing but $J_{\mathrm{val}}$ starts increasing, the model is likely overfitting.

Early stopping selects the parameters with the best validation performance.

$$
\boldsymbol{\theta}^{*}
=
\arg\min_{\boldsymbol{\theta}_t}
J_{\mathrm{val}}(\boldsymbol{\theta}_t)
$$

**Patience** is the number of epochs allowed without validation improvement before training is stopped.

If the validation loss does not improve for $P$ consecutive epochs, training is stopped.

##### Data augmentation

Data augmentation increases the diversity of training data by applying label-preserving transformations.

For an input sample $\boldsymbol{x}$, an augmented sample can be written as

$$
\tilde{\boldsymbol{x}}
=
T(\boldsymbol{x})
$$

where $T$ is a transformation that should not change the semantic label. Common examples include flipping, cropping, rotation and noise injection.

Data augmentation strength controls how strongly the input data is transformed.

For an input sample,

$$
\tilde{\boldsymbol{x}}
=
T_{\alpha}(\boldsymbol{x})
$$

where $\alpha$ controls the strength of the transformation. For example, $\alpha$ may represent the rotation angle, crop ratio, noise level, or color distortion strength.

### Optimizer

### Learning Rate

The learning rate controls the step size of each parameter update.

For gradient descent,

$$
\boldsymbol{\theta}
\leftarrow
\boldsymbol{\theta}
-
\eta
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
$$

where $\eta$ is the learning rate.

### Batch Size

The batch size is the number of training samples used to compute one gradient update.

For a mini-batch $\mathcal{B}$ with size $B$, the mini-batch loss is

$$
J_{\mathcal{B}}(\boldsymbol{\theta})
=
\frac{1}{B}
\sum_{i\in \mathcal{B}}
L^{(i)}(\boldsymbol{\theta})
$$

### Epoch

An **epoch** means that the model has gone through the entire training dataset once. The number of epochs controls how many times the model repeatedly learns from the training dataset.

Suppose the training dataset has $m$ samples and the batch size is $B$. An **iteration** means one parameter update. The number of samples used in one iteration equals the batch size.

$$
\text{iterations per epoch}
=
\left\lceil
\frac{m}{B}
\right\rceil
$$

This assumes that the last incomplete mini-batch is kept. If it is dropped, the number is $\left\lfloor m/B \right\rfloor$.

### Activation Functions

##### Sigmoid

The Sigmoid function maps a real-valued input into the interval $(0,1)$, so it is often used when a scalar output needs to be interpreted as a probability.

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Its derivative can be written only using the function value itself.

$$
\sigma'(x)=\sigma(x)\left(1-\sigma(x)\right)
$$

When $x$ is very large or small, the output becomes close to $1$ or $0$, and the derivative becomes close to $0$.

##### Tanh

The hyperbolic tangent function maps real-valued inputs into $(-1,1)$.

$$
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
$$

It can also be written through the Sigmoid function.

$$
\tanh(x)=2\sigma(2x)-1
$$

The derivative is

$$
\tanh'(x)=1-\tanh^2(x)
$$

Tanh is zero-centered, which is usually more suitable for hidden representations. 

##### Softmax

Softmax maps a vector of logits into a probability distribution over $K$ classes. Let the logit vector be

$$
\boldsymbol{z}=
\begin{bmatrix}
z_1 & z_2 & \cdots & z_K
\end{bmatrix}^{T}
$$

The Softmax output is

$$
\hat{p}_j=\operatorname{softmax}(\boldsymbol{z})_j
=\frac{e^{z_j}}{\sum_{k=1}^{K}e^{z_k}}
$$

The output vector is

$$
\hat{\boldsymbol{p}}=
\begin{bmatrix}
\hat{p}_1 & \hat{p}_2 & \cdots & \hat{p}_K
\end{bmatrix}^{T}
$$

Each component satisfies

$$
0<\hat{p}_j<1
$$

and the components sum to one.

$$
\sum_{j=1}^{K}\hat{p}_j=1
$$

Softmax gives larger logits larger probabilities and smaller logits smaller probabilities.

Softmax is invariant to adding the same constant to every logit.
$$
\operatorname{softmax}(\boldsymbol{z})
=
\operatorname{softmax}(\boldsymbol{z}+C\boldsymbol{1})
$$

##### ReLU

ReLU is the rectified linear unit.

$$
\operatorname{ReLU}(x)=\max(0,x)
$$

Its derivative is

$$
\operatorname{ReLU}'(x)=
\begin{cases}
0 & x<0 \\
1 & x>0
\end{cases}
$$

ReLU is simple and computationally efficient.

The main weakness is the **dying ReLU problem**. If a neuron stays in the negative region for a long time, its output is always $0$, and the gradient passed through it is also $0$.

##### Leaky ReLU

Leaky ReLU modifies ReLU by allowing a small nonzero slope in the negative region.

$$
\operatorname{LeakyReLU}(x)=\max(\alpha x,x)
$$

Equivalently,

$$
\operatorname{LeakyReLU}(x)=
\begin{cases}
\alpha x & x\le 0 \\
x & x>0
\end{cases}
$$

Its derivative is

$$
\operatorname{LeakyReLU}'(x)=
\begin{cases}
\alpha & x<0 \\
1 & x>0
\end{cases}
$$

where $0<\alpha<1$ is usually a small constant.

Leaky ReLU keeps most advantages of ReLU, while reducing the chance that neurons become permanently inactive.