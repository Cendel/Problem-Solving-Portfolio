grid1 = [
    "....................",
    ".>..................",
    "...................<",
    "....................",
    "....................",
    "_________^__________",
]

grid2 = [
    ">...................",
    ">...................",
    ">...................",
    "....................",
    "....................",
    "_________^__________",
]

grid3 = ["...<<<<<<<<<<<<<<<<<<<<<<<..<<<",
         "^______________________________"]

grid4 = [
    "...........................<...........",
    ".......................................",
    ".......................................",
    ".......................................",
    "............<..<..<..<..<..<..<..<..<..",
    ".......................................",
    ".......................................",
    ".......................................",
    "..>......<..<..<..<..<..<..<..<..<..<..",
    "______^________________________________",
]

grid5 = [">.>..",
         "____^"]


def make_list(x):
    grid_lst = []
    for i in x:
        lst = []
        for j in i:
            lst.append(j)
        grid_lst.append(lst)
    return grid_lst


def make_string(x):
    output_grid = []
    for i in x:
        output_grid.append("".join(i))
    return output_grid


def main(grid):
    for i in grid:
        print(i)
    grid = make_list(grid)
    plane_count = sum(row.count(char) for row in grid for char in ("<", ">"))
    missile_pos = grid[-1].index("^")
    while plane_count:
        shoot = False
        grid = make_string(grid)

        grid = make_list(grid)
        for i in range(len(grid) - 1):
            right_lst = []
            left_lst = []
            for j in range(len(grid[i])):
                if grid[i][j] == ">":
                    right_lst.append(j)
                    if j < missile_pos and len(grid) - i == missile_pos - j:
                        shoot = True

                elif grid[i][j] == "<":
                    left_lst.append(j)
                    if j > missile_pos and len(grid) - i == j - missile_pos:
                        shoot = True
            for el in right_lst:
                grid[i][el] = "."
                try:
                    grid[i][el + 1] = ">"
                except IndexError:
                    grid[i][0] = ">"
            for el in left_lst:
                grid[i][el] = "."
                try:
                    grid[i][el - 1] = "<"
                except IndexError:
                    grid[i][-1] = "<"
        if shoot:
            print("SHOOT")
            plane_count -= 1
        else:
            print("WAIT")


main(grid4)
