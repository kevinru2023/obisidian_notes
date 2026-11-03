#data-structures #cs261 #self-study 

> [!Examples]
> ## For code examples in C++, checkout --> [[Basic Data Structures in C++]]
> 

---

#### Terminology: 

- Data Structure: A named location that can be used to store and organize data 📊
	- Example: int nums[3] <-- an array data structure 
- FIFO: First in, First out 
- LIFO: Last in, First out  
- Head: First element in data structure 
- Tail: Last element in data structure 

#### Stack 📚: 
- LIFO data structure 
- Stores objects into a sort of "vertical tower" 🗼
- push() to add to the top 🔝
- pop() to remove 
- peek() to check item at the top 🔝
- empty() to check if stack is empty 
- search() to search for item 
- Uses of stack? 
	1. Undo/redo features in text editors 
	2. moving back/forward through browser history 
	3. backtracking algorithms (maze, file directories)
	4. calling functions (call stack)

#### Queue 🎟️: 
- FIFO data structure 
- A collection designed for holding elements prior to processing 
- Linear data structure
- add to tail= enqueue ➕
- remove item at head = dequeue ➖
- has various methods depending on language 
- actually implemented using a linked list in java (something to keep in mind)
- Uses: 
	1. Keyboard Buffer(Letters should appear on the screen in the order they're pressed)🎹
	2. Printer Queue 🖨️
	3. Used in LinkedLists, PriorityQueues, and Breadth-first search 

#### Priority Queue 👑: 
- FIFO data structure 
- Serves elements with highest priorities first before lower priorities ﹥
- First orders the elements in terms of priority then creates the data structure 
	- So sorts the data then hands out the data structure 
	- Think back of unsorted gpa example just using queue vs priority queue 
- If data type is string then the elements are in alphabetical order 🔤
- can be implemented using heaps for faster complexity! 

#### Linked Lists🖇️:  
- Normal arrays are contiguous meaning the elements are sorted one after another for example: 
	- "A": "123 street", "B": "124 street", "C": "125 street" (not actual streets but memory addresses) 🏠
	- Makes adding things to big arrays very difficult because you have to shift over everything if you want to add something 😮‍💨
-  Made up of a long chain of nodes each containing: 
	1. Data to store 📊
	2. An address to the next node (a pointer) 👉
- Nodes are **in non-consecutive memory locations** and each node knows where the next one points, like a map 🗺️
- You begin at the **Head** and navigate to the **tail** which address is **null** 
- Easy to insert wherever you need because you simply ⎀: 
	1. Take address stored in previous node 
	2. Set address of new node and set it address of previous node
	3. Set previous node address to address of new node 
	- Might want to revisit video if you have trouble visualizing this.
- Easy to delete as well: 
	1. Set previous node to point to the next node in line (we are at the node at which we want to delete in this example)
-  **Singly linked lists** vs **doubly linked lists**: 
	- Single linked lists: 
		- Contain data and address
	- Doubly linked lists: 
		- Contain data, address pointing to previous node, and address pointing to next node
		- Use more memory 
		- Makes it possible to go through a linked list in reverse 
- Advantages✅: 
	1. Dynamic Data Structure (allocates needed memory while running)
	2. Insertion and Deletion of Nodes is easy. O(1) complexity 
	3. No/Low memory waste 
- Disadvantages❌:
	1. Greater memory usage (additional pointer)
	2. No random access of elements (no index [i])
	3. Accessing/searching elements is more time consuming. O(n)
- Uses: 
	1. implement Stacks/Queues
	2. GPS navigation
	3. Music playlist 

#### Dynamic Array 𝌒: 
- An array with a resizable capacity  
- Has different names depending on language: 
	- Python = List 
	- C++ = Vector 
	- JavaScript = Array
	- Java = ArrayList 
- **Static array** vs **Dynamic Array**: 
	- Static: 
		- Has fixed capacity, determined at compile time, which is also it's disadvantage 
		- Can randomly access item at O(1), but searching still takes O(n) same with insert and 
		- Can't increase capacity after array is full 
	- Dynamic: 
		- Has it's own inner static array with its fixed size 
		- After dynamic array is full, it will create a new array with an increase capacity <-- determined by programming language 
		- This means that it will create a new array and will fill it up with values and if the array is not full those values are empty, meaning this potentially takes up a lot of memory! You could counter this by  just simply doing reverse process of above bullet point. 
		- Same time for insert/deletion and still allows for random accessing of elements, also allows for good locality of reference and data cache utilization (elements are next to each other in memory so it makes it easy to see where stuff is)
		- Wastes more memory thank linked lists, shifting elements and expanding/shrinking are all O(n)
- Has a couple different methods but the two most notable are grow and shrink which is what makes a dynamic array, well dynamic. The deletion method is also very interesting (check out code snippets!) 

#### Dynamic Array (ArrayList) vs LinkedList 🥊

| Method                                    | Dynamic Array | Linked List |
| ----------------------------------------- | :-----------: | :---------: |
| Accessing elements                        |       ⚡       |     🐌      |
| Inserting/Deletion (for elements < 1 mil) |       ⚡       |     🐌      |

#### Big O notation ⚡
`"How code slows as data grows"`
- Describes the performance of an algorithm as the amount of data increases 
- Machine Independent (# of steps to completion)
- Ignores smaller operations, ex: O(n +1) --> O(n)
- N is representation of data we are passing in. 
- Graph of times: ![[big_o_graph.png]]
- $O(1)$ = constant time
  - Inserting at the beginning of linked list 
  - random access of an element in an array 
- $O(\log{}n)$ = logarithmic time 
  - Binary Search 
- $O(n)$ = linear time 
  - looping through elements in an array 
  - searching through a LinkedList
- $O(n\log{}n)$ = quasilinear time 
  - Quick sort 
  - Merge sort 
  - Heap sort 
- $O(n^2)$ = quadratic time 
  - insertion sort 
  - selection sort 
  - bubble sort 
- $O(n!)$ = factorial time 
  - Traveling salesman problem 

> [!Algorithms]
> ## For Algorithms, checkout --> [[Popular Algorithms]]
> 