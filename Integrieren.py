from scipy.integrate import quad


def integrand(x):
    # Zu integrierende Funktion
    return x**2


untereGrenze = 0
obereGrenze = 1

result, error = quad(integrand, untereGrenze, obereGrenze)

print(result)
print(error)

