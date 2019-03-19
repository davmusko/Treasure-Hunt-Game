import math
import sys
import random


print(f"Running {sys.path[0]}.py\nwith Python {sys.version[:5]}\n")

# Returns a matrix. len(list) == 60 && len(list[i] == 15
# Change ASCII design of grid in this function
def get_grid():
    grid = []
    for i in range(60):
        grid.append([])
        for j in range(15):
            grid[i].append("X")
    return grid


# Print grid from getNewBoard() with formatting
def printBoard(grid):
    xAxisTens = "    "
    for i in range(1,6):
        xAxisTens += (" " * 9) + str(i)
    print(xAxisTens)
    print("    " + ("0123456789" * 6))

printBoard(get_grid())