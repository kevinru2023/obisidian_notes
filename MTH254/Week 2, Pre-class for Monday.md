#mth254 
# Calculus of Curves (and Motion) 
--- 
Let $\vec{r}(t) = \langle x(t),y(t),z(t)\rangle$ be a vector valued function. The <u>derivative of </u>$\boldsymbol{r}(t)$ is $$\boldsymbol{r'}(t)=\lim_{ h \to 0 }\frac{1}{5}(\boldsymbol{r}(t+h)-\boldsymbol{r}(t))$$(limit of the difference quotients). Wherever this exists $\boldsymbol{r}(t)$ is said to be <u>differentiable</u>. 

Since the limit is component-wise, $\mathbf{r}(t)$ is differentiable at $t = a$ if each component function is differentiable at $t = a$. Where $\mathbf{r}(t)$ is differentiable, $$\mathbf{r}'(t) = \langle x'(t), y'(t) \rangle \quad \text{(or } \langle x'(t), y'(t), z'(t) \rangle \text{)}$$
Where $\mathbf{r}(t)$ is differentiable, a non-zero derivative at $t$ results in a vector that is tangent to the curve at the corresponding point along the graph of $\mathbf{r}(t)$.

![[Screenshot 2024-10-05 at 11.53.15 AM.png]]

--- 
**Unit Tangent Vector** function: When $\mathbf{r}'(t)$ exists and is nonzero, we can define the unit tangent vector function, a function that outputs a unit vector tangent to the curve (at each point along the curve): $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|}$$

--- 
**Properties of Vector Derivatives:**
 - $\frac{d}{dt}(\mathbf{u}(t)+\mathbf{v}(t))=\mathbf{u}'(t)+\mathbf{v}'(t)$
- $\frac{d}{dt}(f(t)\mathbf{u}(t))=f'(t)\mathbf{u}(t)+f(t)\mathbf{u}'(t)$
- $\frac{d}{dt}(\mathbf{u}(t)\cdot \mathbf{v}(t))=\mathbf{u}'(t)\cdot \mathbf{v}(t)+\mathbf{u}(t)\cdot \mathbf{v}'(t)$
- $\frac{d}{dt}(\mathbf{u}(t)\times \mathbf{v}(t))=\mathbf{u}'(t)\times \mathbf{v}(t)+\mathbf{u}(t)\times \mathbf{v}'(t)$

--- 
**Tangent lines:**
Let $C$ be a curve traced out by a vector-valued function $\mathbf{r}(t)$ that is differentiable at $t_{0}$ with $\mathbf{r}'(t_{0})\neq \vec{0}$. Then the *[tangent line](https://math.libretexts.org/Bookshelves/Calculus/Elementary_Calculus_2e_(Corral)/03%3A_Topics_in_Differential_Calculus/3.01%3A_Tangent_Lines)* to $C$ at the point $\mathbf{r}(t_{0})$ is given by $$\vec{\ell}(t)=\mathbf{r}(t_{0})+t\mathbf{r}'(t_{0})$$
![[Screenshot 2024-10-06 at 9.04.52 PM.png]]

--- 
**Intergrals:**

Let $\mathbf{v}(t)$ be a vector-valued function. If $\mathbf{V}(t)$ is a vector-valued function such that $\mathbf{V}'(t)=\mathbf{v}(t)$ then, we call $\mathbf{V}$ an <u>antiderivative</u> of $\mathbf{v}$. Since derivatives are componentwise, so are antiderivatives, you simply take the antiderivative of each component on a vector. 

The <u>indefinite integral</u> is the set of all antiderivatives denoted: $$\int \mathbf{v}(t)dt=\mathbf{V}(t)+\mathbf{C}\text{, where }\mathbf{V}\text{ is an antiderivative of }\mathbf{v}\text{ and }\mathbf{C}\text{ is a constant}$$
The <u>definite intergral</u> is calculated in the following way: $$\int_{a}^b\mathbf{v}(t)dt=\mathbf{V}(b)-\mathbf{V}(a)\text{, where }\mathbf{V}\text{ is an antiderivative of }\mathbf{v}$$

--- 
**Example:**

Let $\mathbf{r}(t)$ represent the **position** of an object against time $t$. The graph of $\mathbf{r}(t)$ represents the <u>path</u> or <u>trajectory</u> of the object.

Then $\mathbf{v}(t) = \mathbf{r}'(t)$ represents the **velocity** of the object, and $\mathbf{a}(t) = \mathbf{v}'(t) = \mathbf{r}''(t)$ represents the **acceleration** of the object. The speed of the object is measured by $|\mathbf{v}(t)| = |\mathbf{r}'(t)|$.

From the velocity $\mathbf{v}(t)$, the <u>definite integral</u>,
$$ \int_a^b \mathbf{v}(t)\, dt = \mathbf{r}(b) - \mathbf{r}(a), $$
calculates the **net displacement** of the object over the time interval $[a, b]$.

Assume $\mathbf{r}(t)$ is a trajectory of an object with constant positive speed: $|\mathbf{r}'(t)| = c > 0$.

Then 
$$ 0 = \frac{d}{dt} \left( c^2 \right) = \frac{d}{dt} \left( |\mathbf{r}'(t)|^2 \right) = \frac{d}{dt} \left( \mathbf{r}'(t) \cdot \mathbf{r}'(t) \right) = 2\mathbf{r}''(t) \cdot \mathbf{r}'(t), $$
which implies 
$$ 0 = \mathbf{r}''(t) \cdot \mathbf{r}'(t), $$
and thus, $\mathbf{r}''(t) \perp \mathbf{r}'(t)$.

For motion with constant speed, we have that the velocity and acceleration vectors are orthogonal.


**Another useful [example](https://canvas.oregonstate.edu/courses/1978938/files/107166747?wrap=1)**
