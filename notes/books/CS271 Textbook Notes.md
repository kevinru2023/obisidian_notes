#books 
## Info  

| Input     | Output                          |
| --------- | ------------------------------- |
| Author    | Kip R. Irvine                   |
| Published | 2007                            |
| Theme     | Assembly                        |
| Keywords  | Computer Architecture, Assembly |
| Date Read | 2025-01-07                      |
| Status    | Reading                         |

--- 
### Summary 

> [!Summary] Summary
> This is the textbook that we are reading for my CS271 class, this is mainly notes and certain concepts that I found interesting/useful. 

- -- 
### Relevant Quotes  
  
> [!quote] Analogy for segmented memory 
> Imagine a large building, in which segments represent the building’s floors. A person can ride the elevator to a particular floor, get off, and begin following the room numbers to locate a room. The offset of a room can be thought of as the distance from the elevator to the room


> [!quote] Storage Sizes 
> The basic storage unit for all data in an x86 computer is a byte, containing 8 bits. Other storage sizes are word (2 bytes), doubleword (4 bytes), and quadword (8 bytes).


---
### Useful definitions


> [!info] Byte addressable memory 
> A single location in memory and x86 processors permit each byte location to have a separate address 


> [!abstract] Central Processer Unit (CPU)
> Where calculations and logic operations take place. This contains 4 main parts, registers which are limited number of storage locations, a high frequency clock, a control unit (CU), and an arithmetic logic unit (ALU)


> [!info] Bus
> A group of parallel wires that transfer data from one part of the computer to another


> [!abstract] Cache Memory
> The first time a program reads a block of data, it leaves a copy in the cache. If a program needs to read the same data a second time, it looks for it in the cache. A cache hit indicates that data is in a cache; a cache miss indicates data is not in cache. 


> [!info] Task Switching 
> Task switching is when the processor saves the state of each task before switching to a new one. A task's state consists of the contents of a processor registers, program counter, status flags, and references to the task's memory segments. 


---
### Notes  
- Assembler is a utility program that converts source code programs (asm) into machine language 
- Linker is a utility program that combines individual files created by an assembler into a single executable 
- A computer has 4 main bus types:
	- Data 
	- I/O
	- Control 
	- Address  
- Executing machine instruction requires three steps: 
	1. Fetch 
	2. Decode 
	3. Execute 
- MSB: the bit farthest left 
- LSB: the bit farthest right 
- A typical program has three segments:
	- code, stored in the CS register 
	- data, stored in the DS register, segments that supplement this can be ES,FS, or GS 
	- stack , stored in the SS register 
- *MOV* does not allow memory to memory assignment
- *OFFSET* is basically the `&` operator in c/c++, it serves to grab an address of a variable 
- *CMP* basically just subtracts two values, to implement if statements or logic based on this you use various flavors of the *JMP* instruction 
---
### Annotations 
- [[CS271 Textbook Annotations# ^56lcgmuva9 | L0 and L1 VM's]]
- [[CS271 Textbook Annotations# ^qael08b0me | Figure showing offset address example]]
- [[CS271 Textbook Annotations#^ixu4vqzfi6p | Conversion charts for different storage sizes]]
- [[CS271 Textbook Annotations#^9c6uqrvrbtb| Different CPU Mode of Operations ]]
- [[CS271 Textbook Annotations#^8gxypwxpn| General Purpose Registers]]
- [[CS271 Textbook Annotations#^4ke9ixua35v| Special Uses of General Purpose Registers]]
- [[CS271 Textbook Annotations#^whnhjip4k| Status Flags]]
- [[CS271 Textbook Annotations#^tlqauysmn2i| ASM syntax]]



