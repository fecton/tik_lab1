# MODULES
# =========================================
import numpy as np

from random import uniform
from math import log2
# =========================================


# GLOBAL
# =========================================
m = 10
matrix = np.zeros((m,m+1))
matrix.dtype = "float16"
Row = []
# Закон розподілу джерел: Геометричний розподіл
# =========================================


# FUNCTIONS
# =========================================
def gen():
    return round(uniform(0.,1.), 3)

def Fact(n: int):
    if n <= 1: return 1
    return n*Fact(n-1)

def show():
    global matrix
    print("\tMATRIX")
    print("\t"+"\t".join([str(x) for x in range(1,m+1)] + ["p(x)"]))
    for i in range(m):
        print("%d\t" % (i+1) +"\t".join([str(matrix[i][x]) for x in range(m+1)]))
    print()


# =========================================


# MAIN CYCLE
# =========================================
for i in range(m):
    Row.append(gen())
    for j in range(m):
        matrix[i][j] = round((Fact(m - 1) / (Fact(j) * Fact(m - 1 -j))) * pow(Row[i], j) * pow(1 - Row[i], m -1 -j), 4)
    matrix[i][m] = Row[i]
# =========================================

show()

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





