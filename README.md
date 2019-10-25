# Simple calculation interpreter

An interpreter that can evaluate simple calculations for learning how computers process human-readable text.

This is a great first step to creating your own programming language, data language, and much more.

The user input is analyzed in two sections of code called the lexer and parser, before finally being interpreted by the interpreter.

## Lexer

The lexer breaks up the input into small segments called tokens, similarly to how we break up sentences into words.

The input `12 + 24` is broken into the number 12, a plus operator, and the number 24.

Whitespace is usually ignored by the lexer.

## Parser

The parser analyzes the sequence of tokens to determine what is intended to happen and in what order.

When the parser sees a number, followed by a plus operator, followed by another number, it passes on that the two numbers should be added together. In the case of a multiply operator added into the mix, the parser can determine that the two numbers next to the multiply operator should be multiplied first before the addition takes place.

## Interpreter

The interpeter simply does what's intended according to the parser's results, and contains the code for all the different math operations.

The interpeter could be swapped out for a compiler which generates machine-readable code that your computer can later execute, or could be swapped out for a transpiler which generates code for another language. 
