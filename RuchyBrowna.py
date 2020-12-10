import numpy as np
import matplotlib.pyplot as plt
from random import randint


# def zapisz_dane:

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
        print("x:", wspolrzednaX, "y:", wspolrzednaY)
        osOdcietych.append(wspolrzednaX)
        osRzednych.append(wspolrzednaY)

    # obliczam wektor koncowego przesuniecia
    wektorPrzesuniecia = np.fabs(np.sqrt(wspolrzednaX ** 2 + wspolrzednaY ** 2))
    print("Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia))

    wykres(osOdcietych, osRzednych, wspolrzednaX, wspolrzednaY, wektorPrzesuniecia)


def wczytajRuchyBrownaZPliku():
    nazwaPliku = input("Wpisz nazwe pliku z ktorego chcesz wczytac dane: ")

    osOdcietychNowa = [0]
    osRzednychNowa = [0]

    try:
        plik = open(nazwaPliku, 'r')
        fileLines = []
        line = plik.readline()
        while line != "":
            line = line.replace("\n", "")
            fileLines.append(line)
            line = plik.readline()
    except FileNotFoundError:
        print("Plik nie istnieje")

    i = 0
    while i < 9:
        osOdcietychNowa.append(float(fileLines[i]))
        i = i + 1
        osRzednychNowa.append(float(fileLines[i]))

    nowaWspolrzednaX = float(fileLines[8])
    nowaWspolrzednaY = float(fileLines[9])
    nowyWektorPrzesuniecia = np.fabs(np.sqrt(pow(float(nowaWspolrzednaX), 2) + pow(float(nowaWspolrzednaY), 2)))
    print("Wektor przesuniecia: {:.2f}".format(nowyWektorPrzesuniecia))
    plik.close()
    wykres(osOdcietychNowa, osRzednychNowa, float(nowaWspolrzednaX), float(nowaWspolrzednaY), nowyWektorPrzesuniecia)


def menu():
    print("Witaj w programie ktory symuluje Ruchy Browna\n\n")
    print("-------------------MENU------------------------")
    print("1. Symulacja Ruchow Browna")
    print("2. Symulacja Ruchow Browna z danymi przygotowanymi w pliku")
    print("9. Koniec Programu")
    wybor = int(input("Wybierz opcje z menu "))
    if (wybor == 1):
        ruchyBrowna()
    elif (wybor == 2):
        wczytajRuchyBrownaZPliku()
    elif (wybor == 9):
        exit(0)
    else:
        print("Przypominam ze numer mial byc 1 2 lub 9")


menu()