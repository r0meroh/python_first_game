# python_first_game
My first attempt at a game in python to practice bringing ideas and concepts to actual code.  open README file to see descriptions of auxilary files.

This program incorporates wav sound files to actions that take place in the game.
The sounds are royalty free wav files downloaded online.
Several libraries are imported into the program that remained unused.  These libraries are left there for educational purposes.
The libraries show which frameworks are mistakenly used or "called" when trying to acheive certain function calls from python2
inside python3.

The program has a foundation of a python game tutotial "SPACE Invaders" for python2, but not only is the program written onto
python3, it also required debugging and additonal code to compensate for library functions that are unaccessible outside of python2.  The tutorial also implemented the program under a Mac osx environment, this program was rewritten and changes were made
to be able to adapt to the Linux/Ubuntu environment.  

The program includes the following added features/functionality:
Player can move all around the screen with functioning missile release from any point the player is located on screen.
Custom drawn (.gif) files that are incorporated into the program.
mulitple sounds triggered under certain events which may also be layered.

Notes:
The game has to be manually terminated by the user in one of two ways:
Closing the graphics window.
Pressing the ENTER key inside the console.

The cat objects do not reiterate if they travel outside the scope of the window, therefore those enemies do not respawn.[FIXED]

Due to limitations, the bone object is still tracted after a collision and although hidden, it may collide with additional enemies.

Game doesn't end when player is hit, not does the player respawn.
