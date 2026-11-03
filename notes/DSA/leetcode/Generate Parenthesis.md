#algorithms #neetcode 

---
# Thoughts: 

This problem took me almost two weeks to get my lazy ass to do it. This problem was labelled as a stack problem but was most defiantly not a stack problem. This was in fact a backtracking problem and was my first introduction to many terms such as recursion tree and pruning (basically going back into a tree). I did not solve this at all, but I did learn a lot about recursion trees and backtracking. 

---
# Reflection: 

Overall the solution was actually not terrible in code, the concepts themselves were just alien to me and was very new. The concept goes as this: 
1. Generate all pair of strings with some conditions which are 
	- String must start with a "("
	- At no point should there be more right parentheses than left parentheses 
2. If at any point we generate a string that we know is not valid lets go back up in the recursion tree 

Overall a lot of this problem was just very alien concepts to me and I really struggle when it comes to these types of problems where I have to generate all possible combinations of something without going too crazy in time complexity (i.e. I suck at dp and backtracking problems). 

---
# Solution: 
```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> results; 
        backtrack(results, "", 0, 0, n); 
        return results;
    }
private: 
    void backtrack(vector<string>& answer, string currString, int lCount, int rCount, int n ){
        if (currString.size() == 2 * n){
            answer.push_back(currString);
            return; 
        }
        if(lCount < n){
            currString += "(";
            backtrack(answer, currString, lCount + 1, rCount, n); 
            currString.pop_back();
        }
        if(lCount > rCount){
            currString += ")";
            backtrack(answer,currString, lCount, rCount + 1, n);
            currString.pop_back(); 
        }
    }
};
```
