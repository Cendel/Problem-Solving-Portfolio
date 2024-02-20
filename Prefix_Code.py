# Question: https://www.codingame.com/training/easy/prefix-code

data = {
    "011": "32",
    "0011": "33",
    "0010": "114",
    "0001": "100",
    "0000": "101",
    "111": "87",
    "110": "72",
    "10": "108",
    "010": "111",
}

origin = "1100000101001001111101000101000010110011"
s = origin
output = ""


def roam(sss, outputt, foundd):
    for i in range(len(sss) - 1, 0, -1):
        print(sss[0:i])
        if sss[0:i] in data.keys():
            print(i)
            if len(sss) > 4:
                print(len(sss))
                outputt = outputt + chr(int(data[sss[0:i]]))
                sss = sss[i::]
            else:
                outputt = outputt + "!"

            foundd = True
            print(sss)
            print(outputt)
    return sss, outputt, foundd


while True:
    found = False
    s, output, found = roam(s, output, found)
    if len(s) == 0:
        print(s)
        print(output)
        break
    if not found:
        print(f"DECODE FAIL AT INDEX {origin.index(s)}")
        break
hh = []
for i in data.keys():
    hh.append(data[i])

print(output)
print(chr(int("32")))
print(len(s))
print(s)
