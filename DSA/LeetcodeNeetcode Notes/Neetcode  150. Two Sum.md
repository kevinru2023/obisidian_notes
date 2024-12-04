#algorithms #neetcode 

---
# Thoughts: 

This was classic Two Sum, but it was my first time approaching this without just using a brute force O($n^2$) approach. So I had to look at a youtube video to see how I could do it. At first I thought two pointers would be the way to get this without using O($n^2$) but then I realized it's just going to slightly decrease the complexity but still have a high time complexity. Hence I watched the youtube video to understand it and the way was to see 

---
# Reflection: 

I'm writing this reflection a bit late, but overall the solution was a really interesting thought experiment for me. I thought I was already decent at recognizing when a problem will require a hash map, but I guess not. Overall I'm not too mad at my performance, i'm defiantly getting a bit better of thinking about different approaches, but I still have a ways to go. 

---
# Solution: 
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        if(nums.size() == 2){
            return {0,1}; 
        }
        map<int,int> mp; //maps number to index

        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]] = i;  // adding everything to the hash map 
        }

        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i]; 
            if(mp.find(diff) != mp.end() && mp[diff] != i){
                return {i, mp[diff]}; 
            }
        }
    }
};
```

--- 
# Tricks learned: 
- you can simply return a vector by just using `{something, something}`
- thinking about simple cases like in line 4-5 