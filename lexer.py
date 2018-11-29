from rply import LexerGenerator

def Lexer():

    lexer = LexerGenerator()

    lexer.add('WHILE', r'wh')
    lexer.add('PRINTF', r'pf')
    lexer.add('IF', r'if')
    lexer.add('ELSE', r'e')
    lexer.add('MAIN', r'main')
    lexer.add('LEFT_PAREN', r'\(')
    lexer.add('RIGHT_PAREN', r'\)')
    lexer.add('SEMI_COLON', r'\;')
    lexer.add('PLUS', r'\+')
    lexer.add('MINUS', r'\-')
    lexer.add('MULT', r'\*')
    lexer.add('DIV', r'\/')
    lexer.add('RIGHT_BRACKETS', r'\}')
    lexer.add('LEFT_BRACKETS', r'\{')
    lexer.add('EQUAL', r'=')
    lexer.add('E_EQUAL', r'==')
    lexer.add('BT', r'>')
    lexer.add('LT', r'<')
    lexer.add('INT', r'\d+')
    lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]*")
    lexer.ignore('\s+')
    
    return lexer.build()