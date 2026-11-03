#algorithms #neetcode 

---
# Thoughts: 
Overall this problem wasn't too difficult other than the fact that I didn't actually solve it in $O(n)$ time complexity but instead solved it in $O(n\log(n))$ time complexity. 


---
# Reflection: 
Initially I looked through comments because I thought this problem would require some smart fuckery in order to solve it because of the $O(n)$ time complexity requirement, but fuck all that I solved it in $O(n\log(n))$ time complexity with the help of a Leetcode comment because I didn't know where to start. (Legit just one comment mentioning a set and seeing if next element exists, I have done something similar before but just forgot.) In all honesty if you don't understand this solution you are beyond cooked. 


---
# Solution: 
```cpp
// this is actually o(nlogn) but some for some reason it accepts it? 
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }

        int maxlength = 1; 
        int currlength = 1; 
        
        set<int> s; 
        for(int i: nums){
            s.insert(i); 
        }

        for(auto i: s){
            cout << i << endl; 
            if(s.find(i+1) != s.end()){
                currlength++;
            }else{
                maxlength = (currlength > maxlength) ? currlength : maxlength; 
                currlength = 1; 
            }
        }
        return maxlength; 
    }
};
```
