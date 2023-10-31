grid1 = ["~ * ~", "~ ~ ~", "~ * ~"]
target = ["* * *", "* ~ *", "* * *"]
player_buttons = "884"

# after the players entered a series of numbers as in above, there is always a button left to complete the
# puzzle. This program helps to find this last button.

for i in grid1:
    print(i)


def button_action(number, grid):
    grid = [list(i.split()) for i in grid]
    ranges = {
        1: [(0, 2), (0, 2)],
        2: [(0, 1), (0, 3)],
        3: [(0, 2), (1, 3)],
        4: [(0, 3), (0, 1)],
        6: [(0, 3), (2, 3)],
        7: [(1, 3), (0, 2)],
        8: [(2, 3), (0, 3)],
        9: [(1, 3), (1, 3)],
    }
    if number == 5:
        for i in range(3):
            grid[i][1] = "~" if grid[i][1] == "*" else "*"
        for j in range(3):
            grid[1][j] = "~" if grid[1][j] == "*" else "*"
        grid[1][1] = "~" if grid[1][1] == "*" else "*"
    else:
        for i in range(ranges[number][0][0], ranges[number][0][1]):
            for j in range(ranges[number][1][0], ranges[number][1][1]):
                grid[i][j] = "~" if grid[i][j] == "*" else "*"

    result = []
    for i in grid:
        result.append(" ".join(i))

    return result

for i in player_buttons:
    grid1=button_action(int(i), grid1)

for i in range(1,10):
    if button_action(i, grid1) == target:
        print(i)