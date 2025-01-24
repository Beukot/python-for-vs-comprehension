import time
import matplotlib.pyplot as plt

def forOutside(len, pow, cond):
    tablica = []

    for x in range(len):
        if x % cond == 0:
            tablica.append(x**pow)

def forInside(len, pow, cond):
    tablica = [x ** pow for x in range(len) if x % cond == 0]

def forOutsideDict(len, pow, cond):
    slownik = {}

    for x in range(len):
        if x % cond == 0:
            slownik[x] = x ** pow

def forInsideDict(len, pow, cond):
    slownik = {x: x ** pow for x in range(len) if x % cond == 0}

pow = 2
cond = 1
runs = 10

forTime = []
comprTime = []

forTimeDict = []
comprTimeDict = []

for i in range(runs):
    start_time = time.time()
    forOutside(100 * (i + 1), pow, cond)
    end_time = time.time()

    forTime.append(end_time - start_time)

    start_time = time.time()
    forInside(100 * (i + 1), pow, cond)
    end_time = time.time()

    comprTime.append(end_time - start_time)

    start_time = time.time()
    forOutsideDict(100 * (i + 1), pow, cond)
    end_time = time.time()

    forTimeDict.append(end_time - start_time)

    start_time = time.time()
    forInsideDict(100 * (i + 1), pow, cond)
    end_time = time.time()

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