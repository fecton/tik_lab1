#!/usr/bin/python3

import numpy as np

N = 10
MATRIX = np.zeros((N,N))

ONE_MATRIX = MATRIX.copy()
TWO_MATRIX = MATRIX.copy()

def GenerateMatrix():
    """
    Генерує потрібну матрицю
    """


    pass

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
        print()

    @staticmethod
    def Matrix_cond():
        """
        Виводить на екран матрицю умовних ймовірностей появи символів первинного та вторинного алфавіту, 
        вторинного та первинного алфавіту.
        """
        pass

    @staticmethod
    def Possibility_one():
        """
        Виводить на екран ймовірність символів ПЕРВИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        pass

    @staticmethod
    def Possibility_two():
        """
        Виводить на екран ймовірність символів ВТОРИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        pass

    @staticmethod
    def Calculations():
        """
        Виводить на екран результати наступних обчислень, а саме:
        - H(A,B)
        - H(A/B)
        - H(B/A)
        - H(A)
        - H(B)
        """
        print("H(A,B) = H(A) + H(B/A) = H(B) + H(A/B)")
        print("H(A,B) = ")                  # !!!
        print("H(A) + H(B/A) = ")           # !!!
        print("H(B) + H(A/B) = ")           # !!!
        print()
        print("H(B/A) = H(A,B) - H(A)")
        print("H(B/A) = ")                  # !!!
        print("H(A,B) - H(A) = ")           # !!!
        print()
        print("H(A/B) = H(A,B) - H(B)")
        print("H(A/B) = ")                  # !!!

def main():
    # a = int(input("1. Generate a matrix\n2. Exit\n> "))
    a = 1
    if(a == 1):
        matrix = GenerateMatrix()

        Show.Matrix_common()

        Show.Possibility_one()

        Show.Possibility_two()
    
        Show.Calculations()


if __name__ == "__main__":
    main()
else:
    print("[ERR] Can't bbe used as a module!")
    exit -1




