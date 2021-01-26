"""
Created on Tue Jan 26 2021

SEP HS21 Aufgabe 4

@author: David Mihajlovic
"""

# a) separat

# b)

import numpy as np


def Fast_LR(A):
    m, n = A.shape
    L = np.eye(m)
    R = A.astype('float')

    for k in range(n - 1):
        L[k + 1:, k] = R[k + 1:, k] / R[k, k]
        R[k + 1:, k:] = R[k + 1:, k:] - np.outer(L[k + 1:, k], R[k, k:])
    print("\nL:")
    print(L)
    print("\nR:")
    print(R)
    return L, R

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


n = 9
A = np.array([[1, 1, 1],
             [2, (2+2**-52), 5],
             [4, 6, 8]])
b = np.array([1, 0, 0], dtype=np.float)

L, R = Fast_LR(A)
A = np.dot(L, R)
print("\nA:")
print(A)

y = solveL(L, b)
x = solveR(R, y)


print("\n", max(abs(A @ x - b)))

# c)

L = np.linalg.solve(A, b)
print(L)
