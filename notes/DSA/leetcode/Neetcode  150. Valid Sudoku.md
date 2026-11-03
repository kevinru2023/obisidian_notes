#algorithms #neetcode 

---
# Thoughts: 
To be honest I had no clue how to tackle this problem, I had a vague idea based off the hints but I'm really bad when it comes to really annoying problems like this that require multiple check on columns and rows. I tried but got stuck on this problem and decided to look at the solution cause fuck Neetcode and fuck Leetcode. 


---
# Reflection: 

I don't even know bro, these problems are just annoying asf to me currently, I am in no mood to solve any, but heres the reflection. Of course it's hash maps, why is it always hash maps and sets. Why is every problem solvable by hash maps why is it always hash maps. OF COURSE THE SOLUTION IS $O(n^2)$ too smh. In all seriousness I have really good notes on this problem on my Ipad because this is def more a visual problem. 

---
# Solution: 
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows, cols;
        map<pair<int, int>, unordered_set<char>> squares;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;
                
                pair<int, int> squareKey = {r / 3, c / 3};

                if (rows[r].count(board[r][c]) || cols[c].count(board[r][c]) || squares[squareKey].count(board[r][c])) {
                    return false;
                }

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};
```
