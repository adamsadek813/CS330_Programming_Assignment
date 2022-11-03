# CS330_Programming_Assignment

This is Adam Sadek's programming assignment for CS330-01. There are two python files within this git repository. The python file titled Sadek_Adam_CS330_Programming_Assignment.py has a lock and an unlock pass code. The user may type anything into the input when prompted to by the "Input: " display. Characters that are not digits between 0-9 are disregarded. 

If the 'unlock' code is found within the input, the status of the lock will be "Unlocked.". If the 'lock' code is found within the input, the status of the lock will be "Locked.". Whichever code is found last will result in the state of the lock changing.

After typing an input string, the user will be told whether the lock is now locked or unlocked. They may then input another string to attempt to lock or unlock the lock. If the input does not include the lock or unlock codes, the status of the lock will remain the same.

The Sadek_Adam_CS330_Programming_Assignment.py file is ran through the terminal by typing 'python' then the name of the file 'Sadek_Adam_CS330_Programming_Assignment.py' then hitting enter. The input should look as follows:
python Sadek_Adam_CS330_Programming_Assignment.py 
(Make sure that the terminal is in the same directory that the python file is in when executing the above code)

The Sadek_Adam_CS330_Programming_Assignment.py file can be exited at any time by pressing ctrl-c. 

The other python file is titled Sadek_Adam_CS330_Programming_Assignment_Pt2.py. This file is for part 2 of the assignment. In it, a random number generator appends a number to a list of numbers until the lock is unlocked (i.e. the access code is found in the randomly generated string of numbers). The file runs 20 trials of this, times each trial, and counts how many numbers are needed for each trial before the access code is found. 

The average time, max time, and min time (in seconds) for the 20 trials is found. The average number of symbols, max number of symbols, and min number of symbols needed for the 20 trials is also found. This data is outputted to the screen. 

The Sadek_Adam_CS330_Programming_Assignment_Pt2.py file is ran through the terminal by typing 'python' then the name of the file 'Sadek_Adam_CS330_Programming_Assignment_Pt2.py' then hitting enter. The input should look as follows:
python Sadek_Adam_CS330_Programming_Assignment_Pt2.py 
(Make sure that the terminal is in the same directory that the python file is in when executing the above code)

The Sadek_Adam_CS330_Programming_Assignment_Pt2.py file can be exited at any time by pressing ctrl-c.

Unit test coverage for Sadek_Adam_CS330_Programming_Assignment.py can be generated by:
1) Installing covereage (can be installed through terminal by entering: pip install coverage) 
2) Run following code: coverage run -m Sadek_Adam_CS330_Programming_Assignment
3) Enter inputs to test the program
      Note: To fully test the program, enter at least 1 input that is: shorter than 6 digits, includes the unlock key, includes the lock key, includes non-digit characters, does not include the lock or unlock key.
4) Exit the program by pressing ctrl-c
5) Run following code to generate unit test coverage report: coverage report

Unit test coveraege can also be generated in the same exact way for Sadek_Adam_CS330_Programming_Assignment_Pt2., except no input is required by the user.

Note: in order to run the test coveraeges, you must be in the same directory as the python files.

There is also a memo included in this repo that includes my part 2 intruder time estimation where the intruder must wait 1 second to see if the lock has unlocked or not. The memo also includes more specific details on how the programs work, my findings, information on the language I chose (python3), as well as a state transition diagram for the Finite Automata.

All testing and programming has been done through Visual Studio Code using Python3.

The author of this github repo and all its contents is Adam Sadek.
