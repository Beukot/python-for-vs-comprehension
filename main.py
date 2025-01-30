import time
import matplotlib.pyplot as plt

def forOutside(len, pow, cond):
    tab = []

    for x in range(len):
        if x % cond == 0:
            tab.append(x**pow)

    return tab

def forInside(len, pow, cond):
    tab = [x ** pow for x in range(len) if x % cond == 0]
    return tab

def forOutsideDict(len, pow, cond):
    slownik = {}

    for x in range(len):
        if x % cond == 0:
            slownik[x] = x ** pow

    return slownik

def forInsideDict(len, pow, cond):
    slownik = {x: x ** pow for x in range(len) if x % cond == 0}
    return slownik

def checkList(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            print("coś nie posortowane...")
            break

pow = 2
cond = 1
runs = 10

forTime = []
comprTime = []

forTimeDict = []
comprTimeDict = []

for i in range(runs):
    start_time = time.time()
    tablica = forOutside(100 * (i + 1), pow, cond)
    end_time = time.time()
    checkList(tablica)

    forTime.append(end_time - start_time)

    start_time = time.time()
    tablica = forInside(100 * (i + 1), pow, cond)
    end_time = time.time()
    checkList(tablica)

    comprTime.append(end_time - start_time)

    start_time = time.time()
    tablica = forOutsideDict(100 * (i + 1), pow, cond)
    end_time = time.time()
    checkList(tablica)

    forTimeDict.append(end_time - start_time)

    start_time = time.time()
    tablica = forInsideDict(100 * (i + 1), pow, cond)
    end_time = time.time()
    checkList(tablica)

    comprTimeDict.append(end_time - start_time)

plt.figure(figsize=(12, 6))

plt.plot([100 * (i + 1) for i in range(runs)], forTime, label='Pętla for', color='blue', marker='o')
plt.plot([100 * (i + 1) for i in range(runs)], comprTime, label='Komprehensja', color='orange', marker='o')
plt.plot([100 * (i + 1) for i in range(runs)], forTimeDict, label='Pętla for na słowniku', color='yellow', marker='s')
plt.plot([100 * (i + 1) for i in range(runs)], comprTimeDict, label='Komprehensja na słowniku', color='green', marker='s')

plt.title('Porównanie czasu zapełnienia tablicy w pętli for zawartej w inicjalizacji tablicy i poza nią')
plt.xlabel('Elementy')
plt.ylabel('Czas [s]')
plt.legend()

plt.savefig('results.png', dpi=300, bbox_inches='tight')

plt.show()

scenario_header = "# Scenariusz"
scenario_text = "Testujemy dwa rodzaje funkcji zapełniające słowniki i listy potęgami kwadratowymi kolejnych iteracji zapełniania tablicy, przy spełnieniu warunku. Program wykonuje każdą z funkcji 10 razy, za każdym razem zwiększając liczbę elementów o 100 począwszy od 100."

results_header = "# Wyniki"
columns = ["Elementy", "Pętla for", "Komprehensja", "Pętla for na słowniku", "Komprehensja na słowniku"]
table = " | " + " | ".join(columns) + " | "
table2 = " | --- | --- | --- | --- | --- |"

with open("results.md", "w") as file:
    file.write(f"{scenario_header}\n{scenario_text}\n{results_header}\n{table}\n{table2}\n")