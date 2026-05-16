# Probability Theory

[toc]

When a probability model is specified or assumed, probability theory provides a mathematical framework for describing and analyzing random phenomena. The basic objects include random events, random variables, probability distributions, and limit theorems.

### Numerical Characteristics

##### Moments

For a random variable $X$, the $k$th raw moment is

$$
\mathbb{E}\left[X^k\right]
$$

The $k$th central moment is

$$
\mathbb{E}\left[\left(X-\mathbb{E}[X]\right)^k\right]
$$

For random variables $X$ and $Y$, the mixed moment of order $k+l$ is

$$
\mathbb{E}\left[X^kY^l\right]
$$

The mixed central moment of order $k+l$ is

$$
\mathbb{E}\left[\left(X-\mathbb{E}[X]\right)^k\left(Y-\mathbb{E}[Y]\right)^l\right]
$$

##### Variance

The variance of $X$ is the second central moment. If $\mu=\mathbb{E}[X]$, then

$$
\operatorname{Var}(X)=\mathbb{E}\left[(X-\mu)^2\right]=\mathbb{E}\left[X^2\right]-\left(\mathbb{E}[X]\right)^2
$$

For constants $a$ and $b$,

$$
\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y)
$$

For observations $x_1,x_2,\ldots,x_n$ with sample mean $\bar{x}$, the unbiased sample variance is

$$
S^2=\frac{1}{n-1}\sum_{i=1}^{n}\left(x_i-\bar{x}\right)^2
$$

Equivalently,

$$
S^2=\frac{1}{n-1}\left(\sum_{i=1}^{n}x_i^2-n\bar{x}^2\right)
$$

##### Covariance

The covariance of $X$ and $Y$ is the second mixed central moment.

$$
\operatorname{Cov}(X,Y)=\mathbb{E}\left[(X-\mu_X)(Y-\mu_Y)\right]
$$

It can also be computed as

$$
\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]
$$

For paired observations $(x_i,y_i)$, the unbiased sample covariance is

$$
\operatorname{Cov}(X,Y)=\frac{1}{n-1}\sum_{i=1}^{n}\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)
$$

##### Covariance Matrix

For a random vector $\boldsymbol{\mathit{X}}=[X_1,X_2,\ldots,X_n]^T$, the covariance matrix is a real symmetric matrix whose $(i,j)$ entry is $\operatorname{Cov}(X_i,X_j)$.

$$
\boldsymbol{\Sigma}=\begin{bmatrix}
\operatorname{Cov}(X_1,X_1) & \operatorname{Cov}(X_1,X_2) & \cdots & \operatorname{Cov}(X_1,X_n) \\
\operatorname{Cov}(X_2,X_1) & \operatorname{Cov}(X_2,X_2) & \cdots & \operatorname{Cov}(X_2,X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\operatorname{Cov}(X_n,X_1) & \operatorname{Cov}(X_n,X_2) & \cdots & \operatorname{Cov}(X_n,X_n)
\end{bmatrix}
$$

##### Linear Portfolio Variance

Let

$$
R=x_1R_1+x_2R_2+x_3R_3
$$

where $x_1$, $x_2$, and $x_3$ are constants. Then

$$
\begin{aligned}
\operatorname{Var}(R)=&\ x_1^2\operatorname{Var}(R_1)+x_2^2\operatorname{Var}(R_2)+x_3^2\operatorname{Var}(R_3) \\
&+2x_1x_2\operatorname{Cov}(R_1,R_2)+2x_1x_3\operatorname{Cov}(R_1,R_3)+2x_2x_3\operatorname{Cov}(R_2,R_3)
\end{aligned}
$$

With $\boldsymbol{\mathit{x}}=[x_1,x_2,x_3]^T$ and covariance matrix $\boldsymbol{\Sigma}$,

$$
\operatorname{Var}(R)=\boldsymbol{\mathit{x}}^T\boldsymbol{\Sigma}\boldsymbol{\mathit{x}}
$$

### Distribution Functions

##### Cumulative Distribution Function

The cumulative distribution function, or CDF, is defined for both discrete and continuous random variables.

$$
F_X(x)=P(X\le x)
$$

For a continuous random variable with density $f_X$, 

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
$$

##### Quantile Function

The percent point function, or PPF, is also called the quantile function. It is the inverse of the CDF when the CDF is strictly increasing. More generally,

$$
F_X^{-1}(p)=\inf\left\{x\in\mathbb{R}:F_X(x)\ge p\right\}
$$

When the inverse is ordinary,

$$
F_X(x)=p\Rightarrow x=F_X^{-1}(p)
$$

##### Probability Mass and Density

The probability mass function, or PMF, describes the probability of each value of a discrete random variable.

$$
p_X(x_k)=P(X=x_k)
$$

The probability density function, or PDF, describes the density of probability for a continuous random variable.

$$
f_X(x)=\frac{dF_X(x)}{dx}
$$

A probability density integrates to one.

$$
\int_{-\infty}^{+\infty} f_X(x)\,dx=1
$$

For $a<b$,

$$
P(a<X\le b)=\int_a^b f_X(x)\,dx=F_X(b)-F_X(a)
$$

##### Joint and Marginal Distributions

For two random variables $X$ and $Y$, the joint CDF is

$$
F_{X,Y}(x,y)=P(X\le x,Y\le y)
$$

If $X$ and $Y$ have a joint density $f_{X,Y}$, then

$$
F_{X,Y}(x,y)=\int_{-\infty}^{x}\int_{-\infty}^{y}f_{X,Y}(u,v)\,dv\,du
$$

The marginal density of one variable is obtained by integrating the joint density over the other variable.

$$
f_X(x)=\int_{-\infty}^{+\infty}f_{X,Y}(x,y)\,dy
$$

$$
f_Y(y)=\int_{-\infty}^{+\infty}f_{X,Y}(x,y)\,dx
$$

##### Independent and Identically Distributed

Random variables are independent and identically distributed, or i.i.d., if they have the same probability distribution and are mutually independent. For independent continuous random variables $X$ and $Y$, the joint density factors as

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y)
$$

For discrete random variables, the same factorization holds for probability mass functions.

### Common Probability Distributions

##### Bernoulli Distribution

A Bernoulli distribution models a single trial with two mutually exclusive outcomes. If $X\sim\operatorname{Bernoulli}(p)$, where $0\le p\le 1$, then

$$
P(X=k)=p^k(1-p)^{1-k}\qquad k\in\{0,1\}
$$

The mean and variance are

$$
\mathbb{E}[X]=p
$$

$$
\operatorname{Var}(X)=p(1-p)
$$

Equivalently, a Bernoulli random variable is a binomial random variable with one trial.

$$
\operatorname{Bernoulli}(p)=\operatorname{Binomial}(1,p)
$$

##### Binomial Distribution

A binomial distribution models the number of successes in $n$ independent Bernoulli trials with success probability $p$. If $X\sim\operatorname{Binomial}(n,p)$, then

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}\qquad k=0,1,2,\ldots,n
$$

The mean and variance are

$$
\mathbb{E}[X]=np
$$

$$
\operatorname{Var}(X)=np(1-p)
$$

##### Poisson Distribution

A Poisson distribution models the number of independent events occurring in a fixed interval of time, area, or volume when the average rate is $\lambda$. If $X\sim\operatorname{Poisson}(\lambda)$, then

$$
P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}\qquad k=0,1,2,\ldots
$$

The mean and variance are both equal to $\lambda$.

$$
\mathbb{E}[X]=\operatorname{Var}(X)=\lambda
$$

If $X_i\sim\operatorname{Poisson}(\lambda_i)$ are mutually independent, then

$$
\sum_{i=1}^{m}X_i\sim\operatorname{Poisson}\left(\sum_{i=1}^{m}\lambda_i\right)
$$

For large $\lambda$, the Poisson distribution can be approximated by a normal distribution with the same mean and variance.

$$
\operatorname{Poisson}(\lambda)\approx N(\lambda,\lambda)
$$

The binomial distribution has a Poisson limit when $n\to\infty$, $p\to0$, and $np\to\lambda$.

$$
\operatorname{Binomial}(n,p)\xrightarrow{d}\operatorname{Poisson}(\lambda)
$$

##### Normal Distribution

The Gaussian distribution, or normal distribution, is a continuous distribution determined by its mean $\mu$ and variance $\sigma^2$. If $X\sim N(\mu,\sigma^2)$ with $\sigma>0$, then its probability density function is

$$
f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

The mean and variance are

$$
\mathbb{E}[X]=\mu
$$

$$
\operatorname{Var}(X)=\sigma^2
$$
