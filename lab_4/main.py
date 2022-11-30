# MODULES
# =========================================
import numpy as np
from random import uniform
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
    print("\t"+"\t".join([str(x) for x in range(1,m+1)] + ["p(x)"]))
    for i in range(m):
        print("%d\t" % i+"\t".join([str(matrix[i][x]) for x in range(m+1)]))
    print()


# =========================================


# MAIN CYCLE
# =========================================
for i in range(m):
    Row.append(gen())
    for j in range(m):
        matrix[i][j] = round((Fact(m - 1) / (Fact(j) * Fact(m - 1 -j))) * pow(Row[i], j) * pow(1 - Row[i], m -1 -j), 4)

# =========================================

show()


