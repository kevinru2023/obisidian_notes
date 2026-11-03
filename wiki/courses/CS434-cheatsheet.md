# CS434 Cheat Sheet

**MLE:** $\theta^*=\operatorname{argmax}_\theta\sum_i\log P(x_i,y_i\mid\theta)$ | **MAP:** adds $+\log P(\theta)$ | Gaussian prior→L2 reg, Laplace prior→L1 reg | **LinReg:** $w^*=(X^\top X)^{-1}X^\top y$, Ridge: $+({\lambda I})$ | **LogReg:** $P(y=1\mid x)=\sigma(w^\top x)$, cross-entropy loss, convex | **Perceptron:** $\hat y=\text{sign}(w^\top x)$, mistake→$w\leftarrow w+yx$, bound $\leq R^2/\gamma^2$ | **Metrics:** $\text{Prec}=\frac{TP}{TP+FP}$, $\text{Rec}=\frac{TP}{TP+FN}$, $F1=\frac{2PR}{P+R}$

---

## k-Nearest Neighbors

**Classify:** $f_k(x)=\operatorname{argmax}_y\sum_{i\in N_k(x)}\mathbf{1}[y_i=y]$ &nbsp;&nbsp; **Regress:** $\frac{1}{k}\sum_{i\in N_k(x)}y_i$

| Metric | Formula | | $k$ | Behavior |
|---|---|---|---|---|
| Euclidean | $\sqrt{\sum(x_i-z_i)^2}$ | | $k=1$ | train err $=0$, overfit |
| Manhattan | $\sum\|x_i-z_i\|$ | | $k=n$ | predict majority, underfit |
| Chebyshev | $\max_i\|x_i-z_i\|$ | | best $k$ | choose via CV |
| Minkowski | $(\sum\|x_i-z_i\|^p)^{1/p}$ | | | |

**Curse of dim:** $1-(1-\varepsilon)^d\to 1$ — all points equidistant, breaks "nearby = similar" &nbsp;|&nbsp; **Cost:** $O(nd)$ inference; normalize features; irrelevant features pollute distance &nbsp;|&nbsp; **LOO-CV:** cheap for kNN — exclude each point from its own neighborhood

---

## Naïve Bayes

**Assumption:** $P(\mathbf{x}\mid y)=\prod_i P(x_i\mid y)$ — features independent given class. Params: $O(cm^d)\to O(cdm)$

**Predict:** $\hat y=\operatorname{argmax}_c\bigl[\log P(y=c)+\sum_i\log P(x_i\mid y=c)\bigr]$ ← log space avoids underflow

| Variant | Features | $P(x_i\mid y)$ | Note |
|---|---|---|---|
| Bernoulli | binary | $p^{x_i}(1-p)^{1-x_i}$ | penalizes absence |
| Multinomial | counts | Multinomial | ignores absence |
| Gaussian | continuous | $\mathcal{N}(\mu_{iy},\sigma_{iy}^2)$ | |

**Laplace smoothing** (fix zero-prob): $P(x_i=v\mid y=c)=\frac{\text{count}(x_i=v,y=c)+\alpha}{\text{count}(y=c)+k\alpha}$ &nbsp;($k$ = # categories, $\alpha=1$ standard)

**NB vs LR:** NB generative, converges $O(\log n)$; LR discriminative, lower asymptotic error. Prefer NB with scarce data.

---

## Support Vector Machines

**Hard-margin** (separable) — maximize margin $\frac{1}{\|\mathbf{w}\|}$:
$$\min_{\mathbf{w},b}\tfrac{1}{2}\mathbf{w}^\top\mathbf{w}\quad\text{s.t.}\quad y_i(\mathbf{w}^\top\mathbf{x}_i+b)\geq 1$$
**Support vectors:** tight constraints ($=1$); only SVs affect solution: $\mathbf{w}^*=\sum_i\alpha_i^*y_i\mathbf{x}_i$, $\sum_i\alpha_iy_i=0$

**Dual (hard):** $\max_\alpha\sum_i\alpha_i-\frac{1}{2}\sum_{ij}\alpha_i\alpha_jy_iy_j\mathbf{x}_i^\top\mathbf{x}_j$ &nbsp;s.t.&nbsp; $\sum_i\alpha_iy_i=0,\ \alpha_i\geq 0$

**Soft-margin** (non-sep) — slack $\xi_i\geq 0$: $\min\tfrac{1}{2}\mathbf{w}^\top\mathbf{w}+C\sum_i\xi_i$ s.t. $y_i(\mathbf{w}^\top\mathbf{x}_i+b)\geq 1-\xi_i$ &nbsp;|&nbsp; Dual: same + $\alpha_i\leq C$

| $C\to\infty$ | hard-margin recovered | | $C\to 0$ | wide margin, ignore errors |
|---|---|---|---|---|

**Hinge loss:** SVM $\equiv\frac{1}{n}\sum_i\max(0,1-y_i\mathbf{w}^\top\mathbf{x}_i)+\lambda\|\mathbf{w}\|^2$ &nbsp;|&nbsp; SVM=hinge, LogReg=log, LinReg=square

**Kernel SVM:** replace $\mathbf{x}_i^\top\mathbf{x}_j\to\kappa(\mathbf{x}_i,\mathbf{x}_j)$; predict $\operatorname{sgn}(\sum_i\alpha_iy_i\kappa(\mathbf{x}_i,\mathbf{z})-b)$ &nbsp;|&nbsp; **Mercer:** $\kappa$ valid iff Gram matrix PSD

| Kernel | Formula |
|---|---|
| Linear | $\mathbf{a}\cdot\mathbf{b}$ |
| Polynomial | $(\mathbf{a}\cdot\mathbf{b}+1)^p$ |
| RBF | $\exp(-\gamma\|\mathbf{a}-\mathbf{b}\|^2)$ — infinite-dim |
