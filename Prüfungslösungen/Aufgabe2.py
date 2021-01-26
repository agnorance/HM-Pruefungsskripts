"""
Created on Tue Jan 26 2021

SEP HS21 Aufgabe 2

@author: David Mihajlovic
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import linalg


# a)


# Funktion definieren
def f(x): return (x ** 2) * np.sin(x)


# Ableitung definieren
def df(x): return (2 * x * np.sin(x)) + (x ** 2 * np.cos(x))


# Konditionszahl berechnen und als Funktion returnen
def Z(x): return np.abs(x) * np.abs(df(x)) / np.abs(f(x))


x = 1

K = abs(x + 1)
print(K)

# b)

# c)
xNull = 0
K = abs(xNull + 1)
print(K)
# Das Problem ist für x ---> 0 gut konditioniert.

# d)
# Range und Schrittweite von x...
y = np.arange(-np.pi * 2, 3 * np.pi)

plt.plot(y, Z(y), '-'), plt.xlabel('y'), plt.ylabel('K(y)')
plt.semilogx()
plt.show()


