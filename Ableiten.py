import sympy as sp


x = sp.Symbol('x')

# Zu ableitende Funktion
f = x**5 - 5 * x**4 - 30 * x**3 + 110 * x**2 + 29 * x - 105

result = sp.diff(f)

print(result)
