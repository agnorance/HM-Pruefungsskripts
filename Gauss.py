import numpy as np


def main(A, b):
    arange(A, b)
    Triang = np.array(A)
    gauss(A, b)
    return Triang, b


def system(A, b):
    for x in range(len(A)):
        if A[x, x] != 1:
            b[x] /= A[x, x]
            A[x] /= A[x, x]


def calculate(A, b, x, y):
    diagonal = A[y, x] / A[x, x]
    b[y] = b[y] - diagonal * b[x]
    A[y] = A[y] - diagonal * A[x]


def arange(A, b):
    for x in range(len(A) - 1):
        swapping(A, b, x)
        for y in range(x + 1, len(A[0])):
            calculate(A, b, x, y)


def swapping(A, b, x):
    if A[x, x] == 0:
        for y in range(x + 1, len(A[0])):
            if A[y, x] == 0:
                raise Exception("Something's wrong, Neo.")
            elif y >= x + 1:
                A[[x, y]] = A[[y, x]]
                b[[x, y]] = b[[y, x]]
                break


def gauss(A, b):
    for i in reversed(range(1, len(A))):
        for j in reversed(range(0, i)):
            calculate(A, b, i, j)
    system(A, b)


# Flugzeugtyp A: 20 FC, 50 BC, 200 EC
# Flugzeugtyp B: 10 FC, 30 BC, 150 EC
# Flugzeugtyp C:  0 FC, 20 BC, 100 EC

# Blair's Extreme SS 240 S  60 M  60
# Mad Dog:        SS 120 S 180 M  90 A
# Dave's Gourmet: SS  80 S 170 M 500
# ----------------------------------
# Portionierung:    3080  4070  5030 b


A = np.array(np.mat("240 120 80; "
                    "60 180 170;"
                    "60 90 500"), dtype=np.float)
b = np.array([3080, 4070, 5030], dtype=np.float)

[Triangular, x] = main(A, b)

print(f"Triangular : \n"
      f"{Triangular}\n")
print(f"X is: {x}\n")


def timeNumpy():
    A = np.array(np.mat("240 120 80; "
                        "60 180 170;"
                        "60 90 500"), dtype=np.float)
    b = np.array([3080, 4070, 5030], dtype=np.float)
    print("Numpy:")
    print("X is: ", np.linalg.solve(A, b))


timeNumpy()
