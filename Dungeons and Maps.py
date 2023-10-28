w = 19
h = 12
n = 2
start_row, start_col = 2, 4

maps = [['###################', '#.................#', '#..>>>v......>T...#', '#..^..>v.....^<...#', '#..^...>v.........#', '#..^....v....>v...#', '#..^....v....^v...#', '#..^...v<....^v...#', '#..^..v<.....^v...#', '#..^<<<......^<...#', '#.................#', '###################'], ['###################', '#.................#', '#...>>>v......>T..#', '#...^..>v.....^<..#', '#...^...>v........#', '#...^....v....>v..#', '#...^....v....^v..#', '#...^...v<....^v..#', '#...^..v<.....^v..#', '#...^<<<......^<..#', '#.................#', '###################']]
result_lst = []

for i in range(len(maps)):
    trap = False
    count = 0
    current = maps[i][start_row][start_col]
    row, col = start_row, start_col
    visited = []

    while True:
        try:
            if current == ">":
                col += 1
            elif current == "<":
                col -= 1
            elif current == "v":
                row += 1
            elif current == "^":
                row -= 1
            elif current == "T":
                result_lst.append([trap, count, i])
                count += 1
                break
            else:
                trap = True
                result_lst.append([trap, count, i])
                break
            if [row,col] in visited:
                trap = True
                break
            else:
                current = maps[i][row][col]
                visited.append([row,col])
                count += 1

        except IndexError:
            trap = True
            result_lst.append([trap, count, i])
            break

counts = w*h
winner = n

for i in result_lst:
    if i[0] == False and i[1] < counts:
        counts = i[1]
        winner = i[2]

print(winner if winner < n else "TRAP")
