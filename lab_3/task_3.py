"""
File: task_3.py
Theory of information and coding
Laboratory word #3

Task 3:
Знайти швидкість передачу повідомлень, складених із таких символів.
1.3 Побудувати оптимальний код повідомленення з використанням методу
Шеннона-Фано, описаного вище.

1.4 Отримайний код має бути переданий ввід кодера (пристрій 1)
на декодер (пристрій 2).

1.5 Декодер має розкодувати отриману послідовність. Можна
Використовувати будь-які пристої для кодування та декодування
"""

# Modules
# =============================================
import math
import collections
# =============================================

# Global variables
# =============================================
TextToEncode = ""
TextToDecode = ""
Text = ""

SDI                         = dict()
codingTable                 = dict()
arrSortedKeys               = []
arrDefaultVer               = []

entropyInput                = 0.0
averageCountBitsPerSymbol   = 0.0
closeCoef                   = 0.0
needModeof                  = False
# =============================================

# Fuctions
# =============================================
def menu() -> None:
    print(""" -= Menu =-
0. Menu
1. Encode
2. Decode
3. Exit""")


# =============================================

# Main program cycle
# =============================================
class Program:

    def main():
        Program.DataIntializationInputText()
        Program.CalculatePossibility()
        Program.GlobalScript()
        Program.CodingText()
        Program.SetDGVSDI()


    @classmethod
    def EnterData():
        global Text

        Text = input("[TEXT] >> ")

    @classmethod
    def DataIntializationInputText():
        global SDI, codingTable

        SDI         = dict()
        codingTable = dict()


    @classmethod
    def CalculatePossibility():
        global Text

        for el in Text:
            if not el in SDI:
                SDI[el] = Text.count(el) / len(Text)
            if not codingTable.get(el, 0):
                codingTable[el] = ""

    @classmethod
    def GlobalScript():
        raise NotImplementedError
    

    @classmethod
    def CodingText():
        raise NotImplementedError


    @classmethod
    def SetDGVSDI():
        raise NotImplementedError


# =============================================

# Additional classes
# =============================================

class GlobalScript:
    @classmethod
    def Main():
        GlobalScript.SortSDIAndCalculateEntropy()
        if not needModeof:
            arrDefaultVer = SDI
        arrSortedKeys = SDI.keys()
        GlobalScript.ShenonFanoMainFunc(0, len(SDI.keys()))
        GlobalScript.CalculateAverageCountBitsPerSymbol()
        GlobalScript.AnalizeGettedCountAndInputEntropy()
        Program.CodingText()
        Program.SetDGVSDI()

    @classmethod
    def ShenonFanoMainFunc(L: int, R: int):
        raise NotImplementedError

    @classmethod
    def CalculateAverageCountBitsPerSymbol():
        raise NotImplementedError

    @classmethod
    def AnalizeGettedCountAndInputEntropy():
        raise NotImplementedError


# =============================================


def work_with_text( text: str ) -> None:
    text = text.lower()
    I = 0
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '/', '*', '!', '@', '#', '$', '%', '^', '&', '?', '(', ')', '[', ']', '{', '}', ' ']
    #Sorting
    for i in symbols:
        c = collections.Counter()
        for symbol in text:
             c[symbol] += 1
    Total = sum(c.values())
    #Shannon's formula
    for i in symbols:
        for symbol in text:
            n = c[i]
        if n > 0:   
            #print(i, c[i]) # Number of certain characters
            p = n / Total # Probability
            I += math.log2(1/p) # Entropy
            # За необхідністю зробити вивід p або I
    pass
    




