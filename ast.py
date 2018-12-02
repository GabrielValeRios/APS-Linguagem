# -*- coding: utf-8 -*-
class Node():
    def __init__(self):
        self.value = None
        self.children = []
    def Evaluate():
        pass

class masterNode(Node):
    def __init__(self,children):
        self.children = children

    def Evaluate(self):
        symbolTable = SymbolTable()
        for i in self.children:
            i.Evaluate(symbolTable)

class returnNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,symbolTable):
        ans = self.children[0].Evaluate(symbolTable)
        return ans

class funcDec(Node):
    def __init__(self,value,children):
        self.value = value
        self.children = children
		
    def Evaluate(self,symbolTable):
        symbolTable.createValue(self.value,self)
        #symbolTable.setValue(self.value,self)

class funcCall(Node):
    def __init__(self,value,children):
        self.value = value
        self.children = children
        self.NewSymbolTable = SymbolTable() #Passar a symboltable atual como ancestor

    def Evaluate(self,symbolTable):
        self.NewSymbolTable.ancestor = symbolTable
        func = symbolTable.getValue(self.value)
        argsName = []
        for i in range(0, len(func.children)-1):
            if func.children[i] != None:
                for j in func.children[i].children:
                    argsName.append(j)
                #argsName.append(ref) #precisa guardar o nome da variável aqui
                func.children[i].Evaluate(self.NewSymbolTable) #Declarou os argumentos na nova ST
                
        if len(self.children) != 0:
            for i in range(0,len(self.children)):
                self.NewSymbolTable.createValue(argsName[i], self.children[i].Evaluate(symbolTable)) #passar o valor dos filhos para a nova ST na ordem correta
        
        #Evaluate do ultimo filho (comandos)
        for e in func.children[len(func.children)-1].children:
            if isinstance(e,returnNode):
                return e.Evaluate(self.NewSymbolTable)
            else:
                e.Evaluate(self.NewSymbolTable)

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,symbolTable):
        return self.value

class VarDecNode(Node):
    def __init__(self,children):
        self.children = children

    def Evaluate(self,symbolTable):
        for i in self.children:
            symbolTable.createValue(i,None)

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbolTable):
        if self.value == "=":
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
            elif self.value == 'bt':
                return self.children[0].Evaluate(symbolTable)>self.children[1].Evaluate(symbolTable)
            elif self.value == 'lt':
                return self.children[0].Evaluate(symbolTable)<self.children[1].Evaluate(symbolTable)
            elif self.value == 'sm':
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
        return symbolTable.getValue(self.value)

class SymbolTable():
    def __init__(self):
        self.symbolTable = {} 
        self.ancestor = None

    def getValue(self, key):
        if key in self.symbolTable:
            return self.symbolTable.get(key)
        else:
            if self.ancestor:
                return self.ancestor.getValue(key)
            else:
                print(key)
                raise ValueError("Senpai")

    def createValue(self,key,value):
        self.symbolTable['{}'.format(key)] = value
        #print("createValue", self.symbolTable)  