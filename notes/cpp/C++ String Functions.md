#Code  
#### Classes 📚
- Variables whose type is a class are considered **objects** 
- Has behaviors and data *(functions and data types such as int)*
- Just basic class stuff like any other language 😱

#### String class functions 🧵
- `my_string.empty();` <-- checks if string is empty 
- `my_string.size();` <-- grabs len of string and returns it 
- `my_string.at(index);` <-- gets value at certain index *(indexed at zero)* and returns it 
- `my_string.find('word', index[optional parameter]);` <-- 
	- finds **if word is in string** and returns index of first letter of word of the first occurrence  of word 
	- **if word not** in string returns **std::string::npos** (a very big number)
	- if word has multiple occurrences you can find them by using loops 
	- Example: 
	```c++ 
	  int count = 0; 
	  do {
		  position = sentence.find("hello"); 
		  if (position != std::string::npos){
			  setence.erase(position, 5); //5 because hello is 5 chars
		  }
		  count++;
	  } while(position != std::string::npos); 
	``` 
- `my_string.substr(int i, int j);` <-- can grab substring starting from index **i** to index **j** and returns it 
	- In c++ the second parameter is a length so it is not similar to python slicing (well mostly)
	- `my_string.substr(int i);` <-- extracts all characters starting from index **i** and returns it
- `my_string.erase();` <-- *in place function* which means it modifies the strings that you use it on, other string functions don't 
	- so `my_string.erase(i,j);` <-- starts erases j characters starting from index **i** 
	- `my_string.erase(i);` <-- erases all characters starting from index **i** 