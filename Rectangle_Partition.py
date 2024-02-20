# Question: https://www.codingame.com/ide/puzzle/rectangle-partition

# Completed!

ys = []
w, h, count_x, count_y = 10, 5, 5, 3
xs = [2, 4, 5, 7, 8]
ys = [1, 2, 4]


xxs = [w]
yys = [h]

for i in range(len(xs)):
    xxs.append(xs[i])
    xxs.append(w - xs[i])
    if i != len(xs) - 1:
        for j in range(i + 1, len(xs)):
            xxs.append(abs(xs[i] - xs[j]))

for i in range(len(ys)):
    yys.append(ys[i])
    yys.append(h - ys[i])
    if i != len(ys) - 1:
        for j in range(i + 1, len(ys)):
            yys.append(abs(ys[i] - ys[j]))

count = 0
for x in xxs:
    count += yys.count(x)

print(count)
