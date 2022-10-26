#!/usr/bin/python3

import numpy as np
from math import log2
from random import randint

# by variant
N = 10

def H(matrix):
    total = 0.
    for i in range(N):
        if matrix[i] <= 0:
            continue
        total += matrix[i]*log2(matrix[i])
    total = abs(total)
    return total

def GenerateMatrix() -> np.array:
    """
    Генерує потрібну матрицю
    """
    MATRIX = np.zeros((N,N))
    pos = [0.05, 0.06, 0.04, 0.04, 0.05, 0.08, 0.04, 0.01, 0.1, 0.14, 0.02, 0.09, 0.01, 0.14, 0.06, 0.02, 0.05]
    while pos:
        p = pos.pop()
        i,j = randint(0,9), randint(0,9)
        while MATRIX[i][j] != 0:
            i,j = randint(0,9), randint(0,9)
        MATRIX[i][j] = p
    return MATRIX

MATRIX = GenerateMatrix()
ONE_MATRIX = MATRIX.sum(axis=1)
TWO_MATRIX = MATRIX.sum(axis=0)

class Show:
    @staticmethod
    def Matrix_common():
        """
        Виводить на екран матрицю ймовірностей спільної появи первинного та вторинного алфавіту.
        """
        print("\t",end="")
        print("\t".join(["<%d>" % (x+1) for x in range(N)]))

        row_i = 1
        for row in MATRIX:
            print("[%d]\t" % row_i, end="")
            print("\t".join([str(x) for x in row]))
            row_i += 1
        print()

    @staticmethod
    def Matrix_cond():
        """
        Виводить на екран матрицю умовних ймовірностей появи символів первинного та вторинного алфавіту, 
        вторинного та первинного алфавіту.
        """
        print("First + second alphabet")
        print("By rows      By columns")
        for i in range(10):
            print(f"p(a{i}) = {round(ONE_MATRIX[i], 2)}\tp(b{i}) = {round(TWO_MATRIX[i], 2)}")

    @staticmethod
    def Possibility_one():
        """
        Виводить на екран ймовірність символів ПЕРВИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        print("Only first")
        for i in range(10):
            print(f"p(a{i}) = {round(ONE_MATRIX[i], 2)}")
        print()

    @staticmethod
    def Possibility_two():
        """
        Виводить на екран ймовірність символів ВТОРИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        print("Only second")
        for i in range(10):
            print(f"p(b{i}) = {round(TWO_MATRIX[i], 2)}")
        print()

    @staticmethod
    def Calculations():
        A = ONE_MATRIX
        B = TWO_MATRIX

        """
        Виводить на екран результати наступних обчислень, а саме:
        - H(A,B)
        - H(A/B)
        - H(B/A)
        - H(A)
        - H(B)
        """
        print("H(A,B) = H(A) + H(B/A) = H(B) + H(A/B)")
        print("H(A,B) = ", H(A+B))

        print()
        print("H(B/A) = H(A,B) - H(A)")
        print("H(B/A) = ", H(A+B) - H(A))
        print("H(A,B) - H(A) = ", H(A+B) - H(A))
        print()
        print("H(A/B) = H(A,B) - H(B)")
        print("H(A/B) = ", H(A+B) - H(B))

def main():
    # a = int(input("1. Generate a matrix\n2. Exit\n> "))
    a = 1
    if(a == 1):
        Show.Matrix_cond()

        Show.Matrix_common()

        Show.Possibility_one()

        Show.Possibility_two()
    
        Show.Calculations()


if __name__ == "__main__":
    main()
else:
    print("[ERR] Can't bbe used as a module!")
    exit -1




