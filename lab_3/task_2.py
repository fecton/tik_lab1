"""
File: task_2.py 
Theory of information and coding
Laboratory word #3

Task 2:
Визначити, наскільки недовантажені символи у другому випадку
Кількість символівв алфавіту k = 13
Тривалості символів: r1 = 1c, r2 = 2c, rk = rk - 1 + 1
Імовірність появи символів взяти з пункту 1.1
"""

from task_1 import task_1_message, InfoAmount_A, symbols,task_2_message, InfoAmount_B, k

from math import log2
from func import unique

print("\n\tTask 2\n")
# Кількість символів алфавіту (команда + 10)
symbols = symbols[:k]


task_1_message = symbols*3
print("Symbols: ", symbols)

MaxEntropy = log2(len(symbols))
Entropy = InfoAmount_B / len(symbols)
UnderLoadedSymb = (MaxEntropy - Entropy) / MaxEntropy
print("UnderLoaded Symbols(b) = ", UnderLoadedSymb)


duration = 0
for i in range(1,k+1):
    duration += Entropy / i

print("Speed of translation(1) = ", duration)

task3 = "aabbccddeeffgghhiijj"
print("Message: ", task3)

probability = 0.0625
Entropy1 = 0
for i in range(0,11):
    Entropy1 += probability * log2(probability)

Entropy1 = abs(Entropy1)

duration2 = 0
for i in range(1,k):
    duration2 += Entropy1 / i

print("Speed of translation(2) = ", duration2)
