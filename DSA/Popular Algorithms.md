#algorithms #cs261 #self-study 

> [!Examples]
> ## For code examples in C++, checkout --> [[Basic Algorithms in C++]]
> 

---
### Linear Search↗️  : 
- Iterate through a collection one item at a time 
- $O(n)$
- Advantages✅: 
	- Fast for searches of small-medium data sets 
	- Does not need to be sorted 
	- Useful for data structs that aren't random access (i.e. linked lists)
- Disadvantages❌: 
	- Slow for large data sets 

### Binary Search 🤖: 
- Finds position of a target value within a sorted array
- At each step half the array is eliminated during each step 
- A popular example is the guessing number game 
- Advantages✅: 
	- Great for large datasets 
	- $O(\log(n))$
- Disadvantages❌:
	- Bad for small datasets 

### Interpolation Search🦯 :
- Improvement over binary search best used for "uniformly" distributed data
- Basically make "guess" where a value might be, based on calculated probe results (this formula is very complicated so worth memorizing )
- If probe is incorrect, search area is narrowed, and new probe is made 
- Average case: $O(\log(\log(n)))$ 
- Worse Case: $O(n)$
- this works because it moves the bounds of the searchable array 

### Bubble sort 🫧: 
- Works by checking if adjacent elements are ordered and if they aren't it switches them. 
- This works by also storing a temp value 
- This bubbles the top elements to the end of the array 
- Not a very efficient  sorting algorithm due to its time complexity $O(n^2)$
- Easy to write however 

### Selection Sort🔦: 
- In place sorting algorithm 
- Keeps track of min value during each iteration, and at the end of iteration we swap variables 
- Each iteration does the following: 
	- Keep track of the min value 
	- At the end of iteration swap the min value where it belongs. 
	- This is done by keeping track of the index of where the min value occurred, moving it where it belongs, and also keeping track of the index of the value that it will be swapped with
- Runtime complexity of $O(n^2)$

### Insertion sort🧩: 
- Begins at index 1, store value in a tmp value, examine elements to the left and shift them if they are bigger than the temp value. 
- Like a jigsaw puzzle, some pieces are together, but we need to move them to make room for one piece 
- Runtime complexity of $O(n^2)$, best case is $O(n)$ 

## Now for a quick detour into recursion 
- What is recursion? : Apply the result of a procedure to a procedure 
- Dividing a problem into sub-problems of the same type as the original 
- Used in advanced into sorting algorithms and navigating trees 
- Advantages ✅: 
	- Easier to read/write 
	- Easier to debug 
- Disadvantages ❌:
	- sometimes slower 
	- uses more memory 
- When defining recursion you need base cases which stops the recursion and the recursive case which is what gets repeated 
- When recursion happens instead of a just invoking one method onto the call stack (like iteration), you call multiple methods onto the call stack (THIS MAKE SO MUCH SENSE NOW) creating more frames. 

Here is an image explaining the differences 
![[Screenshot 2024-08-30 at 7.17.38 PM.png]]