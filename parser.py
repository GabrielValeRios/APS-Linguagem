from rply import ParserGenerator
from ast import *

#ref{
    # https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
    # https://media.readthedocs.org/pdf/rply/latest/rply.pdf
#}

def Parser():
    pg = ParserGenerator(
        ['MAIN','INT','PRINTF','IF','ELSE','WHILE','IDENTIFIER','SEMI_COLON',
        'LEFT_BRACKETS','RIGHT_BRACKETS','PLUS','E_EQUAL','EQUAL',
        'MINUS','MULT','DIV','LEFT_PAREN','RIGHT_PAREN','OR','AND',
        'BT','LT','NOT','COMMA','RETURN'],

        precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MULT', 'DIV']),
        ('left', ['AND', 'OR']),
        ]
    )

    @pg.production('program : funcStatments')
    def program(p):
        return p[0]

    @pg.production('funcStatments : funcDec')
    def func_stats(p):
        return p[0]

    @pg.production('funcStatments : funcDec funcStatments')
    def funcs_stat(p):
        m_n = masterNode([p[0]])
        if isinstance(p[1],funcDec):
            m_n.children.append(p[1])

        mainCall = funcCall('mn',[])
        m_n.children.append(mainCall)
        return m_n

    @pg.production('funcDec : MAIN LEFT_PAREN RIGHT_PAREN LEFT_BRACKETS statments RIGHT_BRACKETS')
    def func_dec_main(p):
        children = [None,p[4]]
        f_d = funcDec(p[0].getstr(),children)
        return f_d

    @pg.production('funcDec : IDENTIFIER LEFT_PAREN args RIGHT_PAREN LEFT_BRACKETS statments RIGHT_BRACKETS')
    def func_dec(p):
        children = [p[2],p[5]]
        f_d = funcDec(p[0].getstr(),children)
        return f_d

    @pg.production('args : IDENTIFIER')
    def arg(p):
        arg_node = VarDecNode([p[0].getstr()])
        return arg_node

    @pg.production('args : IDENTIFIER COMMA args')
    def args(p):
        return VarDecNode([p[0],p[2]])

    @pg.production('statments : statment')
    def statments(p):
        stmnts = StatmentsNode([p[0]])
        return stmnts

    @pg.production('statments : statment statments')
    def statment_statments(p):
        stmnt = None
        if isinstance(p[1],StatmentsNode):
            p[1].children.insert(0,p[0])
            stmnt = p[1]
        else:
            stmnt = StatmentsNode([p[0]])
 
        return stmnt

    @pg.production('statment : IDENTIFIER EQUAL expression SEMI_COLON')
    def identifier(p):
        atr = BinOp(p[1].getstr(),[p[0].getstr(),p[2]])
        return atr

    @pg.production('statment : IDENTIFIER EQUAL funcCall SEMI_COLON')
    def func_call(p):
        atr_call = BinOp(p[1].getstr(),[p[0].getstr(),p[2]])
        return atr_call

    @pg.production('statment : PRINTF expression SEMI_COLON')
    def printf_stat(p):
        pf = PrintfNode([p[1]])
        return pf

    @pg.production('statment : WHILE LEFT_PAREN bool_expression RIGHT_PAREN LEFT_BRACKETS statments RIGHT_BRACKETS')
    def while_stat(p):
        _while = WhileNode([p[2],p[5]])
        return _while

    @pg.production('statment : IF LEFT_PAREN bool_expression RIGHT_PAREN LEFT_BRACKETS statments RIGHT_BRACKETS')
    def if_stat(p):
        if_st = IfElseNode([p[2],p[5],None])
        return if_st

    @pg.production('statment : IF LEFT_PAREN bool_expression RIGHT_PAREN LEFT_BRACKETS statments RIGHT_BRACKETS ELSE LEFT_BRACKETS statments RIGHT_BRACKETS')
    def if_else_stat(p):
        if_else = IfElseNode([p[2],p[5],p[9]])
        return if_else

    @pg.production('statment : RETURN expression SEMI_COLON')
    def return_stat(p):
        r_stat = returnNode([p[1]])
        return r_stat

    @pg.production('funcCall : IDENTIFIER LEFT_PAREN expression RIGHT_PAREN')
    def func_call(p):
        f_call = funcCall(p[0].getstr(),[p[2]])
        return f_call

    @pg.production('expression : expression COMMA expression')
    def expr_expr(p):
        return [p[0],p[2]]

    @pg.production('expression : INT')
    def expr_numb(p):
        e_n = IntVal(int(p[0].getstr()))
        return e_n

    @pg.production('expression : IDENTIFIER')
    def expr_iden(p):
        e_i = VarVal(p[0].getstr())
        return e_i

    @pg.production('expression : expression PLUS expression')
    @pg.production('expression : expression MINUS expression')
    @pg.production('expression : expression MULT expression')
    @pg.production('expression : expression DIV expression')
    def expr_symbols(p):
        e_s = BinOp(p[1].getstr(),[p[0],p[2]])
        return e_s

    @pg.production('bool_expression : relExpression')
    def bool_expression(p):
        b_e = p[0]
        return b_e

    @pg.production('bool_expression : relExpression OR relExpression')
    @pg.production('bool_expression : relExpression AND relExpression')
    @pg.production('bool_expression : relExpression NOT relExpression')
    def bool_expression_double(p):
        b_e_d = BinOp(p[1].getstr(),[p[0],p[2]])
        return b_e_d

    @pg.production('relExpression : expression BT expression')
    @pg.production('relExpression : expression LT expression')
    @pg.production('relExpression : expression E_EQUAL expression')
    def relExpression(p):
        r_e = BinOp(p[1].getstr(),[p[0],p[2]])
        return r_e

    @pg.error
    def error_handle(token):
        raise ValueError(token)

    return pg.build()