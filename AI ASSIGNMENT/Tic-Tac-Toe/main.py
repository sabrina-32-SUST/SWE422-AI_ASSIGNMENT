from math import inf as infinity



humen =  -1
computer = 1
board = [
    [0,0,0],
    [0, 0, 0],
    [0, 0, 0]

]
"minimax fuction  will  choose   the  best  move"


def gameOver(state):
    pass


def evaluate(state):
    pass


def minimax(state, depth, player):
    if player == computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    if depth == 0 or gameOver(state):
        score = evaluate(state)
        return [-1, -1, score]

"main  function"
def main():
    print("hello")

main()