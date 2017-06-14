def printBoard():
    print
    for obj in board:
        print "  ".join(obj)

    print "\n" + "  ".join(columnRef) + "\n"


def getInput():
    userInput = raw_input("Enter column to drop in: ")
    return userInput

def isExit(strng):
    if strng.lower() == "exit":
        return True
    else:
        return False

def isChar(strng):
    if strng.isalpha():
        return True
    else:
        return False

def isOutOfRange(strng):
    if strng >= boardLength or strng < 0:
        return True
    else:
        return False

def isFullColumn(strng):
    if board[0][strng] != "O":
        return True
    else:
        return False

def validateInput():
    value = getInput()
    if isExit(value):
        return "exit"
    if isChar(value) or value == "":
        print "Invalid input"
        return validateInput()
    if isOutOfRange(int(value)-1):
        print "Value is out of range"
        return validateInput()
    if isFullColumn(int(value)-1):
        print "Column is full"
        return validateInput()
    return int(value)-1



def updateBoard(spot, player):
    for i in range(boardHeight-1, -1, -1):
        if board[i][spot] == "O":
            board[i][spot] = player
            break

def horizontal(player):
    winString = player * to_win
    for row in board:
        combString = ""
        for char in row:
            combString += char
        if winString in combString:
            global game_on
            game_on = False

def vertical(player):
    winString = player * to_win
    combList = []
    for i in range(0,boardLength,1):
        combString = ""
        for row in board:
            combString += row[i]
        combList.append(combString)

    for obj in combList:
        if winString in obj:
            global game_on
            game_on = False

def diagonalR(player):
    winString = player * to_win

    combList = []

    # This for loop is for going down vertically, looking up and to the right/down to the left - /
    for i in range(to_win-1,boardHeight,1):
        vert_position = i
        horiz_position = 0
        combString = ""
        while vert_position > -1:
            combString += board[vert_position][horiz_position]
            vert_position -= 1
            horiz_position += 1
        combList.append(combString)



    # This for loop is for going right horizontally, looking up and to the right/down to the left - /
    for i in range(1,boardLength-to_win+1,1):
        vert_position = boardHeight-1
        horiz_position = i
        combString = ""
        while horiz_position < boardLength:
            combString += board[vert_position][horiz_position]
            vert_position -= 1
            horiz_position += 1
        combList.append(combString)



    for obj in combList:
        if winString in obj:
            global game_on
            game_on = False


def diagonalL(player):
    winString = player * to_win


    combList = []

    # This for loop is for going down vertically, looking up and to the left/down to the right - \
    for i in range(to_win-1,boardHeight,1):
        vert_position = i
        horiz_position = boardLength-1
        combString = ""
        while vert_position > -1:
            combString += board[vert_position][horiz_position]
            vert_position -= 1
            horiz_position -= 1
        combList.append(combString)



    # This for loop is for going right horizontally, looking up and to the left/down to the right - \
    for i in range(boardLength-2,to_win-2,-1):
        vert_position = boardHeight-1
        horiz_position = i
        combString = ""
        while horiz_position > -1:
            combString += board[vert_position][horiz_position]
            vert_position -= 1
            horiz_position -= 1
        combList.append(combString)



    for obj in combList:
        if winString in obj:
            global game_on
            game_on = False


def gameOver():
    global turn
    if turn >= boardHeight * boardLength:
        global game_on
        game_on = False
    if turn%2 != 0:
        horizontal(p1)
        vertical(p1)
        diagonalR(p1)
        diagonalL(p1)
    else:
        horizontal(p2)
        vertical(p2)
        diagonalR(p2)
        diagonalL(p2)

boardLength = 7
boardHeight = 6

columnNums = range(1,boardLength+1)
columnRef = []
for num in columnNums:
    columnRef.append(str(num))
p1 = "A"
p2 = "B"

turn = 1
to_win = 4

game_on = True

row = ["O"] * boardLength
board = []
for i in range(0, boardHeight, 1):
    board.append(list(row))

print "Welcome to Connect 4!"
print "Enter the position of where you want to play a piece."
print "You can always type \"exit\" to end the game."


printBoard()
print "Player 1,"
position = ""

while position != "exit" and game_on:
    position = validateInput()
    if position == "exit":
        break
    if turn%2 != 0:
        updateBoard(position,p1)
        printBoard()
        print "Player 2,"

    else:
        updateBoard(position,p2)
        printBoard()
        print "Player 1,"

    gameOver()
    turn += 1

if not game_on:
    if turn >= boardHeight * boardLength:
        print "Tie game! You both suck."
    elif turn%2 == 0:
        print "You lose."
        print "Player 1 wins!!!"
    else:
        print "You lose."
        print "Player 2 wins!!!"

print "Game Over."
