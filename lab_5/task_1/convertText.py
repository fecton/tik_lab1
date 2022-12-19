class ConvertText:
    def __init__(self):
        self.table_2_Prob = {}
        self.table_3_Prob = {}
        self.table_4_Prob = {}
        self.table_5_Prob = {}

        self.table_2_Code = {}
        self.table_3_Code = {}
        self.table_4_Code = {}
        self.table_5_Code = {}
        
    
    def GetProbabilities(self, text: str = "") -> dict:
        if(len(text) == 0):
            return None

        charsProb = {}
        for char in text:
            if(char not in charsProb.keys()):
                charsProb[char] = text.count(char) / len(text)
        
        return charsProb
    
    
    def GetDictionaryForTable3(self, numberOfForm: int = 0) -> dict:
        COUNTS_VAR = 0
        numberTable = None
        middleTable = 0
        
        match(numberOfForm):
            case 3:
                numberTable = self.table_2_Prob
                COUNTS_VAR = 4
                middleTable = 2
            case 4:
                numberTable = self.table_3_Prob
                COUNTS_VAR = 8
                middleTable = 4
            case 5:
                numberTable = self.table_3_Prob
                COUNTS_VAR = 8
                middleTable = 4
        
        newDict = {}
        for i in range(0,COUNTS_VAR):
            if(i < COUNTS_VAR / 2):
                newDict[str(i)] = numberTable[str(i%middleTable)] * self.table_2_Prob['0']
            else:
                newDict[str(i)] = numberTable[str(i%middleTable)] * self.table_2_Prob['1']
        
        match(numberOfForm):
            case 3:
                self.table_3_Prob = newDict
            case 4:
                self.table_4_Prob = newDict
            case 5:
                self.table_5_Prob = newDict
        
        return newDict


    def NormalizeIndex(self, oldDict: dict = {}) -> dict:
        newDict = {}
        for i in range(0, len(oldDict.keys())):
            newDict[str(i)] = list(oldDict.values())[i]
        tmp = "NormalizeIndex"

        a = list(oldDict.keys())
        b = list(oldDict.values())

        for i in range(0, len(oldDict.keys())):
            tmp += "Key: {0} | Value {1}\n".format(a[i], b[i])
        
        print(tmp)
        return newDict


result = ConvertText()




