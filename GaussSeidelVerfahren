import numpy as np


def JacobiOderGaussSeidel(A, b, x_0, tolarance, opt):
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    R = np.triu(A, 1)
    x = [x_0]
    n = 0

    if opt == 'Jacobi_Method':
        while True:
            x_n_new = -np.linalg.inv(D) @ ((L + R) @ x[n] - b)
            n += 1
            if np.linalg.norm(x_n_new - x[n-1], np.inf) < tolarance:
                B = -np.linalg.inv(D) @ (L + R)
                n2 = priori(B, x[1], x[0], tolarance)
                return x_n_new, n, n2
            x.append(x_n_new)
    elif opt == 'GaussSeidel':
        while True:
            x_n_new = -np.linalg.inv(D + L) @ R @ x[n] + np.linalg.inv(
                D + L) @ b
            n += 1
            if np.linalg.norm(x_n_new - x[n-1], np.inf) < tolarance:
                B = -np.linalg.inv(D + L) @ R
                n2 = priori(B, x[1], x[0], tolarance)
                return x_n_new, n, n2
            x.append(x_n_new)


def priori(B, x_1, x_0, tolarance):
    B_norm = np.linalg.norm(B, np.inf)
    return np.log(
        tolarance * (1 - B_norm) / np.linalg.norm(
            x_1 - x_0, np.inf)) / np.log(B_norm)


if __name__ == "__main__":
    A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
    b = np.array([[19], [5], [34]])
    x_0 = np.array([[1], [-1], [3]])
    '''
    A = np.array([[15, 0, 1], [1, 3, 7], [0, 1, 6]])
    y = np.array([[21, 67, 44]]).T
    '''
    tolarance = 10 ** -4
    # opt = 'Jacobi_Method'
    opt = 'GaussSeidel'

    [iterationsvektor, iterationen, aPriori] = JacobiOderGaussSeidel(A, b, x_0, tolarance, opt)
    print("Iterationsvektor:")
    print(iterationsvektor)
    print("\nIterationen:")
    print(iterationen)
    print("\nA-Priori Schätzung:")
    print(aPriori)
