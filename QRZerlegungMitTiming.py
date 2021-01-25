import numpy as np
import math
import timeit


def Serie8_Aufg2(A):
    import numpy as np
    import math

    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')  # change to float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A
    H = np.copy(R)
    for j in np.arange(0, n):
        a = np.copy(H[:, 0]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = sig * length_a * e + a
        u = np.identity(n)
        u[j:, j:] = u[j:, j:] - (
                    2 * np.matmul(v, np.transpose(v)) / (np.matmul(np.transpose(v), v)))  # more elegant solution?
        R = np.matmul(u, R)
        Q = np.matmul(Q, u)
        H = R[j + 1:, j + 1:]
        print(Q, "\n\n", R, "\n\n")

    return (Q, R)


A = np.array([[1, 2, -1],
              [4, -2, 6],
              [3, 1, 0]])
[Q, R] = Serie8_Aufg2(A)

# Teil B
print("Q = \n", Q)
print("R = \n", R)

# A = np.matmul(Q, R) # A = Q * R
# I = np.matmul(np.transpose(Q), Q) # Q muss orthogonal sein: Q^T * Q = I
# print("A = \n", A)
# print("I = \n", I)
# print()
# #
# # # Teil C
# t1 = timeit.repeat("Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100)
# t2 = timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
# avg_t1 = np.average(t1)/100
# avg_t2 = np.average(t2)/100
# #
# print("Average t1:", avg_t1)
# print("Average t2:", avg_t2)
# factor = round(avg_t1/avg_t2, 4)
# print("np.linalg.qr(A) is", factor, "times faster!")
# print()
# #
# print("Timing test with big random A:")
# A = np.random.rand(100, 100)
# t1 = timeit.repeat("Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100)
# t2 = timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
# avg_t1 = np.average(t1)/100
# avg_t2 = np.average(t2)/100
# #
# print("Average t1:", avg_t1)
# print("Average t2:", avg_t2)
# factor = round(avg_t1/avg_t2, 4)
# print("np.linalg.qr(A) is", factor, "times faster!")
# print()
#
# # Die Laufzeit von np.linalg.qr(A) ist offensichlich besser als die eigene Implementation, da es für grössere Matrizen besser skaliert.