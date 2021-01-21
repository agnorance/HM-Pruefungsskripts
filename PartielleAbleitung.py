from sympy import Symbol, Derivative


x = Symbol('x')
y = Symbol('y')

# An Aufgabe anpassen:
function = x ** 2 * y ** 3 + 12 * y ** 4

# Benötigen wir x oder y?
partialDerivativeX = Derivative(function, x)
partialDerivativeY = Derivative(function, y)

# Resultat
print(partialDerivativeX.doit())
print(partialDerivativeY.doit())
