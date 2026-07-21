# Probability Distributions

[toc]

### Discrete Distributions

##### Bernoulli Distribution

If

$$
X\sim\operatorname{Bernoulli}(p),
\qquad 0<p<1
$$

then

$$
P(X=x)=p^x(1-p)^{1-x},
\qquad x\in\{0,1\}
$$

and

$$
\mathbb{E}[X]=p,
\qquad
\operatorname{Var}(X)=p(1-p)
$$

##### Binomial Distribution

If $X$ is the number of successes in $n$ independent Bernoulli trials with success probability $p$, then

$$
X\sim\operatorname{Binomial}(n,p)
$$

and

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},
\qquad k=0,1,\ldots,n
$$

Its numerical characteristics are

$$
\mathbb{E}[X]=np,
\qquad
\operatorname{Var}(X)=np(1-p)
$$

##### Geometric Distribution

If $X$ is the number of trials required to obtain the first success, then

$$
X\sim\operatorname{Geometric}(p)
$$

with

$$
P(X=k)=(1-p)^{k-1}p,
\qquad k=1,2,\ldots
$$

Its numerical characteristics are

$$
\mathbb{E}[X]=\frac{1}{p},
\qquad
\operatorname{Var}(X)=\frac{1-p}{p^2}
$$

The geometric distribution is memoryless:

$$
P(X>m+n\mid X>m)=P(X>n)
$$

##### Hypergeometric Distribution

A population contains $N$ objects, of which $M$ are labeled as successes. If $n$ objects are sampled without replacement and $X$ is the number of successes, then

$$
X\sim\operatorname{Hypergeometric}(N,M,n)
$$

with

$$
P(X=k)
=\frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}
$$

for all integers $k$ satisfying

$$
\max(0,n-N+M)\le k\le\min(n,M)
$$

Its numerical characteristics are

$$
\mathbb{E}[X]=n\frac{M}{N}
$$

$$
\operatorname{Var}(X)
=n\frac{M}{N}\left(1-\frac{M}{N}\right)
\frac{N-n}{N-1}
$$

##### Poisson Distribution

If

$$
X\sim\operatorname{Poisson}(\lambda),
\qquad \lambda>0
$$

then

$$
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!},
\qquad k=0,1,2,\ldots
$$

and

$$
\mathbb{E}[X]=\lambda,
\qquad
\operatorname{Var}(X)=\lambda
$$

If $X\sim\operatorname{Poisson}(\lambda_1)$ and $Y\sim\operatorname{Poisson}(\lambda_2)$ are independent, then

$$
X+Y\sim\operatorname{Poisson}(\lambda_1+\lambda_2)
$$

##### Poisson Approximation to the Binomial Distribution

If

$$
n\to\infty,
\qquad
p\to 0,
\qquad
np\to\lambda
$$

then

$$
\binom{n}{k}p^k(1-p)^{n-k}
\to e^{-\lambda}\frac{\lambda^k}{k!}
$$

Thus, when $n$ is large and $p$ is small,

$$
\operatorname{Binomial}(n,p)
\approx\operatorname{Poisson}(np)
$$

### Continuous Distributions

##### Uniform Distribution

If

$$
X\sim U(a,b),
\qquad a<b
$$

then

$$
f_X(x)=
\begin{cases}
\dfrac{1}{b-a}, & a<x<b\\
0, & \text{otherwise}
\end{cases}
$$

and

$$
\mathbb{E}[X]=\frac{a+b}{2},
\qquad
\operatorname{Var}(X)=\frac{(b-a)^2}{12}
$$

##### Exponential Distribution

If

$$
X\sim\operatorname{Exp}(\lambda),
\qquad \lambda>0
$$

then

$$
f_X(x)=
\begin{cases}
\lambda e^{-\lambda x}, & x>0\\
0, & x\le 0
\end{cases}
$$

Its distribution function is

$$
F_X(x)=
\begin{cases}
0, & x\le 0\\
1-e^{-\lambda x}, & x>0
\end{cases}
$$

and

$$
\mathbb{E}[X]=\frac{1}{\lambda},
\qquad
\operatorname{Var}(X)=\frac{1}{\lambda^2}
$$

The exponential distribution is memoryless:

$$
P(X>s+t\mid X>s)=P(X>t)
$$

##### Normal Distribution

If

$$
X\sim N(\mu,\sigma^2),
\qquad \sigma>0
$$

then

$$
f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]
$$

and

$$
\mathbb{E}[X]=\mu,
\qquad
\operatorname{Var}(X)=\sigma^2
$$

The standard normal distribution is denoted by

$$
Z\sim N(0,1)
$$

with distribution function

$$
\Phi(z)=P(Z\le z)
$$

Standardization gives

$$
Z=\frac{X-\mu}{\sigma}\sim N(0,1)
$$

Therefore,

$$
P(a<X\le b)
=\Phi\left(\frac{b-\mu}{\sigma}\right)
-
\Phi\left(\frac{a-\mu}{\sigma}\right)
$$

and symmetry gives

$$
\Phi(-z)=1-\Phi(z)
$$

If $X_i\sim N(\mu_i,\sigma_i^2)$ are independent, then

$$
\sum_{i=1}^{n}a_iX_i
\sim
N\left(
\sum_{i=1}^{n}a_i\mu_i,
\sum_{i=1}^{n}a_i^2\sigma_i^2
\right)
$$

### Common Two-Dimensional Distributions

##### Two-Dimensional Uniform Distribution

A random vector $(X,Y)$ is uniformly distributed on a bounded region $D$ if

$$
f_{X,Y}(x,y)=
\begin{cases}
\dfrac{1}{\operatorname{Area}(D)}, & (x,y)\in D\\
0, & (x,y)\notin D
\end{cases}
$$

For any measurable region $A$,

$$
P\bigl((X,Y)\in A\bigr)
=\frac{\operatorname{Area}(A\cap D)}{\operatorname{Area}(D)}
$$

A constant joint density on a nonrectangular region does not generally imply that $X$ and $Y$ are independent.

##### Two-Dimensional Normal Distribution

A bivariate normal vector with means $\mu_X,\mu_Y$, standard deviations $\sigma_X,\sigma_Y$, and correlation coefficient $\rho$ has density

$$
\begin{aligned}
f_{X,Y}(x,y)
={}&\frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}\\
&\times\exp\left\{-\frac{1}{2(1-\rho^2)}
\left[
\frac{(x-\mu_X)^2}{\sigma_X^2}
-\frac{2\rho(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y}
+\frac{(y-\mu_Y)^2}{\sigma_Y^2}
\right]\right\}
\end{aligned}
$$

where $-1<\rho<1$.

Its marginal distributions are

$$
X\sim N(\mu_X,\sigma_X^2),
\qquad
Y\sim N(\mu_Y,\sigma_Y^2)
$$

For a bivariate normal vector,

$$
X\text{ and }Y\text{ are independent}
\Longleftrightarrow \rho=0
$$

### Distribution Summary

| distribution | support | expectation | variance |
| --- | --- | --- | --- |
| $\operatorname{Bernoulli}(p)$ | $0,1$ | $p$ | $p(1-p)$ |
| $\operatorname{Binomial}(n,p)$ | $0,1,\ldots,n$ | $np$ | $np(1-p)$ |
| $\operatorname{Geometric}(p)$ | $1,2,\ldots$ | $1/p$ | $(1-p)/p^2$ |
| $\operatorname{Hypergeometric}(N,M,n)$ | feasible integers $k$ | $nM/N$ | $n\frac{M}{N}(1-\frac{M}{N})\frac{N-n}{N-1}$ |
| $\operatorname{Poisson}(\lambda)$ | $0,1,2,\ldots$ | $\lambda$ | $\lambda$ |
| $U(a,b)$ | $a<x<b$ | $(a+b)/2$ | $(b-a)^2/12$ |
| $\operatorname{Exp}(\lambda)$ | $x>0$ | $1/\lambda$ | $1/\lambda^2$ |
| $N(\mu,\sigma^2)$ | $x\in\mathbb{R}$ | $\mu$ | $\sigma^2$ |
