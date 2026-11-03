#algorithms #neetcode 

---
# Thoughts: 

I hate life, I hate DSA, and I suck at programming and should quit. 

---
# Reflection: 

the problem goes as this, if the stack is not empty and the current element at the current index is greater than the element at the top lets execute some code. The code that executes changes the index of the answer array of the top stack index to be the difference between the current index - the top of the stack index. It then pops that value. Afterwards lets push the current index to track it now. Overall I hated this problem and I hate how simple the solution is because it makes me feel fucking braindead. I suck at algorithms so fucking much. 

---
# Solution: 
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> ms;
        vector<int> answer(temperatures.size(), 0); // apparently vectors need to be sized here

        for(int i = 0; i < temperatures.size(); i++){
                while(!ms.empty() && temperatures[i] > temperatures[ms.top()]){
                    answer[ms.top()] = i - ms.top(); 
                    ms.pop();
                }
                ms.push(i); 
        }
        
        return answer;
    }
};

```
