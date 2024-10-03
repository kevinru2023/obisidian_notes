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

 
The problem is asking me to implement this real life basketball game, which has certain rules, I won't reiterate the exact rules as they are above, however I will go over the technical aspects over the problem. The first thing is I am going to have to get user(s) input on which position they want to put the money ball rack on, this would be an `int` between $[1,5]$ and store it in a var,  I would have to include error handling on this as the user is allowed to not put in an number in that range. Afterwards I will have to prompt the user to put in their "shooting capability" which is an `int` between $[1,99]$, again including error handling. Afterwards I am going to to have to implement the shooting for each rack  
