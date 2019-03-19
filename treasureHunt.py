import math
import sys
import random


print(f"Running {sys.path[0]}.py\nwith Python {sys.version[:5]}\n")

# Returns a matrix. len(list) == 60 && len(list[i] == 15
def getNewBoard():
    board = []
    for i in range(60):
        board.append([])
        for j in range(15):
            board[i].append("X")
    return board

print(len(getNewBoard()))
