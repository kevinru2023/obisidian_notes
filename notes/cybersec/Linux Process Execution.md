---
~
---

| Topic  | Linux Process Execution |
| ------ | ----------------------- |
| Date   | Tuesday, February 11th  |
| Course | pwncollege              |
| Class  | Reversering             |



### Questions/Cues
----
- What other type of signal combinations are well known that I need to know about?
- If syscalls are used so much how are they protected? 
- What the hell is PID 1? 

### Notes
---
- In a normal ELF file automatically calls *libc_start_main()* which in turn calls the program's *main()* function 
- Process's entire input at launch (from outside world perspective) contains: 
	- The loaded objects (binaries & libraries)
	- command-line arg's in **argv**
	- "environment" in **envp** 
- Using library functions have some requirements: 
	- The binary's import *symbols* have to be resolved using the libraries *export symbols*
- Almost all programs have to interact with the outside world (things like user space etc.) This is mainly done through *system calls* which are well documented in section 2 of the man pages (**man 2 open** for **open** syscall)
	- **strace** is a utility that allows us to trace syscalls 
	- typical signal combinations include: 
		- fork, execve, wait (**think: a shell**)
		- open, read, write (**think: cat**)
- **Signals** pause process execution and invoke the **handler** which are functions that take one arg, the signal number. Without a handler for a signal the default action is used (often, kill). ***Basically signals are used for when the OS wants to call into a process.*** 
	- Two signals *cannot be handled*: 
		- **SIGKILL** (signal 9) 
		- **SIGSTOP** (signal 19)
- **Shared memory** is another way of interacting with the outside world by sharing memory with other processes. This requires syscalls to establish, once established communication happens without syscalls. 
- Process termination
	- happens in one of two ways: 
		1. Receiving an unhandled signal 
		2. Calling the exit() syscall 
	- All processes must be "*reaped*"
		- After termination, will remain in zombie state until they are wait()ed on by their parent
		- When this happens, their exit code will be ret'ed to the parent and the process will be freed 
		- If the parent process dies without wait()ing on them, they are re-parented to PID 1 and will stay there until cleaned up. 
### Summary
---
An ELF file has many different things it does during execution some include loading in libraries which includes importing symbols. <mark style="background: #FF5582A6;">During execution most interaction through the outside world in a program is done through system calls </mark>which are functions provided usually by the kernel. <mark style="background: #FF5582A6;">Signals also play a vital importance and are used for when an OS wants to call into a process (sort of like interrupting it)</mark>. All processes must be reapead which means they are sort of alive until they are wait()ed on by their parent, which then will return their exit code to the parent and the process will be freed. 
