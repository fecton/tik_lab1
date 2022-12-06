# MODULES
# =====================================================
from math import floor
# =====================================================

SUBSTRING_LEN = 5

# CLASSES
# =====================================================
class Text:
    def __init__(self, text: str):
        self.text                   = text
        self.length                 = len(text)
        self.nodes                  = []
        self.frequencies            = {}
        self.SymbolsPerSubstring    = SUBSTRING_LEN
        self.splitedStrings         = []

        self.resNodes               = []
    
    def Build(self):
        # Build
        source = self.text
        for i in range(len(source)):
            if source[i] not in self.frequencies.values():
                self.frequencies[source[i]] = 0
            self.frequencies[source[i]] += 1

        for key,value in self.frequencies.items():
            self.nodes.append({"symbol": key, "frequency": value})

        self.nodes = sorted(self.nodes, key=lambda x: x["frequency"])

        # Get Symbols Ranges
        low = 0.0
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            n["range"] = n["frequency"] / self.length
            n["low"] = low
            n["high"] = low + n["range"]
            low += n["range"]

        # Split str on N Symbols
        if self.length < self.SymbolsPerSubstring:
            self.splitedStrings.append(self.text)
        
        i = 0
        j = 0
        while i < self.length:
            self.splitedStrings.append(self.text[i:i+self.SymbolsPerSubstring])

            i += self.SymbolsPerSubstring
            j += 1

        f = open("splited.txt", "w", encoding="utf-8")
        for s in self.splitedStrings:
            f.write(s)
        f.close()
        print("Splited strings: COMPLETED\nCheck splited.txt", end="\n"*2)

        f = open("encode.txt", "w", encoding="utf-8")
        for s in self.splitedStrings:
            res = self.Encode(s)
            f.write(str(res))
        f.close()
        print("Encoded strings: COMPLETED\nCheck encode.txt", end="\n"*2)

        f = open("binary.txt", "w", encoding="utf-8")
        for s in self.splitedStrings:
            res = self.Encode(s)
            t = self.GetFractionPart(res)
            t = bin(t)[2:]
            f.write(t)
        f.close()
        print("Binary text: COMPLETED\nCheck binary.txt", end="\n"*2)

    def GetFractionPart(self, number):
        fractionPartStr = (number - floor(number))
        fractionPartStr = "%.8f" % fractionPartStr
        fractionPartStr = fractionPartStr.split('.')[1]
        return int(fractionPartStr)

    def Encode(self, source: str = ""):
        self.nodes.reverse()

        allNodes = []
        
        for i in range(len(source)):
            for j in range(len(self.nodes)):
                n = self.nodes[j]
                if source[i] == n["symbol"]:
                    allNodes.append({"symbol": n["symbol"], "low": n["low"], "high": n["high"]})

        for i in range(1,len(allNodes)):
            for j in range(len(self.nodes)):
                n = self.nodes[j]
                a = allNodes[i]
                if a["symbol"] == n["symbol"]:
                    a_ = allNodes[i-1]
                    a["high"] = a_["low"] + (a_["high"] - a_["low"]) * n["high"]
                    a["low"] = a_["low"] + (a_["high"] - a_["low"]) * n["low"]
        self.resNodes = allNodes

        # print(self.nodes)
        # print(allNodes)

        return round(
            (allNodes[len(allNodes)-1]["low"] + 
            (
                (allNodes[len(allNodes)-1]["high"] - 
                allNodes[len(allNodes)-1]["low"]) / 2
            ) 
            ), 8
        )


# =====================================================



# GLOBAL VARIABLES
# =====================================================
with open('text.txt', 'r', encoding='utf-8') as f:
    MainText = Text(f.read())

# =====================================================



# MAIN CODE
# =====================================================
MainText.Build() 
# =====================================================
