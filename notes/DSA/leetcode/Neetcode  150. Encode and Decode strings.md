#algorithms #neetcode 

---
# Thoughts: 

This problem has always given me trouble, i've gone through and tried this problem multiple times and never managed to get to a solution that made sense to me. Even now I didn't get the solution on my own, I had to heavily look into the solution code to understand how they implemented the logic. This problem should be a good problem to look back on and gain knowledge on how stuff is done especially with the neat loop tricks. 

---
# Reflection: 

So I actually had a somewhat similar intuition to what the solution looks like at least from a logical perspective. I knew approaching the problem that the solution lied into getting the lengths of a string and having them before an actual string. Where I was struggling was figuring out how to allow for any character in terms of decoding for example sure `4meow` could work for this type of encoding, however if it had numbers in it `44eow` would throw it completely off. This is where I got stumped and had to look into the articles and videos on how to approach this problem since this problem is so common everywhere and I stumbled upon the delimiter approach where you have another character after a number to know where the code starts such as `4#meow` which would then solve this issue of numbers. The other issue was also the decoding (so basically I fucking suck cause I had a problem with every step) and knowing how to basically loop through a string once and get all the separate strings without risking breaking the time complexity to just be trash. At this point I had spent ~3 days on one problem so I decided to just look at the code and saw some really neat loop tricks, that I added some notes on in the actual solution with the help of my best friend ChatGPT. 

---
# Solution: 
```cpp
class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedstr = ""; 
        for(string &s: strs){
        // the # here is the deliemter. 
            encodedstr += to_string(s.length()) + "#" + s; 
        }    
        return encodedstr; 
    }

    vector<string> decode(string s) {
        vector<string> decodedstrs; 
        int i = 0;//keeps tracks the current position in the string `s` as we decode it.
        while( i < s.size()){ 
            int j = i; //helps find the position of the delimiter 
			           //`#`, which separates the encoded length 
 of a string from the string itself.
            while(s[j] != '#'){
                j++; // think about what this is doing, 
			         // super sick trick to get the required length
            }
            //grabbing the length here of the string we want
            int length = stoi(s.substr(i, j - i)); 
            
            i = j + 1; // skip the # 
            
            //extract the string 
            j = i + length; 
            decodedstrs.push_back(s.substr(i,length)); 
            
            i = j; // move i to next decoded string 
			       // who tf thought of that way ^? 
        }
        return decodedstrs; 
    }
};

```

--- 
# Tricks learned: 
- The damn loop logic to extract a string was fucking genius and I would never have that of that 
- It's important to really nail down how you can use loops like this. 