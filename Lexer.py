import re
import sys

TOKEN_TYPES = {
    'COMMENT': r'->([^"\\]|\\.)*',
    'KEYWORD': r'take|show|either|or|whatif|var|skip|try|catch|finally|from|func|while|do|skip|to|num|bool|str|stop|carryon|give',
    'NUMBER': r'\d+',
    'STRING': r'"([^"\\]|\\.)*"',
    'BOOL': r'on|off',
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9_]*',
    'OPERATOR': r'''<=|>=|==|<|>|\+|-|!=|\*|/|&&|\|\||!|=''',
    'LEFT_PAREN': r'\(',
    'RIGHT_PAREN': r'\)',
    'LEFT_BRACE': r'{',
    'RIGHT_BRACE': r'}',
    'LEFT_SQUARE_BRACKET': r'\[',
    'RIGHT_SQUARE_BRACKET': r'\]',
    'COMMA': r',',
    'COLON': r':',
    'ENDOFSTMT': r';',
}

TOKEN_REGEX = '|'.join(f'(?P<{token_type}>{pattern})' for token_type, pattern in TOKEN_TYPES.items())

def lexer(text):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, text):
        for name, value in match.groupdict().items():
            if value is not None:
                tokens.append((name.upper(), value))
    return tokens

def get_tokens_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return lexer(text)

def format_tokens(tokens):
    return ',\n'.join(f'<{token_type}, "{token_value}">' for token_type, token_value in tokens)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lexer.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    tokens = get_tokens_from_file(filename)
    output_string = format_tokens(tokens)
    print(output_string)