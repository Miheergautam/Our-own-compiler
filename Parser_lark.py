from lark import Lark 
from Lexer import lexer
from classes import ExtractAST
from sematic_analyser import SemanticAnalyzer

# Loading the grammar from the file
with open("grammar.lark", "r") as f:
    grammar = f.read()

# Creating the parser
parser = Lark(grammar, start="start", parser='lalr')

cust_parser = Lark(grammar, parser="lalr", start="start", debug=True)



if __name__ == "__main__":
    filename = input("Enter the input file: ")

    # Open the file and read the input text
    with open(filename, "r") as f:
        input_text = f.read()

    # Tokenize the input text using the lexer
    tokens = lexer(input_text)

    # Convert tokens to a string of space-separated token values
    token_values = " ".join(token[1] for token in tokens)

    # Parse the input text
    parse_tree = parser.parse(token_values)
    transformed_ast = ExtractAST().transform(cust_parser.parse(token_values))  # Separate transformation step


    # Print the parse tree
    #print(parse_tree)
    #print(parse_tree.pretty())
    print(transformed_ast)

    analyzer = SemanticAnalyzer()
    analyzer.analyze(transformed_ast)