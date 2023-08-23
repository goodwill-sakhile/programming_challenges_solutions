def checkRightSide(i, j,  count, mines_grid):
    if ((j + 1) < (len(mines_grid[i]))):
        if mines_grid[i][j+1] == "*":
            count += 1
    return count
def checkLeftSide(i, j, count, mines_grid):
    if ((j - 1) >= 0):
        if mines_grid[i ][j - 1] == "*":
            count += 1
    return count
def checkTop(i, j, count, mines_grid):
    if ((i - 1) >= 0):
        if mines_grid[i -1][j] == "*":
            count += 1
    return count
def checkDown(i, j, count, mines_grid):
    if ((i + 1) < (len(mines_grid))):
        if mines_grid[i+1][j] == "*":
            count += 1
    return count
def checkTopLeft(i, j, count, mines_grid):
    if ((i - 1) >= 0):
        count = checkLeftSide(i - 1, j, count, mines_grid)
    return count
def checkTopRight(i, j, count, mines_grid):
    if ((i - 1) >= 0):
        count = checkRightSide(i - 1, j, count, mines_grid)
    return count
def checkDownLeft(i, j, count, mines_grid):
    if ((i + 1) < len(mines_grid)):
        count = checkLeftSide(i +1, j, count, mines_grid)
    return count
def checkDownRight(i, j, count, mines_grid):
    if ((i + 1) < (len(mines_grid))):
        count = checkRightSide(i + 1, j, count, mines_grid)
    return count
def findMinesLocation(mines_grid):
    for i in range(len(mines_grid)):
        line = ""
        for j in range(len(mines_grid[i])):
            if mines_grid[i][j] == ".":
                count = 0
                count = checkRightSide(i, j, count, mines_grid)
                count = checkLeftSide(i, j, count, mines_grid)
                count = checkTop(i, j, count, mines_grid)
                count = checkDown(i, j, count, mines_grid)
                count = checkTopLeft(i, j, count, mines_grid)
                count = checkTopRight(i, j, count, mines_grid)
                count = checkDownLeft(i, j, count, mines_grid)
                count = checkDownRight(i, j, count, mines_grid)
                if count > 0:
                    line += str(count)
                else:
                    line += "0"
            else:
                 line += "*"
        print(line)
findMinesLocation([["*", ".", ".", "."], [".", ".", ".", "."], [".","*", ".", "."], [".", ".", ".", "."]])         