#cs162 #design

#### Kevin Rubio | CS162 | 10-2-24
---
## Problem statement: 
	You are tasked with implementing a C++ program that simulates a basketball shooting game, the game supports 2 players which each player attempts to score as many points as possible by making shots from five fixed shooting positions. The game has a couple rules: 
	
	- Each shooting position has a rack of five basketball, the first 4 are regualr balls worth 1pt, the last is a "money ball" worth 2pts, which can only be shot after the first 4 are shot
	  
	- Of the 5 positions the player can choose a position to have a rack that is all "money balls", called the "money rack"
	  
	- Two balls pedestals are positioned between racks 2 & 3 and 3 & 4, these pedestals contain a "Starry" ball worth 3pts
	  
	- After the game is done, players have the option to play again or quit, the program should restart from the beginning until the players decide to quit
	  
	- (EXTRA CREDIT) Allow the game to have up to N players
---
## Understanding the problem: 

 
The problem is asking me to implement this real life basketball game, which has certain rules, I won't reiterate the exact rules as they are above, however I will go over the technical aspects over the problem. 

The first thing is I am going to have to get user(s) input on which position they want to put the money ball rack on, this would be an `int` between $[1,5]$ and store it in a var,  I would have to include error handling on this as the user is allowed to not put in an number in that range. Afterwards I will have to prompt the user to put in their "shooting capability" which is an `int` between $[1,99]$, again including error handling. 

Next, I am going to to have to implement the shooting for each rack where each rack has five shots, the way to determine if a shot is going to be made is to generate a random `int` that is between the range $[1,100]$ and compare this number with the users inputted shooting capability and if the random number is smaller or equal to the shooting capability, then the shot will be marked as made; otherwise it is marked as missed. I will most likely store the shots in an arr as well as an int to keep the total amount of points, so that after all five shots have been shot, I can output the "score" for the rack. I plan to encapsulate this process into a function so I can repeat this for each rack, and keep track of what iteration I am on so I can implement the "Starry Range" shots which is in between racks 2 & 3 and racks 3 & 4. 

After all the racks have been cleared I will output the total amount of points made for that player, this entire process for shooting the racks and keeping store of the points will all be in a separate function so I can repeat for however many players will be playing the game. I plan to keep the total amount of points in an arr as well, I will then use a custom function I will create to get the max value from the array, and if there is a tie it will simply announce tie.  

Finally after the game is concluded I will re-prompt the users to see if they want to play again, if so the game starts from the beginning, this means I will have to encapsulate all previous logic into one big loop. 

--- 
## Pseudocode (EXTRA CREDIT INCLUDED): 
```c++
//main game logic that will return an int that represents the //total score the user got 
int play_game(shooting_capability,pos){
	declare array for racks score 
	
	loop 5 times: 
		if the loop is at 3 or 4 then shoot starry ball 
		
		//shoot_rack will always take the shooting_capability, 
		//i am not going to define it here but it will handle 
		//the random number logic and decide whether a user made 
		//a shot or not  
		
		if the current rack is the same as pos:
			shoot_rack() but with points being more
		else:  
			shoot_rack() with normal points 
		
	int total_score = 0;
	for each score in rack:
		total_score += score 
		
	return total_score	
}

main{
ask user for amount of players 
read n amount of players //used to create dynamic arr,also  
handle_error 

//for the reader, this process of error handling i am going to //call handle_error so I don't have to type it out, but this //should not be confused with a function I am going to reuse 

while n is not int:   
	print error       
	ask for new input 
	read n players 


do: 
	bool play_again
	
	create dynamic arr for n players //this will store each 
									 //players total score  
		
	ask user for money-ball rack pos
	read money-ball rack pos 
	handle_error 
	
	ask user for shooting capability
	read shoot capability 
	handle_error 
	
	for each player: 
		dynamic arr add	play_game(shooting_cability,pos); 
							
	check_winner(); //this will basically be a max function
					//that gets the max number from the arr
					//and print it out the index of the 
					//max number (so the player) 

	ask users if they want to play again 
	read users choice into play_again var 
while(play_again is true)
}
```

--- 
## Test cases

|           Value            |       Expected        | Actual meet expectation |
| :------------------------: | :-------------------: | :---------------------: |
|         users = 5          |       continue        |           yes           |
|          users=.5          | printed error message |           yes           |
|  money-ball rack pos = 3   |       continue        |           yes           |
|  money-ball rack pos =2.5  |     printed error     |           yes           |
|  shooting capability = 60  |       continue        |           yes           |
| shooting capability = 200  |     printed error     |           yes           |
| shooting capability = 60.5 |     printed error     |           yes           |
|     play_again = true      |   game starts over    |           yes           |
|     play_again = false     |     program ends      |          yes            |



