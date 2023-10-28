n = 8
players = [
    ["28", "R", []],
    ["3", "R", []],
    ["13", "L", []],
    ["6", "P", []],
    ["32", "C", []],
    ["5", "R", []],
    ["11", "S", []],
    ["27", "S", []],
    ["22", "L", []],
    ["31", "R", []],
    ["30", "R", []],
    ["10", "P", []],
    ["18", "R", []],
    ["23", "R", []],
    ["8", "R", []],
    ["20", "S", []],
    ["7", "P", []],
    ["19", "P", []],
    ["26", "P", []],
    ["4", "R", []],
    ["16", "C", []],
    ["21", "P", []],
    ["1", "C", []],
    ["14", "C", []],
    ["29", "R", []],
    ["9", "P", []],
    ["25", "C", []],
    ["24", "P", []],
    ["15", "R", []],
    ["2", "L", []],
    ["12", "L", []],
    ["17", "S", []],
]


def contest(first, second):
    if first == second:
        return "Tie"
    elif first == "C":
        return "C" if second in ["P", "L"] else second
    elif first == "P":
        return "P" if second in ["R", "S"] else second
    elif first == "R":
        return "R" if second in ["L", "C"] else second
    elif first == "L":
        return "L" if second in ["S", "P"] else second
    elif first == "S":
        return "S" if second in ["C", "R"] else second


while len(players) > 1:
    losers = []
    for i in range(0, len(players), 2):
        p1 = players[i]
        p2 = players[i + 1]
        loser = ""
        if contest(p1[1], p2[1]) == "Tie":
            loser = p2 if int(p1[0]) < int(p2[0]) else p1
        else:
            loser = p2 if contest(p1[1], p2[1]) == p1[1] else p1
        losers.append(loser)
        p1[2].append(p2[0]) if loser == p2 else p2[2].append(p1[0])
    for p in losers:
        players.remove(p)

print(players[0][0])
print(" ".join(players[0][2]))
