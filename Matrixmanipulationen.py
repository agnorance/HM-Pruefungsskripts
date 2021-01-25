import numpy as np

A = np.array([[10 ** -5, 10 ** -5],
              [2, 3]])

A_tilde = np.array([[10 ** -5 - 10 ** -6, 10 ** -5 - 10 ** -6],
                    [2 - 10 ** -6, 3 - 10 ** -6]])

b = np.array([[0],
              [1]])

b_tilde = np.array([[10 ** -5],
                    [1]])

x = np.array([[2],
              [-1]])

A_inv = np.linalg.inv(A)

print("Eingegebene Matrix:")
print(A, "\n")
print("Inverse:")
print(A_inv, "\n")
print("--- Normen von A ---")
print("1-Norm, Spaltensummennorm:", np.linalg.norm(A, 1))
print("2-Norm, Spektralnorm:", np.linalg.norm(A, 2))
print("inf-Norm, Zeilensummennorm:", np.linalg.norm(A, np.inf))
print("\n--- Normen von A_inv ---")
print("1-Norm, Spaltensummennorm:", np.linalg.norm(A_inv, 1))
print("2-Norm, Spektralnorm:", np.linalg.norm(A_inv, 2))
print("inf-Norm, Zeilensummennorm:", np.linalg.norm(A_inv, np.inf))
print("\n--- Kondition einer Matrix A ---")
print("1-Norm: cond(A) =", np.linalg.norm(A, 1) * np.linalg.norm(A_inv, 1))
print("2-Norm: cond(A) =", np.linalg.norm(A, 2) * np.linalg.norm(A_inv, 2))
print("inf-Norm: cond(A) =", np.linalg.norm(A, np.inf) * np.linalg.norm(A_inv, np.inf))
print("\n--- Abschätzung für fehlerbehaftete Vektoren (Seite 62) ---")
print("1-Norm:")
print("Absoluter Fehler: ||x - x_tilde|| <= ||A_inv|| * ||b - b_tilde|| =",
      np.linalg.norm(A_inv, 1) * np.linalg.norm(b - b_tilde, 1))
print("Relativer Fehler: ||x - x_tilde||/||x|| <= ||A|| * ||A_inv|| * ||b-b_tilde||/||b|| =",
      np.linalg.norm(A, 1) * np.linalg.norm(A_inv, 1) * (np.linalg.norm(b - b_tilde, 1) / np.linalg.norm(b, 1)))
print("2-Norm:")
print("Absoluter Fehler: ||x - x_tilde|| <= ||A_inv|| * ||b - b_tilde|| =",
      np.linalg.norm(A_inv, 2) * np.linalg.norm(b - b_tilde, 2))
print("Relativer Fehler: ||x - x_tilde||/||x|| <= ||A|| * ||A_inv|| * ||b-b_tilde||/||b|| =",
      np.linalg.norm(A, 2) * np.linalg.norm(A_inv, 2) * (np.linalg.norm(b - b_tilde, 2) / np.linalg.norm(b, 2)))
print("inf-Norm:")
print("Absoluter Fehler: ||x - x_tilde|| <= ||A_inv|| * ||b - b_tilde|| =",
      np.linalg.norm(A_inv, np.inf) * np.linalg.norm(b - b_tilde, np.inf))
print("Relativer Fehler: ||x - x_tilde||/||x|| <= ||A|| * ||A_inv|| * ||b-b_tilde||/||b|| =",
      np.linalg.norm(A, np.inf) * np.linalg.norm(A_inv, np.inf) * (
                  np.linalg.norm(b - b_tilde, np.inf) / np.linalg.norm(b, np.inf)))
print("\n--- x = A\\b berechnen ---")
print(np.linalg.lstsq(A, b_tilde, rcond=None)[0])

# print(np.linalg.norm(A_inv, np.inf))
#
# print(np.linalg.norm(A, np.inf)*np.linalg.norm(A_inv, np.inf))
#
# print(np.linalg.norm(B, np.inf))
#
# print(np.linalg.norm(C, np.inf))
#
# print(np.linalg.norm(B, np.inf)/np.linalg.norm(C, np.inf))
#
# print(np.linalg.norm(A_inv, np.inf) * np.linalg.norm(B, np.inf))
#
# print(np.linalg.norm(A, np.inf)*np.linalg.norm(A_inv, np.inf)*(np.linalg.norm(B, np.inf)/np.linalg.norm(C, np.inf)))
#
# print(np.linalg.norm(A-A_tilde, np.inf)/np.linalg.norm(A, np.inf))
#
# print(np.linalg.norm(A, np.inf)*np.linalg.norm(A_inv, np.inf) * np.linalg.norm(A-A_tilde, np.inf)/np.linalg.norm(A,
# np.inf))
#
# x = np.linalg.solve(A_tilde, C)
# print(x)
