#!/usr/bin/python3

# TODO:
"""
Варіанти:
                укр     рус      англ
    Варіант 1:  +       +(той же) +(той же)
    (зв'язаний)

    Варіант 3:  +       +(рівний по сим) +(рів по сим)
    (не зв'яз)

Варіант по номеру команди: 3
Середня кількість слів тексту: 2.000
Варіанти задач: 1,3

Розробити проект для підрахунку кількості інформації на довільному
сайті з використанням обраної методології розробки ПЗ (Канбан, Скрам,
ін.).

Проект повинен дозволяти:
- Визначати кількість інформації на будь-якому сайті.
- Письмовий звіт щодо виконання завдання 2 повинен містити:
- Графічне представлення процесу підрахунку кількості символів
на сайті з використанням методології функціонального моделювання
IDEF0.

Результати розрахунків.
Важливо: категорично ЗАБОРОНЕНО використовувати результати
рішень інших команд. У разі виявлення цього факту вся команда буде
дискваліфікована!!

Після виконання роботи команди повинні подати:
1. Звіт (поштою).
2. Презентацію на пошту.
Презентація повинна містити:
1. Титульний аркуш.
2. Команда з фото і з переліком членів.
3. Опис задачі з математичними моделями.
4. Коротка інформація щодо використовуваної методології з
артефактами її застосування (скриншоти, ін.).
5. Скріншоти програми (за двома завданнями). Графіки обов'язково!
6. Блок схема в IDEF0.
7. Висновки.

Захист роботи виконується публічно за участю усієї команди.
Час на презентацію – 10 хв

"""

# Основна функція виконання
def main():
    pass


# Якщо файл запускається як основний, то викликати основну функцію
if __name__ == "__main__":
    main()
# Інакше повідомити про помилку
else:
    print("[ERR] Sorry, it can't be used like a module")
    
    
# Початок коду!
import random
import string
import pandas as pd
phrase = ""
length = 50
i = 0
#Input language
print('Input "rus" only in small letters')
lang = input("Enter language")
#ENG
if lang == 'Eng' or 'eng' or 'ENG' :
    for i in range(0, 40):
        letters_and_digits = string.ascii_letters + string.digits
        time = ''.join(random.sample(letters_and_digits, length))
        phrase += time
        i += 1

#UKR
if lang == 'Ukr' or 'ukr' or 'UKR':
    f = open('ukr.txt', 'r')

#rus
if lang == 'rus':
    f = open('rus.txt', 'r')

#Character count
quantity = {'Symbols': 0, 'Letters': 0, 'Numbers': 0}
for i in phrase:
    if i.isalpha():
        quantity['Letters'] += 1
    elif i.isdigit():
        quantity['Numbers'] += 1
    else:
        quantity['Symbols'] += 1
Total = quantity['Numbers'] + quantity['Letters'] + quantity['Symbols']
#Output
print(pd.Series(list(phrase)).value_counts())
print('Numbers: %d, Letters: %d, Symbols: %d' % ( quantity['Numbers'], quantity['Letters'], quantity['Symbols']))
print('Total: %d' % Total)
