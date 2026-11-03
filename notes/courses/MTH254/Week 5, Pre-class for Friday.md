#mth254  
## Lagrange Multipliers  
---  
### Lagrange Multipliers for Constrained Optimization:
Given a differentiable function $f(x, y)$ in a region of $\mathbb{R}^2$, we want to find the local extreme values of $f$ constrained to inputs on a curve $C$, defined by $g(x, y) = k$ where $k$ is a constant and $\nabla g(x, y) \neq 0$ for all points on $C$.

1. **Parameterization of the Curve**:  
   Let $C$ be parameterized by $\vec{r}(t) = \langle x(t), y(t) \rangle$, with $x(t)$ and $y(t)$ differentiable. We can define $h(t) = f(x(t), y(t))$ as differentiable.

2. **Using the Chain Rule**:  
   To find extreme values of $h$, we use the Chain Rule: 
   
   $$
   h'(t) = f_x(x(t), y(t)) x'(t) + f_y(x(t), y(t)) y'(t)
   $$
   
   Critical points occur where $h'(t) = 0$, or equivalently:

   $$
   0 = \nabla f(x(t), y(t)) \cdot \vec{r}'(t)
   $$

   This shows that the extreme values of $f$ on $C$ happen where $\nabla f$ is orthogonal to the curve $C$ at that point.

3. **Condition for Constrained Optimization**:
   Since $\nabla g$ is also orthogonal to $C$, it must be that:

   $$
   \nabla f(x, y) = \lambda \nabla g(x, y)
   $$

   for some scalar $\lambda$. This gives us the system to solve:

   $$
\boxed{
   \nabla f(x, y) = \lambda \nabla g(x, y) \text{ and } g(x, y) = k.
   }
$$

---
**Example**:  
![[Screenshot 2024-11-01 at 12.33.25 AM.png]]

To find extreme values of $f(x, y) = x^2 - y^2$ restricted to the unit circle $x^2 + y^2 = 1$, we set $g(x, y) = x^2 + y^2 - 1$. Then solve:

$$
\nabla f = \lambda \nabla g \text{ and } g(x, y) = 1.
$$

Here are the outlined steps:

1. **Compute the Gradients**:  
   - Find $\nabla f$ for $f(x, y) = x^2 - y^2$:  
     $$ 
     \nabla f = \langle 2x, -2y \rangle 
     $$
   - Find $\nabla g$ for $g(x, y) = x^2 + y^2 - 1$:  
     $$ 
     \nabla g = \langle 2x, 2y \rangle 
     $$

2. **Set Up the Equations**:  
   Using the Lagrange multiplier condition $\nabla f = \lambda \nabla g$, we get:
   $$ 
   \langle 2x, -2y \rangle = \lambda \langle 2x, 2y \rangle 
   $$
   This results in two equations:
   - $2x = 2\lambda x$
   - $-2y = 2\lambda y$

3. **Solve for $\lambda$ and Critical Points**:
   - From $2x = 2\lambda x$, we find either $x = 0$ or $\lambda = 1$.
     - If $x = 0$, substitute into the constraint $g(x, y) = 1$:  
       $$ 
       0^2 + y^2 = 1 \Rightarrow y = \pm 1 
       $$
       - For $(x, y) = (0, 1)$ and $(0, -1)$, substitute into $f(x, y)$:
         $$ 
         f(0, \pm1) = 0^2 - (\pm1)^2 = -1 
         $$
         Thus, $(0, 1)$ and $(0, -1)$ are minima with $f = -1$.

   - If $\lambda = 1$, substitute into $-2y = 2\lambda y$:
     $$ 
     -2y = 2y \Rightarrow y = 0 
     $$
     - Substitute $y = 0$ into the constraint $g(x, y) = 1$:
       $$ 
       x^2 + 0^2 = 1 \Rightarrow x = \pm 1 
       $$
       - For $(x, y) = (1, 0)$ and $(-1, 0)$, substitute into $f(x, y)$:
         $$ 
         f(\pm1, 0) = (\pm1)^2 - 0^2 = 1 
         $$
         Thus, $(1, 0)$ and $(-1, 0)$ are maxima with $f = 1$.

4. **Conclusion**:
   - Maximum value of $f(x, y)$ on $C$ is $1$ at points $(1, 0)$ and $(-1, 0)$.
   - Minimum value of $f(x, y)$ on $C$ is $-1$ at points $(0, 1)$ and $(0, -1)$.


---
**3D Extension**:  
For functions $f(x, y, z)$ and a surface constraint $g(x, y, z) = k$, solve:

$$
\boxed{
\nabla f(x, y, z) = \lambda \nabla g(x, y, z) \text{ and } g(x, y, z) = k.
}
$$
---
**Additional Resources:**
- ![](https://www.youtube.com/watch?v=yuqB-d5MjZA)
- ![](https://www.youtube.com/watch?v=aep6lwPqm6I&list=PLCg2-CTYVrQvNGLbd-FN70UxWZSeKP4wV&index=2)
