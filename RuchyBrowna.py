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
    tablicaWartosci = [0]

    for i in range(0, iloscRuchow):
        radian = float((randint(0, 360)) * np.pi / 180)
        wspolrzednaX = wspolrzednaX + krokPrzesuniecia * np.cos(radian)
        wspolrzednaY = wspolrzednaY + krokPrzesuniecia * np.sin(radian)
        wspolrzednaX = round(wspolrzednaX, 2)
        wspolrzednaY = round(wspolrzednaY, 2)
        osOdcietych.append(wspolrzednaX)
        tablicaWartosci.append(wspolrzednaX)
        osRzednych.append(wspolrzednaY)
        tablicaWartosci.append(wspolrzednaY)

    zapiszDaneDoPliku(tablicaWartosci, iloscRuchow)
    print(wspolrzednaX)
    print(wspolrzednaY)
    wektorPrzesuniecia = np.fabs(np.sqrt(wspolrzednaX ** 2 + wspolrzednaY ** 2))
    print("Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia))

    wykres(osOdcietych, osRzednych, wspolrzednaX, wspolrzednaY, wektorPrzesuniecia)


def zapiszDaneDoPliku(tablicaWartosci, iloscRuchow):
    try:
        plik = open('dane1.txt', 'w')
        for i in range(0, iloscRuchow * 2):
            plik.write(str(tablicaWartosci[i + 1]))
            plik.write('\n')
    except FileNotFoundError:
        print("Plik nie istnieje")
    else:
        plik.close()


def wczytajRuchyBrownaZPliku():
    nazwaPliku = input("Wpisz nazwe pliku z ktorego chcesz wczytac dane: ")

    osOdcietych = [0]
    osRzednych = [0]

    try:
        plik = open(nazwaPliku, 'r')
        liniaPliku = []
        linia = plik.readline()
        while linia != "":
            linia = linia.replace("\n", "")
            liniaPliku.append(linia)
            linia = plik.readline()
    except FileNotFoundError:
        print("Plik nie istnieje")
    else:
        i = 0
        while i < 9:
            osOdcietych.append(float(liniaPliku[i]))
            i = i + 1
            osRzednych.append(float(liniaPliku[i]))

        wspolrzednaX = float(liniaPliku[i - 1])
        wspolrzednaY = float(liniaPliku[i])
        wektorPrzesuniecia = np.fabs(np.sqrt(pow(float(wspolrzednaX), 2) + pow(float(wspolrzednaY), 2)))
        print("Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia))
        plik.close()
        wykres(osOdcietych, osRzednych, float(wspolrzednaX), float(wspolrzednaY), wektorPrzesuniecia)


def menu():
    print("Witaj w programie ktory symuluje Ruchy Browna")
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
        print("Przypominam ze numer mial byc 1, 2 lub 9")


menu()