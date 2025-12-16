import numpy as np
import random
plansza_pocz = np.random.choice([0, 1], size=(10, 10), p=[0.8, 0.2])
stara_plansza = plansza_pocz.copy()
nowa_plansza = np.zeros((10, 10), dtype=int)
wysokosc, szerokosc = stara_plansza.shape

szansa_na_podpalenie = 0.8
losuj = random.random()
for i in range(wysokosc):
    for j in range(szerokosc):
        liczba_sasiadow = 0

        if i > 0:
            if j > 0 and stara_plansza[i - 1][j - 1] == 1:
                liczba_sasiadow += 1
            if stara_plansza[i - 1][j] == 1:
                liczba_sasiadow += 1
            if j < szerokosc - 1 and stara_plansza[i - 1][j + 1] == 1:
                liczba_sasiadow += 1

        if j < szerokosc - 1 and stara_plansza[i][j + 1] == 1:
            liczba_sasiadow += 1
        if j > 0 and stara_plansza[i][j - 1] == 1:
            liczba_sasiadow += 1

        if i < wysokosc - 1:
            if j < szerokosc - 1 and stara_plansza[i + 1][j + 1] == 1:
                liczba_sasiadow += 1
            if stara_plansza[i + 1][j] == 1:
                liczba_sasiadow += 1
            if j > 0 and stara_plansza[i + 1][j - 1] == 1:
                liczba_sasiadow += 1

        if stara_plansza[i][j] == 1:
            if liczba_sasiadow == 2 or liczba_sasiadow == 3:
                nowa_plansza[i][j] = 1
            else:
                nowa_plansza[i][j] = 0
        else:
            if liczba_sasiadow == 3 and losuj < szansa_na_podpalenie:
                nowa_plansza[i][j] = 1
            else:
                nowa_plansza[i][j] = 0

for i in range(wysokosc):
    for j in range(szerokosc):
        if stara_plansza[i][j] == 1 and nowa_plansza[i][j] == 1:
            nowa_plansza[i][j] = 2

print(f"wyloswane:{losuj}")
print("Stara plansza:")
print(stara_plansza)
print("\nNowa plansza:")
print(nowa_plansza)