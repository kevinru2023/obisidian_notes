# CTF Write-Up

### Platform: pwncollege 
### Challenge:  File Formats: Magic Numbers 
---
Description: 
The `/challenge/cimg` binary in this level is (the start of) an image rendering program, specifically focusing on the cIMG format. Software identifies the formats of files (e.g., whether the file is a GIF, a JPEG, an MP3, or so on) in a few ways:

1. The file extension. This is the part of the file after the `.`: a `ZardusSmiling.jpg` is probably a JPEG of Zardus smiling, whereas `KanakLaughing.mp3` is probably an MP3 of Kanak laughing.
2. The _magic number_. Files can get renamed, or the filenames associated with files can be lost (e.g., in a partial filesystem failure) or simply missing (e.g., in a data stream). Thus, most file formats include a _magic number_ in the format that a parser can check to identify it.

In this challenge, you must craft a file with a `cimg` extension that contains the correct magic number. You can learn this magic number by reversing the `/challenge/cimg` binary. If you properly get past the magic number check, the challenge will give you the flag!

--- 
### Initial steps: 
So for this challenge we had to craft a file that had the `.cimg` extension and also had some magic numbers in order to pass a check the file checker. With that in mind let's do our initial reconnaissance checking various information about the program. 

1. `file`, when running file we are given the following output: 
```text
./cimg: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f559ac17ecbf3060c88d08a8cf4cbb8e3c89b937, for GNU/Linux 3.2.0, not stripped
```
2. `checksec` 
```text
[*] '/challenge/cimg'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

--- 
### Next steps: 

So as we saw the program has no PIE and was also not stripped, great with this in mind lets try creating a file with the `.cimg` extension! Here is the output when we check how we did: 

```
./cimg /home/hacker/test.cimg 
ERROR: Failed to read cimg header!
```

Okay looks like we need a bit more than just a file with a .cimg extension, lets open up the binary in binary ninja and take a look at where exactly we are failing. Here is the graph view using pseudo c, more on the low level IL later on for my own personal notes. 
![[CleanShot 2025-03-27 at 18.20.50@2x.png]]

So we can see we are def getting past the first check which is good, then the second check where we have `strcmp(strlen(arv[1]) - 5 + argv[1], ".cimg")` which is checking the last five characters to make sure they are `.cimg`.

Well further looking at the graph we can see the error message we were presented in the `read_exact` function call, and before that we call `dup2()` which isn't as interesting, all that is important about that function is it will redirect our stdin to point to the file. `read_exact` is called with a couple arguments getting passed into it with the args being `0, &var_24, 4, "ERROR: Failed to read cimg header", 0xffffffff`. Let's take a look at the function now. 
![[CleanShot 2025-03-27 at 18.27.00@2x.png]]

So it looks like what this function is doing is calling `read()` with the arguments as the following `read(0,&var_24,4)` so this is going to read 4 bytes into the `&var_24`, if it encounters an error and cannot read anything then it will print out the error message we specified and exit with the error code `0xffffffff`. 

So this means we will have to have something in our file but what is that exactly? Well going back to the main graph flow we can actually see something very interesting right after the `read_exact` call. 
![[CleanShot 2025-03-27 at 18.20.50@2x.png]]

Hm what is that long if statement that appears to read in 4 bytes? It look's like it's taking in that `var_24` which we already assumed to be the contents of our file and does checks on it. 

It looks like the byte values are 0x63, 0x49, 0x4d, 0x47. Which convientely convert to cIMG, could this be the magic file number? Let's go ahead and edit the hex values of our file to make this be the head of our file. Our file now looks like this: 
``` 
xxd /home/hacker/test.cimg | head
00000000: 6349 4d47                                cIMG
```

After running the program with our new file we are presented with the flag!
```
./cimg /home/hacker/test.cimg 
pwn.college{Y4XEIT58MjF2rFeAVPhldIuA7hH.QXwAzMwEDLzYTOzUzW}
```

---
### Reflection 

This was a fun little challenge that let me mess around with some things as far as hex editing goes as well as other things. I first tried to tackle the challenge in pure low level IL but did not get far as it was quite confusing, for reference here is a screen shot of the main function in low level IL ![[CleanShot 2025-03-27 at 18.42.50@2x.png]]
I was having a trouble interpreting the various registers setup and trying to figure out what I was actually being read and had to look up quite a lot of information and rely on some AI to figure out what the offsets of argv and argc look like in ASM. However I learnt a lot and hope to continue my reversing journey with these challenges! 