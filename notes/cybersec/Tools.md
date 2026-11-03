---
~
---

| Topic  | Tools               |
| ------ | ------------------- |
| Date   | Sunday, March 16th  |
| Course | Reverse engineering |
| Class  | pwncollege          |



### Questions/Cues
----
- What goes into making a disassembler? 
- What is so special about those addresses that GDB tries to load executables into? 

### Notes
---
- Static tools are tools that analyze a program at rest 
- Simple static tools 
	- **katai struct**: file format parser and explorer 
	- **nm**: list symbols used/provided by ELF files 
	- **strings**: dumps ASCII (and other formats) strings found in a file
	- **objdump**: simple disassembler
	- **checksec**: analyzes security in an executable 
- Advanced Disassemblers 
	- IDA Pro: "Gold standard" expensive as shit 
	- Binary Ninja: IDA's main competitor and my favorite 
	- Ghidra: Created by NSA and open source 
	- Angr management: academic binary analysis framework 
	- Cutter: reverser created by radare2 open source project 
- Dynamic tools analyze a program during run time 
- Simple dynamic tools 
	- **ltrace**: traces library calls 
	- **strace**: traces system calls
	- **gdb**: debugger, goated 
		- this utility also allows scripting! 
- Position independent executables (**PIE**)
	- To understand this it will be easier to understand PDE or position dependent executables, these are executables that are loaded at a static address in memory 
	- PIE's are not loaded at a static address in memory 
	- GDB helps by trying to load executables at `0x0000555555554000` or `0x7ffff7ffc000`
		- This will allow scripting to be easier if you set this address as the `$base` in the `.gdbinit` file 
- *Timeless* Debugging, frees you from having to think of bp ahead of time 
	1. record execution 
	2. rewind execution 
	3. replay execution 
	- Some tools that have this feature 
		- **gdb**: fairly straightforward
		- **rr**: much more performant
		- **qira**: made for reverse engineering
### Summary
---
Overall these set of two lectures were fairly straightforward. Static tools allow you to analyze a code whilst it's not running, whilst dynamic tools allow you to analyze a program as it's running. Some nice topics that were introduced was <mark style="background: #FF5582A6;">PIE which is the concept that programs are loaded into a random place in memory</mark> and also<mark style="background: #FF5582A6;"> Timeless debugging which allows you to step back and step forward through instructions</mark>. 
