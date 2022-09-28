import random
import string
import codecs
import pandas as pd

phrase = ""
length = 50
i = 0
lang = 0
while lang < 4:
    #ENG
    if lang == 1 :
        print('English language')
        for i in range(0, 40):
            letters_and_digits = string.ascii_letters + string.digits
            time = ''.join(random.sample(letters_and_digits, length))
            phrase += time

    #UKR
    if lang == 2:
        print('Ukrainian language')
        with codecs.open('ukr.txt', encoding='utf-8') as fin:
            phrase = next(fin)

    #rus
    if lang == 3:
        print('russian language')
        with codecs.open('rus.txt', encoding='utf-8') as fin:
            phrase = next(fin)

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
    phrase = ''
    lang += 1


import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/National_Aerospace_University_–_Kharkiv_Aviation_Institute'
response = requests.get(url)
take = BeautifulSoup(response.text, 'lxml')
name = take.find_all('span', class_='mw-page-title-main')
faculty = take.find_all('li', class_='marker')

for quote in name:
    print(quote.text)

for quote in faculty:
    print(faculty.text)