# Modules
# =========================================
from math import log2
# =========================================

# Functions
# =========================================
def ShenonFanoMainFunc(L: int, R: int):
        # defining half
    half = 0
    arrSDValues = list(StringDictionary.values())
    i = L
    M = i

    for j in range(L, R):
        half += arrSDValues[j]

    half /= 2

    counterValue = 0
    while( (counterValue + arrSDValues[i] < half) and (i < R) ):
        counterValue += arrSDValues[i]
        i += 1
    deltaFromTopSide    = abs(half - counterValue)
    deltaFromBottomSide = abs((counterValue + arrSDValues[i]) - half)

    if( (deltaFromTopSide > deltaFromBottomSide) and (i < R) ):
        i += 1

    half = i
    for j in range(L, half):
        codingTable[arrSortedKeys[j]] += "1"
    for j in range(half, R):
        codingTable[arrSortedKeys[j]] += "0"

    if half - L > 1:
        ShenonFanoMainFunc(L, half)
    if R - half > 1:
        ShenonFanoMainFunc(half, R)
# =========================================

TextToEncode = "интересно"

StringDictionary    = {}
codingTable         = {}

# Підрахувати вірогідність появлень
# Та заповнити словник літерами з пустими значеннями для майбутнього кодування
for el in TextToEncode:
    if not StringDictionary.get(el, 0):
        StringDictionary[el] = TextToEncode.count(el) / len(TextToEncode)

    if not codingTable.get(el, 0):
        codingTable[el] = ""

entropyInput = 0
StringDictionary = {k:v for k,v in sorted(StringDictionary.items(), key=lambda item : item[1], reverse=True)}

for possibility in StringDictionary.values():
    entropyInput += possibility * log2(possibility)
entropyInput = abs(entropyInput)
print("Entropy : ", round(entropyInput, 4))


arrDefaultVar = list(StringDictionary.values())
arrSortedKeys = list(StringDictionary.keys())

# GlobalScript
# =========================================
# ShenonFanoMainFunc
ShenonFanoMainFunc(0, len(StringDictionary.keys()))

# CalcAverageCountBitsPerSymb
averageCountBitsPerSymbol = 0
for ch in codingTable.keys():
    averageCountBitsPerSymbol += StringDictionary[ch] * len(codingTable[ch])

print("Average Count Bits Per Symbol : ", round(averageCountBitsPerSymbol, 4))

# AnalizGettedCountAndInputEntropy
closeCoef = (averageCountBitsPerSymbol - entropyInput) / entropyInput
print("Degree of closeness : ", round(closeCoef, 4))

if(closeCoef > 0.15):
    needModef = True
    # ModificateSDI
    # ChnageCodingTable
    # SetDGVSDI
    # GlobalScript
# =========================================

# CodingText
res = ""
for i in range(len(TextToEncode)):
    res += codingTable[TextToEncode[i]]
print("Coded text : ", res)

# SetDGVSDI
print("\tSymbol\tPossibility")
for k,v in StringDictionary.items():
    print("\t{0}\t{1}".format(k,v))

print()
print("Encode table")
for k,v in codingTable.items():
    print("\t{0}\t{1}".format(k,v))


