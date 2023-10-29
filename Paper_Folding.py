R, L, U, D = 1, 1, 1, 1
moves = "DRULUR"
v = "L"


def _R(R, L, U, D, move):
    if move in ["R", "L"]:
        if move == "R":
            L, R = L + R, 1
        else:
            R, L = R + L, 1
        U, D = U * 2, D * 2
    else:
        if move == "U":
            D, U = D + U, 1
        else:
            U, D = U + D, 1
        R, L = R * 2, L * 2
    return R, L, U, D


for i in moves:
    R, L, U, D = _R(R, L, U, D, move=i)

print(globals().get(v))

