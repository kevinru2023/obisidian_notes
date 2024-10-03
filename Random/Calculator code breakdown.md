#engr103 

Stuff will be separated by spaces so if they aren't spaces not valid expression, I think.  

### PEMDAS: 
- Going to have to find a way to set order of importance in code
	- Order goes as ["(", "^", "*", "/", "+, "-"]  
- string.find() will be a quick to way to see if parentheses close and open i.e. track how many "(" and ")" there are if they aren't equal then it isn't a valid expression 
	- This lowkey sounds like recursion if the stuff inside parentheses also contains other parentheses so maybe recursively call functions?!  
- Parentheses cannot be empty if the stuff in between is empty then it isn't valid meaning if both "(" and ")" are one index away from each each other i.e. expression[n] and expression[n+1] = "(" and ")" then return false 
- I think the best approach would be using find in order by importance so like if substring.find( "(" ) returns something then start going for that yk? 
- also if no operations in parentheses and just a single num just return num 

### Calculating values: 
- Can lowkey just pass them into functions such as add(num1, num2) which converts num1 and num2 into doubles (assuming num1 and num2 are substrings) and does the operation 
- I think working with substrings will make this much easier 