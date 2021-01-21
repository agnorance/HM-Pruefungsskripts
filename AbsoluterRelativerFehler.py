x = float(input())
xSchlange = float(input())


absoluterFehler = abs(x - xSchlange)
relativerFehler = abs(absoluterFehler/abs(x))

print("Absoluter Fehler:")
print(absoluterFehler)
print("Relativer Fehler:")
print(relativerFehler)
