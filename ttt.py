from copy import deepcopy
from tkinter import *

# al global variables

_X = 'X'
_O = 'O'
_E = 'E'

_SIZE = 4

_DEPTHLIMIT = 14
_WINNER = None
_NODES_GENERATED = 1

_TOP = Tk()
_BOARD = Canvas(height = 850, width = 800)
_USER_X = 0
_USER_Y = 0

# initiating empty grid
grid = [[_E]*_SIZE for i in range(_SIZE)]

# cache will hold all generated and non-repeated game states
cache = {}

# function that generates list of all possible actions for player from a given state
def successors(state, player):
	global _NODES_GENERATED
	_NODES_GENERATED += 1
	result = []
	for i in range(_SIZE):
		for j in range(_SIZE):
			if state[i][j] == _E:
				newState = deepcopy(state)
				if player == 'max':
					newState[i][j] = _X
				elif player == 'min':
					newState[i][j] = _O
				result.append(newState)
	return result


# function to determine if node is terminal node
def isTerminal(state):
	count = 0

	# checking if board full
	for i in range(_SIZE):
		for j in range(_SIZE):
			if state[i][j] != _E:
				count += 1
	if count == _SIZE ** 2:
		return True, 0

	# check if there is a horizontal x win
	for i in range(_SIZE):
		# print state[i]
		if state[i] == [_X for _ in range(_SIZE)]:
			return True, 'max'

	# check if there is a horizontal o win
	for i in range(_SIZE):
		# print state[i]
		if state[i] == [_O for _ in range(_SIZE)]:
			return True, 'min'

	# check for vertical x win
	for i in range(_SIZE):
		vertXList = []
		for j in range(_SIZE):
			vertXList.append(state[j][i])
		if _E not in vertXList and _O not in vertXList:
			return True, 'max'

	# check for vertical o win
	for i in range(_SIZE):
		vertXList = []
		for j in range(_SIZE):
			vertXList.append(state[j][i])
		if _E not in vertXList and _X not in vertXList:
			return True, 'min'

	# check for diagnal left x win
	if all(state[i][i] == _X for i in range(_SIZE)):
		return True, 'max'

	# check for diagnal left o win
	if all(state[i][i] == _O for i in range(_SIZE)):
		return True, 'min'

	# check for diagnal right x win
	if all(state[i][_SIZE-i-1] == _X for i in range(_SIZE)):
		return True, 'max'

	# check for diagnal right o win
	if all(state[i][_SIZE-i-1] == _O for i in range(_SIZE)):
		return True, 'min'

	return False, ''


# function that assigns utility value to terminal states
def evalTerminal(state, player):
	is_terminal, winner = isTerminal(state)
	if not is_terminal:
		raise ValueError('non terminal state in eval terminal')

	if winner == 'max':
		return 1000

	if winner == 'min':
		return -1000

	return 0

# evaluation(state) returns the value for the evaluation function provided in the assignment
def evaluation(state):
	threeX = 0
	twoX = 0
	oneX = 0
	threeO = 0
	twoO = 0
	oneO = 0

	# check if there is a row of 1, 2, 3 X's and no O
	# check if there is a row of 1, 2, 3 O's and no X 
	for i in range(_SIZE):
		if state[i] == [_X, _X, _X, _E] or state[i] == [_X, _X, _E, _X] or state[i] == [_X, _E, _X, _X] or state[i] == [_E, _X, _X, _X]:
			threeX += 1
		elif state[i] == [_X, _X, _E, _E] or state[i] == [_E, _E, _X, _X] or state[i] == [_X, _E, _X, _E] or state[i] == [_E, _X, _E, _X] or state[i] == [_E, _X, _X, _E] or state[i] == [_X, _E, _E, _X]:
			twoX += 1
		elif state[i] == [_E, _E, _E, _X] or state[i] == [_E, _E, _X, _E] or state[i] == [_E, _X, _E, _E] or state[i] == [_X, _E, _E, _E]:
			oneX += 1
		elif state[i] == [_O, _O, _O, _E] or state[i] == [_O, _O, _E, _O] or state[i] == [_O, _E, _O, _O] or state[i] == [_E, _O, _O, _O]:
			threeO += 1
		elif state[i] == [_O, _O, _E, _E] or state[i] == [_E, _E, _O, _O] or state[i] == [_O, _E, _O, _E] or state[i] == [_E, _O, _E, _O] or state[i] == [_E, _O, _O, _E] or state[i] == [_O, _E, _E, _O]:
			twoO += 1
		elif state[i] == [_E, _E, _E, _O] or state[i] == [_E, _E, _O, _E] or state[i] == [_E, _O, _E, _E] or state[i] == [_O, _E, _E, _E]:
			oneO += 1
	
	# check if there is a column of 1, 2, 3 X's and no O 
	# check if there is a column of 1, 2, 3 O's and no X
	for i in range(_SIZE):
		vertList = []
		for j in range(_SIZE):
			vertList.append(state[j][i])
		if vertList == [_X, _X, _X, _E] or vertList[i] == [_X, _X, _E, _X] or vertList[i] == [_X, _E, _X, _X] or vertList[i] == [_E, _X, _X, _X]:
			threeX += 1
		elif vertList[i] == [_X, _X, _E, _E] or vertList[i] == [_E, _E, _X, _X] or vertList[i] == [_X, _E, _X, _E] or vertList[i] == [_E, _X, _E, _X] or vertList[i] == [_E, _X, _X, _E] or vertList[i] == [_X, _E, _E, _X]:
			twoX += 1
		elif vertList[i] == [_E, _E, _E, _X] or vertList[i] == [_E, _E, _X, _E] or vertList[i] == [_E, _X, _E, _E] or vertList[i] == [_X, _E, _E, _E]:
			oneX += 1
		elif vertList[i] == [_O, _O, _O, _E] or vertList[i] == [_O, _O, _E, _O] or vertList[i] == [_O, _E, _O, _O] or vertList[i] == [_E, _O, _O, _O]:
			threeO += 1
		elif vertList[i] == [_O, _O, _E, _E] or vertList[i] == [_E, _E, _O, _O] or vertList[i] == [_O, _E, _O, _E] or vertList[i] == [_E, _O, _E, _O] or vertList[i] == [_E, _O, _O, _E] or vertList[i] == [_O, _E, _E, _O]:
			twoO += 1
		elif vertList[i] == [_E, _E, _E, _O] or vertList[i] == [_E, _E, _O, _E] or vertList[i] == [_E, _O, _E, _E] or vertList[i] == [_O, _E, _E, _E]:
			oneO += 1

	# check if there is a diagnal of 1, 2, 3 X's and no O 
	# check if there is a diagnal of 1, 2, 3 O's and no X
	diagList = []
	for i in range(_SIZE):
		diagList.append(state[i][i])
	if diagList == [_X, _X, _X, _E] or diagList[i] == [_X, _X, _E, _X] or diagList[i] == [_X, _E, _X, _X] or diagList[i] == [_E, _X, _X, _X]:
		threeX += 1
	elif diagList[i] == [_X, _X, _E, _E] or diagList[i] == [_E, _E, _X, _X] or diagList[i] == [_X, _E, _X, _E] or diagList[i] == [_E, _X, _E, _X] or diagList[i] == [_E, _X, _X, _E] or diagList[i] == [_X, _E, _E, _X]:
		twoX += 1
	elif diagList[i] == [_E, _E, _E, _X] or diagList[i] == [_E, _E, _X, _E] or diagList[i] == [_E, _X, _E, _E] or diagList[i] == [_X, _E, _E, _E]:
		oneX += 1
	elif diagList[i] == [_O, _O, _O, _E] or diagList[i] == [_O, _O, _E, _O] or diagList[i] == [_O, _E, _O, _O] or diagList[i] == [_E, _O, _O, _O]:
		threeO += 1
	elif diagList[i] == [_O, _O, _E, _E] or diagList[i] == [_E, _E, _O, _O] or diagList[i] == [_O, _E, _O, _E] or diagList[i] == [_E, _O, _E, _O] or diagList[i] == [_E, _O, _O, _E] or diagList[i] == [_O, _E, _E, _O]:
		twoO += 1
	elif diagList[i] == [_E, _E, _E, _O] or diagList[i] == [_E, _E, _O, _E] or diagList[i] == [_E, _O, _E, _E] or diagList[i] == [_O, _E, _E, _E]:
		oneO += 1

	# check if there is a diagnal of 1, 2, 3 X's and no O 
	# check if there is a diagnal of 1, 2, 3 O's and no X
	diagList = []
	for i in range(_SIZE):
		diagList.append(state[i][_SIZE-i-1])
	if diagList == [_X, _X, _X, _E] or diagList[i] == [_X, _X, _E, _X] or diagList[i] == [_X, _E, _X, _X] or diagList[i] == [_E, _X, _X, _X]:
		threeX += 1
	elif diagList[i] == [_X, _X, _E, _E] or diagList[i] == [_E, _E, _X, _X] or diagList[i] == [_X, _E, _X, _E] or diagList[i] == [_E, _X, _E, _X] or diagList[i] == [_E, _X, _X, _E] or diagList[i] == [_X, _E, _E, _X]:
		twoX += 1
	elif diagList[i] == [_E, _E, _E, _X] or diagList[i] == [_E, _E, _X, _E] or diagList[i] == [_E, _X, _E, _E] or diagList[i] == [_X, _E, _E, _E]:
		oneX += 1
	elif diagList[i] == [_O, _O, _O, _E] or diagList[i] == [_O, _O, _E, _O] or diagList[i] == [_O, _E, _O, _O] or diagList[i] == [_E, _O, _O, _O]:
		threeO += 1
	elif diagList[i] == [_O, _O, _E, _E] or diagList[i] == [_E, _E, _O, _O] or diagList[i] == [_O, _E, _O, _E] or diagList[i] == [_E, _O, _E, _O] or diagList[i] == [_E, _O, _O, _E] or diagList[i] == [_O, _E, _E, _O]:
		twoO += 1
	elif diagList[i] == [_E, _E, _E, _O] or diagList[i] == [_E, _E, _O, _E] or diagList[i] == [_E, _O, _E, _E] or diagList[i] == [_O, _E, _E, _E]:
		oneO += 1

	value = ((6 * threeX) + (3 * twoX) + oneX) - ((6 * threeO) + (3 * twoO) + oneO)

	return value


# driver function for ab search
def alphaBetaSearch(state):
	v, bestSuccessor = maxValue(state, -10000, 10000, 0)
	return bestSuccessor

def maxValue(state, alpha, beta, depth):
	# create cache to hold states found and check if state is repeated
	key = ''.join(''.join(row) for row in state), alpha, beta
	if key in cache:
		return cache[key]
	
	# if state is terminal, assign utility value to that state via evalTerminal function
	is_terminal, _ = isTerminal(state)
	if is_terminal:
		result = evalTerminal(state, 'max'), state
		cache[key] = result
		return result
	v = -10000

	# prevent from printing that max depth is reached too much
	printedDepth = False
	
	# where cuttoff occurs if depth limit reached
	if depth >= _DEPTHLIMIT and not printedDepth:
		printedDepth = True
		print('MAX DEPTH reached in MAX-VALUE')
		print ('Cuttoff due to max depth reached in MAX-VALUE')
		result = evaluation(state), state
		cache[key] = result
		return result
	
	for successor in successors(state, 'max'):
		depth += 1
		mv, _ = minValue(successor, alpha, beta, depth)
		if mv > v:
			v = mv
			bestSuccessor = successor
		if v >= beta:
			result = v, successor
			cache[key] = result
			print('Pruning occurrance in MAX-VALUE')
			return result
		alpha = max(alpha, v)
	result = v, bestSuccessor
	cache[key] = result
	return result


def minValue(state, alpha, beta, depth):
	# create cache to hold states found and check if state is repeated
	key = ''.join(''.join(row) for row in state), alpha, beta
	if key in cache:
		return cache[key]
	
	is_terminal, _ = isTerminal(state)
	if is_terminal:
		result = evalTerminal(state, 'min'), state
		cache[key] = result
		return result
	v = 10000
	
	# prevent from printing that max depth is reached too much
	printedDepth = False

	# where cuttoff occurs if max depth reached
	if depth >= _DEPTHLIMIT and not printedDepth:
		printedDepth = True
		print('MAX DEPTH reached in MIX-VALUE')
		print('Cuttoff due to max depth reached in MIN-VALUE')
		result = evaluation(state), state
		cache[key] = result
		return result
	
	for successor in successors(state, 'min'):
		depth += 1
		mv, _ = maxValue(successor, alpha, beta, depth)
		if mv < v:
			v = mv
			bestSuccessor = successor
		if v <= alpha:
			result = v, successor
			cache[key] = result
			print('Pruning occurrance in MIN-VALUE')
			return result
		beta = min(beta, v)
	result = v, bestSuccessor
	cache[key] = result
	return result

# function to allow user to pick which level of difficulty they would like to play
def level():
	global _DEPTHLIMIT
	allowed = False
	while not allowed:
		level = input("Pick difficulity (1 = easy, 2 = intermediate, 3 = hard): ")
		level = int(level)
		if level > 0 and level < 4:
			allowed = True
	if level == 1:
		_DEPTHLIMIT = 1
	if level == 2:
		_DEPTHLIMIT = 7
	if level == 3:
		_DEPTHLIMIT = 16

# prints states out in command line in readable format
def nicePrint(state):
	for i in range(_SIZE):
		print(state[i])
	print('\n')


# base board for the game
def displayBoard(state):
	global _TOP
	global _BOARD

	#drawing the game board
	_BOARD.create_line(0, 250, 800, 250)
	_BOARD.create_line(0, 450, 800, 450)
	_BOARD.create_line(0, 650, 800, 650)
	_BOARD.create_line(0, 50, 800, 50)
	_BOARD.create_line(200, 50, 200, 850)
	_BOARD.create_line(400, 50, 400, 850)
	_BOARD.create_line(600, 50, 600, 850)
	
	# draws either an X or an O in the right location
	for i in range(4):
		for j in range(4):
			if state[i][j] == _X:
				_BOARD.create_line((0 + (i * 200)), (50 + (j * 200)), (200 + (i * 200)), (250 + (j * 200)))
				_BOARD.create_line((0 + (i * 200)), (250 + (j * 200)), (200 + (i * 200)), (50 + (j * 200)))
			elif state[i][j] == _O:
				_BOARD.create_oval((0 + (i * 200)), (50 + (j * 200)), (200 + (i * 200)), (250 + (j * 200)))
	makeClickButton()
	_BOARD.pack()
	_TOP.title('Tic Tac Toe')

# gets coordinates of the mouse and translate into integer input for the user's move
def find_mouse_xy(event):
	global _TOP
	global _BOARD
	global _USER_Y
	global _USER_X
	mouse_x = _BOARD.winfo_pointerx()
	mouse_y = _BOARD.winfo_pointery()
	if mouse_x < 200:
		_USER_X = 0
	elif mouse_x < 400:
		_USER_X = 1
	elif mouse_x < 600:
		_USER_X = 2
	elif mouse_x < 800:
		_USER_X = 3
	if mouse_y < 250:
		_USER_Y = 0
	elif mouse_y < 450:
		_USER_Y = 1
	elif mouse_y < 650:
		_USER_Y = 2
	elif mouse_y < 850:
		_USER_Y = 3

# function that binds the mouse click
def makeClickButton():
	global _BOARD
	_BOARD.bind('<Button-1>', find_mouse_xy)


# main function to run to play the game
def play(state):
	global _WINNER
	global _NODES_GENERATED
	level()
	
	# see if user would like to go first
	userGoFirst = False
	start = input("Would you like to go first? (Yes/No): ")
	if start == 'Yes':
		userGoFirst = True
	while not isTerminal(state)[0]:
		if not userGoFirst:
			state = alphaBetaSearch(state)
			print('Nodes generated: ' + str(_NODES_GENERATED))
			print('Computers move:')
			# comment out nicePrint (state) to play with GUI
			nicePrint(state)
			# uncomment displayBoard(state) to play with GUI
			#displayBoard(state)
			if isTerminal(state)[0]:
				_, _WINNER = isTerminal(state)
				if _WINNER == 'mai':
					print('Computer won!')
				else:
					print('It\'s a tie!')
		if not isTerminal(state)[0]:
			userGoFirst = False
			# make sure user's input is an allowable game move
			allowed = False
			while not allowed:
				move = input("move: ")
				# comment out next 3 lines of code to play with GUI
				move = tuple(map(int, move.split(',')))
				_USER_X = move[0]
				_USER_Y = move[1]
				if state[_USER_X][_USER_Y] == _E:
					allowed = True
				else:
					print('Move not allowed, try again')
			if allowed:
				state[_USER_X][_USER_Y] = _O
				print('Your move:')
				# comment out nicePrint (state) to play with GUI
				nicePrint(state)
				# uncomment displayBoard(state) to play with GUI
				#displayBoard(state)
				if isTerminal(state)[0]:
					_, _WINNER = isTerminal(state)
					if _WINNER == 'min':
						print('You won!')
					else:
						print('It\'s a tie!')


play(grid)






