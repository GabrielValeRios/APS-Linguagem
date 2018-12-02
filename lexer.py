from rply import LexerGenerator

def Lexer():

    lexer = LexerGenerator()

    lexer.add('WHILE', r'wh')
    lexer.add('PRINTF', r'pf')
    lexer.add('IF', r'if')
    lexer.add('ELSE', r'el')
    lexer.add('MAIN', r'mn')
    lexer.add('RETURN', r'rt')
    lexer.add('LEFT_PAREN', r'\(')
    lexer.add('RIGHT_PAREN', r'\)')
    lexer.add('SEMI_COLON', r'\;')
    lexer.add('COMMA', r'\,')
    lexer.add('PLUS', r'\+')
    lexer.add('MINUS', r'\-')
    lexer.add('MULT', r'\*')
    lexer.add('DIV', r'\/')
    lexer.add('RIGHT_BRACKETS', r'\}')
    lexer.add('LEFT_BRACKETS', r'\{')
    lexer.add('EQUAL', r'=')
    lexer.add('E_EQUAL', r'sm')
    lexer.add('BT', r'bt')
    lexer.add('LT', r'lt')
    lexer.add('OR', r'or')
    lexer.add('AND', r'and')
    lexer.add('NOT', r'not')
    lexer.add('INT', r'\d+')
    lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]*")
    lexer.ignore('\s+')
    
    return lexer.build()