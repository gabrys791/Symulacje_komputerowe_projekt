import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import colors

DRZEWO = 0
PLONACE_DRZEWO = 1
SPALONE_DRZEWO = 2

plansza_pocz = np.zeros((10, 10), dtype=int)

x, y = np.random.randint(0, 10), np.random.randint(0, 10)
plansza_pocz[x][y] = PLONACE_DRZEWO

cmap = colors.ListedColormap(['green', 'orange', 'black'])

stara_plansza = plansza_pocz.copy()
nowa_plansza = np.zeros((10, 10), dtype=int)
wysokosc, szerokosc = stara_plansza.shape
szansa_na_podpalenie = 0.5

plt.ion()
fig, ax = plt.subplots()

symulacja_trwa = True
krok = 0

while symulacja_trwa:
    czy_jest_ogien = False

    for i in range(wysokosc):
        for j in range(szerokosc):

            liczba_plonacych_sasiadow = 0


            if i > 0:
                if j > 0 and stara_plansza[i - 1][j - 1] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1
                if stara_plansza[i - 1][j] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1
                if j < szerokosc - 1 and stara_plansza[i - 1][j + 1] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1

            if j < szerokosc - 1 and stara_plansza[i][j + 1] == PLONACE_DRZEWO:
                liczba_plonacych_sasiadow += 1
            if j > 0 and stara_plansza[i][j - 1] == PLONACE_DRZEWO:
                liczba_plonacych_sasiadow += 1

            if i < wysokosc - 1:
                if j < szerokosc - 1 and stara_plansza[i + 1][j + 1] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1
                if stara_plansza[i + 1][j] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1
                if j > 0 and stara_plansza[i + 1][j - 1] == PLONACE_DRZEWO:
                    liczba_plonacych_sasiadow += 1

            if stara_plansza[i][j] == PLONACE_DRZEWO:
                nowa_plansza[i][j] = SPALONE_DRZEWO
                czy_jest_ogien = True

            elif stara_plansza[i][j] == SPALONE_DRZEWO:
                nowa_plansza[i][j] = SPALONE_DRZEWO

            elif stara_plansza[i][j] == DRZEWO:
                if liczba_plonacych_sasiadow > 0:
                    if random.random() < szansa_na_podpalenie:
                        nowa_plansza[i][j] = PLONACE_DRZEWO
                        czy_jest_ogien = True  # Nowy ogień powstał
                    else:
                        nowa_plansza[i][j] = DRZEWO
                else:
                    nowa_plansza[i][j] = DRZEWO
            else:
                nowa_plansza[i][j] = stara_plansza[i][j]

    ax.clear()
    ax.imshow(nowa_plansza, cmap=cmap, vmin=0, vmax=2)
    ax.set_title(f"Krok symulacji: {krok}")

    plt.draw()
    plt.pause(0.5)
    if PLONACE_DRZEWO not in nowa_plansza:
        print("Koniec ognia!")
        symulacja_trwa = False

    stara_plansza = nowa_plansza.copy()
    krok += 1

plt.ioff()
plt.show()
