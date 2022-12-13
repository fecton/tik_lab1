# MODULES
# =========================================

from random import uniform
from tik_functions import *

m = 10

# Генерація матриці
matrix = GenMatrix_10()

# Вивести матрицю
ShowMatrix(matrix, m)

# Визначити списки вірогідностей
prob_a, prob_b = Probabilities(matrix)

# Вивести масиви вірогідностей
ShowProb(prob_a, prob_b)

Px = [Gen() for x in range(m)]
ev = DefineEverything(matrix, Px)

H_a = ev["H(A)"]
H_b = ev["H(B)"]
# !!!
I_A_B = InfoAmount_Shenon(prob_a+prob_b)
H_ab = ev["H(A/B)"]
H_ba = ev["H(B/A)"]
C    = ev["C"]

print("I(A,B) = %f bits" % I_A_B)
print("H(A) = %f bit/symbol" % H_a)
print("H(B) = %f bit/symbol" % H_b)
print("H(A/B) = %f bit/symbol" % H_ab)
print("H(B/A) = %f bit/symbol" % H_ba)
print("Channel capacity = %f bit/symbol" % C)
