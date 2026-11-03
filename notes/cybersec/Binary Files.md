---
~
---

| Topic  | Binary Files           |
| ------ | ---------------------- |
| Date   | Saturday, January 25th |
| Course | pwncollege             |
| Class  | reverse engineering    |



### Questions/Cues
----
- Is there a way to completely remove or obstruct the fields of ELF section headers? 
- What parts of the ELF headers are most useful for reverse engineering? 

### Notes
---
- ELF file defines a program on disk (giving it an address) and enables execution to allow that
- Other executable formats include PE(Windows) and Mach-o (MacOS)
- ELF program headers (specify information need for program execution)
	- *INTERP*: defines the lib that should be used to load this ELF into memory 
	- *LOAD*: defines a part of the file that should be loaded into memory 
- Using readelf you can see the offset's from it's memory address where a program will be loaded into memory (random due to ASLR)
- Section headers represent a differnet view of ELF with useful information for introspection, debugging, etc. Here are some important sections: 
	- **.text** : the executable code of the program 
	- **.plt & .got** : used to resolve and dispatch library calls 
	- **.data** : used for pre-initialized global writeable data (global arr's with init vals) 
	- **.rodata** : used for blobal read-only data (such as string consts)
	- **.bss** : used for uninitialized global writeable data (such as global arr's without init val's)
- Binaries (& libraries) that use dynamically loaded libraries rely on *symbols* (names) to find libraries, resolve function calls into those libraries, etc. 
- Here are some useful tools to interact with ELF files: 
	- **readelf** : parse elf header 
	- **objdump** : parse ELF header & disassemble the source code 
	- **nm** : to view ELF's symbols 
	- **patchelf** : to change some ELF properties 
	- **objcopy** : to swap out ELF sections 
	- **strip** : to remove otherwise-heplful information (such as symbols)

### Summary
---
ELF header contain various different information about a program and include useful information such as what <mark style="background: #FF5582A6;">function calls</mark> a program makes or what <mark style="background: #FF5582A6;">libraries</mark> a program is using. It is always useful to parse the ELF header to understand what a program is using!!! 
