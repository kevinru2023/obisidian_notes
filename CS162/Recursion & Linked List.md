#cs162 #design 
#### Kevin Rubio | CS162 | 12-2-24
---
## Problem statement: 

	The assignment has two parts, the first is a recursion problem involving finding the amount of ways to the top of a staircase. The second is implementing the Linked List data structure in c++ from scratch. 

---
### Understanding the problem 

For the first part, the main problem lies in understanding what the base cases I will need are. In the problem description there are three different steps to get to the top of the staircase, you can take 1 step (Small step), 2 steps (Medium Step), or 3 steps (Large step). Using these three steps you can get the three base cases where if n = 1 then return 1, n = 2 then return 2, if n = 3 then return 4. These three base cases will be the foundation of the recursion where each other step can be created from these three base cases similar to how mathematical induction works. 

For the second part, I have to complete some functions that were defined in the header file, the functions are : linked_list (copy constructor) , operator=, ~linked_list (destructor), get_length, print, clear, push_front, push_back, insert, pop_front, pop_back, remove, sort_ascending, and sort_descending. For the sorting algorithms I am required to implement a recursive merge sort algorithm. There is a big of logic that I have to make sure I include, for example if the head node  points to a nullptr length should return 0 and other functions like pop_back and pop_front should do nothing. Overall this part of the assignment will require me to look into the edge cases and also understand how I need to traverse the linked list into to accomplish what I need to do. 

--- 
### Pseudocode
```
int ways_to_top(int n ): 
	//might need error handling for n 
	if n == 1: 
		return 1
	else if (n == 2): 
		return 2
	else if (n == 3):
		return 4
	else: 
		// something like this I think? 
		ways_to_top(n - 1) + ways_to_top(n -2 ) + ways_to_top(n -3 )

//this will be in linkedlist.cpp 
linked_list::get_length(): 
	return this->length 

linked_list::push_back(int val): 
		iterate through linked list, change last node to point to a 
		new node with data 

linked_list::push_front(int val): 
	create a new node with the new data and have it point to head, 
	then set that new node as the head.
	 
linked_list::sort_ascending():
	inplace merge sort that sorts in ascending order 
	
linked_list::sort_descending():
	inplace merge sort that sorts in descending order 

linked_list::insert(int val, int index): 
	will go to the node before index and then change that node to point 
	to a new node pointing to the old node. (basically putting itself
	before the node at index)
	
linked_list::pop_front():
	similar to push_front but removes instead 

linked_list::pop_back():
	similar to push_back but removes instead 

linked_list::remove(int index):
	similar to insert but instead removes and if it's at the end will 
	just create the new pointer to point to nothing (nullptr) else it 
	will make it point to the node after the index. 

linked_list::print():
	will print out the contents of the linked list 

linked_list::clear(): 
	will go through and free the entire linked list and it's ptrs 
```
---
### Test Cases: 

| Value                                     | Expected                     | Actually met expectation |
| ----------------------------------------- | ---------------------------- | ------------------------ |
| ways_to_top(4)                            | 7                            | yes                      |
| ways_to_top(5)                            | 13                           | yes                      |
| ways_to_top(6)                            | 24                           | yes                      |
| linkedlist l;                             | creates an empty linked list | yes                      |
| l.get_length()                            | 0                            | yes                      |
| l.push_front(5), l.print()                | "5"                          | yes                      |
| l.push_front(10),l.pop(back),l.print()    | "10"                         | yes                      |
| l.push_back(5),l.sort_ascending,l.print() | "5,10"                       | yes                      |
| l.sort_descending,l.print()               | "10,5"                       | yes                      |
| l.remove(1),l.print()                     | "10"                         | yes                      |
| l.clear(),l.get_length()                  | 0                            | yes                      |
