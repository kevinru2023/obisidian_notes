#Code 
#### Arrays 📋
- A variable that represents a list of other variables 
- Everything in array must be of same type 
	- Ex: `std::string Arr[2] = {std::string "Hello", std::string "Meow"};` <--  ✅ 
	- Ex: `std::string Arr[2] = {std::string "Hello", int 10}` <-- ❌

#### Statically Allocated Arrays ⚡️
- In Engr103 this is the main array type we work with, these arrays have limitations ❌
	1. Size must be specified at declaration 
	2. Size must be compile-time constant *(or a hard coded value)*  
	3. Size can't change post-declaration 

#### Example of array program: 
``` c++
#include <iostream>
using namespace std;
int main(){
	int my_array[10];

	//adding 1-10 to array and prints it 
	for(int i = 0; i < 10; i++){
		cout << "Enter int: ";
		cin >> my_array[i];
	}

	//prints the number reversed
	for(int i=9; i >=0; i--){
		cout << my_array[i] << endl;
	}
}
```


#### A little bit about addresses and arrays ☕️
- Whats an address? A number that represents the location of a variable. 📍
- Arrays are contiguous, meaning everything in array is next to its neighbors 👯‍♂️
- When trying to print out an array `cout << an_array << endl;` <-- this will print out an address
- Arrays access elements by actually doing **pointer arithmetic** 
	- for example `my_array[1]`, actually goes to the memory address of my_array adds the offset of the bytes of the type of the array (such as int, bool , etc..) and add that to it to get the element 

