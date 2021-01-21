import numpy as np
import matplotlib.pyplot as plt


# Funktion definieren
def f(x): return x * np.exp(x)


# Ableitung definieren
def df(x): return np.exp(x) * (x + 1)


# Konditionszahl berechnen und als Funktion returnen
def K(x): return np.abs(x) * np.abs(df(x)) / np.abs(f(x))


# Range und Schrittweite von x...
x = np.arange(-4, 2.00, 1.00)
# oder für bestimmtes x
# x = 1

# K = abs(x + 1)
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
