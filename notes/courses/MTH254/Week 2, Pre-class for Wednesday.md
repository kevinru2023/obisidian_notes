---
tags: mth254
---
# Arc Length & Curvature
---
Consider the curve that is the graph of a differentiable vector-valued function $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ on the domain $[a, b]$ such that $|\mathbf{r}'(t)| \neq 0$ for all $a \leq t \leq b$. Let $P, Q$ be the corresponding points on the curve to $\mathbf{r}(a)$ and $\mathbf{r}(b)$, respectively.
![[Screenshot 2024-10-08 at 10.20.21 AM.png]]
The length of this curve from $\mathbf{r}(a)$ to $\mathbf{r}(b)$ is called the **arc length** of the curve from $P$ to $Q$. 

We can partition the curve into $n$ small pieces such that each of the $n$ pieces looks like:

![[Screenshot 2024-10-08 at 10.21.37 AM.png]]

Then, by using the hypotenuses to estimate the arc length of each of the $n$ little pieces, we get a Riemann sum approximation to the arc length of the whole curve:

$$L \approx \sum_{i=1}^{n} \sqrt{(\Delta x_i)^2 + (\Delta y_i)^2} = \sum_{i=1}^{n} \sqrt{\left( \frac{\Delta x_i}{\Delta t} \right)^2 + \left( \frac{\Delta y_i}{\Delta t} \right)^2} \Delta t.$$

By taking the limit as $n \to \infty$ (such that the length of all the pieces tends towards 0), we converge on the exact arc length with the integral:

$$L = \int_a^b \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} dt = \int_a^b ||\mathbf{r}'(t)|| \, dt$$
(similar result in 3D).

In the context of $\mathbf{r}(t)$ representing an object's position as it moves from $P$ towards $Q$ without stopping, the integral of the speed equals the distance traveled by the object along the trajectory, which is also the arc length of the curve from $P$ to $Q$.

Arc Length for some graphs turns out to be $\int \sqrt{ 1+f'(x)^2 }dx$


---  
Recall: One can use polar coordinates $(r, \theta)$ to describe points in the $xy$-plane, where $r$ is the (signed) distance to the origin and $\theta$ is an angle measured counter-clockwise from the positive $x$-axis. In particular, $x = r \cos(\theta)$ and $y = r \sin(\theta)$.

Suppose $r = f(\theta)$, which describes a polar curve.

![[Screenshot 2024-10-08 at 10.23.53 AM.png]]

Then, $x = f(\theta) \cos \theta$ and $y = f(\theta) \sin \theta$. So, the length of the curve from $\theta = \alpha$ to $\theta = \beta$ is:

$$L = \int_{\alpha}^{\beta} \sqrt{\left( \frac{dx}{d\theta} \right)^2 + \left( \frac{dy}{d\theta} \right)^2} d\theta = \int_{\alpha}^{\beta} \sqrt{\left( f'(\theta) \cos \theta - f(\theta) \sin \theta \right)^2 + \left( f'(\theta) \sin \theta + f(\theta) \cos \theta \right)^2} d\theta.$$

This can be simplified to:

$$L = \int_{\alpha}^{\beta} \sqrt{(f'(\theta))^2 + (f(\theta))^2} d\theta.$$

---

Let $\mathbf{r}(t)$ be a differentiable vector-valued function on $[a, b]$ such that $|\mathbf{r}'(t)| \neq 0$ for $a \leq t \leq b$.

Recall: The **unit tangent vector function** for $\mathbf{r}(t)$ is:

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|}$$

The magnitude of the unit tangent vector $|\mathbf{T}(t)| = 1$ for all $t$, so $\mathbf{T}(t)$ only changes direction, never magnitude.

Define the **curvature function** $\kappa(t)$ as the function that outputs the magnitude of the rate of change in $\mathbf{T}(t)$ with respect to arc length $s$. Symbolically **(want to avoid using this btw)**:

$$\kappa(t) = \left| \frac{d \mathbf{T}}{ds} \right|.$$
Since the arc length from $a$ to $t$ along the graph of $\mathbf{r}(t)$ is given by $s(t) = \int_a^t |\mathbf{r}'(u)| \, du$, we have:

$$\frac{ds}{dt} = |\mathbf{r}'(t)|.$$

Then, by the Chain Rule:

$$\left| \frac{d \mathbf{T}}{dt} \right| = \left| \frac{d \mathbf{T}}{ds} \cdot \frac{ds}{dt} \right| = \kappa(t) |\mathbf{r}'(t)|.$$

Thus, $\boxed{\kappa(t) = \frac{|\mathbf{T}'(t)|}{|\mathbf{r}'(t)|}}$

---

The circle of radius $R$ centered at $(x_0, y_0)$ is the graph of $\mathbf{r}(t) = \langle x_0 + R \cos(t), y_0 + R \sin(t) \rangle$. We have that $\mathbf{r}'(t) = R \langle -\sin(t), \cos(t) \rangle$, with $R = |\mathbf{r}'(t)|$, and hence:

$$\mathbf{T}(t) = \langle -\sin(t), \cos(t) \rangle$$
is the unit tangent vector function. Then $\mathbf{T}'(t) = \langle -\cos(t), -\sin(t) \rangle$ and $|\mathbf{T}'(t)| = 1$. Hence, the curvature is $\kappa(t) = \frac{1}{R}$.

In $\mathbb{R}^3$, the curvature is:

$$
\boxed{\kappa(t) = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3}}
$$

Let $\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|}$ (the principal unit normal vector function). Since $\mathbf{T}$ is constant in magnitude, $\mathbf{N}$ is perpendicular to $\mathbf{T}$ and hence orthogonal to the graph of $\mathbf{r}(t)$.

--- 
Let $\mathbf{v} = \mathbf{r}'$ and $\mathbf{a} = \mathbf{v}' = \mathbf{r}''$. Then:

$$\mathbf{v} = |\mathbf{v}| \mathbf{T},$$
so:
$$\mathbf{a} = \frac{d}{dt} (|\mathbf{v}|) \mathbf{T} + |\mathbf{v}| \mathbf{T}'(t) = \frac{d}{dt} (|\mathbf{v}|) \mathbf{T} + \kappa(t) |\mathbf{v}|^2 \mathbf{N}.$$

Therefore, the **tangential component of acceleration** is $\frac{d}{dt} (|\mathbf{v}|) \mathbf{T}$ with magnitude $\left|\frac{d}{dt} (|\mathbf{v}|) \right|$, and the **orthogonal component of acceleration** is $\kappa(t) |\mathbf{v}|^2 \mathbf{N}$ with magnitude $\kappa(t) |\mathbf{v}|^2$.

---
