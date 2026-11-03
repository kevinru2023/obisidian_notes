---
~
---

| Topic  | Data Access          |
| ------ | -------------------- |
| Date   | Saturday, March 15th |
| Course | Reverse Engineering  |
| Class  | pwncollege           |



### Questions/Cues
----
- What does heap data access look like
- When do we use the heap? 
- What does the heap look like in asm? 

### Notes
---
- Accessing **data on the stack**: 
	- `push` 
	- `pop` 
	- **rsp**-relative accesses: 
		- load: `mov rdx, [rsp+0x10]`
		- store: `mov [rsp+0x10], rdx`
		- offsets *positive* because `rsp` points to bottom of stack frame 
	- **rbp**-relative accesses
		- load: `mov rdx, [rbp-0x10]`
		- store: `mov [rbp-0x10], rdx` 
		- offsets *negative* because `rbp` points to top of stack frame![[stackframe 1.png]]
	- via reference 
		- `mov rdx, rsp; mov [rdx], 0x41`
		- `mov rdx, rbp; mov [rdx], 0x41`
- Accessing **data in ELF sections** 
	- Data in *.bss*, *.rodata*, and *.data* are stored at known offsets from the program code. 
	- Accessed via **rip**-relative instructions
		- Load: `mov rax, [rip+0x20040]`
		- Store: `mov [rip+0x20040], rax`
		- Reference: `lea rax, [rip+0x20040]` , [LEA instruction](https://stackoverflow.com/questions/1658294/whats-the-purpose-of-the-lea-instruction) 
- Accessing **data on the heap** 
	- Pointers to heap data are generally stored in memory or on the stack 
	- Keep in the mind the *difference* between the following 
		- Stack data access: `mov rax, rsp` , `mov rdx, [rax]`
		- **Arbitrary data access via stack-stored ref**: `mov rax, [rsp]`, `mov rdx, [rax]` (note here in the 1st instruction rsp has to contain a pointer in order for this deref to work)****
- Data structures
	- Type information is lost in compilation process. *You have to piece type information together based on how data is used by code* 

### Summary
---
When accessing data <mark style="background: #FF5582A6;">we have three types of data access; data on the stack, data in ELF sections, and data on the heap</mark>. Most data accessing occurs through some stack manipulation i.e. `mov rax, [rbp-0x10]`.  Each different type of data access has it's own type of nuances of storing, loading, and referencing data. <mark style="background: #FF5582A6;">When reversing a program, data types are lost and therefore in order to understand a program you will had to piece type information based on how data is used by the code. </mark>
