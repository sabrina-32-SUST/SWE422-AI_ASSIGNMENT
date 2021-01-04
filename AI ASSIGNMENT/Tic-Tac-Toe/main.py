import platform
import time
from math import inf as infinity
from os import system
from random import choice

humen =  -1
computer = 1
board = [
    [0,0,0],
    [0, 0, 0],
    [0, 0, 0]

]
"check  possibilities  of  wins"
def wins(state, player):

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


"game over state"
def gameOver(state):
    return wins(state, humen) or wins(state, computer)



def evaluate(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

"""
Each empty cell will be added into cells list
"""
def emptyCells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

"""
    A move is valid if the chosen cell is empty
    
    """
def validMove(xCoordinate, yCoordinate):

    if [xCoordinate, yCoordinate] in emptyCells(board):
        return True
    else:
        return False

"""
   Player  move  if the coordinates are valid
    
    """
def setMove(xCoordinate, yCoordinate, player):

    if validMove(xCoordinate, yCoordinate):
        board[xCoordinate][yCoordinate] = player
        return True
    else:
        return False


"minimax fuction  will  choose   the  best  move"
def minimax(state, depth, player):
    if player == computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    if depth == 0 or gameOver(state):
        score = evaluate(state)
        return [-1, -1, score]
    for cell in emptyCells(state):
        xCoordinate, yCoordinate = cell[0], cell[1]
        state[xCoordinate][yCoordinate] = player
        score = minimax(state, depth - 1, -player)
        state[xCoordinate][yCoordinate] = 0
        score[0], score[1] = xCoordinate, yCoordinate
    if player == computer:
        if score[2] > best[2]:
            best = score  # maximum value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


"""
   Clears the console
   """
def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')
 """
    Print the board on console
     """
def render(state, computer_choice, humen_choice):

    chars = {
        -1: humen_choice,
        +1: computer_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

 """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    """


def xCoordinate(args):
    pass


def yCoordinate(args):
    pass


def ai_turn( computer_choice, humen_choice):

    depth = len(emptyCells(board))
    if depth == 0 or gameOver(board):
        return

    clean()
    print(f'Computer turn [{ computer_choice }]')
    render(board,  computer_choice, humen_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, computer)
        x, y = move[0], move[1]

    setMove(xCoordinate, yCoordinate, computer)
    time.sleep(1)

 """
    The Human plays choosing a valid move.
     
    """
def human_turn( computer_choice, humen_choice):

    depth = len(emptyCells(board))
    if depth == 0 or gameOver(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{humen_choice}]')
    render(board, computer_choice, humen_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = setMove(coord[0], coord[1], humen)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')



"main  function"
def main():

    clean()
    humen_choice = ''  # X or O
    computer_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while humen_choice != 'O' and humen_choice != 'X':
        try:
            print('')
            humen_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if humen_choice == 'X':
        computer_choice = 'O'
    else:
        computer_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(emptyCells(board)) > 0 and not gameOver(board):
        if first == 'N':
            ai_turn(computer_choice , humen_choice)
            first = ''

        human_turn(computer_choice , humen_choice)
        ai_turn(computer_choice , humen_choice)

    # Game over message
    if wins(board, humen):
        clean()
        print(f'Human turn [{humen_choice}]')
        render(board, computer_choice , humen_choice)
        print('YOU WIN!')
    elif wins(board, computer):
        clean()
        print(f'Computer turn [{computer_choice}]')
        render(board,computer_choice , humen_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board,computer_choice , humen_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()