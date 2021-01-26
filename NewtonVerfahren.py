import numpy as np


# a)
def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
        # print(xn) uncomment to see iterations
    print('Exceeded maximum iterations. No solution found.')
    return None


# Funktion
def f(x):
    return -np.exp(x) + np.sqrt(x) + 2.


# Ableitung
def Df(x):
    return (1 / 2 * np.sqrt(x)) - np.exp(x)


print(newton(f, Df, 0.5, 10e-7, 10))
