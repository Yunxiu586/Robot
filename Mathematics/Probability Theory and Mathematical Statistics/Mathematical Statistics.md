# Mathematical Statistics

[toc]

### Population, Sample, and Statistics

##### Population and Random Sample

A population is represented by a random variable $X$ with distribution $F(x;\theta)$, where $\theta$ is an unknown parameter.

A simple random sample from the population is

$$
X_1,X_2,\ldots,X_n
$$

where the variables are independent and identically distributed with the same distribution as $X$.

A statistic is a function of the sample that does not contain unknown parameters:

$$
T=T(X_1,\ldots,X_n)
$$

A realized value of the sample is denoted by

$$
x_1,x_2,\ldots,x_n
$$

and the corresponding realized value of a statistic is called an observed statistic.

##### Sample Mean, Variance, and Moments

The sample mean is

$$
\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

The sample variance is

$$
S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2
$$

The identity

$$
\sum_{i=1}^{n}(X_i-\bar{X})^2
=\sum_{i=1}^{n}X_i^2-n\bar{X}^2
$$

is frequently useful.

The $k$-th sample raw moment and sample central moment are

$$
A_k=\frac{1}{n}\sum_{i=1}^{n}X_i^k
$$

and

$$
B_k=\frac{1}{n}\sum_{i=1}^{n}(X_i-\bar{X})^k
$$

respectively. In particular,

$$
A_1=\bar{X},
\qquad
B_2=\frac{n-1}{n}S^2
$$

If the population has mean $\mu$ and variance $\sigma^2$, then

$$
\mathbb{E}[\bar{X}]=\mu,
\qquad
\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}
$$

and

$$
\mathbb{E}[S^2]=\sigma^2
$$

### Sampling Distributions

##### Quantile Convention

For a continuous distribution with distribution function $F$, its lower $p$-quantile $q_p$ is defined by

$$
P(X\le q_p)=p
$$

The notation used below is

$$
z_p,
\qquad
t_p(\nu),
\qquad\chi_p^2(\nu),
\qquad F_p(\nu_1,\nu_2)
$$

for the lower $p$-quantiles of the standard normal, Student's $t$, chi-square, and $F$ distributions.

##### Chi-Square Distribution

If $Z_1,\ldots,Z_\nu$ are independent standard normal random variables, then

$$
\sum_{i=1}^{\nu}Z_i^2\sim\chi_\nu^2
$$

Its expectation and variance are

$$
\mathbb{E}[\chi_\nu^2]=\nu,
\qquad
\operatorname{Var}(\chi_\nu^2)=2\nu
$$

If $U\sim\chi_{
u_1}^2$ and $V\sim\chi_{
u_2}^2$ are independent, then

$$
U+V\sim\chi_{\nu_1+\nu_2}^2
$$

##### Student's $t$ Distribution

If

$$
Z\sim N(0,1),
\qquad
U\sim\chi_\nu^2
$$

are independent, then

$$
T=\frac{Z}{\sqrt{U/\nu}}\sim t_\nu
$$

The $t$ distribution is symmetric about zero:

$$
t_p(\nu)=-t_{1-p}(\nu)
$$

##### $F$ Distribution

If

$$
U\sim\chi_{\nu_1}^2,
\qquad
V\sim\chi_{\nu_2}^2
$$

are independent, then

$$
F=\frac{U/\nu_1}{V/\nu_2}
\sim F_{\nu_1,\nu_2}
$$

If $F\sim F_{\nu_1,\nu_2}$, then

$$
\frac{1}{F}\sim F_{\nu_2,\nu_1}
$$

and the quantiles satisfy

$$
F_p(\nu_1,\nu_2)
=\frac{1}{F_{1-p}(\nu_2,\nu_1)}
$$

##### Sampling from a Normal Population

If

$$
X_1,\ldots,X_n\overset{\mathrm{i.i.d.}}{\sim}N(\mu,\sigma^2)
$$

then

$$
\bar{X}\sim N\left(\mu,\frac{\sigma^2}{n}\right)
$$

$$
\frac{(n-1)S^2}{\sigma^2}\sim\chi_{n-1}^2
$$

and $\bar{X}$ and $S^2$ are independent. Therefore,

$$
\frac{\bar{X}-\mu}{S/\sqrt{n}}
\sim t_{n-1}
$$

For two independent normal samples,

$$
X_1,\ldots,X_{n_1}\sim N(\mu_1,\sigma_1^2)
$$

$$
Y_1,\ldots,Y_{n_2}\sim N(\mu_2,\sigma_2^2)
$$

we have

$$
\frac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2}
\sim F_{n_1-1,n_2-1}
$$

If $\sigma_1^2=\sigma_2^2=\sigma^2$, define the pooled variance

$$
S_p^2
=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}
{n_1+n_2-2}
$$

Then

$$
\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}
{S_p\sqrt{1/n_1+1/n_2}}
\sim t_{n_1+n_2-2}
$$

### Point Estimation

##### Estimator and Estimate

An estimator is a statistic used to estimate an unknown parameter:

$$
\hat{\theta}=\hat{\theta}(X_1,\ldots,X_n)
$$

After the sample is observed, the numerical value

$$
\hat{\theta}(x_1,\ldots,x_n)
$$

is called an estimate.

##### Method of Moments

Suppose the distribution contains $k$ unknown parameters $\theta_1,\ldots,\theta_k$. Let

$$
\mu_j'(\theta_1,\ldots,\theta_k)=\mathbb{E}[X^j]
$$

be the $j$-th population raw moment. The method of moments sets

$$
A_j=\mu_j'(\theta_1,\ldots,\theta_k),
\qquad j=1,\ldots,k
$$

and solves for the unknown parameters.

For a one-parameter model, the first moment is usually used first:

$$
\bar{X}=\mathbb{E}[X]
$$

If the first moment does not identify the parameter, a higher moment may be required.

##### Maximum Likelihood Estimation

For a discrete distribution with probability mass function $p(x;\theta)$, the likelihood is

$$
L(\theta)
=\prod_{i=1}^{n}p(X_i;\theta)
$$

For a continuous distribution with density $f(x;\theta)$,

$$
L(\theta)
=\prod_{i=1}^{n}f(X_i;\theta)
$$

A maximum likelihood estimator is any value satisfying

$$
\hat{\theta}_{\mathrm{MLE}}
\in\arg\max_{\theta\in\Theta}L(\theta)
$$

It is usually easier to maximize the log-likelihood

$$
\ell(\theta)=\ln L(\theta)
$$

An interior maximum often satisfies

$$
\frac{d\ell(\theta)}{d\theta}=0
$$

but the parameter space, endpoints, and whether the support depends on $\theta$ must always be checked.

##### Evaluation of Estimators

An estimator $\hat{\theta}$ is unbiased if

$$
\mathbb{E}[\hat{\theta}]=\theta
$$

Its bias is

$$
\operatorname{Bias}(\hat{\theta})
=\mathbb{E}[\hat{\theta}]-\theta
$$

Among unbiased estimators of the same parameter, the estimator with smaller variance is more efficient. Thus, if

$$
\operatorname{Var}(\hat{\theta}_1)
<\operatorname{Var}(\hat{\theta}_2)
$$

then $\hat{\theta}_1$ is more efficient than $\hat{\theta}_2$.

An estimator is consistent if

$$
\hat{\theta}_n\xrightarrow{P}\theta
$$

A sufficient condition is

$$
\mathbb{E}[\hat{\theta}_n]\to\theta,
\qquad
\operatorname{Var}(\hat{\theta}_n)\to 0
$$

### Interval Estimation

##### Confidence Interval

A random interval

$$
\bigl(L(X_1,\ldots,X_n),U(X_1,\ldots,X_n)\bigr)
$$

is a confidence interval for $\theta$ with confidence level $1-\alpha$ if

$$
P_\theta\bigl(L<\theta<U\bigr)=1-\alpha
$$

The probability statement concerns the random interval before observing the sample, not the fixed parameter after the sample is observed.

##### One Normal Mean with Known Variance

For a sample from $N(\mu,\sigma^2)$ with known $\sigma^2$, a two-sided confidence interval for $\mu$ is

$$
\bar{X}\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

##### One Normal Mean with Unknown Variance

For a sample from $N(\mu,\sigma^2)$ with unknown $\sigma^2$, a two-sided confidence interval for $\mu$ is

$$
\bar{X}\pm t_{1-\alpha/2}(n-1)\frac{S}{\sqrt{n}}
$$

##### One Normal Variance

For a sample from $N(\mu,\sigma^2)$ with unknown $\mu$, a two-sided confidence interval for $\sigma^2$ is

$$
\left(
\frac{(n-1)S^2}{\chi_{1-\alpha/2}^2(n-1)},
\frac{(n-1)S^2}{\chi_{\alpha/2}^2(n-1)}
\right)
$$

##### Difference of Two Normal Means

If two independent normal populations have known variances, a confidence interval for $\mu_1-\mu_2$ is

$$
(\bar{X}-\bar{Y})
\pm z_{1-\alpha/2}
\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}
$$

If the variances are unknown but equal, a confidence interval is

$$
(\bar{X}-\bar{Y})
\pm t_{1-\alpha/2}(n_1+n_2-2)
S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

##### Ratio of Two Normal Variances

For two independent normal samples, a confidence interval for $\sigma_1^2/\sigma_2^2$ is

$$
\left(
\frac{S_1^2/S_2^2}{F_{1-\alpha/2}(n_1-1,n_2-1)},
\frac{S_1^2/S_2^2}{F_{\alpha/2}(n_1-1,n_2-1)}
\right)
$$

One-sided confidence intervals are obtained from the same pivotal quantities by using the corresponding one-sided quantiles.

### Hypothesis Testing

##### Basic Concepts

A hypothesis test compares a null hypothesis $H_0$ with an alternative hypothesis $H_1$.

A Type I error occurs when $H_0$ is rejected although it is true. Its probability is

$$
\alpha=P(\text{reject }H_0\mid H_0\text{ is true})
$$

A Type II error occurs when $H_0$ is not rejected although $H_1$ is true. Its probability is

$$
\beta=P(\text{do not reject }H_0\mid H_1\text{ is true})
$$

The significance level is the prescribed upper bound for the Type I error probability.

The standard procedure is:

1. state $H_0$ and $H_1$;
2. choose a statistic whose distribution under $H_0$ is known;
3. determine the rejection region at significance level $\alpha$;
4. calculate the observed statistic and make the decision.

For a two-sided test, the rejection probability is split between both tails. For a one-sided test, the rejection region lies in the direction specified by $H_1$.

##### Test for One Normal Mean with Known Variance

To test

$$
H_0:\mu=\mu_0
$$

when $\sigma^2$ is known, use

$$
Z=\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}
$$

For the two-sided alternative $H_1:\mu\ne\mu_0$, reject $H_0$ when

$$
|Z|>z_{1-\alpha/2}
$$

For $H_1:\mu>\mu_0$, reject when

$$
Z>z_{1-\alpha}
$$

For $H_1:\mu<\mu_0$, reject when

$$
Z<-z_{1-\alpha}
$$

##### Test for One Normal Mean with Unknown Variance

When $\sigma^2$ is unknown, use

$$
T=\frac{\bar{X}-\mu_0}{S/\sqrt{n}}
\sim t_{n-1}
$$

under $H_0$. The rejection regions have the same form as above, with normal quantiles replaced by $t$ quantiles.

##### Test for One Normal Variance

To test

$$
H_0:\sigma^2=\sigma_0^2
$$

use

$$
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}
\sim\chi_{n-1}^2
$$

For $H_1:\sigma^2\ne\sigma_0^2$, reject $H_0$ when

$$
\chi^2<\chi_{\alpha/2}^2(n-1)
$$

or

$$
\chi^2>\chi_{1-\alpha/2}^2(n-1)
$$

For $H_1:\sigma^2>\sigma_0^2$, reject when

$$
\chi^2>\chi_{1-\alpha}^2(n-1)
$$

For $H_1:\sigma^2<\sigma_0^2$, reject when

$$
\chi^2<\chi_{\alpha}^2(n-1)
$$

##### Test for the Difference of Two Normal Means

If two independent normal populations have known variances, test $H_0:\mu_1-\mu_2=\delta_0$ using

$$
Z=
\frac{(\bar{X}-\bar{Y})-\delta_0}
{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}
$$

If the variances are unknown but equal, use

$$
T=
\frac{(\bar{X}-\bar{Y})-\delta_0}
{S_p\sqrt{1/n_1+1/n_2}}
\sim t_{n_1+n_2-2}
$$

under $H_0$.

##### Test for the Ratio of Two Normal Variances

To test

$$
H_0:\frac{\sigma_1^2}{\sigma_2^2}=r_0
$$

use

$$
F=\frac{S_1^2/S_2^2}{r_0}
\sim F_{n_1-1,n_2-1}
$$

For the two-sided alternative, reject $H_0$ when

$$
F<F_{\alpha/2}(n_1-1,n_2-1)
$$

or

$$
F>F_{1-\alpha/2}(n_1-1,n_2-1)
$$

For an upper-tailed alternative, reject for large values of $F$; for a lower-tailed alternative, reject for small values of $F$.
