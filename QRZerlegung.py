import numpy as np


def QR(A):
    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')  # change to float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)  # orthogonal
    R = A

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:n, j]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * abs(length_a) * e
        u = (1 / abs(np.linalg.norm(v))) * v
        I = np.eye(n - j, n - j)
        H = I - (2 * u.dot(np.transpose(u)))
        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = Qi.dot(R)
        Q = Q.dot(np.transpose(Qi))

    return Q, R  # A = QR


# HIER MATRIX ANPASSEN
A = np.array(np.mat("1 -2 3; "
                    "-5 4 1; "
                    "2 -1 3"), dtype=np.float64)
Test = np.random.rand(100, 100)
Z, Y = (QR(A))
print("\nAufgabe 2 b)")
print("\nQ Matrix: ")
print(Z)
print("\nR Matrix: ")
print(Y)
print("\nDie Berechnung von Q * R ergibt wieder die ursprüngliche Matrix: ")
print(Z.dot(Y))
