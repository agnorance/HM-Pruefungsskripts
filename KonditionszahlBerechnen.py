import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import linalg


# Funktion definieren
def f(x): return (x ** 2) * np.sin(x)


# Ableitung definieren
def df(x): return (2 * x * np.sin(x)) + (x ** 2 * np.cos(x))


# Konditionszahl berechnen und als Funktion returnen
def K(x): return np.abs(x) * np.abs(df(x)) / np.abs(f(x))


# Range und Schrittweite von x...
x = np.arange(-4,2.05,0.05)
# oder für bestimmtes x
# x = 1

# K = abs(x + 1)
L = K(x)
print(L)
plt.plot(x, K(x), '-'), plt.xlabel('x'), plt.ylabel('K(x)')
plt.show()
# b)
"""
Gut konditioniertes Problem fuer K <= 1        

Forderung: |x+1| <= 1    

Fuer x > -1: 
  Forderung: 1 + x <= 1 
    => x <= 0                                  2P
Fuer x < -1:
  Forderung: -(1+x) <= 1
    => -1-x <= 1
    => -x <= 2
    => x >= -2                                 2P

Gute Konditionierung fuer -2 <= x <= 0         1P

"""

A = np.array([[240, 120, 80],
              [60, 180, 170],
              [60, 90, 500]])
b = np.array([[3080],
              [4070],
              [5030]])
Ainv = np.linalg.inv(A)
Ainv = sp.linalg.norm(Ainv)
Anorm = sp.linalg.norm(A)
k = A * Ainv
print(k)


"""
d) cond(A) = ||A||*|| A^-1 || = 7.3512

"""
