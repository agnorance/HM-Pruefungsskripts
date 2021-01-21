import numpy as np


def sekantenVerfahren(f, x0, x1, tol):
    x = [x0, x1]
    n = 1

    while True:
        x_m = x[n] - ((x[n] - x[n - 1]) / (f(x[n]) - f(x[n - 1]))) * f(x[n])
        if abs(x[n] - x_m) < tol:
            return x_m
        x.append(x_m)
        n += 1


# Funktionen
def f(x):
    return (np.e ** (x ** 2)) + (x ** -3) - 10


def g(x):
    return 4 * x + 5


# Startwerte
x0 = -1
x1 = -2

# Toleranz
tol = 10 ** -5

# Gewünschte Funktion anpassen (f oder g?)
print(sekantenVerfahren(f, x0, x1, tol))

# Wegen Auslöschung kann Newton-Verfahren nicht genauer ausgeführt werden?
