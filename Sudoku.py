sudoku = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]


def result(grid):
    for i in range(9):
        row = []
        col = []

        for j in range(9):
            currentrow = grid[i][j]
            currentcol = grid[j][i]
            if currentrow in row or currentcol in col:
                return "false"
            else:
                row.append(currentrow)
                col.append(currentcol)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = set()
            for k in range(i, i + 3, 1):
                for l in range(j, j + 3, 1):
                    subgrid.add(grid[k][l])
            if len(subgrid) < 9:
                return "false"

    return "true"


print(result(sudoku))
