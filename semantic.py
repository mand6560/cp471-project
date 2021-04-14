def checker(tokens, symbol_table):
    OPERATORS = ["+", "-", "/", "*", "="]
    COMPARISON = ["==", "<", ">", ">=", "<=", "!="]

    SEMANTIC_ERROR = "Semantic Eror"

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
            symbolVal = symbol_table[value][0].split(" ")
            if symbol_table[value][1] == "int":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif char.isdigit():
                            int(char)
                        elif symbol_table[char][1] != "int":
                            return "Error: Oops something broke... It is what it is"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    return "Error: Oops something broke... It is what it is"

            elif symbol_table[value][1] == "float":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif '.' in char:
                            float(char)
                        elif symbol_table[char][1] != "float":
                            return "Error: Oops something broke... It is what it is"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    return "Error: Oops something broke... It is what it is"

            elif symbol_table[value][1] == "string":
                if type(symbol_table[value][0]) != str:
                    return "Error: Oops something broke... It is what it is"

            elif symbol_table[value][1] == "bool":
                try:
                    for char in symbolVal:
                        if char in OPERATORS:
                            pass
                        elif char != "true" and char != "false":
                            return "Error: Oops something broke... It is what it is"
                        elif symbol_table[char][1] != "bool":
                            return "Error: Oops something broke... It is what it is"
                except ValueError:
                    return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
                except KeyError:
                    return "Error: Oops something broke... It is what it is"

