## What is a sliding window? 

Fixed Size: 
- Imagine a buffer that is continuous and slap a window in a subset of the buffer, if that window contains the value we want and it is the best window we have, we save that window. 

Dynamic Size: 
- We grow and shrink the array up until we reach the end of the array based off some criteria.
 
Abstract Naive Brute Force Approach: 
- Start an index, and enumerate through all possible combinations, involves duplicate work O($n^2$)

## What are the benefits 

- Reduces time complexity 
- Allows for attacking problems for iterable items 
## How to spot the patterns 
- Things we iterate over sequentially 
	- contiguous sequence of elements 
	- strings, arrays, linked list 
- min,max, longest, shortest, contained 
	- maybe we need to calculate something 

## Question variants
- Fixed length 
	- max sum subarray of size k 
- Dynamic variant 
	- smallest sum >= to some value s 
- Dynamic variant w/ Auxiliary Data Structure 
	- longest substring w/ no more than k distinct characters (hash set or hash map)
	- String permutations

## Commonalities between Questions
Want to look for one or two of the criteria: 
- Everything grouped sequentially 
- Longest, smallest, constants, max, min 


## Example problems 

**Static Example:**
```cpp
class Solution{
public: 
	int findMaxSumSubarray(vector<int> &arr,int k){
		int maxVal = INT_MIN; 
		int currentRunningSum = 0; 

		for( int i = 0; i < arr.length(); i++){
			if( i >= k - 1){
				maxVal = max(maxVal, currentRunningSum);
				currentRunningSum -= arr[i - (k - 1)];
			}
		}
		
		return maxVal; 
	}
};
```

> [!NOTE]
> In line 10, this is essentially increasing the window, since we are subtracting the length of k! 

**Dynamic Example:** 
```cpp 
class Solution{
public:
	int smallestSubarray(int targetSum, vector<int> &arr){
		int minWindowSize = INT_MAX; 
		int currentWindowSum = 0;
		int windowStart = 0; 
		for (int windowEnd = 0; windowEnd < arr.length(); windowEnd++){
			currentWindowSum += arr[windowEnd]; 
			while(currentWindowSum >= targetSum){
				minWindowSize = min(minWindowSize, windowEnd - windowStart +1); // delta of window size 
				currentWindowSum -= arr[windowStart]; //shrinking array here 
				windowStart++;
			}
			} 
	}
}
```