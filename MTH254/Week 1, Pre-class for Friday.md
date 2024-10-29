#mth254 
# Planes, Lines and curves 
---
**Planes:** A <u>plane</u> in $\mathbb{R^3}$ is a copy of $\mathbb{R^2}$ embedded in space. It is uniquely determined by a point in it and an orthogonal direction to it. 

Suppose $(x_0,y_0,z_0)$ is a point in plane P. Suppose $\vec{n} = \langle{a,b,c}\rangle$ is a non-zero vector that is orthogonal to the plane called a <u>normal</u> vector. Note: The angle between two planes is the angle $\theta$ so that $0 \leq \theta \leq \frac{\pi}{2}$.

![[Screenshot 2024-10-03 at 10.19.30 AM.png]]

Let $(x,y,z)$ represent an arbitrary point in the plane. Then the vector $\vec{u} = \langle{x-x_0, y-y_{0},z-z_{0}}\rangle$ is perpendicular to $\vec{n}$. So the plane is determined by $\vec{n}\cdot\vec{u} = 0$, equivalently $a(x-x_{0}) + b(y-y_{0}) +c(z-z_{0}) = 0$, or $ax +by + cz = d$ where $d = ax_0 + by_0 +cz_0$. 

Explanation in this [video](https://canvas.oregonstate.edu/courses/1978938/pages/preparation-for-fri-week-1-2?module_item_id=24780155) at <u>1:32</u>
Another explanation in this [video](https://www.youtube.com/watch?v=HjJ140TYbXQ) 

---
**A function of one var that outputs a vector is a <u>vector-valued function</u>**. Such as $\vec{u}(t) = \langle{x(t),y(t)}\rangle$ (2D) or $\vec{v}(t) = \langle{x(t),y(t),z(t)}\rangle$ (3D), where each component is a function. The graph of these functions is a curve traced out by the pos of the heads of the vectors $\vec{v}(t)$ when their tails are placed at the origin. 

![[Screenshot 2024-10-03 at 10.54.57 AM.png]]
*graph of $\vec{v}(t) = \langle{\cos(t), \sin(t)}\rangle$* 

![[Screenshot 2024-10-03 at 10.57.33 AM.png]]
*graph of $\vec{u}(t) = \langle{t\sin (t),t\cos(t), t}\rangle$ for $t \geq 0$* 

---
**Lines in a plane or in space:**
let $\ell$ be a line in $\mathbb{R^2}$ or $\mathbb{R^3}$. The line $\ell$ is uniquely determined by two distinct points on it. Let $A$ and $B$ be two points on $\ell$. Let $\vec{r_{0}} = \vec{OA}$ where $O$ is the origin and $\vec{d} = \vec{AB}$, which is parallel to the line $\ell$. Then the line $\ell$ is the graph of $\vec{r}(t)=\vec{r_{0}}+t\vec{d}$.   

![[Screenshot 2024-10-03 at 1.55.07 PM.png]]
Explanation on this in this [video](https://canvas.oregonstate.edu/courses/1978938/pages/preparation-for-fri-week-1-2?module_item_id=24780155) at <u>9:09</u> 

In terms of cords, the graph of $\vec{r}(t) = \langle{x_{0}+t(x_{1}-x_{0}),y_{0}+t(y_{1}-y_{0}),z_{0}+t(z_{1}-z_{0})}$
or 
$\vec{r}(t)=P+t \vec{d}$ where p is the starting point and d is the direction vector

---
**Limits:**

A vector $\vec{v}(t)$ approaches a vector limit $\vec{L}$ as $t$ approaches $a$ if $|\vec{v}(t) - \vec{L}|$ is arbitrarily close to $0$ for $t$ sufficiently close to $a$, but not equal to $a$. If $\vec{v}(a)$ equals the limit of $\vec{v}(t)$ as $t\to a$, then $\vec{v}(t)$ is continuous at $t =a$ 

The limit of a vector-valued function exists if and only if the corresponding limit of each component function exists. 

WTF does all this mean? This is legit just single variable calc but with vectors instead lol. 

---

**(Supplemental instruction) Revisiting Lines in $\mathbb{R^2}$ to better understand planes in $\mathbb{R^3}$:**

In traditional algebra, we learn that a line through the point $(x_{0},y_{0})$ with slope $m$ is given by the equation $y-y_{0} = m(x -x_{0})$ (point slope form)

While we don't pay attention to the standard form of a line, $ax+by =c$. We are going to put this form in focus: 

Let $a,b,c$ be real numbers such that not both of $a,b$ are zero. Let $\ell$ be the line of points $(x,y)$ in $\mathbb{R^2}$ that satisfy $ax+by=c$. Let $(x_{0},y_{0})$ be a particular point on this line, which means $ax_{0}+by_{0}=c$ and consequently, $$\displaylines{ax+by=ax_{0}+by_{0}\to \newline a(x-x_{0})+b(y-y_{0})=0\to \newline \langle a,b\rangle \cdot \langle x-x_{0},y-y_{0}\rangle =0 \to \langle a,b \rangle \perp \langle x-x_{0},y-y_{0}\rangle}$$
Since for any $(x,y) \neq (x_{0},y_{0})$ on the line, the non zero vector $\langle x-x_{0},y-y_{0}\rangle$ is parallel to the line $\ell$, it follows that $\langle a,b \rangle \perp \ell$

![[Screenshot 2024-10-03 at 2.44.36 PM.png]]
*Line $2x+y=4$, with the vector $\langle 2,1 \rangle$ drawn with its tail at a point on the line.* 

Now let's say $\ell$* is the line through a point $(x_{0},y_{0})$ that is perpendicular to the non-zero vector $\vec{v}=\langle a,b\rangle$ in $\mathbb{R^2}$. Then for any $(x,y)$ on the line, $$\displaylines{\langle a,b\rangle \perp \langle x-x_{0}, y-y_{0}\rangle \to \langle a,b \rangle \cdot \langle x-x_{0}, y-y_{0}\rangle = 0 \to \newline a(x-x_{0})+b(y-y_{0})=0 \to \newline ax+by =c \text{ where } c=ax_{0}+by_{0}}$$
**Geometric significance:** Let $\vec{v} = \langle a,b \rangle$ in $\mathbb{R^2}$ be a non-zero vector and $L$ be a line in $\mathbb{R^2}$. $\vec{v}$ is orthogonal $L$ if and only if $L$ consists of the points in $\mathbb{R^2}$ satisfying the equation $ax+by=c$ for some real num $c$ 

Suppose $(x_{0}, y_{0},z_{0})$ is a point in a plane $P$. Suppose $\vec{n}=\langle a,b,c \rangle$ is a non-zero vector that is orthogonal to the plane. 

![[Screenshot 2024-10-03 at 3.09.44 PM.png]]

Let $(x,y,z)$ represent an arbitrary point in the plane. Then the vector $\vec{u}=\langle x-x_{0},y-y_{0},z-z_{0} \rangle$, then $\vec{u}\perp{}\vec{n}$. So the plane is determined by $\vec{n}\cdot{}\vec{u}=0$, equivalently $\boxed{ax+by+cz=d \text{ where } d=ax_{0}+by_{0}+cz_{0}}$. Which is called the standard form for an equation of the plane. 
	
Using this, the geometric significance of the "standard form" is the same regardless if its a line in $\mathbb{R^3}$ or a plane in $\mathbb{R^3}$. The vector formed the coefficients on the variables is perpendicular to the geometric object.

Additionally, for the vector $\vec{n}$ <u>any scalar multiple vector of this normal vector</u> is also considered to be orthogonal to the plane! 

This [video](https://youtu.be/2sZKZHyaQJ8?si=wxH85sSqhx9KC8ec) explains this concept really well 

---
**Example:**
Let’s find an equation for the plane through the points $(1, 1, 2), (3, 1, 1)$ and $(2, 4, 0)$. We create two displacement vectors, with tails at $(1, 1, 2)$ and heads at the other points, and cross them, to produce a normal vector to the plane. $$\displaylines{\vec{v}=\langle 2,0,-1 \rangle \newline \vec{w}=\langle 1,3,-2 \rangle \newline \newline \vec{v}\times\vec{w}=\langle 3,3,6\rangle. \text{ So we can use } \vec{n}=\langle1,1,2 \rangle \text{ as a normal vector to our plane.}}$$
Hence an equation of the plane is $x+y+2z=6$ since $1+1+2(2)=6$ 
