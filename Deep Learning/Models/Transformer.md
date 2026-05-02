# Transformer

The Transformer is a sequence transduction model that **relies solely on self-attention mechanisms**. This makes the model more **parallelizable** during training. Self-attention also lets the model draw global dependencies between positions directly, so long-range dependencies have shorter paths to learn. Multi-head attention further allows the model to attend to different representation subspaces at different positions. 

[toc]

### Architecture

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/image-20260502162255648.png" alt="image-20260502162255648" style="zoom: 28%;" />

### Encoder

##### Input Embedding

The input tokens are discrete symbols. The model first uses learned embeddings to convert them into vectors of dimension $d_{\text{model}}$. In the base Transformer,

$$
d_{\text{model}}=512
$$

For an input token $x_i$, the embedding layer produces a vector

$$
\boldsymbol{e}_i \in \mathbb{R}^{d_{\text{model}}}
$$

The embedding layer does not yet encode word order. It only maps each token into a continuous representation space where semantic and syntactic information can be learned.

The same idea is used on the decoder side output tokens are also converted to vectors of dimension $d_{\text{model}}$. The model **shares the same weight matrix** between the two embedding layers and the pre-softmax linear transformation. In the embedding layers, the weights are multiplied by

$$
\sqrt{d_{\text{model}}}
$$

This rescales the token embeddings before they are added to the positional encodings. Since the embeddings are then passed into the encoder and decoder stacks as $d_{\text{model}}$-dimensional representations, the scaling keeps their magnitude suitable for the following attention and feed-forward sub-layers.

##### Positional Encoding

 The order information is injected by adding positional encodings to the input embeddings at the bottoms of the encoder and decoder stacks.

The embedding and positional encoding have the same dimension, so they can be summed

$$
\boldsymbol{h}_i^{(0)}=\boldsymbol{e}_i+\boldsymbol{p}_i
$$

where $\boldsymbol{p}_i\in\mathbb{R}^{d_{\text{model}}}$ is the positional encoding at position $i$.

The sinusoidal positional encoding is defined as

$$
PE_{(pos,2i)}=\sin\left(pos/10000^{2i/d_{\text{model}}}\right)
$$

$$
PE_{(pos,2i+1)}=\cos\left(pos/10000^{2i/d_{\text{model}}}\right)
$$

Here, $pos$ is the position and $i$ is the dimension index. Each dimension corresponds to a sinusoid, and the wavelengths form a geometric progression.

The reason for this design is that, for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$. This helps the model learn to attend by relative positions.

##### Encoder Stack

The encoder is composed of a stack of

$$
N=6
$$

identical layers. Each encoder layer has two sub-layers.
$$
\text{Multi-Head Self-Attention}
\rightarrow
\text{Position-wise Feed-Forward Network}.
$$
Each sub-layer is wrapped by a residual connection followed by layer normalization

$$
\operatorname{LayerNorm}(\boldsymbol{x}+\operatorname{Sublayer}(\boldsymbol{x})).
$$

The sub-layer learns a transformation, while the residual path keeps the original representation available. The residual connection helps optimization, and layer normalization stabilizes the scale of hidden representations.

##### Self-Attention

In encoder self-attention, **queries, keys, and values all come from the output of the previous encoder layer**. For each position, the model forms three vectors $\boldsymbol{q}_i, \boldsymbol{k}_i, \boldsymbol{v}_i.$

They are obtained by learned linear projections from the current hidden representation. Intuitively

$$
\boldsymbol{q}_i
$$

represents what position $i$ is looking for,

$$
\boldsymbol{k}_j
$$

represents what position $j$ offers for matching, and

$$
\boldsymbol{v}_j
$$

contains the information that will be aggregated if position $j$ is attended to.

An attention function maps a query and a set of key-value pairs to an output. For one query position, the **attention weights** are
$$
\alpha_{ij}
=
\operatorname{softmax}_j
\left(
\frac{\boldsymbol{q}_i\boldsymbol{k}_j^{T}}{\sqrt{d_k}}
\right)
$$

The weight assigned to each value is computed by a **compatibility function** of the **query** with the corresponding **key**.

The output vector at position $i$ is
$$
\boldsymbol{o}_i
=
\sum_j \alpha_{ij}\boldsymbol{v}_j.
$$

This lets each input position attend to all positions in the previous encoder layer. 

Therefore, the representation at one token can directly incorporate information from any other token, regardless of distance.

Here, $n$ is the sequence length, and $d$ is the representation dimension of each token.

+ For self-attention, the **complexity per-layer** is $O(n^2\cdot d)$ because each of the $n$ positions attends to all $n$ positions, and each compatibility computation involves a $d$-dimensional representation. 

+ The **sequential operations** is $O(1)$ because all positions can be computed in parallel by matrix multiplication. 

+ The **maximum path length** is $O(1)$ because any two positions can be directly connected within one self-attention layer, which makes long-range dependencies easier to learn.

##### Scaled Dot-Product Attention

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/image-20260502162229980.png" alt="image-20260502162229980" style="zoom: 28%;" />

The input consists of queries and keys of dimension $d_k$, and values of dimension $d_v$. 

In practice, the attention function is computed on a set of queries simultaneously, packed together into a matrix $Q$. The keys and values are also packed together into matrices $K$ and $V$.

Assume there are $n_q$ query positions and $n_k$ key-value positions. Then the matrix dimensions are

$$
Q\in\mathbb{R}^{n_q\times d_k}
$$

$$
K\in\mathbb{R}^{n_k\times d_k}
$$

$$
V\in\mathbb{R}^{n_k\times d_v}
$$

The **dot product** $QK^T$ measures compatibility between queries and keys.
$$
QK^T\in\mathbb{R}^{n_q\times n_k}
$$

The **scaling factor**
$$
\frac{1}{\sqrt{d_k}}
$$
prevents the softmax function from entering regions of extremely small gradients when $d_k$ is large, mitigating the vanishing gradient issue of the dot product.

The **softmax** converts compatibility scores into attention weights. Multiplication by $V$ forms the weighted sum of values.
$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
$$

Therefore, each query position produces one output vector of dimension $d_v$. Each row of the attention matrix represents the attention distribution of one query position over all key-value positions, showing how much that token attends to every token.
$$
\text {Attention}(Q,K,V)\in\mathbb{R}^{n_q\times d_v}
$$
The optional **mask** is applied before the softmax. It is used to mask out illegal connections by setting their attention scores to $-\infty$.

With a mask matrix $M$, scaled dot-product attention can be written as

$$
\operatorname{MaskedAttention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}} + M
\right)V
$$

where

$$
M_{ij}=0
$$

for allowed connections, and

$$
M_{ij}=-\infty
$$

for illegal connections.

##### Multi-Head Attention

<img src="/home/yunxiu/Desktop/ROS2_study/Pictures/image-20260502162536180.png" alt="image-20260502162536180" style="zoom: 28%;" />

Instead of performing a single attention function with $d_{\text{model}}$-dimensional queries, keys, and values, the Transformer linearly projects them $h$ times with different learned projections.
$$
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O
$$

where

$$
\operatorname{head}_i
=
\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V)
$$

The projection matrices are

$$
W_i^Q\in\mathbb{R}^{d_{\text{model}}\times d_k}
$$

$$
W_i^K\in\mathbb{R}^{d_{\text{model}}\times d_k}
$$

$$
W_i^V\in\mathbb{R}^{d_{\text{model}}\times d_v}
$$

$$
W^O\in\mathbb{R}^{hd_v\times d_{\text{model}}}
$$

In the base model,

$$
h=8,\qquad d_k=d_v=d_{\text{model}}/h=64
$$

Each head attends in a different representation subspace. This allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, the weighted averaging process may inhibit this diversity.

After all heads are computed in parallel, their outputs are concatenated and projected back to $d_{\text{model}}$.

##### Add & Norm

The output of multi-head self-attention is not passed directly to the next module. It first goes through residual addition and layer normalization.

For an encoder hidden vector $\boldsymbol{x}$,

$$
\boldsymbol{u}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{x}
+
\operatorname{MultiHeadSelfAttention}(\boldsymbol{x})
\right)
$$

This operation preserves the previous representation and adds the attention-based update. It also keeps the representation normalized before entering the feed-forward sub-layer.

##### Layer Normalization

Let

$$
\boldsymbol{a}=\boldsymbol{x}+\operatorname{Sublayer}(\boldsymbol{x})
$$

where $\boldsymbol{a}\in\mathbb{R}^{d_{\text{model}}}$ is the representation of one token position after residual addition. Layer normalization normalizes this vector across its feature dimension.

First, compute the mean and variance

$$
\mu=\frac{1}{d_{\text{model}}}\sum_{j=1}^{d_{\text{model}}}a_j
$$

$$
\sigma^2=\frac{1}{d_{\text{model}}}\sum_{j=1}^{d_{\text{model}}}(a_j-\mu)^2
$$

Normalize and apply learned scale and bias parameters

$$
\operatorname{LayerNorm}(\boldsymbol{a})
=
\boldsymbol{\gamma}\odot
\frac{\boldsymbol{a}-\mu}{\sqrt{\sigma^2+\epsilon}}
+
\boldsymbol{\beta}
$$

where $\boldsymbol{\gamma}$ and $\boldsymbol{\beta}$ are learned parameters, $\epsilon$ is a small constant for numerical stability, and $\odot$ denotes element-wise multiplication.

Layer normalization is **applied independently to each token representation**. It does not normalize across the batch dimension or across different sequence positions. In the Transformer, it keeps the hidden representation at each position on a stable scale before the next sub-layer.

##### Position-wise Feed-Forward Network

After self-attention, each encoder layer contains a fully connected feed-forward network. It is applied to each position separately and identically.

$$
\operatorname{FFN}(\boldsymbol{x})
=
\max(0,\boldsymbol{x}W_1+\boldsymbol{b}_1)W_2+\boldsymbol{b}_2
$$
It consists of two linear transformations with a ReLU activation in between.

The input and output dimensionality is

$$
d_{\text{model}}=512
$$

and the inner-layer dimensionality is

$$
d_{\text{ff}}=2048
$$

Self-attention mixes information across positions. The feed-forward network transforms the representation at each position independently. Therefore, one encoder layer alternates between token interaction and position-wise nonlinear transformation.

The feed-forward sub-layer also uses residual connection and layer normalization

$$
\boldsymbol{h}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{u}
+
\operatorname{FFN}(\boldsymbol{u})
\right)
$$

After $N$ encoder layers, the encoder produces the memory sequence

$$
\boldsymbol{z}=(\boldsymbol{z}_1,\ldots,\boldsymbol{z}_n)
$$

This sequence is passed to the decoder.

### Decoder

##### Output Embedding

The decoder receives the target sequence shifted right. During training, the model is given the previous ground-truth output tokens as input and learns to predict the next token.

For target positions,

$$
(y_1,\ldots,y_m)
$$

the decoder input is offset so that the prediction at position $i$ cannot directly see $y_i$. This offset works together with masking to preserve the **auto-regressive** property.

As in the encoder, decoder input tokens are converted to embeddings and summed with positional encodings

$$
\boldsymbol{s}_i^{(0)}=\boldsymbol{e}_i^{\text{target}}+\boldsymbol{p}_i
$$

##### Decoder Stack

The decoder is also composed of
$$
N=6
$$

identical layers. Each decoder layer has three sub-layers

$$
\text{Masked Multi-Head Self-Attention}
\rightarrow
\text{Encoder-Decoder Multi-Head Attention}
\rightarrow
\text{Position-wise Feed-Forward Network}.
$$

Each sub-layer is wrapped with residual connection and layer normalization.

The decoder differs from the encoder in two essential ways. First, its self-attention is masked so that positions cannot attend to subsequent positions. Second, it contains an encoder-decoder attention layer, where the decoder attends over the encoder output.

##### Masked Multi-Head Self-Attention

The self-attention sub-layer in the decoder is modified to prevent positions from attending to subsequent positions, preserving the auto-regressive property.

In this layer, queries, keys, and values all come from the previous decoder representation. For position $i$, attention is only allowed over positions

$$
j\leq i
$$

Positions $j>i$ are masked out by setting the corresponding values in the input of the softmax to

$$
-\infty
$$

After the softmax, these positions receive attention weight 0. Combined with the offset output embeddings, this ensures that the prediction for position $i$ can depend only on known outputs at positions less than $i$.

The sub-layer output is

$$
\boldsymbol{r}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{s}
+
\operatorname{MaskedMultiHeadSelfAttention}(\boldsymbol{s})
\right)
$$

##### Encoder-Decoder Multi-Head Attention

The decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.

In this attention layer, the queries come from the previous decoder layer, while the memory keys and values come from the output of the encoder

$$
Q \leftarrow \text{previous decoder layer}
$$

$$
K,V \leftarrow \text{encoder output}
$$

This allows every position in the decoder to attend over all positions in the input sequence, following the typical encoder-decoder attention mechanism in sequence-to-sequence models.

The operation is

$$
\operatorname{MultiHead}(Q_{\text{dec}},K_{\text{enc}},V_{\text{enc}})
$$

The output is passed through residual connection and layer normalization

$$
\boldsymbol{a}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{r}
+
\operatorname{MultiHeadAttention}
(Q_{\text{dec}},K_{\text{enc}},V_{\text{enc}})
\right)
$$

##### Linear Projection and Softmax

The decoder output is passed through a learned linear transformation followed by a softmax function.

For decoder output vector $\boldsymbol{d}_i$, the logits are

$$
\boldsymbol{l}_i=\boldsymbol{d}_iW_{\text{vocab}}+\boldsymbol{b}_{\text{vocab}}
$$

The next-token distribution is

$$
P(y_i\mid y_{<i},x)
=
\operatorname{softmax}(\boldsymbol{l}_i)
$$

The softmax converts logits into predicted next-token probabilities over the vocabulary.

During inference, the model generates tokens auto-regressively. The token predicted at one step is fed back into the decoder input for the next step. During training, the shifted target sequence allows all positions to be processed in parallel under the causal mask.

### Forward Flow

The source tokens are embedded and enriched with positional encodings

$$
\boldsymbol{h}^{(0)}
=
\operatorname{Embedding}(x)
+
PE
$$

The encoder repeatedly applies

$$
\boldsymbol{u}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{h}^{(\ell-1)}
+
\operatorname{MultiHeadSelfAttention}
(\boldsymbol{h}^{(\ell-1)})
\right)
$$

$$
\boldsymbol{h}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{u}^{(\ell)}
+
\operatorname{FFN}(\boldsymbol{u}^{(\ell)})
\right)
$$

After $N$ layers, the encoder output is

$$
\boldsymbol{z}=\boldsymbol{h}^{(N)}
$$

The decoder receives shifted target embeddings plus positional encodings

$$
\boldsymbol{s}^{(0)}
=
\operatorname{Embedding}(y_{<i})
+
PE
$$

Each decoder layer applies masked self-attention,

$$
\boldsymbol{r}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{s}^{(\ell-1)}
+
\operatorname{MaskedMultiHeadSelfAttention}
(\boldsymbol{s}^{(\ell-1)})
\right)
$$

then encoder-decoder attention,

$$
\boldsymbol{a}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{r}^{(\ell)}
+
\operatorname{MultiHeadAttention}
(Q_{\text{dec}},K_{\text{enc}},V_{\text{enc}})
\right)
$$

then the position-wise feed-forward network,

$$
\boldsymbol{s}^{(\ell)}
=
\operatorname{LayerNorm}
\left(
\boldsymbol{a}^{(\ell)}
+
\operatorname{FFN}(\boldsymbol{a}^{(\ell)})
\right)
$$

Finally, the decoder output is projected to vocabulary logits and normalized

$$
P(y_i\mid y_{<i},x)
=
\operatorname{softmax}
\left(
\boldsymbol{s}_i^{(N)}W_{\text{vocab}}+\boldsymbol{b}_{\text{vocab}}
\right)
$$
