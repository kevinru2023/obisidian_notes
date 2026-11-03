## Crackmes Challenges notes
--- 
**practice_2_rengr:**

Output when run: 
```
Original Message: Hello, Reverse Engineer!
Encrypted Message: =447tx
=.=*+=x6?16==*y
Decrypted Message: Hello, Reverse Engineer!

Enter passcode:
```

- So looks like we are first shown example of how the encryption takes place, looks like it's using numerals, lowercase letters, and some special characters 
- Looks like we need a passcode to pass the challenge 


Binary Reversing Notes: 
- One function that we pass in a string and we have a function that encrypts and decrypts? 
- The above makes me think we can just run the same process or algorithm on the decrypted string to probably get the password
- Annnd the password is hard coded in `1337`, sick challenge bro 😒, one of these days it's going to not be overly simple.... 
- looks like the function just xors every character of the string $n$ times where $n$ is the $len(s)$ with the character $X$ or
  
--- 

