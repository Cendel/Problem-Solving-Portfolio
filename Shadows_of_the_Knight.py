import math
[w, h], low, left = [int(i) for i in input().split()], 0, 0
n = int(input())
x0, y0 = [int(i) for i in input().split()]

while True:
    bom = input()
    if "U" in bom:
        h = y0
        y0 = low+math.floor((h-low)/2)
    if "D" in bom:
        low = y0
        y0 = h-round((h-low)/2)
    if "L" in bom:
        w = x0
        x0 = left+math.floor((w-left)/2)
    if "R" in bom:
        left = x0
        x0 = w-round((w-left)/2)

    print(x0, y0)
