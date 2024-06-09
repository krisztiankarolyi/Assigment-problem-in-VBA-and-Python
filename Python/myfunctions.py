import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.optimize import linprog

 
def feltolt0(matrix: list, n: int, m: int):
    """
    Üres kétdimenziós tömböt feltölt 0-kal \n
    pl1: \n
    hsz = 2, tsz = 3:
    matrix = [[0, 0, 0], [0, 0, 0]] \n
    pl2: \n
    hsz = 3, tsz = 2:
    matrix = [[0, 0], [0, 0], [0, 0]]

    :param n:
    :param m:
    :param matrix: list
    :return:
    """

    for i in range(n):
        sor = []
        for j in range(m):
            sor.append(0)
        matrix.append(sor)


def feltolt_binarismatrix(n: int, m: int, binarismatrix: list, eredmenytomb: list):
    """
    A linprog függvény által visszaadott eredménytömb (res.x)
    alapján feltöltjük a bináris mátrixot. \n
    pl: \n
    binarismatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] \n
    eredmenytomb = [ 0.  1. -0.  0.  0. -0.  0.  1.  0.  0.] \n
    return binarismatrix = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
    :param m:
    :param n:
    :param binarismatrix:
    :param eredmenytomb: res.x
    :return:
    """

    for i in range(n):
        for j in range(m):
            binarismatrix[i][j] = int(eredmenytomb[i * m + j])


def space_mentesit(line: str):
    """
    Egy kapott 'numerikus' stringből eltávolítja a szóközöket,
    majd visszaadja a szóközmentesített 'numerikus' stringet. \n
    pl: '10 7 6 5 5 4' -> '1076554'
    :param line: a szöveges állomány egy sora
    :return: seged : str
    """

    seged = ""
    for j in range(len(line)):
        if line[j].isnumeric():
            seged += line[j]
    return seged


def feltolt_jegymatrix(jegymatrix: list, line: str):
    """
    feltölti s hozzáadja a jegymátrix egy sorát az együtthatókkal a
    paraméteren át megkapott "line" stringből, amelyre
    először meghívja a space_mentesit() függvényt \n \n
    Egy négy hallgatós (n=4) séma esetén a függvényt 4x kell meghívni,
    hogy a jegymátrix kész legyen.
    :param line: txt állomány egy sora, pl: 4 9 8 6 5
    :param jegymatrix:
    :return: None
    """

    seged = space_mentesit(line)
    sor = []
    for i in range(len(seged)):
        if int(seged[i]) == 1 and int(seged[i + 1]) == 0:
            sor.append(int(seged[i] + seged[i + 1]))
        elif int(seged[i]) == 0:
            continue
        else:
            sor.append(int(seged[i]))
    jegymatrix.append(sor)


def convert_1D(jegymatrix: list):
    """
    2D listát 1D listává alakít \n
    pl: \n
    jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]] \n
    return lista = [4, 9, 8, 6, 5, 6, 4, 7, 4, 4]
    :param jegymatrix: list[list]
    :return: lista: list
    """

    lista = []
    for i in range(len(jegymatrix)):
        for j in range(len(jegymatrix[i])):
            lista.append(jegymatrix[i][j])
    return lista


def transzponalas(jegymatrix: list):
    """
    sor-oszlop bejárás helyett oszlop-sor bejárás \n
    pl: \n
    jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]] \n
    return lista = [[8, 8, 4, 5], [4, 7, 10, 8], [5, 7, 6, 7]]
    :param jegymatrix: list[list]
    :return: lista: list
    """

    lista = []
    for j in range(len(jegymatrix[0])):
        sor = []
        for i in range(len(jegymatrix)):
            sor.append(jegymatrix[i][j])
        lista.append(sor)
    return lista


def general_kfbe(n: int, m: int):
    """
    Generálja a kfbe listát n-m bármilyen relációja esetén \n
    1. Eset: n == m == 2: \n
        kfbe = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]] \n
            n == m == 3 \n
        kfbe = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1]]

    2. Eset: n < m (2 < 3): \n
        kfbe = [[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]] \n

    3. Eset: n > m (4 > 3) \n
        kfbe(np.array) = [[1 1 1 0 0 0 0 0 0 0 0 0], [0 0 0 1 1 1 0 0 0 0 0 0],
                          [0 0 0 0 0 0 1 1 1 0 0 0], [0 0 0 0 0 0 0 0 0 1 1 1]]
    :param n: hallgatók száma
    :param m: tételek száma
    :return: kfbe
    """

    if n == m:
        kfbe = []
        for _ in range(2 * n):
            kfbe.append([0] * (n ** 2))
        # elso fele
        for i in range(n):
            for j in range(n):
                kfbe[i][i * n + j] = 1

        # masodik fele
        for i in range(n, 2 * n):
            for j in range(n ** 2):
                if (n - i + j) % n == 0:
                    kfbe[i][j] = 1

        return kfbe

    elif n < m:
        kfbe = []
        for _ in range(n):
            kfbe.append([0] * (n * m))

        for i in range(n):
            for j in range(m):
                kfbe[i][i * m + j] = 1

        return kfbe

    else:
        kfbe = []
        for _ in range(n):
            kfbe.append([0] * (n * m))

        for i in range(n):
            for j in range(m):
                kfbe[i][i * m + j] = 1

        return kfbe


def general_kfje(n: int):
    """
    Generálja a kfje listát \n
    (n, m) = (2, 3) -> kfje = [1, 1]
    :param n: hallgatók száma
    :return: kfje
    """

    kfje = []
    for _ in range(n):
        kfje.append(1)
    return kfje


def general_kfje_egyenlo(n: int):
    """
    n == m == 2: \n
    kfje = [1, 1, 1, 1] \n
    n == m == 3 \n
    kfje = [1, 1, 1, 1, 1, 1]
    :param n: hallgatók száma
    :return: kfje
    """
    kfje = []
    for _ in range(2 * n):
        kfje.append(1)
    return kfje


def general_kfb(n: int, m: int):
    """
    Generálja a kfb listát \n
    n < m (2 < 3): \n
    kfb = [[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]
    :param n: hallgatók száma
    :param m: tételek száma
    :return: kfb
    """

    kfb = []
    for _ in range(m):
        kfb.append([0] * (n * m))

    for i in range(m):
        for j in range(n * m):
            if (j - i) % m == 0:
                kfb[i][j] = 1

    return kfb


def general_kfj(n: int, m: int):
    """
    Generálja a kfj listát n<m és n>m esetén \n
    (n=m esetén a kfj nem létezik) \n \n
    (n, m) = (2, 3): \n
    kfj = [1, 1, 1] \n
    (n, m) = (4, 3): \n
    kfj(np.array) = [1, 1, 1]
    :param n: hallgatók száma
    :param m: tételek száma
    :return: kfj
    """

    kfj = []
    kisebb = n < m
    for _ in range(m):
        if kisebb:
            kfj.append(1)
        else:
            kfj.append(int(n / m))
    return kfj


def general_bounds(n: int, m: int):
    """
    n = m = 2: \n
    bounds = [(0, 1), (0, 1), (0, 1), (0, 1)] \n
    (n, m) = (2, 3) \n
    bounds = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
    :param n: hallgatók száma
    :param m: tételek száma
    :return: bounds
    """
    a = (0, 1)
    bounds = [a] * (n * m)
    return bounds


def sorMaxAvg(n: int, matrix: list):
    """
    Kiszámítja a jegymátrixban minden sorban a jegyek maximumát,
    ezeket összegzi, majd átlagolja (elossza a hallgatók számával)
    :param n: hallgatók száma
    :param matrix: jegyek_matrix
    :return: float(osszeg / n)
    """
    osszeg = 0
    for i in range(len(matrix)):
        sormax = matrix[i][0]
        for j in range(len(matrix[i])):
            if matrix[i][j] > sormax:
                sormax = matrix[i][j]
        osszeg += sormax
    return float(osszeg / n)


def sorMinAvg(n: int, matrix: list):
    """
    Kiszámítja a jegymátrixban minden sorban a jegyek maximumát,
    ezeket összegzi, majd átlagolja (elossza a hallgatók számával)
    :param n:
    :param matrix: jegyek_matrix
    :return: float(osszeg / n)
    """
    osszeg = 0
    for i in range(len(matrix)):
        sormax = matrix[i][0]
        for j in range(len(matrix[i])):
            if matrix[i][j] < sormax:
                sormax = matrix[i][j]
        osszeg += sormax
    return float(osszeg / n)


def cfEredmenyGeneralas(jegymatrix: list, binarismatrix: list):
    """
    A célfüggvény értékét adja vissza
    :param jegymatrix:
    :param binarismatrix:
    :return: sum
    """
    osszeg = 0
    sorok_szama = len(jegymatrix)
    oszlopok_szama = len(jegymatrix[0])
    for i in range(sorok_szama):
        for j in range(oszlopok_szama):
            osszeg += jegymatrix[i][j] * binarismatrix[i][j]
    return osszeg


def lp(n: int, m: int, cf: list, binarismatrix: list):
    """
    Paraméterként kapja a célfüggvényt (1D lista), illetve a 0-s
    bináris mátrixot, amelyet a függvény visszaad feltöltve. \n
    n-m bármilyen relációjára kiszámítja a kfje, kfbe, (kfj), (kfb), bounds
    listákat (a linprog függvény paraméterei) a generáló függvények által
    majd meghívja a linprog() függvényt.
    :param n: hallgatók száma
    :param m: tételek száma
    :param cf: 1D lista
    :param binarismatrix: 2D nullmátrix
    :return: res
    """

    if n == m:

        kfje = general_kfje_egyenlo(n)
        kfbe = general_kfbe(n, m)
        bounds = general_bounds(n, m)
        res = linprog(c=cf, A_eq=kfbe, b_eq=kfje, bounds=bounds)

        feltolt_binarismatrix(n, m, binarismatrix, res.x)
        return res

    elif n < m:

        kfbe = general_kfbe(n, m)
        kfje = general_kfje(n)
        kfb = general_kfb(n, m)
        kfj = general_kfj(n, m)
        bounds = general_bounds(n, m)
        res = linprog(c=cf, A_eq=kfbe, b_eq=kfje, A_ub=kfb, b_ub=kfj, bounds=bounds)

        feltolt_binarismatrix(n, m, binarismatrix, res.x)
        return res

    else:
        kfbe = np.array(general_kfbe(n, m))
        kfje = np.array(general_kfje(n))
        kfb = -1 * np.array(general_kfb(n, m))
        kfj = -1 * np.array(general_kfj(n, m))
        bounds = general_bounds(n, m)
        res = linprog(c=cf, A_eq=kfbe, b_eq=kfje, A_ub=kfb, b_ub=kfj, bounds=bounds)

        feltolt_binarismatrix(n, m, binarismatrix, res.x)
        return res


def legjobb_huzas(n: int, result: float, maxatlag: float):

    """
    Feltétel: már lefuttattuk a linprog() függvényt, és a bináris mátrixot
    feltöltöttük.  \n \n
    Maximalizálás esetén, ha a célfüggvény értéke egyenlő a jegymátrixban
    a sorok maximumainak az összegének az átlagával, akkor mindenki azt a
    tételt húzta, amiből a legjobban felkészült, különben nem.
    :param n: hallgatók száma
    :param result: célfüggvény értéke
    :param maxatlag: a jegymátrixban
    a sorok maximumainak az összegének az átlaga
    :return: print(szöveg)
    """

    if (result / n) == maxatlag:
        print("Mindenki azt a tételt húzta, amiből a legjobban felkészült!")
    else:
        print("Nem mindenki azt a tételt húzta, amiből a legjobban felkészült!")


def legrosszabb_huzas(jegymatrix: list, binarismatrix: list):

    """
    Feltétel: már lefuttattuk a linprog() függvényt, és a bináris mátrixot
    feltöltöttük.  \n \n
    Minimalizálás esetén, a jegymátrixnak és bináris mátrixnak bármely
    két megfelelő elemének szorzata egyenlő 4, akkor van olyan hallgató,
    aki 4-est húzott, különben nincs. \n \n
    A jegymátrix és a bináris megfelelő elemeinek szorzataiból készítünk
    egy 1D listát, és megnézzük, hogy van-e 4-es benne.
    :param jegymatrix:
    :param binarismatrix:
    :return:
    """

    kihuzott_lista = []
    sorok_szama = len(jegymatrix)
    oszlopok_szama = len(jegymatrix[0])
    for i in range(sorok_szama):
        for j in range(oszlopok_szama):
            kihuzott_lista.append(jegymatrix[i][j] * binarismatrix[i][j])

    if 4 in kihuzott_lista:
        print("Van olyan hallgató, aki 4-est húzott")
        return True
    else:
        print("Senki sem húzott 4-est")
        return False
