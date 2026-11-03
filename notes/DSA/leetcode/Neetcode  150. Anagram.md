#algorithms #neetcode 

---
# Thoughts: 

This problem was super fun to tackle, at first I had an approach that would have worked but ultimately decided not to go about (was going to be $O(n^2)$ time). Afterwards even after I came up with a solution I realized I couldn't really do this in linear time, so for the first time, on my own I realized a problem couldn't be solved in linear time and i'm really proud of that. My first approach was the following: 

>what im thinking is having a seperate function that reimplements the anagram function
then checking if it returns yes. Then adding it to a map that contains a string and the following strings as well. 

but afterwards I decided that this approach seemed to tedious and decided to go about another approach after a conversation with [chatgpt](https://chatgpt.com/share/673470df-c120-8001-bdbb-91fa1b1265f5)

---
# Reflection: 

Overall I took way longer to force myself to do this problem but I really shouldn't have I learned a lot about problems and was thinking about various different methods I previously wouldn't have such as sorting and hashing. I think this problem is a great stepping stone to attack harder problems and am glad I tackled this problem and struggled. Onto the next.

---
# Solution: 
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> groups; 
        unordered_map<string, vector<string>> mp; 
        
        for(string s: strs){
            string t = s; // due to in place for sort
            sort(t.begin(),t.end()); // n log n
            
            mp[t].push_back(s); 
        }

        for(auto &c: mp){
            // because map is a pair type
            groups.push_back(c.second);
        }
        return groups; 
    }
};
```

--- 
# Tricks learned: 
- fucking `sort()` ?! this is where I started to realize c++ can act more like python and I just didn't know it lmao 
- maps are pairs so you access keys & values  by using `p.first` and `p.second` 