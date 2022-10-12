#!/usr/bin/python3

from math import log

# Тексти
# Функція, що повертає текст з файлів
def getc(filename: str) -> str:
    return open(filename+".txt", encoding="utf-8").read()

# Дістаємо текст з файлів
UKRAINIAN_TEXT = getc("ukrainian")
ENGLISH_TEXT = getc("english")
GERMAN_TEXT = getc("german")

INCOHERENT_ENG = getc("in_english")
INCOHERENT_UKR = getc("in_ukrainian")
INCOHERENT_GER = getc("in_german")

# Алфавіти
ENGLISH_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
GERMAN_ALPHABET = "abcdefghijklmnopqrstuvwxyzäöüß"


# Потужність алфавіту
ENG_PWR     = 23
UKR_PWR     = 33
GER_PWR  = 30

# Задання кількості символів за трьома різними мовами двох текстів
def alphabet_symbol_count() -> list:

    arr = [{},{},{},{},{},{}]
    mass = [
        (ENGLISH_TEXT, ENGLISH_ALPHABET), 
        (UKRAINIAN_TEXT, UKRAINIAN_ALPHABET), 
        (GERMAN_TEXT, GERMAN_ALPHABET),

        (INCOHERENT_ENG, ENGLISH_ALPHABET), 
        (INCOHERENT_UKR, UKRAINIAN_ALPHABET), 
        (INCOHERENT_GER, GERMAN_ALPHABET)
    ]

    i = 0
    for text, alphabet in mass:
        text = text.lower()
        for symbol in alphabet:
            if text.count(symbol) > 0:
                arr[i][symbol] = text.count(symbol)
        i+=1

    return arr


# Основна функція
def main():
    CUSTOM_TEXT = ""
    op = 0
    while 1:
        # Свитч меню
        match op:
            # Менюшка
            case 0:
                print("""Меню:
0. Показати це меню
1. Вивести текстів
2. Частота якогось символу
3. Розмір текстів
4. Ввести свій текст 
""")
            # Вивести тексти
            case 1:
                print("Зв'язані тексти: ")
                print("УКРАЇНСЬКИЙ ТЕКСТ")
                print(UKRAINIAN_TEXT, end="\n"*3)

                print("АНГЛІЙСЬКИЙ ТЕКСТ")
                print(ENGLISH_TEXT, end="\n"*3)

                print("НІМЕЦЬКИЙ ТЕКСТ")
                print(GERMAN_TEXT, end="\n"*6)


                print("Не зв'язані тексти: ")
                print("УКРАЇНСЬКИЙ ТЕКСТ")
                print(INCOHERENT_UKR, end="\n"*3)

                print("АНГЛІЙСЬКИЙ ТЕКСТ")
                print(INCOHERENT_ENG, end="\n"*3)

                print("НІМЕЦЬКИЙ ТЕКСТ")
                print(INCOHERENT_GER, end="\n"*3)

            # Підрахувати кількість усіх символів, або показити лише заданий
            case 2:
                if not CUSTOM_TEXT:
                    arr = alphabet_symbol_count()

                    # Відсортувати кожний словник
                    for i in range(6):
                        arr[i] = {k: v for k, v in sorted(arr[i].items(), key=lambda x: x[1], reverse=False)}

                    symbol = input("СИМВОЛ (скіп, якщо хочеш побачити усю кількість символів): ")

                    textes = [ENGLISH_TEXT, UKRAINIAN_TEXT, GERMAN_TEXT, INCOHERENT_ENG, INCOHERENT_UKR, INCOHERENT_GER]
                    names = ["англійському", "українському", "німецькому"] * 2

                    if symbol:
                        for i in range(6):
                            if i % 3 == 0 and i != 0:
                                print("Не зв'язані тексти")
                            elif i == 0:
                                print("Зв'язані тексти")
                            try:
                                print(f"У {names[i]} тексті символ '{symbol}' з частотою {arr[i][symbol] / len(textes[i])}")
                            except KeyError:
                                print(f"У {names[i]} тексті символ '{symbol}' не наявний") 
                    else:
                        for i in range(6):
                            print(f"[+] {names[i].title()}", end="")
                            if i > 2:
                                print(" (не зв'язана): ")
                            else:
                                print(": ") 
                        
                            print(len(arr[i].keys()))
                            for k,v in arr[i].items():
                                # print(v, len(textes[i]))
                                print(f"{k} : {v / len(textes[i])}")
                            print(end="\n"*2)
                else:
                    print("[+] Кастомному: ")
                    arr = {}
                    language = input("Мова: (eng/ger/ukr) ")
                    alphabet = ""
                    match language.lower():
                        case "eng":
                            alphabet = ENGLISH_ALPHABET
                        case "ger":
                            alphabet = GERMAN_TEXT
                        case "ukr":
                            alphabet = UKRAINIAN_ALPHABET
                        case _:
                            alphabet = ENGLISH_ALPHABET
                        
                    for symbol in alphabet:
                        if CUSTOM_TEXT.count(symbol) > 0:
                            arr[symbol] = CUSTOM_TEXT.count(symbol)
                    arr = {k: v for k, v in sorted(arr.items(), key=lambda x: x[1])}
                    print(arr)

            # Виведення розмірність тексту
            case 3:
                print("--= Розмірність у бітах =---")

                if not CUSTOM_TEXT:

                    tmp = [UKRAINIAN_TEXT, ENGLISH_TEXT, GERMAN_TEXT, INCOHERENT_UKR, INCOHERENT_ENG, INCOHERENT_GER]
                    pws = [UKR_PWR, ENG_PWR, GER_PWR]
                    j = 0
                    for i in range(6):
                        tmp[i] = len(tmp[i]) * log(pws[j],2) / 1024
                        j += 1
                        if j == 3:
                            j = 0

                    print("Зв'язний текст")
                    print("[+] УКРАЇНСЬКИЙ ТЕКСТ:\t", tmp[0], "МБ")
                    print("[+] АНГЛІЙСЬКИЙ ТЕКСТ:\t", tmp[1], "МБ")
                    print("[+] НІМЕЦЬКИЙ ТЕКСТ:\t", tmp[2], "МБ")

                    print("Не зв'язний текст")
                    print("[+] УКРАЇНСЬКИЙ ТЕКСТ:\t", tmp[3], "МБ")
                    print("[+] АНГЛІЙСЬКИЙ ТЕКСТ:\t", tmp[4], "МБ")
                    print("[+] НІМЕЦЬКИЙ ТЕКСТ:\t", tmp[5], "МБ")
                else:
                    print("[+] Кастомний текст: ", len(CUSTOM_TEXT) * log(ENG_PWR, 2))
            # Введення кастомного тексту
            case 4:
                CUSTOM_TEXT = input("Enter: ")

        op = int(input(">> "))


# Якщо файл запускається як основний, то викликати основну функцію
if __name__ == "__main__":
    main()
# Інакше повідомити про помилку
else:
    print("[ERR] Вибачай, цей не може бути використаним яяк модуль")

