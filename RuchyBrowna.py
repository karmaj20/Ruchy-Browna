import numpy as np
import matplotlib.pyplot as plt
from random import randint


def wykres(osOdcietych, osRzednych, wspolrzednaX, wspolrzednaY, wektorPrzesuniecia):
    poczatekUkladuX = 0
    poczatekUkladuY = 0

    for punkt in osOdcietych:
        connection_x = [poczatekUkladuX, wspolrzednaX]
        connection_y = [poczatekUkladuY, wspolrzednaY]

    line1 = plt.plot(osOdcietych, osRzednych, "o:")
    line2 = plt.plot(connection_x, connection_y, 'b')
    plt.setp(line1, color='g', linewidth=2, alpha=0.5)
    plt.legend(["Dane :\nRuch czasteczki",
                "Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia)], loc="upper left")
    plt.xlabel("os X")
    plt.ylabel("os Y ")
    plt.title("Ruchy Browna")
    plt.grid(True)
    plt.show()


def ruchyBrowna():
    iloscRuchow = int(input("Ile ruchow?: "))
    krokPrzesuniecia = int(input("Podaj krok przesuniecia: "))

    wspolrzednaX = 0
    wspolrzednaY = 0

    osOdcietych = [0]
    osRzednych = [0]

    for i in range(0, iloscRuchow):
        radian = float((randint(0, 360)) * np.pi / 180)
        wspolrzednaX = wspolrzednaX + krokPrzesuniecia * np.cos(radian)
        wspolrzednaY = wspolrzednaY + krokPrzesuniecia * np.sin(radian)
        wspolrzednaX = round(wspolrzednaX, 2)
        wspolrzednaY = round(wspolrzednaY, 2)
        osOdcietych.append(wspolrzednaX)
        osRzednych.append(wspolrzednaY)

    # obliczam wektor koncowego przesuniecia
    wektorPrzesuniecia = np.fabs(np.sqrt(wspolrzednaX ** 2 + wspolrzednaY ** 2))
    print("Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia))

    wykres(osOdcietych, osRzednych, wspolrzednaX, wspolrzednaY, wektorPrzesuniecia)


ruchyBrowna()