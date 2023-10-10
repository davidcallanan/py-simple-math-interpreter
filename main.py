from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("calc > ")
        value = Interpreter().visit(Parser(Lexer(text).generate_tokens()).parse())
        if value is not None:
            print(value)
    except Exception as e:
        print(e)
