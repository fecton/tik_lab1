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

from func import *


def main():
    # message = input("Enter your message: ")
    message = "ferfioergjirejigeio"
    # Кількість повторень символів
    sizes = size_caulculation(message)
    print("Повідомлення: %s" % message)

    print("Кількість повторень")
    for key in sizes.keys():
        print("%s : %s" % (key, sizes[key]))

    print("Можливість появи")
    prob = probability(message)
    for i in prob:
        print(round(i, 5), end=" ")
    print()
    print("Ентропія: %f" % Entropy(prob))
    print("Відcортований за спаданням можливість мояви") 
    prob = sorted(prob)
    for i in prob:
        print(round(i, 5), end=" ")
    print()

    ShannonFanoRec(message)

def menu():
    print(""" Menu
    - 1. Encode
    - 2. Decode
    - 3. Exit
    """)

main()
exit()

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