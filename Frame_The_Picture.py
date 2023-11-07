frame = "Oo:"
h, w = 3, 7
picture = ["   _o  ", " _< \\_ ", "(_)>(_)"]

grid_h = h + 2 + (len(frame) * 2)
grid_w = w + 2 + (len(frame) * 2)

grid = [[" " for x in range(grid_w)] for _ in range(grid_h)]

for i in range(len(frame)):
    for j in range(grid_h):
        if grid[j][i] == " ":
            grid[j][i] = frame[i]
            grid[j][0 - 1 - i] = frame[i]
        for k in range(grid_w):
            if grid[i][k] == " ":
                grid[i][k] = frame[i]
                grid[0 - 1 - i][k] = frame[i]

start = len(frame) + 1
end = grid_w - len(frame) - 1
for i in range(len(picture)):
    for j in range(len(picture[i])):
        grid[start + i][start + j] = picture[i][j]

for i in grid:
    print("".join(i))
