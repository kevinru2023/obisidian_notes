#cs162 #design 
#### Kevin Rubio | CS162 | 10-30-24
---
## Problem Statement: 
	This assignment is asking me to write a program that will impleent a simplified version of a single pokémon battle. It will contain 3 pokémon Charamander, Squirtle, and Bulbasaur. This assignment aims to provide an introduction to oop (object oriented programming) and requires 3 classes: move, pokemon, and battle class. The program is a two-player game that first asks each trainer to choose their pokemon. The trainers cannot choose the same pokemon. Afterwards a turn-based battle will begin. At the start of each trainer's turn information will be printed out regarding whose turn it is and information about the pokemon. Each trainer will be prompted to either use a move or heal. The battle will continue alteranting between trainers turn while the trainer's pokemon have a HP > 0. Once a trainer's pokemon runs out of HP the winner will be declared via terminal.  

---
## Understanding the problem: 

Other than the basic game logic the primary bulk of this program will include implementing the classes correctly. The Pokémon class will have to have a dynamic array of moves, and each of those moves has various information such as the type of attack and the damage it will deal. Then the last required class I have to implement will be the battle class which will contain information about the pokémon and the state of the battle itself. 

In the battle itself there are various factors I will have to consider such as the options the trainer chooses whether it be to use a move, heal, or to swap (extra credit). I will most likely have to encompass this to be information that a class holds whether that be the battle class or another class I make. I will also have to implement the required damage calculation and output it to the terminal as well. This means I will also have to pay attention to the different type of the attacks pokémon and how it will affect their damage they output. In terms of the extra credit function swap, I will have to implement a way for a user to select different pokémon as long as they are above 0 hp. 

In terms of actual implementation a lot of the information will have to encapsualted into classes and I will have to get and edit a lot of that information, for example on the move class I will have to edit the amount of uses a move has depending if the trainer uses the move or not. 

---
## Pseudocode (EXTRA CREDIT INCLUDED): 
```
CREATE MOVE CLASS 
CREATE POKEMON CLASS 
CREATE BATTLE CLASS 

Create instances of the class for each pokémon for each pokémon 
 - Bulbasaur
 - Charamander
 - Squirtle
 - Pidgey (Extra credit) 

let trainer_1 pick pokemon 
let trainer_2 pick pokemon 
let trainer_1 pick pokemon (extra credit) 
let trainer_2 prick pokemon (extra credit) 

run game while pokemon are above 0 hp: 
	prompt trainer_x for option: 
		- swap 
		- move 
		- heal 

	do something based on trainer_x option: 
		- if move do damage calc 
		- if swap see if we can swap pokemon and then do it 
		- heal if we have it 

	after action check if the other trainers pokemon are fainted if not we continue 

print winner 

(note all these options include error handling, but not type error handling)
```
---
## Testcases : 

| value                                  | expected                                                              | actual meet expectation |
| -------------------------------------- | --------------------------------------------------------------------- | ----------------------- |
| trainer 1:  pick pokemon = 12          | "pick valid pokemon plz"                                              | yes                     |
| trainer 1: pick pokemon = 1            | ""                                                                    | yes                     |
| trainer 1: pick pokemon = "charmander" | undefined behavior                                                    | yes                     |
| trainer 1 turn: which option = 4       | Please pick valid option"                                             | yes                     |
| trainer 1 turn : 1 (move)              | "select move: (move options here)"                                    | yes                     |
| trainer 1 turn: 2 (heal)               | if user has heal and pokemon can get healed, then pokemon gets healed | yes                     |
