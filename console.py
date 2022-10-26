import random

Rows = 20
Cols = 20
Mines = 20
Placed_Mines = 0
Grid = [["⬜" for row in range(Rows)] for col in range(Cols)]
Unrevealed_Grid = [["⬜" for row in range(Rows)] for col in range(Cols)]

def amount_bombs(row, col):
    global Unrevealed_Grid
    bombs = 0
    if row == 0:
        if col == 0:
            if Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col+1] == "💣":
                bombs += 1
        elif col == Cols-1:
            if Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col-1] == "💣":
                bombs += 1
        else:
            if Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
    elif row == Rows-1:
        if col == 0:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col+1] == "💣":
                bombs += 1
        elif col == Cols-1:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col-1] == "💣":
                bombs += 1
        else:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col+1] == "💣":
                bombs += 1
    else:
        if col == 0:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col+1] == "💣":
                bombs += 1
        elif col == Cols-1:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col-1] == "💣":
                bombs += 1
        else:
            if Unrevealed_Grid[row-1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col-1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row-1][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row][col+1] == "💣":
                bombs += 1
            elif Unrevealed_Grid[row+1][col+1] == "💣":
                bombs += 1
    return bombs
while Placed_Mines <= Mines:
    x = random.randint(0, Rows-1)
    y = random.randint(0, Cols-1)
    if Unrevealed_Grid[x][y] != "💣":
        Unrevealed_Grid[x][y] = "💣"
        Placed_Mines += 1

for row in range(Rows):
    for col in range(Cols):
        if amount_bombs(row, col) == 1:
            Unrevealed_Grid[row][col] = "1️⃣"
        elif amount_bombs(row, col) == 2:
            Unrevealed_Grid[row][col] = "2️⃣"
        elif amount_bombs(row, col) == 3:
            Unrevealed_Grid[row][col] = "3️⃣"
        elif amount_bombs(row, col) == 4:
            Unrevealed_Grid[row][col] = "4️⃣"
        elif amount_bombs(row, col) == 5:
            Unrevealed_Grid[row][col] = "5️⃣"
        elif amount_bombs(row, col) == 6:
            Unrevealed_Grid[row][col] = "6️⃣"

# print(amount_bombs(5, 0))

# for Row in Unrevealed_Grid:
#     print("".join(Row))