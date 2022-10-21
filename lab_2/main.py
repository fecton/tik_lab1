#!/usr/bin/python3

def GenerateMatrix():
    """
    Генерує потрібну матрицю
    """
    pass

class Show:
    @classmethod
    def Matrix_common():
        """
        Виводить на екран матрицю ймовірностей спільної появи первинного та вторинного алфавіту.
        """
        pass

    @classmethod
    def Matrix_cond(alphabet: str):
        """
        Виводить на екран матрицю умовних ймовірностей появи символів первинного та вторинного алфавіту, 
        вторинного та первинного алфавіту.
        """
        pass

    @classmethod
    def Possibility_one():
        """
        Виводить на екран ймовірність символів ПЕРВИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        pass

    @classmethod
    def Possibility_two():
        """
        Виводить на екран ймовірність символів ВТОРИННОГО алфавіту,
        отриманої наа підставі матриці спільної появи.
        """
        pass

    @classmethod
    def Calculations():
        """
        Виводить на екран результати наступних обчислень, а саме:
        - H(A,B)
        - H(A/B)
        - H(B/A)
        - H(A)
        - H(B)
        """
        pass

def main():
    pass

if __name__ == "__main__":
    main()
else:
    print("[ERR] Can't bbe used as a module!")
    exit -1




