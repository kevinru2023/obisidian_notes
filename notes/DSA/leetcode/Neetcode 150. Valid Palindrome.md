#algorithms #neetcode 

---
# Thoughts: 
Overall this was a very easy problem, I had some minor bugs in my code here and there but in general I got the solution completely on my own. What's funny is I was thinking this was a stack problem because I clicked on stack problems in the Neetcode path but accidentally clicked two pointers and was losing my shit over how this would be a stack problem vs two pointers. 


---
# Reflection: 

Overall the solution was really simple and easy, get valid characters, start at both ends of the string then see if the characters match up. I also took the time to do the analysis of time complexity and space complexity and both ended up coming out to $O(n)$ which ended up being correct in my analysis of the algorithm. This is a good start into two pointers, but I am going back to working on stack problems. 

---
# Solution: 
```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower); //convert the characters to lowercase. in place. 

        int left = 0; 
        int right = s.length() - 1; 

        while(left < right){
            bool leftcheck = isalnum(s[left]);
            bool rightcheck = isalnum(s[right]); 

            if(leftcheck && rightcheck){ // if both are characters in valid ranges 
                if(s[left] != s[right]){ // characters not equal. 
                    return false; 
                }
                left++; 
                right--; 
            }else{
                if (!leftcheck) left++; 
                if (!rightcheck) right--; 
            }
        }
        return true; 
    }
};
```
