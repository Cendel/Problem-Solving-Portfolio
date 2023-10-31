instructions = ['fg4', 'ls11', 'oe7']
#instructions = ['ft17', 'PLANTft9', 'nf17', 'PLANTnf9', 'PLANTjm5']
columns = {}
for char in range(ord("a"), ord("s")+1):
    columns.update({chr(char): (char - ord("a"))*2})
rows = {}
for char in range(ord("a"), ord("y")+1):
    rows.update({chr(char): (char - ord("a"))})
grid = [["{" if x%2==0 else "}" for x in range(38)] for i in range(25)]


print(instructions)


for i in instructions:
    do, c, r, d = "MOW", 0, 0, 0
    if i.startswith("PLANTMOW"):
        do, c, r, d = "reverse", i[8:9], i[9:10], int(i[10::])
    elif i.startswith("PLANT"):
        do, c, r, d = "PLANT", i[5:6], i[6:7], int(i[7::])
    else:
        do, c, r, d = "MOW", i[0:1], i[1:2], int(i[2::])
    a = d//2 if (d-d//2)%2==0 else (d//2)+1
    b= a//2
    for j in range(a):
        for y in range(columns[c]-(d//2*2),columns[c]+(d//2*2)+1,2) :
            if columns["a"] <= y <= columns["s"] and rows[r]+j-b <=rows["y"]:
                grid[rows[r]+j-b][y] = " " if do=="MOW" else "{" if do=="PLANT"  else " " if do=="reverse" and grid[rows[r]-b-j][y] =="{" else "{"
                grid[rows[r]+j-b][y+1] = " " if do=="MOW" else "}" if do=="PLANT"  else " " if do=="reverse" and grid[rows[r]-b-j][y+1] == "}" else "}"

    z = (d-a)//2
    for j in range(1, z+1):
        for y in range(columns[c]-(d//2*2)+j*2,columns[c]+(d//2*2)-j*2+1,2):
            if columns["a"] <= y <= columns["s"] and rows[r]-b-j >= rows["a"] and rows[r] + b + j <= rows["y"] :
                grid[rows[r]-b-j][y] =  " " if do=="MOW" else "{" if do=="PLANT"  else " "  if do=="reverse" and grid[rows[r]-b-j][y] =="{"  else "{"
                grid[rows[r]-b-j][y+1] = " " if do == "MOW" else "}" if do == "PLANT" else " " if do=="reverse" and grid[rows[r] - b - j][y+1] == "}" else "}"
                grid[rows[r]+b+j][y] =  " " if do=="MOW" else "{" if do=="PLANT"  else " " if do=="reverse" and grid[rows[r] + b + j][y] =="{"  else "{"
                grid[rows[r]+b+j][y+1] = " " if do == "MOW" else "}" if do == "PLANT" else " " if do=="reverse" and grid[rows[r] + b + j][y+1] == "}" else "}"



for i in grid:
    print("".join(i))

print(11//2)

print(columns)
print(rows)
