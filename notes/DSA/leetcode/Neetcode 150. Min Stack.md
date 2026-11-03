#algorithms #neetcode 

---
# Thoughts: 
So initially when approaching this problem I was thinking I had to implement my own stack data structure and also keep a track of a minimum element using another variable to keep track of the minimum. However I quickly realized that:  
1. This approach would not work since after popping an element the min could change 
2. Implementing a stack from scratch seemed to be the wrong path. 

So I decided to look at the hints on Neetcode and saw that we were allowed to use the stack data structure (who knew you could use stack on a stack problem that implements a stack?) and then quickly wrote up my own solution. 


---
# Reflection: 

One thing I learned doing this problem is that I have to pay more attention to the constraints and understand the problem fully, I spent a bit too much time doing some error handling. If I had just looked at the requirements and read them over and took my time, I would have saved myself 5 minutes of programming. I have to make a good habit of **reading the damn problem fully**.

---
# Solution: 
```cpp
class MinStack {
private:
    stack<int> s, m;  

public:
    MinStack() {
    }
    
    void push(int val) {
        s.push(val); 
        if(m.empty() || val <= m.top()){
            m.push(val); 
        }
    }
    
    void pop() {
        if(s.top() == m.top()){
            m.pop(); 
        }
        s.pop();
    }
    
    int top() {
        return s.top(); 
    }
    
    int getMin() {
        return m.top();
    }
};
```
