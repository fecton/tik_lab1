import numpy as np
from random import shuffle, uniform
from math import log2, ceil, log10


def GenMatrix_10() -> np.ndarray:
    """Генерує матрицю 10x10 і повертає її
    
    @return Готову матрицю 10х10
    """

    m = 10
    matrix = np.zeros(shape=(m,m))

    a = [0.02, 0.02, 0.006, 0.004, 0.02, 0.001, 0.003, 0.005, 0.001, 0.03, 0.04, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.03, 0.05, 0.04, 0.01, 0.1, 0.02, 0.01, 0.04, 0.06, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.004, 0.02, 0.09, 0.14, 0.06, 0.02, 0.02, 0.01, 0.002, 0.01]
    shuffle(a)
    b = [x * 0.5 for x in a]*2
    row = np.array(b)
    matrix = row.reshape((m,m))

    return matrix


def GenMatrix_Random(m: int) -> np.ndarray:
    """
    Генерує повністю випадкову матрицю

    @param m Розмірність квадратної матриці

    @return Випадкова матриця MxM
    """
    matrix = np.zeros(shape=(m,m))
    for i in range(m):
        for j in range(m):
            matrix[i][j] = Gen()
    return matrix


def ShowMatrix(matrix: np.ndarray, m: int, showIndexes: bool = False):
    """
    Виводить матрицю
    """
    print("\tMATRIX")
    if showIndexes:
        print("\t"+"\t".join([str(x) for x in range(1,m+1)]))
        for i in range(m):
            print("%d\t" % (i+1) +"\t".join([str(matrix[i][x]) for x in range(m)]))
    else:
        for i in range(m):
            print("\t".join([str(matrix[i][x]) for x in range(m)]))

    print()


def Entropy(prob: list) -> float:
    """H(x) - Повертає значення ентропії
    @param Список з вірогідністями появи

    @return Ентропію

    Довідка:
    Ентропія - міра невизначеності інформації. Або ж математичне очікування H(x) випадкової величини I(x) визначеною на ансаблі {X, p(x)}, т.е. вона характерезує середнє значення кількості інформації, що приходить на 1 символ.
    """
    entropy = 0
    for i in prob:
        entropy += i*log2(i)
    entropy *= -1
    return entropy


def DefineEverything(matrix: np.ndarray, Px: list) -> dict:
    """
    Отримує матрицю і повертає словник обчислень:
        - H(A)          )
        - H(B)          ) = \ 
        - H(A/B)        ) = / ентропія
        - H(B/A)        )
        - C             
        - D

    @param Матриця

    @return Повертає словник з обчисленнями
    """
    m = len(matrix)
    prob_a, prob_b = Probabilities(matrix)

    PAB = np.zeros(shape=(m,m))
    PBA = np.zeros(shape=(m,m))

    for i in range(m):
        for j in range(m):
            data = matrix[i][j]
            PAB[i][j] = data / prob_b[j]
            PBA[i][j] = data / prob_a[i]

    H_AB    = 0
    H_BA    = 0
    C       = 0
    D       = m - 1 # Втрати в каналі зв'язку з алфавітом довжиною 11

    for i in range(m):
        K = 0
        L = 0
        for j in range(m):
            C += prob_a[i] * PBA[i][j] * log2(PBA[j][i] / prob_b[j])
            x = matrix[i][j]
            y = matrix[j][i]
            L += x*log2(x)
            K += y*log2(y)

        H_BA += L * Px[i]
        H_AB += K * Px[i]

    H_AB    *= -1
    H_BA    *= -1
    D       *= H_BA

    res = {}
    res["H(A)"] = Entropy(prob_a)
    res["H(B)"] = Entropy(prob_b)
    res["H(A/B)"] = H_AB
    res["H(B/A)"] = H_BA
    res["D"] = D
    res["C"] = abs(C)

    return res


def Probabilities(matrix: np.ndarray) -> tuple:
    """pX & pY - Повертає значення кортежа з pX та pY на основі вхідної матриці
    @param Вхідна матриця

    @return Кортеж з двух елементів: [pX, pY]
    """
    pX = matrix.sum(axis=-1)
    pY = matrix.sum(axis=0)
    m = len(matrix)

    for i in range(m):
        pX[i] = GeometricFormula(pX[i], i)
        pY[i] = GeometricFormula(pY[i], i)

    return (pX, pY)


def GeometricFormula(p: float, n: int) -> float:
    """
    Формула геометричного розподілення 

    @param p Вірогідність
    @param n Індекс

    @return Значення
    """
    q = 1 - p

    return p*q**(n-1)


def ShowProb(prob_a: np.ndarray, prob_b: np.ndarray) -> None:
    """
    Вводить значення первинного і вторинного алфавіту
    """
    m = len(prob_a)

    string_a = "Первинний алфавіт\n"
    string_b = "Вторинний алфавіт\n"

    a = 0
    b = 0

    for i in range(1, m+1):
        string_a += "p(a%s) = %f\n" % (i, prob_a[i-1])
        string_b += "p(b%s) = %f\n" % (i, prob_b[i-1])

        a += prob_a[i-1]
        b += prob_b[i-1]
    
    print(string_a)
    print("Totally: ", a)
    print()

    print(string_b)
    print("Totally: ", b)
    print()


def InfoAmount_Hartli(N: int) -> float:
    """
    I - Кількість інформації за Хартлі
    Кількість інформації в повідомленні із N
    рівновірогіних повідомлень

    Довідка:
    I = log2(N) = log(m) = log(1/p) = -log(p)
    Якщо вірогідність символа афавіту рівновірогідна, то ця вірогідність (p = 1/m), і те що N = m
    """
    I  = log2(N)

    return I


def InfoAmount_Shenon(prob: list) -> float:
    """
    I - Кількість інформації за Шеноном.
    
    Кількість інформації в повідомлення із N 
    НЕ рівновірогідних йому елементів дорівнює цій формулі
    """
    I = 0

    for i in prob:
        I += i * log2(i)
    I *= -1 

    return I


def Redundancy(prob: list, k: float = None) -> float:
    """
    R - надмірність повідомлень. Приймає на вході список вірогідностей

    Автоматичне підраховує H_max та H_x і повертає значення

    @param Список вірогідностей
    @param (optional) коєфіцієнт стискання

    @return Значення надмірності
    """

    R = 0
    if k is not None:
        R =  1 - k
    else:
        H_max   = ceil(Entropy(prob))
        H_x     = Entropy(prob)

        R = (H_max - H_x) / H_max
    return R


def SpeedOfTranslation(prob: list, speed1: float = 1.0) -> float:
    try:
        R = Entropy(prob) / speed1
    except ZeroDivisionError:
        R = 0
    return R


def Gen() -> float:
    """
    Generated float number in the range [0, 1]
    """
    return uniform(0., 1.)


def DynamicRange(Pmax, Pmin):
    """
    Повертає динамічний діапазон (D)
    """

    try:
        return 10*log10(Pmax/Pmin)
    except ZeroDivisionError:
        return 0


def CapacityOfChannel(t: float, f: float, w: float = None, pc: float = None, pn: float = None):
    """
    Визначає об'єм каналу зв'язку
    
    @param t  Тк - довждина інтервалу часу на який предоставлено канал
    @param f  Fк - ефективність полоси пропускання канала зв'язку
    @param w  Wк - логарифмічне перевищення сигналу (optional)
    @param pc Pс - потужність синалу, зафіксована у канальному довкіллі (optional)
    @param pk Pк - потужність перешкод у канальному довкіллі (optional)

    @return Об'єм каналу зв'язку
    """

    if w is not None:
        return t*f*w
    else:
        return t*f*log2(1+pc/pn)


