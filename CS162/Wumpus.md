#cs162 #design 
#### Kevin Rubio | CS162 | 10-2-24
---
## Problem statement: 

	The task for this assignment is to recreate a game called Wumpus the objective is to  to start working with polymorphism and C++ class templates from the STL. The game will require many different required classes along with some error handling. 

---
## Understanding the problem: 

This is a very large assignment compared to many others in this course, the main problem will be to make sure my room and event classes are properly implemented. I am thinking of going the way of implementing my event class to have some virtual functions to enable my classes to be able to override said functions. The game itself is going to contain a 2D vector of room objects where each room in itself has an event pointer which can either point to one event or be a nullptr ( indicating that an event is not in the current room ). The events themselves are going to be classes derived from an event class with each class having it's own special functionality like the bat swam which will make the player walk in a random direction. Some events are going to a have a percept which will display text anytime a player is near a room that contains said event, which will require me to implement a way to detect if a player is near a room with an event that has a percept along with it. The player will move using AWSD movement and will also be able to fire an arrow if the player has picked up an arrow before. The said arrow will have the functionality to be able to kill the Wumpus. The arrow will have it's own specific movement, in which it will have to travel through each room if it still hasn't the Wumpus, and will stop once it hits the edge of the map. 

---
## Pseudocode: 

![[Wumpus Design.png]]

---
## Test Cases: 

| Value                                                 | Expected                                                                            | Actually met expectation |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------ |
| Player movement at map edge                           | Prompt player for a different direction                                             | yes                      |
| Player movement within the map                        | Player proceeds to the selected room                                                | yes                      |
| Percepts triggered by event proximity                 | Prints the associated percept                                                       | yes                      |
| No percept-triggering events nearby                   | No percept is printed                                                               | yes                      |
| Player fires arrow with available arrows              | Arrow is fired, and it checks whether it hits the Wumpus or travels for three rooms | yes                      |
| Player fires arrow with no available arrows           | Error message is printed                                                            | yes                      |
| Arrow hits the Wumpus                                 | Ends the game                                                                       | yes                      |
| Arrow hits the edge of the map (doesn't reach Wumpus) | Arrow travels for three rooms or stops when it hits the map edge                    | yes                      |
| Player enters key that isn't AWSD or F                | Print error message asking for valid key                                            | yes                      |

