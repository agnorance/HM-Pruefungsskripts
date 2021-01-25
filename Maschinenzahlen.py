import numpy as np
import struct


# Function returns octal representation
def float_bin(number, places=3):
    # split() seperates whole number and decimal
    # part and stores it in two seperate variables
    whole, dec = str(number).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    dec = int(dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
        # Multiply the decimal value by 2
        # and seperate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        # Convert the decimal part
        # to integer again
        dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res


# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


###################################
# Berechnung Maschinengenauigkeit #
###################################
print("\n###############################\nBerechnung Maschinengenauigkeit\n###############################\n")
print("eps = B/2 * B**-n")

# Dezimalarithmetik
n = 16  # Stellen
B = 10  # Basis
eps_dezimal = B / 2 * B ** -n
print("eps_dez:", eps_dezimal)

# Binärarithmetik
n = 52  # Stellen
B = 2  # Basis
eps_bin = B / 2 * B ** -n
print("eps_bin:", eps_bin)

# Hexadezimalarithmetik
n = 14  # Stellen
B = 16  # Basis
eps_hexa = B / 2 * B ** -n
print("eps_hexa:", eps_hexa)

# Vergleich Dezimal und Binär
if eps_dezimal < eps_bin:
    print("Die Rechenmaschine mit Dezimalarithmetik rechnet genauer da eps_dez < eps_bin.")
elif eps_dezimal > eps_bin:
    print("Die Rechenmaschine mit Binärarithmetik rechnet genauer da eps_bin < eps_dez.")
else:
    print("Beide Maschinen scheinen gleich genau zu rechnen.")

# Vergleich Dezimal und Hexa
if eps_dezimal < eps_hexa:
    print("Die Rechenmaschine mit Dezimalarithmetik rechnet genauer da eps_dez < eps_hexa.")
elif eps_dezimal > eps_hexa:
    print("Die Rechenmaschine mit Hexadezimalarithmetik rechnet genauer da eps_hexa < eps_dez.")
else:
    print("Beide Maschinen scheinen gleich genau zu rechnen.")

# Vergleich Hexa und Binär
if eps_hexa < eps_bin:
    print("Die Rechenmaschine mit Hexadezimalarithmetik rechnet genauer da eps_hexa < eps_bin.")
elif eps_hexa > eps_bin:
    print("Die Rechenmaschine mit Binärarithmetik rechnet genauer da eps_bin < eps_hexa.")
else:
    print("Beide Maschinen scheinen gleich genau zu rechnen.")

###########################
# Zu Maschinenzahl runden #
###########################
print("\n#######################\nZu Maschinenzahl runden\n#######################\n")

x = np.sqrt(3)  # Input
print("Eingegebene Zahl:", x)
print("Binäre Darstellung:", float_bin(x, places=15), "* 2^0 -> muss normalisiert werden")

###########################
# Anzahl Maschinenzahlen berechnen #
###########################
print("\n#######################\nAnzahl verschiedener Maschinenzahlen berechnen\n#######################\n")

# x-stellige Gleitpunktzahlen
x = 15
# y-stellige Expontenten
y = 5

# Möglichkeiten für x-stellige Mantisse im Dualsystem
xPossibilities = 2 ** x

# Möglichkeiten für y-stellige Exponenten im Dualsystem
yPossibilities = 2 ** (y + 1)  # + 1 mit Vorzeichen

print("\nPossibilites:")
print(xPossibilities * (yPossibilities - 1) + 1)  # + 1 wegen 0

###########################
# Serie 3 Aufgabe 1 #
###########################
print("\n#######################\nSerie 3 Aufgabe 1\n#######################\n")

# Dezimalarithmetik
n = 10  # Stellen
B = 10  # Basis
eps_dezimal = B / 2 * B ** -n
print("eps_dez:", eps_dezimal)
x = float(str(eps_dezimal)[:-4]) - 1
x = x * 0.1
print(x)
berechenbar = 1. + eps_dezimal
nicht_berechenbar = 1. + (x * 10 ** (-n - 1))
print(berechenbar)
print('{0:.10f}'.format(nicht_berechenbar))


