import numpy as np  # import biblioteki do obliczeń naukowych
from random import randint

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
        print("x:", wspolrzednaX,"y:", wspolrzednaY)
        osOdcietych.append(wspolrzednaX)
        osRzednych.append(wspolrzednaY)
        
    #obliczam wektor koncowego przesuniecia
    wektorPrzesuniecia = np.fabs(np.sqrt(wspolrzednaX**2 + wspolrzednaY**2))
    print("Wektor przesuniecia: {:.2f}".format(wektorPrzesuniecia))
    
ruchyBrowna()