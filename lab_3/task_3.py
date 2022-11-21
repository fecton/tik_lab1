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

from math import log2
from task_1 import unique

def size_caulculation(s: str) -> dict:
    """
    Підраховує кількість символів і повертає у вигляді словника
    @param s Текст

    @return Словник з унікальними ключами та їх кількістю
    """
    d = {}

    for i in unique(s):
        d[i] = s.count(i)
    
    return d

def probability(s: str) -> list:
    """
    Приймає строку і повертає вірогідність кожного символу

    @param d Строка

    @return Повертає можливість появи кожного елемента
    """

    d = size_caulculation(s)
    
    arr = []
    i = 0
    for symbol in d.keys():
        arr[i] = d[symbol] / len(s)
        i += 1
    return arr


def Entropy(nums: list) -> float:
    sum = 0.
    
    for i in range(len(nums)):
        d = log2(nums[i])
        sum += d * nums[i]

    return abs(sum)
    

def DivisionGroups(arr: list):
    deltas = []
    divIndex = len(arr) - 1
    sum1 = 0
    sum2 = 0
    for index in range(1,len(arr)):
        sum1 += arr[index]
        for i in range(index, len(arr)):
            sum2 += arr[i]

        deltas[index - 1] = sum1 - sum2
        if(index > 1 and abs(deltas[index-2]) < abs(deltas[index-1])):
            divIndex = index - 1
            break

    return divIndex

def ShannonFanoRec(arr: list, codShannon: str, start: int) -> None:
    divIndex = DivisionGroups(arr)

    for i in range(0,divIndex):
        codShannon[start + i] += "0"

    for i in range(divIndex, len(arr)):
        codShannon[start + i] += "1"

    if divIndex > 1:
        leftpart = arr[divIndex]

    if divIndex < len(arr)-1:
        rightpart = arr[divIndex+1:]
        ShannonFanoRec(rightpart, codShannon, start + divIndex)


def Encode(text: str):
    s1 = 'ッ'    
    s2 = 'あ'

    code = text.replace('1', s1)
    code = code.replace('0', s2)

    # indexOf = symbols.index('1')
    # if indexOf >= 0:
    #     symbols[indexOf] = s1
    
    # indexOf = symbols.index('0')
    # if indexOf >= 0:
    #     symbols[indexOf] = s2

    # indexOf = symbols.index(s1)
    # if(indexOf >= 0):
    #     symbols[indexOf] = '1'

    # indexOf = symbols.index(s2)
    # if indexOf >= 0:
    #     symbols[indexOf] = '0'

    return code

def Decode(code: str):
    s1 = 'ッ'    
    s2 = 'あ'

    text = code

    text = text.replace(s1, '0')
    text = text.replace(s2, '1')
    #     symbols[indexOf] = s1
    
    # indexOf = symbols.index('0')
    # if indexOf >= 0:
    #     symbols[indexOf] = s2
    
    # text = ""
    # for i in range(0,len(code)):
    #     for j in range(0,len(symbols)):
    #         if code[i:len(codes[j])] == codes[j]:
    #             text += symbols[j]
    #             t += len(codes[j]) - 1
    #             break
    
    # indexOf = symbols.index(s1)
    # if indexOf >= 0:
    #     text = text.replace(s1, '1')
    
    # indexOf = symbols.index(s2)
    # if indexOf >= 0:
    #     text = text.replace(s2, '0')

    # indexOf = symbols.index(s2)
    # if indexOf >= 0:
    #     symbols[indexOf] = '1'

    # indexOf = symbols.index(s2)
    # if indexOf >= 0:
    #     symbols[indexOf] = '0'
    
    return text

def menu():
    print(""" Menu
    - 1. Encode
    - 2. Decode
    - 3. Exit
    """)

op = 0
while 1:
    match op:
        case 0:
            menu()
        case 1:
            value = input("Enter value to encode: ")
            print("Encoded: ", Encode(value))
        case 2:
            value = input("Enter value to decode: ")
            print("Decoded: ", Decode(value))
        case 3:
            exit()
        case _:
            print("Invalid operation!")
    op = int(input('>> '))