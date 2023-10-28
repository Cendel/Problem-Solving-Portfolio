import math
def creating_gen(index):
    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]
    yield months[index]
    yield months[index + 2]


next_month = creating_gen(0)
print(next(next_month), next(next_month))

ada = [[1, 2, 3], [4, 5, 6]]

a, b = 4, 3

directions = [
    (a + x, b + y)
    for x in range(-1, 2)
    for y in range(-1, 2)
    if (0 <= a + x < 5) and (0 <= b + y < 5) and (x, y) != (0, 0)
]

print(directions)

a = "23727372"
a = sorted(a)
print(a)

print(list(a).reverse())

b = [1,2,3]
c = reversed(b)
print([x for x in c])

s=[ord(i)-65 for i in "ADALARDA"]
print(sum(filter(lambda i:not i%2,s))-sum(filter(lambda i:i%2,s)))

print (math.gcd(3, 6))

lst = "abcd"
print(lst)
print(*lst)
lst = ["a", "b", "c", "d"]
print(*lst)

print(math.ceil(1.23))


a = "jasdASDfC.a.fa-df-aijSADFA!"

print(a.swapcase())

print(23//3)
