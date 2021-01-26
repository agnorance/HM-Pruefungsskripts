import numpy as np


# LR Zerlegung (ohne Zeilentausch) mit einer for-Schleife
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


A = np.array(np.mat("1 1 1; "
                    "2 2 5;"
                    "4 6 8"), dtype=np.float)

L, R = Fast_LR(A)
print("\nA:")
print(np.dot(L, R))
