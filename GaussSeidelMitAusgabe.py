import numpy as np

# y = Ax
A = np.array([[15, 0, 1],
              [1, 3, 7],
              [0, 1, 6]])
y = np.array([[21,
               67,
               44]]).T

D = np.diag(np.diag(A))
print("D:")
print(D)
R = np.triu(A) - D
print("\nR:")
print(R)
L = np.tril(A) - D
print("\nL:")
print(L)

# Startvektor x0 = 0
x = np.array([[0, 0, 0]]).T

# Gauss-Seidel mit Ausgabe jeder Iteration
for k in np.arange(1, 7):
    x = -np.linalg.inv(D + L) @ R @ x + np.linalg.inv(D + L) @ y
    print("\nIteration: {}".format(k))
    print(x)

"""
Frage: Was ist der Vorteil eines iterativen Loesungsverfahrens wie Gauss-Seidel
gegenueber direkten Loesungsverfahren?

Bei grossen Gleichungssystemen ist der numerische Aufwand von exakten
Lösungsverfahren zu gross. Iterative Verfahren sind bei solchen
(insbesondere diagonal dominanten) Gleichungsystemen effizienter
"""
