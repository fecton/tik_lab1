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
import requests
from bs4 import BeautifulSoup
from collections import Counter
import collections
import math

#Displaying information about the text
print('Information about the university on wikipedia')
print()

#Set url
url = 'https://en.wikipedia.org/wiki/National_Aerospace_University_–_Kharkiv_Aviation_Institute'
response = requests.get(url)
take = BeautifulSoup(response.text, 'lxml')

# Take data
KhAI = take.find_all('div', class_='mw-parser-output')

#Print
for quote in KhAI:
    wikipedia = quote.text.lower()
    print(wikipedia)

I = 0
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '-', '+', '/', '*', '!', '@', '#', '$', '%', '^', '&', '?', '(', ')', '[', ']', '{', '}']
#Sorting
for i in symbols:
    c = collections.Counter()
    for symbol in wikipedia:
         c[symbol] += 1
    print(i, c[i])
Total = sum(c.values())
#Shannon's formula
for i in symbols:
    for symbol in wikipedia:
        n = c[i]
    if n > 0:   
        p = Total / n 
        I += math.log2(1/p)

#Data sorting
quantity = {'Letters': 0, 'Numbers': 0}
for i in wikipedia:
    if i.isalpha():
        quantity['Letters'] += 1
    elif i.isdigit():
        quantity['Numbers'] += 1
Total = quantity['Numbers'] + quantity['Letters']

#Output
print('Numbers: %d, Letters: %d' % ( quantity['Numbers'], quantity['Letters']))
print('Total: %d' % Total)
print('I = %d' % -I)


# Якщо файл запускається як основний, то викликати основну функцію
if __name__ == "__main__":
    main()
# Інакше повідомити про помилку
else:
    print("[ERR] Sorry, it can't be used like a module")
    
