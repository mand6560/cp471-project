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
    lexer_results = lexer.scan(file_contents)
    # Check for lexer error condition
    if lexer_results[0] == 'error':
        print('Error: lexer error, invalid token %s detected...' % lexer_results[1])
        sys.exit(1)
    else:
        tokens, functions, variables = lexer.scan(file_contents)
    print("Tokens: {}".format(tokens))
    print("Functions: {}".format(functions))
    print("Variables: {}".format(variables))

    # Fill out symbol table with results from lexer
    for function in functions:
        symbol_table[function[1]] = function[0]
    for variable in variables:
        symbol_table[variable[1]] = variable[0]

    print('Symbol Table: ')
    for key in symbol_table.keys():
        print('%s -> %s' % (key, symbol_table[key]))

    # Perform parsing
    parsing_result = syntaxAnalyzer.parse(tokens)
    # Parser returns -1 in case of error
    if parsing_result == -1:
        print('Error: parsing error, check your code and try again...')
        sys.exit(1)

    # Perform semantic analysis
    pass
    # Perform backend
    pass


if __name__ == '__main__':
    main()
