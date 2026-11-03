#books 
## Info  

| Input     | Output                      |
| --------- | --------------------------- |
| Author    | Antti Laaksonen             |
| Published | July 3, 2018                |
| Theme     | DSA                         |
| Keywords  | Data Structures, Algorithms |
| Date Read | 12-4-2024                   |
| Status    | Not done                    |

--- 
### Summary 

> [!Summary] Summary
> Contents

- -- 
### Relevant Quotes  
  
> [!quote] Definition of design of algorithms 
>  The design of algorithms consists of problem solving and mathematical thinking. Skills for analyzing problems and solving them creatively are needed.

> [!quote] Modular Arithmetic 
> Sometimes, the answer to a problem is a very large number but it is enough  
to output it ”modulo m”, i.e., the remainder when the answer is divided by m

---
### Useful Definitions 

> [!info] Arithmetic Progression
> A sequence of numbers where the difference between any two consecutive numbers is a constant. Checkout this [[Competitive Programmer’s Handbook Annotations #^lf8mlryn45m|Example]] for a generic formula on calculating a sum of an arithmetic progression 
> 


> [!Info] Geometric Progression 
> Similar to Arithmetic Progression except it's a sequence of numbers where the ratio between any two consecutive numbers is constant. Check this [[Competitive Programmer’s Handbook Annotations #^fqj5hx2wvfb|Example]] for a formula on calculating the sum of a geometric progression. 



---
### Code/Math Snippets 

 $$\displaylines{\text{Properties of the remainder}\newline(a+b)\mod{m} = (a\mod{m}+b\mod{m} )\mod{m}\newline(a-b)\mod{m} = (a\mod{m}-b\mod{m} )\mod{m}\newline(a\cdot b)\mod{m} = (a\mod{m} \cdot b\mod{m} )\mod{m} }$$
 
```cpp
// calculating factorial using modulo 
long long x = 1;  
for (int i = 2; i <= n; i++) {  
x = (x*i)%m;  
}  
cout << x%m << "\n";
```

---
### Notes  
- Compiling with the `-O2` flag can help optimize the code if programming with c++
- `\n` works faster than `std::endl`
- in order to use long long you have to do a postfix of `LL`, so something like `long long x = 123LL`
- Macros are insanely useful if you have long function calls you need to make, checkout this [[Competitive Programmer’s Handbook Annotations #^iturnoxvhkf|Example]]
-  The C functions `scanf` and `printf` can be faster than typical c++ stdio
---
### Annotations
- [[Competitive Programmer’s Handbook Annotations #^1f5hm3wtpkmi |About Floating point Comparison]]
- [[Competitive Programmer’s Handbook Annotations #^5ug7mf4msj4|Tips about Shortening Code]]
- [[Competitive Programmer’s Handbook Annotations #^tzj33zkfg6|Section about different mathematical functions]]
- [[Competitive Programmer’s Handbook Annotations #^wxo54q67q3o|Different Competitions]]