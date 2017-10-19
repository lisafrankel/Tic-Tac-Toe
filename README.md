#Tic Tac Toe

Play tic tac toe!  Built using alpha beta search AI algoirthm.

Getting started

Command line
To run my code using the command line interface, enter:
python3 <yourfilepath>/ttt.py
To play, the user tells the program if he/she would like to go first, and what difficulty the
user would like. When the program prints ‘move:’, the user inputs ‘x,y’ integer
coordinates of where they’d like to place an O.

0,0 0,1 0,2 0,3
1,0 1,1 1,2 1,3
2,0 2,1 2,2 2,3
3,0 3,1 3,2 3,3

If the user tries to place an O in a space that is not empty, the program will ask them to
try again.

GUI
To my code using the GUI interface, follow the comment guidelines within the code. I
have written what lines to uncomment out, and which lines to comment out, to change
it from command line to GUI.
When using the GUI , in order for my program to take the input after a user has clicked
on the area they want to place an O, and then must go back to the command line and
press enter.
Program Design

Imports
Deepcopy is used to make deep copies of states in my successor function. In order to
create my GUI I imported tkinter.
Global variables

Several global variables are used, seen at the top of the code:
* _X, _O, _E, and _SIZE are used for readability.
* _DEPTHLIMIT is used so that my alpha beta search can reference it, and is
changed when the user selects different levels of difficulty.
* _WINNER is used only in the play function, to see who the winner is.
_NODES_GENERATED is used to track how many nodes are generated
throughout the game.
* _TOP, _BOARD, _USER_X, and _USER_Y are all used in various ways to
implement the GUI.
* Grid is initialized as an empty 4x4 2d array, where ‘E’ represents an empty space
* Cache is where all my generated states are held, to stop from evaluating
repeated states

Functions
* successors(state, player) is a function that generates list of all possible actions
for player from a given state. It checks every space that either an X or O could be
placed, and returns a list of these 2d arrays.
* isTerminal(state) is function to determine if node is terminal node. It checks if
there has been a win either X’s or O’s, or if the grid is full.
* evalTerminal(state, player) is a function that assigns utility value to terminal
states
* evaluation(state) is a function that returns the value for the evaluation function
provided in the assignment. It first sums up all of the needed variables (i.e. how
many horizontal 3 X’s in a row are there without an O, how many vertical 2 O’s in
a column are there without ant X’s, etc). It then plugs these variables into the
formula provided in the assignment sheet and returns that value.
* alphabetasearch(state), maxValue(state, alpha, beta, depth), and
minValue(state, alpha, beta, depth) are implemented similarly to the provided
pseudo code. maxValue, and minValue take depth as an additional input, to
track if they’ve reached the MAX-DEPTH and need to use cutoff and refer to the
evaluation function instead. A cache is used to store all the generated states.
* level() takes the user’s input to pick a difficulty level. The levels of difficulty are
based on different the depth limits. The max depth limit this program uses is 16,
in which case it is impossible to beat the program. The other two levels are
possible to win, with the easiest having only a depth of 1, and the intermediate
level having a depth of 7.
* niceprint(state) prints a given state in the command line in a readable format
* displayBoard(state) draws the board, and also draws the Xs and Os onto the
board when needed.
* find_mouse_xy(event) gets coordinates of the mouse when the user clicks on
the game board and translate into integer input of x, y indices for the user's
move on the grid
* makeClickButton() is a function that binds the mouse click
* play(state) is the main function that when run starts the game. The user is first
asked if they would like to go first, and then asked what difficulty they would
like. This function uses the alpha beta search to generate the programs/max
players moves, and calls isTerminal(state) on every new state to see if they game
has been one, and if so who the winner is.
