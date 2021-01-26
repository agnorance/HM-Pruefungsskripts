"""
Created on Tue Jan 26 2021

SEP HS21 Aufgabe 1

@author: David Mihajlovic
"""

# a)
# Der grösste Exponent den man speichern kann ist 4.
#
# b)
# max = 0.11111 * 2 ** 3
# min = 0.10000 * 2 ** 0
#
# c)

# Binärarithmetik
n = 5  # Stellen
B = 2  # Basis
eps_bin = B / 2 * B ** -n
print("eps_bin:", eps_bin)

# Hexadezimalarithmetik
n = 2  # Stellen
B = 16  # Basis
eps_hexa = B / 2 * B ** -n
print("eps_hexa:", eps_hexa)

# Vergleich Hexa und Binär
if eps_hexa < eps_bin:
    print("Die Rechenmaschine mit Hexadezimalarithmetik rechnet genauer da eps_hexa < eps_bin.")
elif eps_hexa > eps_bin:
    print("Die Rechenmaschine mit Binärarithmetik rechnet genauer da eps_bin < eps_hexa.")
else:
    print("Beide Maschinen scheinen gleich genau zu rechnen.")

# Die Maschinen rechnen demnach genau gleich genau.

