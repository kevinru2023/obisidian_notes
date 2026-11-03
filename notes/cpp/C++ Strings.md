#Code 
#### Char: Primitive type that stands for character 
- Holds just one character 
- Example:
	```c++ 
	char my_fav_num = "A"; 
	```
- Intergral type: A type of data that can be converted to and from whole numbers, without **loss of information**
- Means you can convert char --> int 
	- Example: `static_cast<int>(my_fav_num)` <-- valid code! (because of ascii table)

#### String:  A data type that can be included by using `include <string>`
- To use type, use `std::string` before initializing something with string data type 
	- Ex: 
	```c++ 
	std::string word = "Hello world!"; 
	std::cout << word << std:endl; //prints Hello world! 
	```
- Can compare strings using `a == b` where a and b are ***strings***
- Can also check if string is empty in three ways: 
	1. `if(word == "")`
	2. `if(word.empty())` <-- because strings are classes in c++!!! 
	3. `if(word.size() == 0)` 
- Can escape characters using backslashes 
	- Example: `cout << " \"Hello world\" " << endl` <-- backslashes escape the `" "` 
- When using `cin >> sentence;`, the `>>` ignores the white spaces then starts consuming the characters until it encounters another whitespace. So basically it **only gets one word** 
	- Can counter this by using `std::getline();` <-- function from `stdlib` that allows getting data from the terminal 
		- `std::getline();` has two parameters (stream to read from, variable to store) ex: `std:getline(std::cin, sentence)` <-- assuming sentence is a string var 
		- The `>>` and `std::getline()` don't work very well together you have to do weird work arounds such as `std::cin.ignore(num)` 
	- **Parameters are copies of their arguments** <-- memorize this for 162 and onward this is why we use pass by reference 😃 