import numpy as np
import matplotlib.pyplot as plt


def fixpunkt(alpha):
    print('Alpha:', alpha)
    k = 0.1
    F = lambda x: alpha * x * (1 - x)
    y = np.array([])
    for j in range(100):
        y = np.append(y, k)
        k = F(k)  # y-Werte, Fixpunktgleichung: k = a * k * (1-k)
    print(y)
    return y


def main():
    anziehendeListe = np.arange(0.25, 3.25, 0.25)
    abstossendeListe = np.arange(0.25, 4.25, 0.25)
    k = np.arange(0.00, 4.00, pow(10, -2))  # x-Werte
    for currentAlpha in abstossendeListe:  # abstossende/anziehende Liste hier ändern
        y = fixpunkt(currentAlpha)
        plt.title('Alpha: ' + str(currentAlpha))
        plt.xlabel('alpha-Werte')
        plt.ylabel('y-Werte der Iterationsformel')
        plt.plot(y)
        plt.grid()
        plt.show()


if __name__ == "__main__":
    main()

    # a) a anziehend: 0.25
    # a abstossend: 3.25

    # b) Der Fixpunkt ist der Schnittpunkt der Geraden F(x) = x mit der Fixpunktgleichung. Das heisst an dieser Stelle
    # sind die Anzahl Neuerkrankte gleich der Anzahl Genesener. Die Anzahl Kranke bleibt somit nach einiger Zeit
    # für a > 1 konstant.

    # c)
    # Weil der Fixpunkt k immer gleich bleibt, gilt: k(i) = k(i+1) = k
    # Somit: 1/(1-k) = alpha
    # Oder: 1-/1/(alpha) = k
    #  a ≤ 1 die Krankheit verschwindet
    #  a > 1 die Krankheit existiert vorwährend
