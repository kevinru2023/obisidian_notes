---
~
---

| Topic  | Linux Process Loading  |
| ------ | ---------------------- |
| Date   | Thursday, January 23rd |
| Course | pwncollege             |
| Class  | reverse engineering    |



### Questions/Cues
---
- How do processes individually communicate with each other? How does a parent communicate to it's children or sibling? 
- So are processes basically inheriting the behavior of the parent process when created? 
- Does macOS have something similar to `/proc/sys/fs/binfmt_misc`? What about Windows? 
- Is there a process called to map the virtual memory space to a physical process or is this handled by the kernel? 

### Notes
---
- Every Linux process has: 
	- state (running, waiting, stopped, zombie)
	- priority (& other scheduling information)
	- parent, siblings, children 
	- shared resources (files, pipes, sockets)
	- virtual memory space 
	- security context 
		- effective uid and gid 
		- saved uid and gid 
		- capabilities
- Processes come from cloning one another similar to how cells perform *mitosis*  
- When a process is loaded, the kernel checks if a file is executable, if not **execve** will fail. 
- Afterwards the Linux Kernel looks at what the file starts with (the header)
- `/proc/sys/fs/binfmt_misc` is where the kernel checks if matches a header it knows (something like that)
- The process of cloning is very noticeable in the case of making a bash script echoing `/bin/echo` really good example here at *9:00*: ![video](https://youtu.be/kUMCAzSOY-o?list=PL-ymxv0nOtqqQ4NR1JnbWoHNm0Q8EspO1&t=549)
- The process inheritance is *recursive* 
- The process for *dynamically linked ELFS* is a bit different: 
	- Process loading is done by the ELF interpreter specified in the Binary (know as the loader) this is done by the kernel 
	- The interpreter locates the libraries (Does this through env var's)
	- The interpreter loads the libraries 
- **strace** is a great tool to see what syscalls a process makes 
- Each Linux process has a *virtual memory space* which contains the following: 
	- The binary 
	- Libraries 
	- heap 
	- stack 
	- any memory specifically mapped by the program 
	- helper regions 
- You can see the whole virtual memory space by looking at `/proc/self/maps` 
- **libc** is the standard C library which most processes end up linking 
- Statically linked binaries 
	- Binaries that have *no external dependencies* (implemented instead in the same binary) 
	- Are <mark style="background: #FF5582A6;">not</mark> dynamically linked 
	- The loading process is simple, *the binary is loaded*. 
	- Take up more memory (increased file size)
- Every ELF and binary can initialize code that is to run before the program is actually launched 
- *Constructors* are functions that run before the program is actually launched (you can make your own in a program!) 
### Summary
---
A process has a couple different parts that contain various specific parts of it such as its permissions, resources, and virtual memory space. Processes are made by cloning itself similar to mitosis. <mark style="background: #FFB8EBA6;">Binaries can either be dynamically linked or statically linked</mark>, with the difference being statically linked binaries implement the libraries it uses into the binary itself. <mark style="background: #FFB8EBA6;">Processes can use constructors in order to execute functions before the program is actually launched</mark>. Each program has virtual memory space which is different from physical memory space and there exists ways to map between both spaces.
