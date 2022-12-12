import numpy as np
from random import shuffle
from math import log2, ceil


def factorial(n: int) -> int:
    """
    Факторіал числа
    """
    if n <= 1: return 1
    return n*factorial(n-1)


def gen_matrix_10() -> np.ndarray:
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


def pX_pY(matrix: np.ndarray) -> tuple:
    """pX & pY - Повертає значення кортежа з pX та pY на основі вхідної матриці
    @param Вхідна матриця

    @return Кортеж з двух елементів: [pX, pY]
    """
    pX = matrix.sum(axis=-1)
    pY = matrix.sum(axis=0)

    return (pX, pY)


def InfoAmount_Hartli(N: int):
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


