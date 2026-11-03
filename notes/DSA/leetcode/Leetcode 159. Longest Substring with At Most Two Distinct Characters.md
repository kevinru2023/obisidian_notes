#algorithms #leetcode

---
# Thoughts:

This problem was a bit hard for me, I at first approached it with a generic one pointer approach with a set to keep track of characters, this solution did not work, I then realized that the problem could be solved with two pointers, which did get me a bit farther but I ultimately got stuck. Heres whats I learned. 

- Sometimes a problem requires more than one method. This problem was solved using a hash map that kept track of indexes and also used two pointers 
- The video solution used a really cool approach by first considering the string as an array (obvious) and treating each index as an unknown, I think this could be really useful as it will erase that mindset I have when it comes to certain problems. 
- The solution solves out base cases first so I need to think about that as well, it could lead to faster base case solves 
---
# Reflection:

I can improve on these problems by considering these problems from an even further view. I think it might be beneficial to attack some of these problems by pen and paper first and really try to get a solution on paper down first, before I even write code. 

---
# Solution: 
```cpp
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        // Start the window at length == 1
        size_t n = s.length();

        // Handle base case
        if (n < 3) {
            return n;
        }

        int left = 0, right = 0;
        map<char, int> mp; // Track character indices
        int mxlen = 2;

        while (right < n) {
            mp[s[right]] = right;
            right++;

            if (mp.size() == 3) {
                int del_index = INT_MAX;
                for (const auto& element : mp) {
                    del_index = min(del_index, element.second);
                }
                mp.erase(s[del_index]);
                left = del_index + 1;
            }
            mxlen = max(mxlen, right - left);
        }
        return mxlen;
    }
};
```
