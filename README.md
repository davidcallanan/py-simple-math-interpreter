# Python - Simple Math Interpreter

An interpreter, written from scratch in Python, that can evaluate simple math calculations.

This is useful for learning how computers process human-readable text and is a great first step to creating your own programming language, data language, etc.

The user input is analyzed in two sections of code called the lexer and parser, before finally being interpreted by the interpreter.

## Lexer

The lexer groups the input characters into small segments called tokens and identifies the type of each token, similarly to how we group letters into words such as nouns and verbs.

The characters in the input `12 + 24` are grouped into the tokens `NUMBER:12`, `PLUS`, and `NUMBER:24`.

Whitespace is usually ignored by the lexer.

The tokens are then passed on to the parser.

## Parser

The parser analyzes the sequence of tokens to determine what is intended to happen and in what order, similarly to how we make sense of sentences based on the sequence and types of words.

When the parser sees `NUMBER`, followed by `PLUS`, followed by `NUMBER`, it passes on that the two numbers should be added together. In the case of a multiply operation added into the mix, the parser can determine that the two numbers next to the multiply operator should be multiplied first before the addition takes place.

The result, respresented as a tree, is then pased on to the interpreter.

## Interpreter

The interpeter simply does what's intended according to the parser's results, and contains the code for all the different math operations.

The interpeter could be swapped out for a compiler which generates machine-readable code that your computer can later execute, or could be swapped out for a transpiler which generates code for another language.

# Running the Program

Requirements:
 - [Python3](https://www.python.org/downloads/) ^3.8

Run: `$PYTHON3 main.py` where `$PYTHON3` should be replaced with your Python3 binary, often `python` or `python3` will do.

Unit testing:

 - `$PYTHON3 -m unittest lexer_test`
 - `$PYTHON3 -m unittest parser_test`
