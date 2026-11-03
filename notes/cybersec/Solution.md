# Crackme Solution 
--- 
This challenge was a fun quick little 10 minute challenge that was surprisingly enjoyable.

When first looking through the binary you are handed this output: 

```
Original Message: Hello, Reverse Engineer!
Encrypted Message: =447tx
=.=*+=x6?16==*y
Decrypted Message: Hello, Reverse Engineer!

Enter passcode:
```

So it looks like we need the passcode, well opening up the binary in binja immediately using pseudo c we are handed the following disassembly: 

![[CleanShot 2025-05-12 at 02.10.05@2x.png]]

Now I have some renamed inputs here as well as one type change to make it more obvious where the user's input is getting checked is. As we can see it compares our input to the number `1337`  (originally hex 0x539) so let's enter that in as our password and see if we can get the success message. 
![[CleanShot 2025-05-12 at 02.14.14@2x.png]]

Cool looks like I was right, so the solution is to just enter 1337, nice and easy challenge! 