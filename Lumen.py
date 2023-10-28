# https://www.codingame.com/ide/puzzle/lumen

room_map = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "3", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "3", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "3", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["3", "X", "X", "X", "X", "X", "X", "X", "3", "X", "X", "3", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "3"],
    ["X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "3", "X", "3", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "3", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "3", "X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "X", "3"],
    ["X", "X", "X", "X", "X", "X", "3", "X", "X", "X", "3", "X", "X", "X", "X"],
    ["X", "3", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
]


n = 15
l = 3

# visualize the original grid:
for i in room_map:
    print("".join(i))

for i in range(l, -1, -1):
    for j in range(n):
        for k in range(n):
            if room_map[j][k] == str(i):
                current = room_map[j][k]
                directions = [
                    (j + x, k + y)
                    for x in range(-1, 2)
                    for y in range(-1, 2)
                    if (0 <= j + x < n) and (0 <= k + y < n) and (x, y) != (0, 0)
                ]
                for d in directions:
                    cell = room_map[d[0]][d[1]]

                    if not cell.isdigit():
                        room_map[d[0]][d[1]] = (
                            str(int(current) - 1) if int(current) > 0 else "0"
                        )

count = 0
candle_count = 0
for i in range(n):
    for j in range(n):
        if room_map[i][j] == "0":
            count += 1
        if room_map[i][j] != "X":
            candle_count += 1
print()
# visualize the processed grid:
for i in room_map:
    print("".join(i))

# outputs the count of dark areas:
print(n*n if candle_count == 0 else count)
