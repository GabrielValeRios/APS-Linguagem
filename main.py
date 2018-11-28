from lexer import Lexer
from parser import Parser
from ast import SymbolTable
import sys

with open("test") as f:
	    content = f.readlines()
content = [x.strip().replace('\n', '') for x in content] 

code = ""
for line in content:
    code+=line

l = Lexer()
p = Parser()

for token in l.lex(code):
    print(token)    

st = SymbolTable()

p.parse(l.lex(code)).Evaluate(st)