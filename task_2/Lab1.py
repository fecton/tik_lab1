import requests
from bs4 import BeautifulSoup

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
    wikipedia = quote.text
    print(wikipedia)

#Data sorting
quantity = {'Symbols': 0, 'Letters': 0, 'Numbers': 0}
for i in wikipedia:
    if i.isalpha():
        quantity['Letters'] += 1
    elif i.isdigit():
        quantity['Numbers'] += 1
    else:
        quantity['Symbols'] += 1
Total = quantity['Numbers'] + quantity['Letters'] + quantity['Symbols']

#Output
print('Numbers: %d, Letters: %d, Symbols: %d' % ( quantity['Numbers'], quantity['Letters'], quantity['Symbols']))
print('Total: %d' % Total)
print('The site is encoded in UTF-8 format, 1 character = 1 Byte => %d Byte or %d KB' % ( Total, round(Total / 1024)))
