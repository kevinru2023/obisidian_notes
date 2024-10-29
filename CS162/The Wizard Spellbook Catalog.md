#cs162 #design 

#### Kevin Rubio | CS162 | 10-21-24
---
## Problem Statement: 
	The great wizard school of Pogwarts has been adding a lot of new spellbooks to their library lately. As a result of all the new literature, some mischeivous students have been learnign spells that are dangerous. In addition, it has become increasingly difficult for the staff to find specific spells they. want to teach in class 

	In order to alleviate these issues, the school administration has hired you to create a spellbook catalog program that will allow for access restrictin and make searching for spellbooks easier. 

	To simplify your task, the school has provided you with their spellbook and wizard profile information. These come in the form of two text files: a wizzards text file, and a spellbooks text file.
	
	The spellbooks text file contains a list of Pogwarts's spellbooks and their included spells. This file will give you the spellbook and spell information that your program will organize and display. 

	The wizards text file contains a listing of all wizards associated with Pogwarts. This file will give your program the information needed to control what spellbooks users can access. 

	The formats of these files will be discussed later. The starter code includes examples of these text files that you may use for testing your program: wizards.txt and spellbooks.txt 

--- 
## Understanding the problem: 

The problem is asking for me to write a program that when ran takes in two command line arguments. The first being the name of a file containing information wizards which itself contains the following format:
```
<number of wizards in file>

<wizard name> <wizard ID#> <wizard password> <wizard position title> <wizard beard length>

<wizard name> <wizard ID#> <wizard password> <wizard position title> <wizard beard length>

<wizard name> <wizard ID#> <wizard password> <wizard position title> <wizard beard length>
```
The second argument will be the name of a file containing information about the spellbooks and included spells. The file itself will contain the following format: 
```
<total number of spellbooks in the file> 

<title of first spellbook> <author> <number of pages> <edition> <number of spells in book>

<title of spell> <success rate> <effect>
<title of spell> <success rate> <effect>
<title of spell> <success rate> <effect>
...
<title of spell> <success rate> <effect>
<title of spell> <success rate> <effect>
<title of spell> <success rate> <effect>
```

I will have to make it so my program reads all the data from the two files and store it in memory. This will require me to use various structs and dynamic arrays to store the information as it will be changing. The implementation is also required to use a one of each : header file, makefile, driver file and implementation file.

The program will also have to prompt the user for login credentials to ensure the right access to the right users. This will be done by prompting the user for an ID and password (Both have certain formats as well). If the inputted credentials are not found in the `wizards.txt` file then the user will be prompted to re-enter them, after three attempts the program will print out an error message and terminate. 

If the user is found the program will display various information including the name, ID, school position, and beard length of the wizard corresponding to the inputted ID. 

Afterwards the program will list various different ways to search and display spellbook and spell information until they choose to quit. Listed as such: 

1. Display All: Prints all spellbooks and spells information that the user has access to
2. Search spellbook by name: Will prompt user for a spellbook name. if it's not in the db given then it will print out an error otherwise it will do the following: 
	1. print information to the terminal, this will print out all information of the spellbook 
	2. write information to an output file, will prompt user for name of output file, then will open the file in append mode and write all information of the spellbook to the output file. 
	3. (only if 1 or 2 isn't chosen) reprompts for options 1 & 2
3. Search spells by effect: There are 5 spell effects, the user will get prompted for a valid spell effect. This will also make sure the user has the right access rights before prompting for the following: 
	1. Print information to the terminal, meaning all informaiton of all the spells with the chosen effect will be printed to the terminal 
	2. will be similar to 2.2 but instead will write all information of the spells with the chosen file. 
4. Quit, this will terminate the program. 

Along with the given requirements the program has various required structs and functions that I will not go over here. There are however required files which are: 
1. catalog.hpp: This header file contains all struct declarations and function prototypes
2. catalog.cpp: This implementation file contains all function definitions, except for main()
3. run_wizard.cpp: This driver file contains the main function
4. Makefile

Along with these requirements I also plan on doing both the extra credit which includes: 
1. Adding an additional searching/printing option which sorts spellbooks by average success rate of spells. This option will also have the similar printing and writing to an output file options. 
2. Include error handling for every invalid user input including different types and invalid values of the correct type. 

--- 
## Pseudocode (EXTRA CREDIT INCLUDED): 
``` 
set up functionality for dynamic arrays and structs here 

prompt user for wizard info file name (handle errors)  
prompt user for spellbook info file name (handle errors)  

prompt user for id (handle errors)  
prompt user for password (handle errors)  

print out user info if correct and found  

loop until user chooses to quit:  
    print options:  
    1. Display all spellbooks and spells  
    2. Search spellbook by name  
    3. Search spells by effect  
    4. Sort spellbooks by average success rate (extra credit)  
    5. Quit  

    prompt user for option (1-5)  

    if option == 1:  
        check what spells user has access to and print 

    if option == 2:  
        prompt user for spellbook name (handle errors)
        if no errors prompt user for method:
		    1. Print to terminal 
		    2. Write to output file 
            

    if option == 3:  
        prompt user for spell effect and check for permissions
        if no errors prompt user for method:
		    1. Print to terminal 
		    2. Write to output file 

    if option == 4: // Extra credit  
        sort spellbooks by average success rate in descending order  
        if no errors prompt user for method:
		    1. Print to terminal 
		    2. Write to output file

    if option == 5:  
       quit program 
```
--- 
## Test Cases: 

| Value                                                 | Expected                                                                                                                   | Actually met expectation |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Wizard/Spellbook info filename = meow.ts              | "error please input valid file type"                                                                                       | yes                      |
| Wizard/Spellbook info filename= meow.txt              | prompts user for login creds                                                                                               | yes                      |
| login id = non valid login  (1st time)                | "login not found please try again"                                                                                         | yes                      |
| login id = non valid login  (2rd time)                | "login not found please try again"                                                                                         | yes                      |
| login id = non valid login  (3rd time)                | "Invalid login", program terminates                                                                                        | yes                      |
| program option 1:                                     | prompts user for printing to screen or output to file                                                                      | yes                      |
| program opt 2 = invalid spellbook name                | "please enter a valid spellbook name" reprompt user for spellbook name                                                     | yes                      |
| program opt 2 = valid spellbook name                  | prompts user for printing to screen or  output to file                                                                     | yes                      |
| program opt 3 = invalid spell effect                  | "invalid spell effect" reprompt user for spell effect                                                                      | yes                      |
| program opt 3 = valid spell effect                    | prompt user for printing to screen or output to file                                                                       | yes                      |
| program opt 4                                         | will sort spellbooks by average success rate in descending order and then prompt user to print to screen or output to file | yes                      |
| Opts 1-4  sub opts not printing or outputting to file | reprompt user to either print to screen or output to file                                                                  | yes                      |
| program opt 5                                         | terminate program                                                                                                          | yes                      |
| any opt not 1-5                                       | prompt user for valid option                                                                                               | yes                      |
