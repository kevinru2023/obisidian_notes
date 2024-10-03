#code 

#### Arrays 📚
- `double arr[3] {1, 2 ,3};` <-- valid syntax to initialize array 
- Segmentation fault <-- caused by trying to access out of bounds memory 

#### Memory 🧠
- Valgrind <-- tool for debugging, useful for memory debugging 

#### References 👉 
```c++
void change_to_1000(int var){
	var = 1000;
}
int main(){
	int x = 10; 
	cout << x << endl; // prints 10 
	change_to_1000(x); 
	cout << x << endl; //prints 10 
}
```
- ⬆️ this is because variables take make a copy of the parameter passed in, not the actual variable 

- Indirection: 
	1. Pass in the ADDRESS of the variable that you want to change 
	2. Go to location in memory stored within the parameter and change **that** value to 1000 
- Two ways to do indirection 
	 1. Pointers 
	 2. References 
	Example (Using references): 
	```c++ 
	void change_to_1000(int& var){ //the & means reference, can also do int &var
		var = 1000; 
	}
	int main(){
		int x = 10; 
		cout << x << endl; //prints 10 
		change_to_1000(x); 
		cout << x << endl; //prints 1000 
	}
	```
	
- References don't have to be parameters (most of the time they are though)
	Example: 
	```c++
		double my_double = 3.14; 
		double& r = my_double;
		
		r = 9.81; 
		cout << my_double << endl; //prints 9.81 

		my_double = 100.5; 
		cout << r << endl; //prints 100.5  
	```

- Can't make a reference to a constant 

- Limitations: 
	- Can't change references, it will only change the variable it references (no shit)
	- Must initialize reference as soon as you declare it so `string my_string_reference;` is not valid 
	- Pointers are ways to get around these limitations 
	- Dangly references can lead to buffer overflow issues which is why thing likes RCE and ACE exist :) 

- Can return a reference from a function but it's **problematic** because functions delete variables that are out of scope.