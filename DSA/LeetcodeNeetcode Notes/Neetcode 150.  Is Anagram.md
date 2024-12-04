#algorithms #neetcode 

---
# Thoughts: 

So I may or may not have attempted this problem while fucked up, but heres my general thoughts. Overall I think I could have understood this problem better if I knew about classes having comparison operators, but because I didn't have that prerequisite knowledge i was stuck going on in a loop not knowing how to do this problem in O($n$) instead of O($n^2$) but after looking at the work-through I realized I could. In general I feel like I just learned more about the way C++ maps operate, I think I need to give more credit to C++ objects and look more into depth into them. They operate more like python than I realized and I think thats where i'm stuck right now, where i'm assuming I have to do everything from scratch. 

---
# Reflection:

Kind of disappointed that I needed as much help to solve this one out but I know I could have probably brute forced a really inefficient solution, but I need to stop doing that. I need to sit down and think about the problem, while also realizing what tools I have to solve them. 

---
# Solution: 
```cpp
class Solution {

public:
	bool isAnagram(string s, string t) {
	
		if(s.length() != t.length()){
			return false; 
		}
	
		unordered_map<char, int> smap;
		unordered_map<char, int> tmap;
	
		for(int i = 0; i < s.length(); i++){
			smap[s[i]]++;
			tmap[t[i]]++;
		}
	
		return smap == tmap;
	}

};
```

--- 
# Tricks learned: 
- Maps have an equality operator which is super sick 
- If you don't care about validating the map syntax `map[key]++` is a super quick way to count occurrences