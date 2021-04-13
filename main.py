import sys

import lexer
import syntaxAnalyzer
import semantic
import backend


def main():

    # Get source file name
    try:
        source_file_name = sys.argv[1]
    except IndexError:
        print('Error: no source file provided')
        sys.exit(1)

    # Open the source file and get it contents
    try:
        with open(source_file_name, 'r') as source_file:
            file_contents = ''
            for line in source_file:
                file_contents += line
    except FileNotFoundError:
        print('Error: source file doesn\'t exist')
        sys.exit(1)

    # Symbol Table creation
    symbol_table = {}

    # Perform lexical analysis
    tokens, functions, variables = lexer.scan(file_contents)
    print("Tokens: {:}\n".format(tokens))
    print("Functions: {}\n".format(functions))
    print("Variables: {}\n".format(variables))

    # Fill out symbol table with results from lexer
    for function in functions:
        symbol_table[function[1]] = function[0]
    for variable in variables:
        symbol_table[variable[1]] = variable[0]

    print('Symbol Table: ' + str(symbol_table))

    # Perform parsing
    print(syntaxAnalyzer.parse(tokens))
    
    # Perform semantic analysis
    pass
    # Perform backend
    pass


if __name__ == '__main__':
    main()
