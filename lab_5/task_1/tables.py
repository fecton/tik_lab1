import numpy as np
from math import log2
from huffman import HuffmanTree
from convertText import result

def CalcEntropy(probabilities: list = []):
    entropy = 0
    for a in probabilities:
        entropy += a * log2(a)
    return -entropy

def CalcAverageLengthPerSymb(probab: dict = {}, codes: dict = {}):
    n_c = 0
    for k,v in probab:
        n_c += v * len(codes[k])
    return n_c

def CalcAverageLength(codes: dict = {}):
    n = 0
    for k,v in codes:
        n += len(v)
    n /= len(codes)

def Table1(text: str = ""):
    if(len(text) == 0):
        return
    
    hf = HuffmanTree()

    tmpDict = hf.BuildNodes(text)
    result.table_2_Prob = tmpDict
    result.table_2_Prob = result.NormalizeIndex(result.table_2_Prob)
    
    codes = hf.BuildHuffmanTree()

    m = len(codes.keys())
    dgv = [["" for y in range(m)] for x in range(m)]

    a = list(codes.keys())
    b = list(codes.values())
    for i in range(m):
        dgv[0][i] = a[i]
        bt = b[i]
        for o in bt:
            if(bool(o) == True):
                dgv[3][i] += '1'
            else:
                dgv[3][i] += '0'

        dgv[1][i] = "x%d" % i
        dgv[2][i] = hf.Frequencies[a[i]]
        dgv[4][i] = len(dgv[3][i])
    
    newDict = {}
    for i in range(0, len(a)):
        newDict[str(i)] = b[i]

    result.table_2_Code = newDict


def Table2(text: str = ""):
    newDict = result.GetDictionaryForTable3(3)
    hf = HuffmanTree()
    tmpDict = hf.BuildNodes(result.table_3_Prob)

    codes = hf.BuildHuffmanTree()
    result.table_3_Code = codes

    a = list(codes.keys())
    b = list(codes.values())

    m = len(a)

    dgv = [["" for y in range(m)] for x in range(m)]
    for i in range(0,m):
        bt = b[i]
        for o in bt:
            if(bool(o) == True):
                dgv[3][i] += "1"
            else:
                dgv[3][i] += "0"
        dgv[1][i] = "x%d" % i
        dgv[2][i] = hf.Frequencies(a[i])
        dgv[4][i] = len(dgv[3][i])

    dgv[0][0] = "x1*x1"
    dgv[1][1] = "x1*x2"
    dgv[0][2] = "x2*x1"
    dgv[0][3] = "x2*x2"


def Table3(text: str = ""):
    newDict = result.GetDictionaryForTable3(4)

    hf = HuffmanTree()

    tmpDict = hf.BuildNodes(result.table_4_Prob)
    codes = hf.BuildHuffmanTree()
    result.table_4_Code = codes

    a = list(codes.keys())
    b = list(codes.values())

    m = len(a)
    dgv = [["" for y in range(m)] for x in range(m)]

    orderedNodes = sorted(hf.nodes, key=lambda item: item.AddName)
    i = 0
    
    for o in hf.Frequencies:
        dgv[1][i] = "x%d" % i 
        dgv[2][i] = str(o)
        for q in codes[o]:
            if(bool(q) == True):
                dgv[3][i] += "1"
            else:
                dgv[3][i] += "0"
        dgv[4][i] = len(dgv[3][i])
        i+=1
    
    dgv[0][0] = "x1*x1*x1"
    dgv[0][1] = "x1*x1*x2"
    dgv[0][2] = "x1*x2*x1"
    dgv[0][3] = "x1*x2*x2"
    dgv[0][4] = "x2*x1*x1"
    dgv[0][5] = "x2*x1*x2"
    dgv[0][6] = "x2*x2*x1"
    dgv[0][7] = "x2*x2*x2"


def Table4(text: str = ""):
    newDict = result.GetDictionaryForTable3(5)

    hf = HuffmanTree()
    tmpDict = hf.BuildNodes(result.table_5_Prob)
    codes = hf.BuildHuffmanTree()
    result.table_5_Code = codes

    a = list(codes.keys())
    b = list(codes.values())

    m = len(a)
    dgv = [["" for y in range(m)] for x in range(m)]
    orderedNodes = sorted(hf.nodes, key=lambda item: item.AddName)
    i = 0

    for o in hf.Frequencies:
        dgv[1][i] = "x%d" % i 
        dgv[2][i] = str(o)
        for q in codes[o]:
            if(bool(q) == True):
                dgv[3][i] += "1"
            else:
                dgv[3][i] += "0"
        dgv[4][i] = len(dgv[3][i])
        i+=1
    
    dgv[0][0] = "x1*x1*x1*x1"
    dgv[0][1] = "x1*x1*x1*x2"
    dgv[0][2] = "x1*x1*x2*x1"
    dgv[0][3] = "x1*x1*x2*x2"
    dgv[0][4] = "x1*x2*x1*x1"
    dgv[0][5] = "x1*x2*x1*x2"
    dgv[0][6] = "x1*x2*x2*x1"
    dgv[0][7] = "x1*x2*x2*x2"
    dgv[0][8] = "x2*x1*x1*x1"
    dgv[0][9] = "x2*x1*x1*x2"
    dgv[0][10] = "x2*x1*x2*x1"
    dgv[0][11] = "x2*x1*x2*x2"
    dgv[0][12] = "x2*x2*x1*x1"
    dgv[0][13] = "x2*x2*x1*x2"
    dgv[0][14] = "x2*x2*x2*x1"
    dgv[0][15] = "x2*x2*x2*x2"


COUNT_GROUP = 4
dgv = [["" for y in range(COUNT_GROUP)] for x in range(COUNT_GROUP)]

class Table6:

    def SetGenerallyParams():
        listProbab = [
            result.table_2_Prob,
            result.table_3_Prob,
            result.table_4_Prob,
            result.table_5_Prob
        ]
        dgv = Table6.dgv
        dgv[0][0] = str(log2(2))
        dgv[0][1] = str(log2(4))
        dgv[0][2] = str(log2(8))
        dgv[0][3] = str(log2(16))
        for i in range(0,Table6.COUNT_GROUP):
            dgv[1][i] = (CalcEntropy(listProbab[i]))


    def SetParamsRow(tableN: int = 2):
        arr = [result.table_2_Prob, result.table_3_Prob, result.table_4_Prob, result.table_5_Prob]
        rra = [result.table_2_Code, result.table_3_Code, result.table_4_Code, result.table_5_Code]

        index = -2 + tableN
        
        prob = arr[index]
        code = rra[index]

        dgv[5][index] = CalcAverageLengthPerSymb(prob, code)
        dgv[4][index] = CalcAverageLength(code)
        dgv[3][index] = 1 - (float(dgv[1][index]) / log2(2**(tableN - 1)))

        tmp = float(dgv[5][0])

        dgv[7][index] = (tmp - float(dgv[1][index])) / tmp
        dgv[2][index] = min((result.table_2_Code),key=lambda item: len(item))
        dgv[6][index] = float(dgv[2][index]) / float(dgv[5][index])

    
    def SetParamsRow(table_number: int = 2):
        arr = [result.table_2_Code, result.table_3_Code, result.table_4_Code, result.table_5_Code]
        rra = [result.table_2_Prob, result.table_3_Prob, result.table_4_Prob, result.table_5_Prob]

        # -2 + 2 = 0
        # -2 + 3 = 1
        # -2 + 4 = 2
        # -2 + 5 = 3

        index = -2 + table_number

        prob = arr[index]
        code = rra[index]

        dgv = Table6.dgv
        dgv[5][index] = CalcAverageLengthPerSymb(prob, code)
        dgv[4][index] = CalcAverageLength(code)
        dgv[3][index] = 1 - (float(dgv[1][index]) / log2(2*(table_number-1)))

        tmp = float(dgv[5][0])

        dgv[7][index] = (tmp - float(dgv[1][index])) / tmp
        dgv[2][index] = min((code),key=lambda item: len(item))
        dgv[6][index] = float(dgv[2][index]) / float(dgv[5][index])

