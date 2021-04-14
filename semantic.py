def checker(tokens, symbol_table):
    OPERATORS = ["+", "-", "/", "*", "="]
    COMPARISON = ["==", "<", ">", ">=", "<=", "!="]

    SEMANTIC_ERROR = "Semantic Error"

    bracketStack = []
    openBracket = ["{", "(", "["]
    closeBracket = ["}", ")", "]"]

    for tok in tokens:
        classify = tok[0]
        value = tok[1]

        if classify == "bracket":
            if value in openBracket:
                bracketStack.append(value)
            else:
                temp = bracketStack.pop()
                if closeBracket[openBracket.index(temp)] != value:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)

        elif classify == "op" and value not in OPERATORS:
            return "Error: {}, token not a valid operation".format(SEMANTIC_ERROR)

        elif classify == "comp" and value not in COMPARISON:
            return "Error: {}, token not a valid comparison operation".format(SEMANTIC_ERROR)

        elif classify == "RTRN_STMT" and value != "return":
            return "Error: {}, token not a valid return statement".format(SEMANTIC_ERROR)
        
        elif classify == "func_def" and value != "func":
            return "Error: {}, token not a valid function declaration".format(SEMANTIC_ERROR)

        elif classify == "id":
            symbolVal = symbol_table[value][0].strip(" ").split(" ")

            if symbol_table[value][1] == "int":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif char.isdigit():
                            int(char)
                        elif symbol_table[char][1] != "int":
                            return "Error: Oops something broke... It is what it is 1"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    print(symbol_table[value],char,symbol_table)
                    return "Error: Oops something broke... It is what it is 2"

            elif symbol_table[value][1] == "float":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif '.' in char:
                            float(char)
                        elif symbol_table[char][1] != "float":
                            return "Error: Oops something broke... It is what it is 3"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    return "Error: Oops something broke... It is what it is 4"

            elif symbol_table[value][1] == "string":
                if type(symbol_table[value][0]) != str:
                    return "Error: Oops something broke... It is what it is 5"

            elif symbol_table[value][1] == "bool":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif char != "true" and char != "false":
                            return "Error: Oops something broke... It is what it is 6"
                        elif symbol_table[char][1] != "bool":
                            return "Error: Oops something broke... It is what it is 7"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    return "Error: Oops something broke... It is what it is 8"
    return 1

