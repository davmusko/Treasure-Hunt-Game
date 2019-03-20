import math
import sys
import random


print(f"Running {sys.path[0]}.py\nwith Python {sys.version[:5]}\n")

# Returns a matrix. grid[x-axis][y-axis]
# Change ASCII design of grid in this function
def get_grid():
    grid = []
    for i in range(60):
        grid.append([])
        for j in range(15):
            grid[i].append("X")
    return grid


# Prints playing board and axes from a grid.
def print_board(grid):
    # Create a string for the x-axis 10's place
    xAxisTens = "    "
    for i in range(1, 6):
        xAxisTens += (" " * 9) + str(i)

    # Create a string for the x-axis 1's place
    xAxis = ""
    for i in range(10):
        xAxis += str(i)
    xAxis = "   " + (xAxis * 6)


    # Prints for x-axes
    print(xAxisTens)
    print(xAxis)


    # Print each row grid[0][0] + grid[1][0] + grid[2][0]
    #                grid[0][1] + grid[1][1] + grid[2][1] ect....
    for row in range(len(grid[0])):
        # Adds a space for padding to y-axis, single digit numbers
        if row < 10:
            padding = " "
        else:
            padding = ""

        # Create string for each row.
        boardRow = ""
        for column in range(len(grid)):
            boardRow += grid[column][row]

        print("%s%s %s %s" % (padding, row, boardRow, row))





# Below for testing only
print_board(get_grid())