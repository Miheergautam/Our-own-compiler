# Switch Compiler

**Switch** is a custom programming language compiler built using Python. This project features a complete toolchain that processes Switch source code through several stages: Lexical Analysis, Parsing, and Semantic Analysis.

## Features

- **Lexer**: 
  The lexer tokenizes the input Switch source code into a stream of tokens using the [Lark](https://github.com/lark-parser/lark) library. It supports various constructs such as keywords, identifiers, numbers, operators, and punctuation.

- **Parser**: 
  Using Lark, the parser converts the token stream into an Abstract Syntax Tree (AST). It ensures that the Switch source code adheres to the correct syntactical structure by validating against a context-free grammar.

- **Semantic Analysis**: 
  After parsing, the compiler performs semantic analysis on the AST. This phase checks for logical errors like variable scope issues, type mismatches, and other context-dependent concerns that the parser does not catch.

- **Python Implementation**: 
  The entire compiler is implemented in Python, leveraging the Lark library for Lexical and Syntactical analysis. This makes the compiler easy to extend and modify.
