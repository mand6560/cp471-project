temp = """func hello {
	int x = 5;
	int y = 4;
	int z = 10;
	if (x < y) {
		y = y + 5;
		return y;
}
elif ( z > y ) {
	z = z - 3;
	return z;
}
	else {
		return x;
}
}


"""


 
BRACKETS = ["{", "}", "(", ")","[", "]"]
OPERATORS = ["+", "-", "/", "*", "="]
COMPARISON = ["==", "<", ">", ">=", "<=", "!="]
 
def scan(text):
    # Split the block of text 
    newText= text.split("{")
    filterText = []
    for line in newText:
        codeLine = line.split("\n")
        for filterLine in codeLine:
            filterText.append(filterLine.strip(" \n\t"))
    TOKENS = []
    VARIABLE_NAMES = []
    VARIABLE_TYPES = []
    FUNCTION_NAMES = []
    BRACKET_STACK = []
    i = 0
    for cLine in filterText:
        i+=1
        if cLine == "":
            continue
        funcBool = False
        varBool = False
        endLine = False
        # startBracket = False
        # startVal = None
        endBracket = False
        endVal = None

        intFlag = False
        floatFlag = False
        stringFlag = False

        cLine = cLine.split(" ")
        for token in cLine:
            token = token.strip()

            if len(token) != 1:
                if token[-1] == ";":
                    token = token[:-1]
                    endLine = True

                elif token[-1] in BRACKETS:
                    print(token)
                    token = token[:-1]
                    endBracket = True
                    endVal = token[-1]

                if token[0] in BRACKETS:
                    token = token[1:]
                    TOKENS.append(("bracket", token[0]))


            if token in BRACKETS:
                TOKENS.append(("bracket", token))

            elif token == "return":
                TOKENS.append(("RTRN_STMT", token))
            
            elif token == "if" or token == "elif" or token == "else":
                TOKENS.append(("cond", token))

            elif token in COMPARISON:
                TOKENS.append(("comp", token))

            elif token == "for":
                TOKENS.append(("for_loop", token))

            elif token == "while":
                TOKENS.append(("while_loop", token))

            # Current token is func --> Next token is a function name
            elif token == "func":
                funcBool = True
                TOKENS.append(("func_def", token))
                BRACKET_STACK.append("{")
            
            # Current token is a datatype --> Next token is a variable name
            elif token in ["int", "float", "string"]:
                TOKENS.append(("dataType",token))
                varBool = True
                if token == "int":
                    intFlag = True
                elif token == "float":
                    floatFlag = True
                else:
                    stringFlag = True
 
            # Previous token toggled Function flag --> Current token is function name (reset flag)
            elif funcBool == True:
                TOKENS.append(("id", token))
                FUNCTION_NAMES.append((token, "PROC"))
                TOKENS.append(("bracket", "{"))
                funcBool = False
 
            # Previous token toggled variable flag --> Current token is variable name (reset flag)
            elif varBool == True:
                TOKENS.append(("id", token))
                varBool = False
                VARIABLE_NAMES.append(token)
                if floatFlag == True:
                    VARIABLE_TYPES.append("FLOAT")
                    floatFlag = False
                elif intFlag == True:
                    VARIABLE_TYPES.append("INT")
                    intFlag = False
                elif stringFlag == True:
                    VARIABLE_TYPES.append("STRING")
                    stringFlag = False
 
            # Token is an operator
            elif token in OPERATORS:
                TOKENS.append(("op", token))
                
            # Token is a comparator
            elif token in COMPARISON:
                TOKENS.append("comp", token)

            # Token is an already defined variable name
            elif token in VARIABLE_NAMES:
                TOKENS.append(("id", token))
 
            # Token is an already defined function name
            elif token in FUNCTION_NAMES:
                TOKENS.append(("func", token))
            
            # Token is a function
            elif "(" in token:
                TOKENS.append(("func", token))
 
            # Token is an Integer            
            elif token.isdigit():
                TOKENS.append(("int", token))
 
            # Roundabout way to find whether the token is a float number
            elif "." in token:
                try:
                    float(token)
                    TOKENS.append(("float", token))
                except:
                    pass
 
            # # If token is a singular bracket
            # elif token in BRACKETS and (chr(ord(token) - 1) in BRACKET_STACK[-1] or chr(ord(token) - 2) in BRACKET_STACK[-1]):
            #     BRACKET_STACK.pop()
            #     pass #TODO - WILL HANDLE LATER...
 
            else:
                pass # THROW ERROR MESSAGE
                print(token)
                print("ERROR")

            if endLine == True:
                TOKENS.append(("END", ";"))
                endLine = False
            elif endBracket == True:
                TOKENS.append(("bracket", endVal))
                endBracket = False

    VARIABLES = []
    for i in range(len(VARIABLE_NAMES)):
        VARIABLES.append((VARIABLE_TYPES[i], VARIABLE_NAMES[i]))
    print("Tokens: {:}\n".format(TOKENS))
    print("Functions: {}\n".format(FUNCTION_NAMES))
    print("Variables: {}\n".format(VARIABLES))
    return TOKENS, FUNCTION_NAMES, VARIABLES


scan(temp)
