# Probability Theory

[toc]

### Random Events and Probability

##### Sample Space and Events

The sample space $\Omega$ is the set of all possible outcomes of a random experiment. An event is a subset of $\Omega$.

For events $A$ and $B$,

$$
A^c=\Omega\setminus A,
\qquad
A\setminus B=A\cap B^c
$$

$$
A\cup B=\{\omega:\omega\in A\text{ or }\omega\in B\},
\qquad
A\cap B=\{\omega:\omega\in A\text{ and }\omega\in B\}
$$

Events $A_1,A_2,\ldots$ are mutually exclusive if

$$
A_i\cap A_j=\varnothing,
\qquad i\ne j
$$

A collection $B_1,\ldots,B_n$ is a partition, or a complete group of events, if

$$
B_i\cap B_j=\varnothing\quad(i\ne j),
\qquad
\bigcup_{i=1}^{n}B_i=\Omega
$$

De Morgan's laws are

$$
\left(\bigcup_i A_i\right)^c=\bigcap_i A_i^c,
\qquad
\left(\bigcap_i A_i\right)^c=\bigcup_i A_i^c
$$

##### Probability and Its Properties

A probability measure $P$ satisfies

$$
P(A)\ge 0,
\qquad
P(\Omega)=1
$$

and for pairwise disjoint events $A_1,A_2,\ldots$,

$$
P\left(\bigcup_{i=1}^{\infty}A_i\right)
=\sum_{i=1}^{\infty}P(A_i)
$$

Important consequences are

$$
P(\varnothing)=0,
\qquad
P(A^c)=1-P(A)
$$

$$
A\subseteq B\Longrightarrow P(A)\le P(B)
$$

$$
P(A\setminus B)=P(A)-P(A\cap B)
$$

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

For three events,

$$
\begin{aligned}
P(A\cup B\cup C)
={}&P(A)+P(B)+P(C)\\
&-P(A\cap B)-P(A\cap C)-P(B\cap C)\\
&+P(A\cap B\cap C)
\end{aligned}
$$

##### Classical and Geometric Probability

If a finite sample space has $N$ equally likely outcomes and event $A$ contains $N_A$ outcomes, then

$$
P(A)=\frac{N_A}{N}
$$

The basic counting formulas are

$$
A_n^k=\frac{n!}{(n-k)!},
\qquad
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

For a geometric probability model with a uniformly selected point in a region $\Omega$,

$$
P(A)=\frac{m(A)}{m(\Omega)}
$$

where $m$ denotes the appropriate length, area, or volume.

### Conditional Probability and Independence

##### Conditional Probability and Multiplication Formula

For $P(B)>0$,

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

Hence,

$$
P(A\cap B)=P(B)P(A\mid B)=P(A)P(B\mid A)
$$

More generally,

$$
P\left(\bigcap_{i=1}^{n}A_i\right)
=P(A_1)P(A_2\mid A_1)\cdots
P\left(A_n\mid\bigcap_{i=1}^{n-1}A_i\right)
$$

##### Law of Total Probability and Bayes' Formula

If $B_1,\ldots,B_n$ is a partition with $P(B_i)>0$, then

$$
P(A)=\sum_{i=1}^{n}P(B_i)P(A\mid B_i)
$$

For $P(A)>0$,

$$
P(B_j\mid A)
=\frac{P(B_j)P(A\mid B_j)}{
\sum_{i=1}^{n}P(B_i)P(A\mid B_i)}
$$

##### Independence

Events $A$ and $B$ are independent if

$$
P(A\cap B)=P(A)P(B)
$$

Events $A_1,\ldots,A_n$ are mutually independent if for every nonempty subset $I\subseteq\{1,\ldots,n\}$,

$$
P\left(\bigcap_{i\in I}A_i\right)=\prod_{i\in I}P(A_i)
$$

Pairwise independence does not in general imply mutual independence.

##### Independent Repeated Trials

In $n$ independent Bernoulli trials with success probability $p$, the probability of exactly $k$ successes is

$$
\binom{n}{k}p^k(1-p)^{n-k}
$$

The probability of at least one success is

$$
1-(1-p)^n
$$

### Random Variables and Their Distributions

##### Random Variables and Distribution Functions

A random variable $X$ is a real-valued function on $\Omega$. Its cumulative distribution function is

$$
F_X(x)=P(X\le x)
$$

Every distribution function is nondecreasing and right-continuous, with

$$
\lim_{x\to-\infty}F_X(x)=0,
\qquad
\lim_{x\to\infty}F_X(x)=1
$$

For $a<b$,

$$
P(a<X\le b)=F_X(b)-F_X(a)
$$

##### Discrete Random Variables

A discrete random variable has a probability mass function

$$
p_X(x_k)=P(X=x_k)
$$

satisfying

$$
p_X(x_k)\ge 0,
\qquad
\sum_k p_X(x_k)=1
$$

Its distribution function is

$$
F_X(x)=\sum_{x_k\le x}p_X(x_k)
$$

##### Continuous Random Variables

A continuous random variable has a probability density function $f_X$ satisfying

$$
f_X(x)\ge 0,
\qquad
\int_{-\infty}^{\infty}f_X(x)\,dx=1
$$

and

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
$$

At every continuity point of $f_X$,

$$
f_X(x)=F_X'(x)
$$

For a continuous random variable,

$$
P(X=x)=0
$$

##### Distribution of a Function of One Random Variable

For $Y=g(X)$, the distribution-function method is

$$
F_Y(y)=P(g(X)\le y)
$$

If $X$ is continuous and $g$ is strictly monotone with inverse $x=g^{-1}(y)$, then

$$
f_Y(y)=f_X\bigl(g^{-1}(y)\bigr)
\left|\frac{d}{dy}g^{-1}(y)\right|
$$

The distribution-function method remains valid when $g$ is not monotone.

### Multidimensional Random Variables

##### Joint, Marginal, and Conditional Distributions

For a two-dimensional random variable $(X,Y)$, the joint distribution function is

$$
F_{X,Y}(x,y)=P(X\le x,Y\le y)
$$

For a discrete pair,

$$
p_{X,Y}(x_i,y_j)=P(X=x_i,Y=y_j)
$$

with marginal distributions

$$
p_X(x_i)=\sum_j p_{X,Y}(x_i,y_j),
\qquad
p_Y(y_j)=\sum_i p_{X,Y}(x_i,y_j)
$$

If $p_X(x_i)>0$, then

$$
P(Y=y_j\mid X=x_i)
=\frac{p_{X,Y}(x_i,y_j)}{p_X(x_i)}
$$

For a continuous pair with joint density $f_{X,Y}$,

$$
P\bigl((X,Y)\in D\bigr)
=\iint_D f_{X,Y}(x,y)\,dx\,dy
$$

The marginal densities are

$$
f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy
$$

$$
f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx
$$

If $f_X(x)>0$, then

$$
f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)}
$$

##### Independence of Random Variables

Random variables $X$ and $Y$ are independent if

$$
F_{X,Y}(x,y)=F_X(x)F_Y(y)
$$

For discrete random variables, this is equivalent to

$$
p_{X,Y}(x_i,y_j)=p_X(x_i)p_Y(y_j)
$$

For continuous random variables, it is equivalent to

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y)
$$

almost everywhere.

##### Distributions of Simple Functions

If $X$ and $Y$ are independent discrete random variables and $Z=X+Y$, then

$$
P(Z=z)=\sum_x P(X=x)P(Y=z-x)
$$

If $X$ and $Y$ are independent continuous random variables, then

$$
f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)\,dx
$$

For independent $X_1,\ldots,X_n$ with common distribution function $F$,

$$
P\left(\max_i X_i\le x\right)=F(x)^n
$$

$$
P\left(\min_i X_i>x\right)=\bigl(1-F(x)\bigr)^n
$$

Hence,

$$
F_{\max}(x)=F(x)^n,
\qquad
F_{\min}(x)=1-\bigl(1-F(x)\bigr)^n
$$

### Numerical Characteristics

##### Mathematical Expectation

For a discrete random variable,

$$
\mathbb{E}[X]=\sum_k x_kp_X(x_k)
$$

For a continuous random variable,

$$
\mathbb{E}[X]=\int_{-\infty}^{\infty}x f_X(x)\,dx
$$

For a function $g$,

$$
\mathbb{E}[g(X)]=\sum_k g(x_k)p_X(x_k)
$$

or

$$
\mathbb{E}[g(X)]=\int_{-\infty}^{\infty}g(x)f_X(x)\,dx
$$

For a function of two random variables,

$$
\mathbb{E}[g(X,Y)]
=\sum_i\sum_j g(x_i,y_j)p_{X,Y}(x_i,y_j)
$$

or

$$
\mathbb{E}[g(X,Y)]
=\iint_{\mathbb{R}^2}g(x,y)f_{X,Y}(x,y)\,dx\,dy
$$

Linearity gives

$$
\mathbb{E}[aX+bY+c]=a\mathbb{E}[X]+b\mathbb{E}[Y]+c
$$

If $X$ and $Y$ are independent and the expectations exist, then

$$
\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]
$$

##### Variance and Moments

The variance and standard deviation are

$$
\operatorname{Var}(X)=\mathbb{E}\bigl[(X-\mathbb{E}[X])^2\bigr],
\qquad
\operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}
$$

Equivalently,

$$
\operatorname{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2
$$

For constants $a$ and $b$,

$$
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)
$$

The $k$-th raw moment and $k$-th central moment are

$$
\mathbb{E}[X^k],
\qquad
\mathbb{E}\bigl[(X-\mathbb{E}[X])^k\bigr]
$$

##### Covariance and Correlation

The covariance is

$$
\operatorname{Cov}(X,Y)
=\mathbb{E}\bigl[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\bigr]
$$

Equivalently,

$$
\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]
$$

The correlation coefficient is

$$
\rho_{XY}
=\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}
$$

provided both variances are positive. It satisfies

$$
-1\le\rho_{XY}\le 1
$$

For constants $a_i$ and random variables $X_i$,

$$
\operatorname{Var}\left(\sum_{i=1}^{n}a_iX_i\right)
=\sum_{i=1}^{n}a_i^2\operatorname{Var}(X_i)
+2\sum_{i<j}a_ia_j\operatorname{Cov}(X_i,X_j)
$$

If the random variables are pairwise independent, all covariance terms vanish.

Independence implies zero covariance when the moments exist, but zero covariance does not generally imply independence. For jointly normal random variables, zero covariance is equivalent to independence.

##### Chebyshev's Inequality

If $\mathbb{E}[X]=\mu$ and $\operatorname{Var}(X)=\sigma^2<\infty$, then for every $\varepsilon>0$,

$$
P(|X-\mu|\ge\varepsilon)
\le\frac{\sigma^2}{\varepsilon^2}
$$

### Laws of Large Numbers and Central Limit Theorems

##### Convergence in Probability

A sequence $X_n$ converges in probability to $X$, written

$$
X_n\xrightarrow{P}X
$$

if for every $\varepsilon>0$,

$$
P(|X_n-X|\ge\varepsilon)\to 0
$$

##### Chebyshev's Law of Large Numbers

If $X_1,X_2,\ldots$ are pairwise independent with finite variances and

$$
\frac{1}{n^2}\sum_{i=1}^{n}\operatorname{Var}(X_i)\to 0
$$

then

$$
\frac{1}{n}\sum_{i=1}^{n}\left(X_i-\mathbb{E}[X_i]\right)
\xrightarrow{P}0
$$

In particular, if the variables have a common mean $\mu$ and uniformly bounded variances, then

$$
\frac{1}{n}\sum_{i=1}^{n}X_i\xrightarrow{P}\mu
$$

##### Bernoulli's Law of Large Numbers

If $N_n$ is the number of successes in $n$ independent Bernoulli trials with success probability $p$, then

$$
\frac{N_n}{n}\xrightarrow{P}p
$$

##### Khinchin's Law of Large Numbers

If $X_1,X_2,\ldots$ are independent and identically distributed with finite mean $\mu$, then

$$
\frac{1}{n}\sum_{i=1}^{n}X_i\xrightarrow{P}\mu
$$

##### De Moivre-Laplace Theorem

If $X_n\sim\operatorname{Binomial}(n,p)$ and $0<p<1$, then

$$
\frac{X_n-np}{\sqrt{np(1-p)}}
\xrightarrow{d}N(0,1)
$$

Thus, for large $n$,

$$
P(a\le X_n\le b)
\approx
\Phi\left(\frac{b+0.5-np}{\sqrt{np(1-p)}}\right)
-
\Phi\left(\frac{a-0.5-np}{\sqrt{np(1-p)}}\right)
$$

where the $0.5$ terms are the continuity correction.

##### Lindeberg-Levy Central Limit Theorem

If $X_1,X_2,\ldots$ are independent and identically distributed with

$$
\mathbb{E}[X_i]=\mu,
\qquad
\operatorname{Var}(X_i)=\sigma^2>0
$$

then

$$
\frac{\sum_{i=1}^{n}X_i-n\mu}{\sigma\sqrt{n}}
\xrightarrow{d}N(0,1)
$$

Equivalently, for large $n$,

$$
\bar{X}\approx N\left(\mu,\frac{\sigma^2}{n}\right)
$$
