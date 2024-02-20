# Question: https://www.codingame.com/ide/puzzle/object-insertion

# Completed!

a, b = 3, 2
shape = [".*", "**", ".*"]


c, d = 8, 10
grid = [
    "#..#######",
    "#.##..####",
    "###..##...",
    "####.#####",
    "##.#######",
    "##......##",
    "##.....###",
    "########..",
]

"""for i in grid:
    print(i)

for i in shape:
    print(i)"""

count = 0
found_list = []
for i in range(c - a + 1):
    for j in range(d - b + 1):
        found = True
        found_grid = []
        for k in range(a):
            for l in range(b):
                if shape[k][l] == "*":
                    if not grid[i + k][j + l] == ".":
                        found = False
                        break
                    else:
                        found_grid.append([i + k, j + l])
        if found:
            found_list.append(found_grid)

            if not found:
                break
        if found:
            count += 1
print(count)
output_grid = []
if count == 1:
    lst = []
    for i in grid:
        i = [x for x in i]
        lst.append(i)
    for i in found_list[0]:
        lst[i[0]][i[1]] = "*"
    for i in lst:
        output_grid.append("".join(i))
    for i in output_grid:
        print(i)
