---
~
---

| Topic  | Functions and Frames    |
| ------ | ----------------------- |
| Date   | Saturday, February 22nd |
| Course | pwncollege              |
| Class  | Reverse Engineering     |

### Questions/Cues
----
- How does `-fomit-frame-pointer` work under the hood, how is this allowed? 
- How does one just recognize which syscall is being made off of the asm? 
### Notes
---
- Program consists of **modules**, which are made up functions, that contain blocks of instructions that operate on variables and data structures
- Modules are libraries that developers rely on to build software (such as libc)
- *Functions* represent fairly well-encapsulated functionality that *have a goal* which are usually as follows:
	- set some data
	- calculate/retrieve/validate data 
	- dispatch(call) other functions
	- perform some action on the outside world (syscalls)
- Functions are represented as a **graph** 
	- Each **block** is a set of instructions that will execute a set of instructions that will execute one after the other 
	- Blocks are joined by **edges**, representing conditional and unconditional jumps 
	- Understanding what blocks do and what conditions trigger can help you understand a function's logic. 
- Functions often begin with a prologue and end with an epilogue
	- Usually start with setting up the stack frame i.e. 
		- `push ebp`
		- `mov ebp, esp`
	- End with tearing down the stack frame i.e. 
		- `mov esp, ebp`
		- `pop ebp`
- Stack is a region of memory used to store local variables and call contexts (for more notes on this check GoodNotes)
	- Starts out storing the environment variables and program arguments 
	- **Prologue:** 
		1. Save off the caller's bp 
		2. Set the current sp as the bp 
		3. "allocate" space on the stack (subtract from sp)
	- **Epilogue:** 
		1. "deallocate" the stack (`mov esp, ebp`), *data is not destroyed by default*
		2. Restore the old bp 
- `-fomit-frame-pointer` is something modern compliers can do, which omits frame pointers and allows `rbp` to be used as a general purpose register
### Summary
---
A program consists of functions which under the hood are assembly instructions that setup a stack frame. Operations for local variables and some other functionality include manipulation of two primary registers when it comes to stack frames, which are `esp or rsp` and `ebp or rbp`.<mark style="background: #FF5582A6;"> Each function has a prologue and an epilogue which include setting up registers for the stack frame</mark>. <mark style="background: #FF5582A6;">Functions can be represented as a graph with blocks which are instructions that will execute one after the other and edges which are conditional and unconditional jumps.</mark> A good understanding of a function's graph can lead to a understanding of the function itself. 
