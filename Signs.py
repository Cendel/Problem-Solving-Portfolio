command = ["left", "3", "11", "7", "7", "3"]

command2 = ["right", "3", "9", "8", "6", "2"]

direction = command[0]

amount, height, thickness, spacing, indent = [int(i) for i in command[1:6]]


if direction == "right":
    template = f"{('>'*thickness+' '*spacing)*amount}".rstrip()
    for i in range(height // 2 + 1):
        print(" " * i * indent + template, end="")
        print()
    for i in range(height // 2):
        print(" " * (indent * (height // 2 - i - 1)) + template, end="")
        print()
else:
    template = f"{('<'*thickness+' '*spacing)*amount}".rstrip()
    for i in range(height // 2 + 1):
        print(" " * (height//2 -i) * indent + template, end="")
        print()
    for i in range(height // 2):
        print(" " * (i+1) * indent + template, end="")
        print()
