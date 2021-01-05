from math import inf as infinity
from random import choice
import platform
import time
from os import system



HUMAN = -1
COMPUTER = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):

    if wins(state, COMPUTER):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


"""
Possibilities of  wins
  """
def wins(state, player):

    winState = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in winState:
        return True
    else:
        return False


"""
computer  wins  or  human
  """
def gameOver(state):

    return wins(state, HUMAN) or wins(state, COMPUTER)


"""
   empty cell  in  the list

 """
def emptyCells(state):

    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


"""
valid  move = empty  cells
  """
def validMove(x, y):

    if [x, y] in emptyCells(board):
        return True
    else:
        return False


"""
 move  will  set  if  the  cell  is  valid
  """
def setMove(x, y, player):

    if validMove(x, y):
        board[x][y] = player
        return True
    else:
        return False


"""
  MINIMAX function  for  the best move

   """
def minimax(state, depth, player):

    if player == COMPUTER:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or gameOver(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in emptyCells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTER:
            if score[2] > best[2]:
                best = score  # maximum value
        else:
            if score[2] < best[2]:
                best = score  # minimum value

    return best

"""
clearing  console
"""
def clean():

    osName = platform.system().lower()
    if 'windows' in osName:
        system('cls')
    else:
        system('clear')

"""
 showing board  on  console
      """
def render(state, computer_choice, human_choice):


    chars = {
        -1: human_choice,
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


def computer_turn(computer_choice, human_choice):

    depth = len(emptyCells(board))
    if depth == 0 or gameOver(board):
        return

    clean()
    print(f'Computer turn [{computer_choice}]')
    render(board, computer_choice, human_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMPUTER)
        x, y = move[0], move[1]

    setMove(x, y, COMPUTER)
    time.sleep(1)


"""
  valid move  for human

   """
def human_turn(computer_choice, human_choice):

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
    print(f'Human turn [{human_choice}]')
    render(board, computer_choice, human_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = setMove(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')



"""Main  function """
def main():

    clean()
    human_choice = ''  # X or O
    computer_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while human_choice != 'O' and human_choice != 'X':
        try:
            print('')
            human_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if human_choice == 'X':
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
            computer_turn(computer_choice, human_choice)
            first = ''

        human_turn(computer_choice, human_choice)
        computer_turn(computer_choice, human_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{human_choice}]')
        render(board, computer_choice, human_choice)
        print('YOU WIN!')
    elif wins(board, COMPUTER):
        clean()
        print(f'Computer turn [{computer_choice}]')
        render(board, computer_choice, human_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, computer_choice, human_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()