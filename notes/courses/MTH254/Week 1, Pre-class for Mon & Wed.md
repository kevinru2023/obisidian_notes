#mth254 
# Dot and Cross Products
---
**2D:** The dot product of two vectors $\vec{u} = \langle{u_1,u_2} \rangle$﻿ and $\vec{v} = \langle{v_1,v_2}\rangle$﻿ is the scalar $u_1v_1 + u_2v_2$﻿  

**3D:** the dot product of two vectors $\vec{u} = \langle{u_1,u_2,u_3}\rangle$﻿ and $\vec{v} = \langle{v_1,v_2,v_3}\rangle$﻿ is the scalar $u_1v_1+u_2v_2+u_3v_3$﻿

**Dot product is denoted by** $\vec{u} \cdot \vec{v}$﻿

![[Screenshot_2024-09-29_at_8.26.26_PM.png]]

==**Additional identity:**== ====$\boxed{\vec{u}\cdot\vec{v}=|\vec{u}||\vec{v}|\cos{\theta}}$====﻿ ==(derived from law of cosines)==

==$\vec{u}\perp\vec{v}$==﻿ ==**if and only if**== ==$\vec{u}\cdot\vec{v} = 0$==﻿

**Orthogonal projection:** The orthogonal projection of $\vec{u}$﻿ onto $\vec{v} \not = 0$﻿, denoted $p = proj_v(\vec{u})$﻿, is defined as the scalar multiple of $\vec{v}$﻿ that is orthogonal to $\vec{u}-\vec{p}$﻿. Picture below(**u-p** and **v** are $\perp$﻿)

![[2885cf22-a9fd-427d-81ae-790360c19a33.png]]

  

==**formula for above**== ==$\boxed{proj_v(u) = (\frac{\vec{u}\cdot\vec{v}}{\vec{v}\cdot\vec{v}})\vec{v}}$==﻿

Supplementary [explanation](https://flexbooks.ck12.org/cbook/ck-12-precalculus-concepts-2.0/section/7.5/primary/lesson/vector-projection-pcalc/)
Supplementary [example](https://math.stackexchange.com/questions/3843684/find-the-magnitude-of-the-force-required-to-keep-a-4000-lb-car-from-rolling-down)

---
**Cross product:** the cross product of two 3D vectors $\vec{u} = \langle{u_1,u_2,u_3}\rangle$﻿ and $\vec{v} = \langle{v_1,v_2,v_3}\rangle$﻿ (in that order) is $\vec{u}\times\vec{v}$﻿ and is defined as:

$\boxed{\vec{u}\times\vec{v} = \langle{u_2v_3 - u_3v_2,u_3v_1-u_1v_3,u_1v_2-u_2v_1}\rangle}$

![[Screenshot_2024-09-29_at_9.17.38_PM.png]]

the above helps with memorization of the formula, honestly I could see how this could be confusing so just go to timestamp **9:55** on this [video](https://canvas.oregonstate.edu/courses/1978938/pages/preparation-for-mon-and-wed-week-1?module_item_id=24780150).

  

$\boxed{\vec{u}\times\vec{v} = |\vec{u}||\vec{v}|\sin{\theta}}$

  

due to the above, one can show that $|\vec{u}\times\vec{v}|$﻿ is the area of the parallelogram whose non-parallel sides are $\vec{u}$﻿ and $\vec{v}$﻿

![[Screenshot_2024-09-29_at_9.33.56_PM.png]]


For a proof of this geometrically check out timestamp **14:36** on this [video](https://canvas.oregonstate.edu/courses/1978938/pages/preparation-for-mon-and-wed-week-1?module_item_id=24780150)
**If vectors** $\vec{u},\vec{v}$﻿ **in** $\mathbb{R}^3$﻿ **are orthogonal then their cross product is equal to a vector orthogonal to both and with a magnitude equal to the product of their magnitudes.**