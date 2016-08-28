# Author: Nathan Calderon
# Filename: Tic_Tac_Toe.py

# This is a Tic Tac Toe game written in python

# Import
import pprint
import random

# functions
# print the tic tac toe board
def printTheBoard(board):
    print('\nThe official board.')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9] + '\n')

# choose who is X and who is O
def computer_XO(user_XO):
    if user_XO == 'X':
        computer_XO = 'O'
    else:
        computer_XO = 'X'
    return computer_XO

# how the computer chooses a move
def computerMove(computer_XO):
    available = []
    for k,v in theBoard.items():
        if v == ' ':
            available.append(k)
    index = random.randint(1,9)

    def isEmpty(a):
        for item in a:
            if item == 'X':
                return False
                break
            if item == 'O':
                return False
                break
            else:
                return True

    if isEmpty(available):
        theBoard[index] = computer_XO
    else:
        for k, v in theBoard.items():
            if v == ' ':
                theBoard[k] = computer_XO
                break

# user defined move          
def UserMove(userGridPick, XO):
    for k in theBoard.keys():
        if k == userGridPick:
            theBoard[k] = XO

# verify user entry
def userXOVerify(selection):
    if selection in ('X', 'O'):
        return selection
    else:
        print('You did not enter and X or an O silly.')
        print("You will be O's.")
        return 'O'

# print the board for user help
def boardGrid():
    print('The player "help" board.')
    key=[]
    value=[]
    for k,v in theBoard.items():
        key.append(k)
        value.append(v)

    count=1
    for item in value:
        if item in ('X', 'O'):
            print(item, end="")
            if str(count) in ('1','2','4','5','7','8'):
                print('|', end="")
            elif str(count) in ('3','6'):
                print('\n-----')
        elif item == ' ':
            print(str(count), end="")
            if str(count) in ('1','2','4','5','7','8'):
                print('|', end="")
            elif str(count) in ('3','6'):
                print('\n-----')
        count = count + 1
    print('\n')
    del key
    del value

# determine if any row has three Xs or Os
def countCheck(row):
    if row == ['X','X','X']:
        return True
    if row == ['O','O','O']:
        return True
    else:
        return False

# determine if a placement is valid
def gameCheck():
    top = []
    middle = []
    bottom = []
    right = []
    mid = []
    left = []
    rightDiag = []
    leftDiag = []
    condition = False
    for k,v in theBoard.items():
        if k in (1, 2, 3):
            top.append(v)
        if k in (4, 5, 6):
            middle.append(v)
        if k in (7, 8, 9):
            bottom.append(v)
        if k in (3, 6, 9):
            right.append(v)
        if k in (2, 5, 8):
            mid.append(v)
        if k in (1, 4, 7):
            left.append(v)
        if k in (3, 5, 7):
            rightDiag.append(v)
        if k in (1, 5, 9):
            leftDiag.append(v)
    if countCheck(top):
        return True
    if countCheck(middle):
        return True
    if countCheck(bottom):
        return True
    if countCheck(right):
        return True
    if countCheck(mid):
        return True
    if countCheck(left):
        return True
    if countCheck(rightDiag):
        return True
    if countCheck(leftDiag):
        return True
    else:
        return False

################## main ############

# variables
condition = True
while condition:

    print('Welcome to Tic Tac Toe!')     # Program opening message
    print("Do you want to be X's or O's?", end=' ')  # User chooses 'X' or 'O'
    userXO = str(input())
    userXO = userXO.upper()             # User choice to uppercase

    userXO = userXOVerify(userXO)       # User choice verified

    computerXO = computer_XO(userXO)    # Computer designated player piece
    print('The computer will be: ' + str(computerXO))

    theBoard = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '}

    ################# game play ###############
    ## computer move 1
    print('The computer will go first.')
    computerMove(computerXO)            # first move made by computer
    printTheBoard(theBoard)             # print the starting board to the screen
    boardGrid()                         # print board for user placement

    for items in range(0,8):
        ## user move 1
        print('What is your next move? Choose a number from the grid to place'
              ' your ' + str(userXO) + ': ', end=' ')
        userSelection = int(input())        # user enters grid number for placement
        UserMove(userSelection, userXO)     # grid number converted to userXO
        printTheBoard(theBoard)             # print the board to the screen
        if gameCheck():
            print('You Won!')
            print('Congrats you beat a shitty computer program.')
            break

        ## computer move 2
        print("Computer's turn.")
        computerMove(computerXO)
        printTheBoard(theBoard)
        boardGrid()
        if gameCheck():
            print('You Lost!')
            print('Really? You just lost to a shitty computer program.')
            break

    print('Would you like to play again?' + '(True or False)')
    condition = input()


