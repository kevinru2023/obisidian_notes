#mth254 
## Tangent Planes, Linear Approximation & Optimization of Functions of Two Variables  
---  
**Tangent Planes to Implicit Surfaces:**  
Given a surface in 3D defined by $F(x, y, z) = C$, a constant level set, it implies:  
- For any explicit function $z = f(x, y)$, we can set $F(x, y, z) = 0$ as $F(x, y, z) = z - f(x, y)$.  
- The gradient $\nabla F$ at a point on this level set is orthogonal to the surface, serving as the normal vector for the tangent plane:  
  $$
\boxed{
  \nabla F(x_0, y_0, z_0) \cdot \langle x - x_0, y - y_0, z - z_0 \rangle = 0
  }
$$

### Tangent Plane for $z = f(x, y)$  
For the surface $z = f(x, y)$ at $(x_0, y_0, z_0)$:  
- Tangent plane equation :   
  $$
\boxed{
  z = z_0 + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)
  }
$$
- Or: $$f_{x}(x_{0},y_{0},z_{0})(x-x_{0})+f_{y}(x_{0},y_{0},z_{0})(y-y_{0})+f_{z}(x_{0},y_{0},z_{0})=0$$
### Linear Approximation  
The linear approximation $L(x, y)$ near $(x_0, y_0)$ is:  
$$
\boxed{
f(x, y) \approx L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)
}
$$

In differential terms:  
$$
\boxed{
dz = f_x(x_0, y_0) dx + f_y(x_0, y_0) dy
}
$$

---  

**Example: Tangent Plane Calculation**  
For $f(x, y) = 100 - x^2 - y^4$ at $(x, y) = (3, 1)$:
![[Screenshot 2024-10-27 at 3.24.43 PM.png]]
- Given $F(x, y, z) = z + x^2 + y^4 - 100 = 0$  
- Gradient $\nabla F = \langle 6, 4, 1 \rangle$  
- Tangent plane equation:  
  $$
  6x + 4y + z = 112
  $$

---  

 **Optimization of $f(x, y)$:**
- **Local Maxima/Minima**: $f(x, y)$ has a local max/min at $(x_0, y_0)$ if $f(x_0, y_0)$ is the largest/smallest value within a neighborhood.  
- **Critical Points**: $(x_0, y_0)$ is critical if $\nabla f(x_0, y_0) = 0$ or if a partial derivative does not exist.  
- **Saddle Point**: Occurs at $(x_0, y_0)$ if every neighborhood contains values of $f$ both greater and less than $f(x_0, y_0)$.  

**Second Derivative Test:**
Let $D(x, y) = f_{xx}f_{yy} - (f_{xy})^2$:  
1. $D > 0$ and $f_{xx} > 0$: Local minimum.  
2. $D > 0$ and $f_{xx} < 0$: Local maximum.  
3. $D < 0$: Saddle point.  
4. $D = 0$: Test is inconclusive.  

---  

**Example: Classifying Critical Points for $f(x, y) = x^2 y^2 - xy^2 + 2x^2 y - 2xy + 5$**  
1. Critical points: solve $\nabla f = 0$  
2. Compute $D(x, y)$ to classify.  

| $(x_0, y_0)$ | $D(x_0, y_0)$ | $f_{xx}(x_0, y_0)$ | Conclusion    |
| ------------ | ------------- | ------------------ | ------------- |
| (0, 0)       | -4            | -                  | Saddle        |
| (1, 0)       | -4            | -                  | Saddle        |
| (0, -2)      | -4            | -                  | Saddle        |
| (1, -2)      | -4            | -                  | Saddle        |
| (0.5, -1)    | 1             | -2                 | Local maximum |

---  

**Extreme Value Theorem:**  
For a function $f$ on a closed, bounded region:  
1. Check values at all critical points within the region.  
2. Evaluate $f$ on the boundary for global extremes.  

**Example**: For $f(x, y) = e^{4x + y^2 - x^2}$ on $x^2 + y^2 \leq 9$:  
1. **Find critical points within the region**:  
   - Compute $\nabla f = \langle 2(2 - x)e^{4x + y^2 - x^2}, 2y e^{4x + y^2 - x^2} \rangle = \vec{0}$.  
   - Solving $\nabla f = 0$ gives the interior critical point $(2, 0)$.

2. **Evaluate on the boundary**:  
   - Substitute $y = \pm \sqrt{9 - x^2}$ to get $f(x, y) = e^{4x + 9 - 2x^2}$.  
   - Define $g(x) = f(x, \pm \sqrt{9 - x^2}) = e^{4x + 9 - 2x^2}$ and find critical points by setting $g'(x) = 0$.  
   - Solving $g'(x) = 2(1 - x)e^{4x + 9 - 2x^2} = 0$, we get $x = 1$ with $y = \pm 2\sqrt{2}$.

3. **Check endpoints of the boundary**:  
   - At $x = \pm 3$ (on the boundary), evaluate $f(3, 0)$ and $f(-3, 0)$.

4. **Summary of critical points**:
   - $(x, y) = (-3, 0)$, $f(x, y) = e^{-21}$ (Global minimum)
   - $(x, y) = (1, \pm 2\sqrt{2})$, $f(x, y) = e^{11}$ (Global maximum)
   - $(x, y) = (2, 0)$, $f(x, y) = e^4$ (Not a global extreme)
   - $(x, y) = (3, 0)$, $f(x, y) = e^3$ (Not a global extreme)

--- 
**Additional Resources:**
- Khan Academy 
  - ![](https://www.youtube.com/watch?v=cHNT7_F8m1Y)
  - ![](https://www.youtube.com/watch?v=H2hOwKszKRo)
  - ![](https://youtu.be/QL6qb1h65hg?si=jgdj6kwc8uFUGLRV)

- Dr. Trefor ![](https://www.youtube.com/watch?v=wqtr4Udz8AY)
- [LibreText](https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/14%3A_Differentiation_of_Functions_of_Several_Variables/14.04%3A_Tangent_Planes_and_Linear_Approximations)
