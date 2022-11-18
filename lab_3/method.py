from .task_1 import unique,log2

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


def Encode(text: str, symbols: str, codes: str):
    code = text.replace('1', '')

