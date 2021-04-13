import sys
import lexer
import parser
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
                file_contents += line.strip()
    except FileNotFoundError:
        print('Error: source file doesn\'t exist')
        sys.exit(1)

    print(file_contents)

    # Perform lexical analysis
    tokens = lexer.scan(file_contents)
    # Perform parsing
    parser.parse(tokens)
    # Perform semantic analysis
    pass
    # Perform backend
    pass


if __name__ == '__main__':
    main()
