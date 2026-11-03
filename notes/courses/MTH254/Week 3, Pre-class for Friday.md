#mth254 
# Limits of Functions of Several Variables & Continuity 
--- 
A function $f(x,y)$ has a <u>limit</u> of $L$ as $(x,y)$ approaches $(x_0,y_0)$ if $|f(x,y)-L|$ can be made arbitrarily small for all domain points in a  in a suﬃciently small punctured disk centered at $(x_0,y_0)$.  Notation:$\lim_{ (x,y) \to(x_{0},y_{0}) } f(x,y)=L$

A function $f(x,y,z)$ has a <u>limit</u> of $L$ as $(x,y,z)$ approaches $(x_{0},y_{0},z_{0})$ if $|f(x,y,z)-L|$ can be made arbitrarily small for all domain points in a sufficiently small punctured ball centered at $(x_{0},y_{0},z_{0})$. Notation: $\lim_{ (x,y,z) \to (x_{0},y_{0},z_{0}) }f(x,y,z)=L$ to evaluate limits, one can use techniques including algebra, polar coordinates and concepts from single-variable limits.

---
**Example:** Evaluate $\lim_{ (x,y) \to (0,0) } \frac{\sin(\sqrt{ x^2+y^2 })}{\sqrt{ x^2+y^2 }}$. One can speculate based on the graph that this limit exists (as a finite number) even though the function $f(x,y)=\frac{\sin{\sqrt{ x^2+y^2 }} }{\sqrt{ x^2+y^2 }}$ is undefined at the origin. 

![[Screenshot 2024-10-21 at 12.46.05 PM.png]]

Using the polar substitution, $r=\sqrt{ x^2+y^2 }$ and that $\lim_{ (x,y) \to (0,0) }\sqrt{ x^2+y^2 }=0$ we can convert the limit into a  single-variable limit and just recall that $\frac{\sin(\alpha)}{\alpha}\to 1$ is $\alpha \to 0$:$$\displaylines{\lim_{ (x,y) \to (0,0) } \frac{\sin(\sqrt{ x^2+y^2 })}{\sqrt{ x^2+y^2 }}=\lim_{ r \to 0^+ } \frac{\sin(r)}{r}=1}$$

---
**Example:** Evaluate $\lim_{ (x,y) \to (1,1) }\frac{x-y}{x^2-3xy+2y^2}$
Using that $x^2-3xy+2y^2=(x-y)(x-2y)$, we have 
$$\lim_{ (x,y) \to (1,1) }\frac{x-y}{x^2-3xy+2y^2}=\lim_{ x,y \to (1,1) }\frac{x-y}{(x-y)(x-2y)}=\lim_{ (x,y) \to (1,1) } \frac{1}{x-2y}=-1$$

---
**2-Path Tests:** (2D) If there are two distinct paths approaching $(x_{0},y_{0})$ in the domain of $f(x,y)$ such that the limits of $f(x,y)$ as $(x,y)$ approaches $(x_{y},y_{0})$ along these paths are distinct then  $\lim_{ (x,y) \to (x_{0},y_{0}) }f(x,y)$ does not exist. 

(3D) If there are two distinct paths approaching $(x_{0},y_{0},z_{0})$ in the domain of $f(x,y,z)$ such that the limits of $f(x,y,z)$ as $(x,y,z)$ approaches $(x_{0},y_{0},y_{0})$ along these paths are distinct then $\lim_{ (x,y,z) \to (x_{0},y_{0},z_{0}) }f(x,y,z)$ does not exist. 

**Example:** Justify that the limit $\lim_{(x,y,z) \to (0,0,1)} \frac{2xy(z-1)}{x^3 + (z-1)^3}$ does not exist (dne). Consider approaching $(0,0,1)$ along the line $\vec{r}(t) = \langle t,t,1 \rangle$ as $t \to 0$. Along this path: $$ \lim_{(t,t,1) \to (0,0,1)} \frac{2tt(1-1)}{t^3 + (1-1)^3} = \lim_{t \to 0} \frac{0}{t^3} = 0 $$ Consider approaching $(0,0,1)$ along the line $\vec{v}(t) = \langle t,t,t+1 \rangle$ as $t \to 0$. Along this path: $$ \lim_{(t,t,t+1) \to (0,0,1)} \frac{2tt(t+1-1)}{t^3 + (t+1-1)^3} = \lim_{t \to 0} \frac{2t^3}{2t^3} = 1 $$ Therefore, $\lim_{(x,y,z) \to (0,0,1)} \frac{2xy(z-1)}{x^3 + (z-1)^3}$ does not exist.

---
**Additional Resources:**
-  Organic Chemistry Tutor![Organic Chemistry Tutor](https://www.youtube.com/watch?v=E1lMMBpz8YM&t=947s)
- [LibreText](https://math.libretexts.org/Bookshelves/Calculus/Calculus_3e_(Apex)/12%3A_Functions_of_Several_Variables/12.02%3A_Limits_and_Continuity_of_Multivariable_Functions)

