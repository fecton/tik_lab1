from math import log2

def to_2(number: int, maxSize: int = -1) -> str:
    dwa = bin(number)[2:]
    if len(dwa) != maxSize and maxSize != -1:
        dwa = "0"*(maxSize - len(dwa)) + dwa
    return dwa

def unique(s: str) -> str:
    """
    Gets unique values from a string and returns it
    @param s - string
    @return string of unique elements
    """
    a = ""
    for i in s:
        if i not in a:
            a += i
    return a

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
    Приймає строку і повертає вірогідність кожного символу у списку

    @param d Строка

    @return Повертає можливість появи кожного елемента
    """

    d = size_caulculation(s)
    
    arr = []
    for symbol in d.keys():
        arr.append(d[symbol] / len(s))

    return arr


def Entropy(nums: list) -> float:
    """
    Обчислення значення ентропії H(x)

    @param nums Список чисел

    @return Значення ентрпоії
    """

    sum = 0.
    
    for i in range(len(nums)):
        d = log2(nums[i])
        sum += d * nums[i]

    return abs(sum)
    
def ShannonFanoRec(codShannon: str) -> None:
    to_encode_table = {}
    c = 0
    mlength = len(to_2(len(unique(codShannon))))
    for i in unique(codShannon):
        to_encode_table[i] = to_2(c, mlength)
        c += 1
        print("%s : %s" % (i, to_encode_table[i]))
    
    m = codShannon
    for i in unique(codShannon):
        m = m.replace(i, to_encode_table[i])
    print("Повідомлення в оптимальному коді: ", m)    

    decoded = ""
    while m:
        current = m[:3]
        m = m[3:]
        decoded += list(to_encode_table.keys())[(list(to_encode_table.values()).index(current))]

    print("Розкодування прямого коду: ", decoded)

    t = round(len(list(to_encode_table.keys())) / mlength,2)
    print("Середнє на символ число двійкових розрядів коду: ", t)
    print("Ступінь близькості середнього на символ числа двійкових розрядів коду до ентропії: ", t / Entropy(probability(codShannon)))
