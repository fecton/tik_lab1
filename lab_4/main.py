# MODULES
# =========================================
import numpy as np

from random import uniform, shuffle
from math import log2
# =========================================


# GLOBAL
# =========================================
m = 10
matrix = np.zeros((m,m))

# Генерація випадкової матриці
a = [0.02, 0.02, 0.006, 0.004, 0.02, 0.001, 0.003, 0.005, 0.001, 0.03, 0.04, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.03, 0.05, 0.04, 0.01, 0.1, 0.02, 0.01, 0.04, 0.06, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.004, 0.02, 0.09, 0.14, 0.06, 0.02, 0.02, 0.01, 0.002, 0.01]
shuffle(a)
b = [x * 0.5 for x in a]*2
row = np.array(b)
matrix = row.reshape((m,m))

# Закон розподілу джерел: Геометричний розподіл
# =========================================
# P(x = n) = p1(1-p)**(n-1)

# FUNCTIONS
# =========================================
def gen():
    """
    Генерує випадкове число від нуля до одиниці, та округляє до тисячних (0.001)
    """
    return round(uniform(0.,1.), 3)

def Fact(n: int):
    """
    Факторіал числа
    """
    if n <= 1: return 1
    return n*Fact(n-1)

def show():
    """
    Вивести матрицю
    """
    global matrix
    print("\tMATRIX")
    print("\t"+"\t".join([str(x) for x in range(1,m+1)]))
    for i in range(m):
        print("%d\t" % (i+1) +"\t".join([str(matrix[i][x]) for x in range(m)]))
    print()

def matrix_cond():
    """
    Виводить на екран матрицю умовних ймовірностей появи символів первинного та вторинного алфавіту, 
    вторинного та первинного алфавіту.
    """

    ONE_MATRIX = matrix.sum(axis=1)
    TWO_MATRIX = matrix.sum(axis=0)

    print("Первинний алфавіт")

    for i in range(10):
        print(f"p(a{i}) = {ONE_MATRIX[i]}")
    print()
    print("Total: ", ONE_MATRIX.sum(),end="\n"*2)

    print("Вторинний алфавіт")
    for i in range(10):
        print(f"p(b{i}) = {TWO_MATRIX[i]}")
    print()
    print("Total: ", TWO_MATRIX.sum(),end="\n"*2)

# =========================================


# MAIN CYCLE
# =========================================
matrix_cond()
show()
# =========================================


"""
pX = []
pY = []
D = m - 1
HX = 0 # H(A)
HY = 0 # H(B)

for i in range(m):
    PBj = 0.
    pX.append(0)
    pY.append(0)
    for j in range(m):
        data1 = matrix[i][j]
        data2 = matrix[j][i]
        pX[i] += data1
        pY[i] += data2
        PBj += Row[j] * data2
    HY += PBj * log2(PBj)
    HX += Row[i] * log2(Row[i])

HX = abs(HX)
HY = abs(HY)

PAB = np.zeros((m,m)) # P(A/B)
PBA = np.zeros((m,m)) # P(B/A)

PAB.dtype = "float16"
PBA.dtype = "float16"

for i in range(m):
    for j in range(m):
        data = matrix[i][j]
        PAB[i][j] = data / pY[i]
        PBA[i][j] = data / pX[i]

HAB, HBA = 0, 0
C = 0
for i in range(m):
    K = 0
    L = 0
    for j in range(m):
        try:
            C += pX[i] * PBA[j][i] * log2(PBA[j][i] / pY[j])
        except ValueError:
            pass
        data1 = matrix[i][j]
        data2 = matrix[j][i]
        try:
            L += data1 * log2(data1)
        except ValueError:
            pass
        try:
            K += data2 * log2(data2)
        except ValueError:
            pass
    HBA += L * Row[i]
    HAB += K * Row[i]

C    = abs(C)
HBA  = abs(HBA)
HAB  = abs(HAB)
D   *= HBA

IXY = (m - 1) * HX - HBA
print("H(A) = ", HX, "bit/symbol")
print("H(B) = ", HY, "bit/symbol")
print("D = ", D, "bit")
print("I(A,B) = ", IXY, "bit")
print("H(A/B) = ", HAB, "bit/symbol")
print("H(B/A) = ", HBA, "bit/symbol")
print("C = ", C, "bit/symbol")

"""



