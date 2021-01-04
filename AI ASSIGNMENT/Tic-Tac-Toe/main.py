from math import inf as infinity



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




"main  function"
def main():
    print("hello")

main()