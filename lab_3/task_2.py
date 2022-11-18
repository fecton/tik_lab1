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

from .task_1 import *

print("\n\tTask 2\n")

MaxEntropy = log2(len(symbols))
Entropy = InfoAmount_B
UnderLoadedSymb = (MaxEntropy - Entropy) / Entropy

print("UnderLoaded Symbols(b) = ", UnderLoadedSymb)

