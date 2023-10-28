grid = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", ".", ".", "x"],
    [".", ".", "x", ".", ".", ".", ".", ".", ".", "x"],
    [".", ".", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", ".", "x", ".", "x", ".", ".", ".", "x", "."],
    ["x", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", "x", ".", ".", ".", "x"],
]

width = 10
height = 7

mine_list = []

for x in range(height):
    for y in range(width):
        if grid[x][y] == "x":
            mine_list.append([x, y])


def shoot(grid, x, y):
    for i in range(x - 1, x + 2, 1):
        for j in range(y - 1, y + 2, 1):
            if height > i >= 0 and width > j >= 0:
                if [i, j] in mine_list:
                    grid[i][j] = "."
                elif str(grid[i][j]).isdigit():
                    grid[i][j] = str(int(grid[i][j]) + 1)
                else:
                    grid[i][j] = 1


for i in mine_list:
    shoot(grid, i[0], i[1])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = str(grid[i][j])

result = []
for row in grid:
    result.append("".join(row))

for i in result:
    print(i)
