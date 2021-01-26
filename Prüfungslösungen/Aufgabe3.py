"""
Created on Tue Jan 26 2021

SEP HS21 Aufgabe 3

@author: David Mihajlovic
"""

import numpy as np
import matplotlib.pyplot as plt


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


print("\nSchnittpunkt:")
print(newton(f, Df, 0.5, 10e-7, 10))


# b)
# Aufgabe b)
def fixpunkt(x):
    k = 0.1
    F = lambda x: np.log(np.sqrt(x) + 2)
    y = np.array([])
    for j in range(100):
        y = np.append(y, k)
        k = F(k)  # y-Werte, Fixpunktgleichung: k = a * k * (1-k)
    print(y)
    return y


def main():
    k = np.arange(0.5, 1.5, pow(10, -7))  # x-Werte
    for currentAlpha in k:  # abstossende/anziehende Liste hier ändern
        y = fixpunkt(currentAlpha)
        plt.title('x: ' + str(currentAlpha))
        plt.xlabel('x-Werte')
        plt.ylabel('y-Werte der Iterationsformel')
        plt.plot(y)
        plt.grid()
        plt.show()


if __name__ == "__main__":
    main()

xL = 0.5
xR = 1.5

fx = f(np.array([xL, xR]))
fxMin = np.min(fx)
fxMax = np.max(fx)
dfx = Df(np.array([xL, xR]))
lambd = np.max(np.abs(dfx))

print("\nVoraussetzungen Banascher Fixpunkt:")
print(lambd < 1)
print(fxMin > xL)
print(fxMax < xR)
print("Lipschitz: ")
print(lambd)
