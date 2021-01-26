import numpy as np
from LRZerlegung import Fast_LR


# Löse Rx = b
def solveR(R, b):
    n = len(b)
    x = np.zeros(n)

    x[-1] = b[-1] / R[-1, -1]
    for k in range(n - 2, -1, -1):
        x[k] = (b[k] - np.sum(R[k, k + 1:] * x[k + 1:])) / R[k, k]
    return x


# Löse Lx = b
def solveL(L, b):
    n = len(b)
    x = np.zeros(n)
    x[0] = b[0] / L[0, 0]
    for k in range(1, n):
        x[k] = (b[k] - np.sum(L[k, :k] * x[:k])) / L[k, k]
    return x


n = 3
A = np.array(np.mat("1 1 1; "
                    "2 2 5;"
                    "10 6 2"), dtype=np.float)
b = np.array([1, 0, 0], dtype=np.float)

L, R = Fast_LR(A)
A = np.dot(L, R)
print("\nA:")
print(A)

y = solveL(L, b)
x = solveR(R, y)


print("\n", max(abs(A @ x - b)))
