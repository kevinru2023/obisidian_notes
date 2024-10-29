#mth254 
## Partial Derivatives & Chain Rules
---
The partial derivative of $f(x, y)$ with respect to $x$ is given by

$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}.
$$

This $x$-partial derivative is also given the subscript notation $f_x$.

The partial derivative of $f(x, y)$ with respect to $y$ is given by

$$
\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}.
$$

This $y$-partial derivative is also given the subscript notation $f_y$.

Analogous definitions exist for the $x$-, $y$-, and $z$-partial derivatives of $f(x, y, z)$.

For example,

$$
\frac{\partial}{\partial y} \left( xy^2 \right) = \lim_{h \to 0} \frac{x(y+h)^2 - xy^2}{h} = \lim_{h \to 0} \frac{x(y^2 + 2hy + h^2) - xy^2}{h} = \lim_{h \to 0} \frac{2hxy + xh^2}{h} = 2xy.
$$

So, to calculate a partial derivative of a function $f$ with respect to a certain variable, regard the other variable(s) as constant(s) and take the derivative. <u>All the rules of differential calculus apply with the other variable(s) treated as constants</u>.

---
**Example:**

$$
\frac{\partial}{\partial y} \left( \cos(2y) e^{x^2/y} \right) = -2 \sin(2y) e^{x^2/y} - \frac{x^2}{y^2} \cos(2y) e^{x^2/y}.
$$

the $x-$ and $y-$ partial derivative of $f(x,y)$ evaluated at a $(x_{0},y_{0})$ is the slope ate $(x_{0},y_{0,},f(x_{0},y_{0}))$ along the $y-$ and $x-$ traces on $z=f(x,y)$ at $y=y_0$ and $x=x_{0}$ respectively:  
![[Screenshot 2024-10-22 at 6.51.32 PM.png]]

---
**Higher-order partial derivatives:** are partial derivatives of partial derivatives. The order corresponds to how many derivatives have been taken.

For instance,

$$
\frac{\partial}{\partial x} \left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial x^2} = f_{xx} \space \space \space \text{and} \quad \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial x \partial y} = f_{yx}.
$$
#### (examples of second order partial derivatives)

$$\frac{\partial}{\partial x} \left( \frac{\partial}{\partial x} \left( \frac{\partial g}{\partial z} \right) \right) = \frac{\partial^3 g}{\partial x^2 \partial z} = g_{zxx}
$$
#### (example of a third order partial derivative) 

Higher-order partial derivatives involving more than one variable are called mixed partial derivatives.

---
**Theorem (Equality of Mixed Partials):** Let $f(x, y)$ be a function and assume the mixed partials $f_{xy}$ and $f_{yx}$ are continuous. Then $f_{xy} = f_{yx}$.

The function $z = f(x, y)$ is differentiable at $(x_0, y_0)$ provided $f_x(x_0, y_0)$ and $f_y(x_0, y_0)$ exist and that

$$
\Delta z = f_x(x_0, y_0) \Delta x + f_y(x_0, y_0) \Delta y + \epsilon_1 \Delta x + \epsilon_2 \Delta y,
$$

where $\epsilon_1$ and $\epsilon_2$ both approach 0 as $\Delta x$ and $\Delta y$ approach 0.

---
**Theorem:** If a function $f(x, y)$ has partial derivatives defined on an open region containing $(x_0, y_0)$, where both $f_x$ and $f_y$ are continuous at $(x_0, y_0)$, then $f$ is differentiable at $(x_0, y_0)$.

---
**Theorem (Differentiability Implies Continuity):** If a function $f(x, y)$ is differentiable at $(x_0, y_0)$, then it is continuous at $(x_0, y_0)$.

Consider the function:

$$
f(x, y) = \begin{cases} 
\frac{2xy}{x^2 + y^2} & \text{if } (x, y) \neq (0, 0), \\
0 & \text{if } (x, y) = (0, 0).
\end{cases}
$$

Then,

$$
f_x(0, 0) = \lim_{h \to 0} \frac{f(0+h, 0) - f(0, 0)}{h} = 0 \quad \text{and} \quad f_y(0, 0) = \lim_{h \to 0} \frac{f(0, 0+h) - f(0, 0)}{h} = 0.
$$

However, this function is not differentiable at $(0, 0)$ as it isn’t even continuous at $(0, 0)$. Just consider the limit as $(x, y) \to (0, 0)$.

---
**Chain Rules:**

Suppose $z$ is a function of $x$ and $y$, which are each functions of $t$. Then we have:

$$
\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt}.
$$

Suppose $w$ is a function of $x$, $y$, and $z$, which are each functions of $t$. Then we have:

$$
\frac{dw}{dt} = \frac{\partial w}{\partial x} \frac{dx}{dt} + \frac{\partial w}{\partial y} \frac{dy}{dt} + \frac{\partial w}{\partial z} \frac{dz}{dt}.
$$

For more complex cases, where $z$ is a function of $x$ and $y$, which are functions of $s$ and $t$, we have:

$$
\frac{\partial z}{\partial s} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial s},
$$

$$
\frac{\partial z}{\partial t} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial t}.
$$

Similarly, for $w$:

$$
\frac{\partial w}{\partial s} = \frac{\partial w}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial s} + \frac{\partial w}{\partial z} \frac{\partial z}{\partial s},
$$

$$
\frac{\partial w}{\partial t} = \frac{\partial w}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial w}{\partial y} \frac{\partial y}{\partial t} + \frac{\partial w}{\partial z} \frac{\partial z}{\partial t}.
$$

To determine the appropriate Chain Rule, one can draw a tree diagram, where each variable that directly depends on other variables is a node with edges emanating downward to those variables it directly depends on, until we reach the independent variables at the bottom.
![[Screenshot 2024-10-22 at 6.58.34 PM.png]]

---
**Implicit Differentiation:**

Suppose $y = f(x)$ is implicitly defined by $F(x, y) = C$, where $C$ is a constant. By differentiating both sides with respect to $x$, we get $F_x + F_y \frac{dy}{dx} = 0, \quad \text{so} \quad \frac{dy}{dx} = -\frac{F_x}{F_y}.$
![[Screenshot 2024-10-22 at 7.00.16 PM.png]]
Similarly, if $z = f(x, y)$ is implicitly defined by $F(x, y, z) = k$, where $k$ is a constant, then $f_x = -\frac{F_x}{F_z}, \quad f_y = -\frac{F_y}{F_z}.$
![[Screenshot 2024-10-22 at 7.01.07 PM.png]]

---
**Additional Resources:**
- Khan Academy![Khan academy](https://www.youtube.com/watch?v=AXqhWeUEtQU)
- Organic Chemistry Tutor ![](https://www.youtube.com/watch?v=JAf_aSIJryg)
- [LibreText](https://math.libretexts.org/Bookshelves/Calculus/Calculus_3e_(Apex)/12%3A_Functions_of_Several_Variables/12.03%3A_Partial_Derivatives)
- [Khan Academy (article)](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives)


