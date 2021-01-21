import numpy as np
import matplotlib.pyplot as plt


def horner(p, x):
    y = p[0] * np.ones(x.shape, dtype=np.float64)
    for k in range(1, p.size):
        y = y * x + p[k] * np.ones(x.shape, dtype=np.float64)
    return y


def polynomLoesenAbleitenIntegrieren(a, xmin, xmax):
    a = np.array(a, dtype=np.float64)
    x = np.arange(xmin, xmax, 0.01)
    p = horner(a, x)
    dp = derivative(a, x)
    pint = integral(a, x)
    return x, p, dp, pint


def derivative(a, x):
    adiff = a[0:-1] * np.arange(a.size - 1, 0, -1)
    ydiff = horner(adiff, x)
    return ydiff


def integral(a, x):
    aint = np.zeros(a.size + 1)
    aint[0:-1] = a / np.arange(a.size, 0, -1)
    yint = horner(aint, x)
    return yint


# 1x^5, -5x^4, -30x^3, 110x^2, 29x, -105 -> 1, -5, -30, 110, 29, -105
# --> HIER AN AUFGABE ANPASSEN
[x, p, dp, pint] = polynomLoesenAbleitenIntegrieren([1, -5, -30, 110, 29, -105], -10, 10)

plt.figure()
plt.plot(x, p, label="Polynom")
plt.plot(x, dp, label="Ableitung")
plt.plot(x, pint, label="Stammfunktion")
plt.ylim(-3000, 3000)
plt.grid()
plt.legend()
plt.show()