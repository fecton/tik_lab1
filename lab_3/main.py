"""
File: main.py
Theory of information and coding
Laboratory word #3
"""


# IMPORTS
import numpy as np
from math import log2

# GLOBAL VARIABLES

# Кількість символів алфавіту
k = 25


# FUNCTIONS

def symbol_counts(text: str) -> dict:
    """
    Отримує текст і повертає список з буквами в тексті та їх кількістю

    @param Текст, у якому виконати підрахунок

    @return Список з кількостями символів
    """

    dicti = {}
    text = text.lower()
    for symbol in text:
        if symbol not in dicti.values():
            dicti[symbol] = text.count(symbol)

    return dicti

# MAIN



