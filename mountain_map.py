# Question: https://www.codingame.com/training/easy/mountain-map

# Completed!

# n = int(input())  # the number of mountains
# m = [int(i) for i in input().split()] # height of each mountain

n = 7
m = [3, 9, 2, 4, 7]
base = [i*2 for i in m]
c = [0 for i in m]

for i in range(max(m)):
    output = ""
    for j in range(len(m)):
        if m[j] < max(m) - i:
            output += " " * base[j]
        else:
            output += " " * ((base[j] - 2-c[j])//2) + "/" + \
                " " * c[j] + "\\" + " " * ((base[j] - 2-c[j])//2)
            c[j] = c[j]+2
    print(output.rstrip())
