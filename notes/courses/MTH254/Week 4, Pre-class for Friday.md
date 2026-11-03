#mth254 
## Directional Derivatives & The Gradient
---
### Directional Derivatives:
Suppose $z = f(x, y)$ (or $w = g(x, y, z)$), and you want to know how $z$ (or $w$) changes at the point $(x_0, y_0)$ (or $(x_0, y_0, z_0)$) in the direction of a unit vector $\hat{u} = \langle a, b \rangle$ (or $\hat{v} = \langle a, b, c \rangle$). 

- The directional derivative of $f$ in the direction $\hat{u}$ is:

$$
D_{\hat{u}} f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + ha, y_0 + hb) - f(x_0, y_0)}{h}
$$

- For 3D functions: 

$$
D_{\hat{v}} g(x_0, y_0, z_0) = \lim_{h \to 0} \frac{g(x_0 + ha, y_0 + hb, z_0 + hc) - g(x_0, y_0, z_0)}{h}.
$$

Instead of using the limit definition, we can use the following formula, derived using the chain rule, where $\hat{u}$ is a unit vector in the direction of some vector $\vec{v}$:

$$
\boxed{
D_{\hat{u}} f(x_0, y_0) = \nabla f(x_0, y_0) \cdot \hat{u} 
}
$$

(or in 3D):

$$
\boxed{
D_{\hat{v}} g(x_0, y_0, z_0) = \nabla g(x_0, y_0, z_0) \cdot \hat{v}.
}
$$

Another way of thinking of this formula is $$\nabla_{\vec{v}}f=a\frac{\partial f}{\partial x}+b\frac{ \partial f }{ \partial y }$$
where $f$ is a function such as $f(x,y)$ and $a$ and $b$ are nudges in a certain direction *(check out khan academy video)*
![[Screenshot 2024-10-24 at 7.28.32 PM.png]]
*(picture of directional slope)*

---
**Gradient:**
- The gradient of a function points in the direction of the greatest rate of increase.
- For a function $f(x, y)$, the gradient is:

$$
\vec{\nabla}f = \langle f_x, f_y \rangle
$$

For $g(x, y, z)$:

$$
\vec{\nabla}g = \langle g_x, g_y, g_z \rangle.
$$

---
**Example:**
Let $f(x, y) = x^3 y^2 + \tan^{-1}(xy)$. We need to find the directional derivative at $(1, 3)$ in the direction $\langle 3, -4 \rangle$. 

1. First, scale the vector to a unit vector:

$$
\hat{u} = \frac{1}{5} \langle 3, -4 \rangle.
$$

2. The gradient of $f$ is:

$$
\vec{\nabla}f = \langle 3x^2 y^2 + \frac{y}{1 + x^2 y^2}, 2x^3 y + \frac{x}{1 + x^2 y^2} \rangle,
$$

3. Evaluating this at $(1, 3)$:

$$
\vec{\nabla}f(1, 3) = \langle 27.3, 6.1 \rangle.
$$

4. Finally, compute the directional derivative:

$$
D_{\hat{u}} f(1, 3) = \frac{1}{50}(273(3) + 61(-4)) = \frac{23}{2}.
$$

---
**Maximum and Minimum Directional Derivatives:**
- The directional derivative is maximized when $\hat{u}$ is in the direction of $\nabla f(x_0, y_0)$ and minimized when it is opposite.

- Maximum value: $|\nabla f(x_0, y_0)|$
- Minimum value: $-|\nabla f(x_0, y_0)|$

---
**Gradients and Level Curves:**
If $\vec{r}(t) = \langle x(t), y(t) \rangle$ is a differentiable parametrization of a level curve $f(x, y) = C$, then:

$$
\nabla f(\vec{r}(t)) \cdot \vec{r}'(t) = 0
$$

<u>This means the gradient is orthogonal (perpendicular) to the level curve at any point.</u> Similarly, for a function $g(x, y, z)$, the gradient is perpendicular to the level surface.

Here is a gradient drawn amongst level curves of $f(x,y)=2x+y-x^2$
![[Screenshot 2024-10-24 at 7.40.51 PM.png]]
*Note: A similar result holds for the gradient of a scalar function $g(x,y,z)$ (with cont. first order partials) and level surfaces of $g(x,y,z)$.*

---
**Additional Resources:**
- Khan Academy ![](https://www.youtube.com/watch?v=N_ZRcLheNv0)
- [LibreText](https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/14%3A_Differentiation_of_Functions_of_Several_Variables/14.06%3A_Directional_Derivatives_and_the_Gradient)

