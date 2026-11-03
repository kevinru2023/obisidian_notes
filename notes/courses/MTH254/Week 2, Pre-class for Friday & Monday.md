#mth254 

# Functions of several variables
--- 
![[typical_3d_function_graphs.excalidraw]]
(3D graphs basically)
(Study Achieve 2.6 to really nail down equations to graphs)
Note: A hyperbolic paraboloid is also called a "saddle" (looks like a Pringle to me)

--- 
**Trace:** A trace is in $\mathbb{R^3}$ is the cross-section of the surface cut by a plane (intersection of the surface and plane). When the plane corresponds to $x = k$, $y= k$ or$z = k$ the resulting trace is called an x-trace, y-trace, or z-trace.

Here is the z-trace at $z = k$ along the surface $z = C− \sqrt{x^2 + y^2}$  where $k < C$ are constants. (The z-trace here btw is the cone)
![[Screenshot 2024-10-10 at 5.15.27 PM.png]]
*(The top point is $x,y =0$, any point where $z=k$ and below $z=c$ is the circle area)*

--- 
A function $f$ of two variables x and y is often expressed with $z$ set to the output, $z = f (x, y)$ and the graph of that surface is the graph of $f(x, y)$. The <u>domain</u> is a subset $D$ of the $xy$-plane at which $f$ is defined. The <u>range</u> is $R= {f (x, y)|(x, y) ∈D}$, a subset of the real numbers. Since each $(x, y)$ in the domain $f(x, y)$ has a unique output, every vertical line through the graph of $f(x, y)$ intersects it at most once. (This shit really just describing a normal function tbh)

Here is the graph the function $f(x, y) =\sqrt{-1 + x^2 + y^2 }$. Note the domain is $\{{(x, y) ∈\mathbb{R^2}| x^2 + y^2 ≥ 1}\}$and the range is $[0, ∞)$.

![[Screenshot 2024-10-10 at 5.29.29 PM.png]]

--- 
Consider a surface defined by $z = f (x, y)$. Imagine the intersection of the surface with various planes parallel to the $xy$-plane (where $z = k$). These $z\text{-traces}$ in $xyz$-space are called contours, and projected into the $xy\text{-plane}$, they are called level sets (aka level curves since they are usually curves). Several level sets together is called a <u>contour map</u>.

Here is a contour map for $f(x,y)=2x+y-x^2$

![[Screenshot 2024-10-10 at 5.37.23 PM.png]]
*(Imagine each of these lines coming out to you by a factor of their constant, so 40 would come out 40 units)*

Similar ideas exist for functions $f (x, y, z)$ of three variables. Their graphs are in 4-dimensions so we don’t draw them, but their *level* sets (*aka level surfaces*) where $f (x, y, z) = k$ for various constants $k$ are in 3D. (Just think about it how we showed what it would look like in 2D we can't do the same in 3D)

For example, the level sets of $f (x, y, z) = e−x^2−y^2 −z^2$ are spheres of radii $0 < r$ centered at $(0,0,0)$
