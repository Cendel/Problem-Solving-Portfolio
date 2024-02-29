# Question: https://www.codingame.com/ide/puzzle/rational-number-tree

# Completed!


lines = ["4317/6106",
         "763/2777",
         "2161/4405",
         "3769/2435",
         "1015/1109",
         "4989/5617",
         "53/36",
         "3553/3727",
         "2617/2241",
         "115/1002",
         "RLLLLRLRRRRRRRRRRRRRLRLRLLRR",
         "RLLLLLLLLRLLLLLLLLLLRLLLLLLLLLLLLLLLRRRR",
         "LRRRRLLLLLLLLLLLLLLRRLLLRLRRRRRR",
         "LRRRRRRRRRLLRRLLLLLLLRLLRRRRR",
         "LRLRLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRLRRRR",
         "LRLRRRLLRRLRRLLLLL",
         "LRRRRRRRRRRRRRRRRRLRRLLLLRRRLRRRRRR",
         "LRRRRRRLRLLLLRLLLLLLL",
         "LRRRRRRRRRRRRRRRRRRRLLRRLLLLLRRR",
         "LRRRLRLRLLRRRRRRLLLLLLLLL"]


def right_branch(list_a, list_b):
    return f"{int(list_a[0]) + int(list_b[1][0])}/{int(list_a[1]) + int(list_b[1][1])}"


def left_branch(list_a, list_b):
    return f"{int(list_a[0]) + int(list_b[0][0])}/{int(list_a[1]) + int(list_b[0][1])}"


for line in lines:

    parent = ["0/1", "1/0"]
    current = "1/1"

    if line[0] in "LR":
        for i in line:
            current_list = current.split("/")
            parent_list = [x.split("/") for x in parent]
            spare = current
            if i == "R":
                current = right_branch(current_list, parent_list)
                parent[0] = spare
            else:
                current = current = left_branch(current_list, parent_list)
                parent[1] = spare
        print(current)

    else:
        output = ""
        while current != line:
            current_list = current.split("/")
            parent_list = [x.split("/") for x in parent]
            spare = current

            if eval(line) > eval(current):
                output += "R"
                current = current = right_branch(current_list, parent_list)
                parent[0] = spare

            elif eval(line) < eval(current):
                output += "L"
                current = left_branch(current_list, parent_list)
                parent[1] = spare
        print(output)
