'''
author: DM
'''

import sympy as sp


x = sp.Symbol('x')

# Zu ableitende Funktion
f = 230 * x ** 4 + 18 * x ** 3 + 9 * x ** 2 - 221 * x -9

result = sp.diff(f)

print(result)
