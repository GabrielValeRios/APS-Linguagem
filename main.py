# ref : https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df

from lexer import Lexer
from parser import Parser
import sys

with open("test") as f:
	    content = f.readlines()
content = [x.strip().replace('\n', '') for x in content] 

code = ""
for line in content:
    code+=line

l = Lexer()

for token in l.lex(code):
    print(token)

p = Parser()   

root = p.parse(l.lex(code))
#print("root",root.children[0].children[1].children[1].children[0].value)
root.Evaluate()