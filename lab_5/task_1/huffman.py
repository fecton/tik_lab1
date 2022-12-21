class Node:
    def __init__(self, symbol: str = "", frequency: float = 0.0, Right = None, Left = None, addName: str = ""):
        self.symbol     = symbol
        self.frequency  = frequency
        self.Right      = Right
        self.Left       = Left
        self.AddName    = addName

    def __str__(self) -> str:
        return "symbol: {0}, frequency: {1}, right: {2}, left: {3}, addname: {4}".format(self.symbol, self.frequency, self.Right, self.Left, self.AddName)

    def Traverse(self, symbol: str = "", data: list = []):
        if(self.Right == None and self.Left == None):
            if(symbol == self.symbol):
                return data
            else:
                return None
        else:
            left  = []
            right = []

            if(self.Left != None):
                leftPath = []
                leftPath += data
                leftPath.append(False)
                
                left = self.Left.Traverse(symbol, leftPath)
            
            if(self.Right != None):
                rightPath = []
                rightPath += data
                rightPath.append(True)

                right = self.Right.Traverse(symbol, rightPath)
            
            if(left != None):
                return left
            else:
                return right


class HuffmanTree:
    def __init__(self):
        self.indexAddName   = 0
        self.nodes          = []
        self.root           = None
        self.Frequencies    = {}
    

    def BuildNodes(self, text: str = ""):
        if(len(text) == 0):
            return None
        self.Frequencies = {}
        for c in text:
            if(c not in self.Frequencies.keys()):
                self.Frequencies[c] = text.count(c) / len(text)

        self.nodes = []
        self.indexAddName = 0

        self.Frequencies = {k:v for k,v in sorted(self.Frequencies.items(), key=lambda item: item[1], reverse=True)}
        tmp = "Build nodes\n"
        for k,v in self.Frequencies.items():
            tmp += "{0} - {1}\n".format(k, str(v)) + "\n"
            # self.nodes.append({"symbol": k, "frequency": v, "addName": "x"+str(self.indexAddName)})
            self.nodes.append(Node(k, v, None, None, "x"+str(self.indexAddName)))
            self.indexAddName += 1
        # print(tmp)
        return self.Frequencies
    

    def BuildNodes2(self, inputProbabilities: dict = {}):
        self.Frequencies = inputProbabilities

        self.nodes = []
        self.indexAddName = 0

        for k,v in self.Frequencies:
            # self.nodes.append({"symbol": k, "frequency": v, "addName": "x"+str(self.indexAddName)})
            self.nodes.append(Node(k,v,None,None,"x"+str(self.indexAddName)))
            self.indexAddName += 1
        
        return self.Frequencies
    

    def BuildHuffmanTree(self):
        while len(self.nodes) > 1:
            orderedNodes = sorted(self.nodes, key=lambda item: item.AddName, reverse=True)
            if(len(orderedNodes) >= 2):
                taken = orderedNodes[:2]
                # parent = {
                #     "symbol": "!",
                #     "frequency": taken[0]["frequency"] + taken[1]["frequency"],
                #     "left": taken[0],
                #     "right": taken[1],
                #     "addName": "x"+str(self.indexAddName)
                # }
                parent = Node(
                    symbol="!",
                    frequency=taken[0].frequency + taken[1].frequency,
                    Left = taken[0],
                    Right = taken[1],
                    addName="x"+str(self.indexAddName)
                )
                # self.nodes.remove(taken[0])
                # self.nodes.remove(taken[1])
                self.nodes.append(parent)
                self.nodes.pop(0)
                self.nodes.pop(0)
                # from pprint import pprint
                # pprint([str(x) for x in self.nodes])
            
            if self.nodes[0]:
                self.Root = self.nodes[0]
            else:
                self.Root = 0
        
        huffmanCodesTable = {}
        tmp = "Frequencies:\n"
        for k,v in self.Frequencies.items():
            tmp += "key: {0} | value: {1}\n".format(k,v)
        # print(tmp)
        
        for k in self.Frequencies.keys():
            huffmanCodesTable[k] = self.Root.Traverse(k, [])

        return huffmanCodesTable
    

    def Encode(self, source: str = ""):
        encodedSource = []
        for i in range(len(source)):
            encodedSymbol = self.Root.Traverse(source[i], [])
            encodedSource += encodedSymbol
        return encodedSource


    def Decode(self, bits: list = []):
        current = self.Root
        decoded = ""

        for bit in bits:
            if(bit):
                if(current.Right != None):
                    current = current.Right
            else:
                if(current.Left != None):
                    current = current.Left

            if (current.Left == None and current.Right == None):
                decoded += current["symbol"]
                current = self.Root

        return decoded






