class Node():
    def __init__(self):
        self.value = None
        self.children = []
    def Evaluate():
        pass

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,symbolTable):
        return self.value

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbolTable):
        if self.value == "=":
            #print(self.children[0],self.children[1].Evaluate(symbolTable),self.value)
            symbolTable.createValue(self.children[0],self.children[1].Evaluate(symbolTable))
        else: 
            if self.value == '+':
                return self.children[0].Evaluate(symbolTable)+self.children[1].Evaluate(symbolTable)
            elif self.value == '-':
                return self.children[0].Evaluate(symbolTable)-self.children[1].Evaluate(symbolTable)
            elif self.value == '*':
                return self.children[0].Evaluate(symbolTable)*self.children[1].Evaluate(symbolTable)
            elif self.value == '/':
                return self.children[0].Evaluate(symbolTable)//self.children[1].Evaluate(symbolTable)
            elif self.value == '>':
                return self.children[0].Evaluate(symbolTable)>self.children[1].Evaluate(symbolTable)
            elif self.value == '<':
                return self.children[0].Evaluate(symbolTable)<self.children[1].Evaluate(symbolTable)
            elif self.value == '==':
                return self.children[0].Evaluate(symbolTable)==self.children[1].Evaluate(symbolTable)
            elif self.value == '&&':
                return self.children[0].Evaluate(symbolTable) and self.children[1].Evaluate(symbolTable)
            elif self.value == '||':
                return self.children[0].Evaluate(symbolTable) or self.children[1].Evaluate(symbolTable)

class PrintfNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,symbolTable):
        print(self.children[0].Evaluate(symbolTable))

class IfElseNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,symbolTable):
        if self.children[0].Evaluate(symbolTable):
            return self.children[1].Evaluate(symbolTable)
        elif self.children[2] != None:
            return self.children[2].Evaluate(symbolTable)

class WhileNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,symbolTable):
        while self.children[0].Evaluate(symbolTable):
            self.children[1].Evaluate(symbolTable)

class StatmentsNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,symbolTable):
        for i in self.children:
            i.Evaluate(symbolTable)

class VarVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,symbolTable):
        #print("OLAAa", self.value)
        return symbolTable.getValue(self.value)

class SymbolTable():
    def __init__(self):
        self.symbolTable = {} 

    def getValue(self, key):
        print("OLAA", self.symbolTable)
        if key in self.symbolTable:
            return self.symbolTable.get(key)

    def createValue(self,key,value):
        #print("oi",key,value)
        self.symbolTable['{}'.format(key)] = value    