
$(\mathbb{Z}/20\mathbb{Z})^\times$ (also written $U(20)$) is the

group of units

of $\mathbb{Z}_{20}$ — the set of elements in ${1, 2, \ldots, 19}$ that are

relatively prime to 20

, under multiplication mod 20. Formally: $$(\mathbb{Z}/20\mathbb{Z})^\times = { k \in \mathbb{Z}_{20} \mid \gcd(k, 20) = 1 }$$ An element $k$ has a multiplicative inverse in $\mathbb{Z}_n$ iff $\gcd(k,n)=1$ (Judson Prop 3.1), so these are exactly the invertible elements.

For $n = 20$:

since $20 = 2^2 \cdot 5$, the elements coprime to 20 are those not divisible by 2 or 5: $$U(20) = {1, 3, 7, 9, 11, 13, 17, 19}$$

Order:

$|U(20)| = \varphi(20) = \varphi(4)\cdot\varphi(5) = 2 \cdot 4 = 8$. By the Fundamental Theorem of Finite Abelian Groups, $U(20) \cong \mathbb{Z}_2 \times \mathbb{Z}_4$ (since $U(4) \cong \mathbb{Z}_2$ and $U(5) \cong \mathbb{Z}_4$ by CRT). Sources: [[wiki/concepts/groups]], [[sources/courses/mth343/judson12.md]]