#algorithms #neetcode 

---
# Thoughts: 

So for this problem I actually had a solution in mind and instead of worrying about the time complexity right away decided to implement it because I didn't want to procrastinate this problem like I have been with others. Overall this problem honestly didn't seem to hard to grasp but my implementation was lacking. 

---
# Reflection: 

So for this problem I decided to use a map to associate numbers with frequency and used a cpp function to grab the max elements and then delete said element from map so I can grab the max frequencies. I know this approach had $O(n^2)$ solution but I could not think of another way to implement this. After I submitted and got a solution I decided to look into what the other solutions approaches were . I also did not realize Neetcode gave hints so defiantly using those next time because one of them flat out gave which sorting algorithm to use (bucket sort). I am not surprised I didn't get this then because I didn't even know a sorting algorithm like that, and to be honest I am kind of surprised that some sorting algorithms are better than others. I have to look into which sorting and searching algorithms might apply during some problems in order to understand which tools to use when approaching a problem, glad I tackled this problem. 

---
# Solution: 
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> output; 
        map<int, int> frequencyCount; 

        // used for detecting type automatically , for better clarity later
        using pair_type = decltype(frequencyCount)::value_type; 
        
        for(int c: nums){
            frequencyCount[c]++; // adding to hash map here 
        }

        for(int i = 0; i < k; i++){
            auto pr = max_element( // neat element 
                frequencyCount.begin(), frequencyCount.end(),
                [] (const pair_type & p1, const pair_type & p2) { 
                    return p1.second < p2.second;
                }
            );
            output.push_back(pr->first); 
            frequencyCount.erase(pr); 
        }
        return output; 
    }
};
```

---
# Optimal Solution + Video Explanation: 

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        
		//Each index i in freq will store a vector of 
		//numbers that appear exactly i times in nums.
		//this can be thought of the process of creating buckets! 
        vector<vector<int>> freq(nums.size() + 1); 
        
        for (int n : nums) {
            count[n]++;
        }
	        //This iterates over the count map and places each 
	        //number (entry.first) into the freq vector at 
	        //the index corresponding to its frequency (entry.second).
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

		//collecting the most frequent elements. 
        vector<int> res;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
```

![](https://youtu.be/YPTqKIgVk-k?t=271)


--- 
# Tricks learned: 
- Not really relevant to optimal solution but this is where I picked up on templates 
- Initializing vectors to empty vectors don't actually produce garbage values apparently it just initializes them to empty vectors!. 