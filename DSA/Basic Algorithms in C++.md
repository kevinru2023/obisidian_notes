#algorithms #cs261 #self-study 
### Linear search 
```c++ 
#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int value); // Function declaration

int main() {
    int arr[5] = {1, 3, 5, 7, 9};

    int index = linearSearch(arr, 5, 7); // Pass the size of the array
    cout << index << endl;

    return 0;
}

int linearSearch(int arr[], int size, int value) { // Corrected function signature
    for(int i = 0; i < size; i++) {
        if(arr[i] == value) {
            return i;
        }
    }
    return -1;
}
```

### Binary Search: 
```c++ 
#include <iostream> 
using namespace std; 

int binarySearch(int arr[], int size, int target); 

int main(){
	int arr[100000]; 
	int target = 777777; 
	
	for(int i = 0; i < 100000; i++){ //just for populating purposes 
		arr[i] = i; 
	}
	
	int index = binarySearch(arr, 100000, target); 

	if(index == -1){
		cout << "target not found" << endl; 
	}else{
		cout << "element found at: " << index << endl;  
	}
	return 0; 
}

int binarySearch(int arr[], int size, int target){
	int low = 0; 
	int high = size - 1;
	
	while(low <= high){
		int middle = low + (high - low) / 2; 
		int val = arr[middle]; 

		if(val < target){
			low = middle + 1;
		}
		else if(val > target){
			high = middle - 1;
		}else{
			return middle; //target is found 
		}
	}
	return -1; //if the target is not found 
}
```

### Interpolation search
```c++ 
#include <iostream>
using namespace std;

int interpolationSearch(int arr[],int size, int target);

int main(){
	int arr[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
	int size = sizeof(arr) / sizeof(int);
	int index = interpolationSearch(arr, size, 256);

	if(index != -1){
		cout << "element found at: " << index << endl;
	}else{
		cout << "element not found" << endl;
	}

	return 0;
}

int interpolationSearch(int arr[], int size, int target){
	int high = size - 1;
	int low = 0;

	while(target >= arr[low] && target <= arr[high] && low <= high){
		int probe = low +(high - low) * (target - arr[low]) /
					(arr[high] - arr[low]);

		cout << "probe: " << arr[probe] << endl;
		if(arr[probe] == target){
			return probe;
		}
		else if(arr[probe] < target){
			low = probe + 1;
		}else{
			high = probe + 1;
		}
	}
	return -1; //target not found
}
```
