lst = [
    ["A"],
    [
        "C",
        "B",
        "A",
        "C",
        "B",
        "A",
        "C",
        "B",
        "A",
        "C",
        "B",
        "A",
        "C",
        "B",
        "A",
        "C",
        "B",
        "A",
    ],
    ["C", "C", "C", "C", "C", "B", "B", "B", "B", "B", "A", "A", "A", "A", "A"],
    ["B", "D", "N", "I", "D", "P", "D"],
    ["C", "O", "D", "I", "N", "G", "A", "M", "E"],
]


lst = [[ord(i) for i in j] for j in lst]
for i in lst:
    print(i)

for i in lst:
    sort = [i[0]]
    for j in range(1, len(i)):
        if i[j] in sort:
            continue
        control_lst = [0, 0]
        check = False
        for k in sort:
            if i[j] < k and (k - i[j]) < k - control_lst[0]:
                check = True
                control_lst[0] = k
                control_lst[1] = sort.index(k)
        if check:
            sort[control_lst[1]] = i[j]
        else:
            sort.append(i[j])
    print(len(sort))
