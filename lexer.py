temp = """func example1 {

    int num1 = 1.0;
    int num2 = 2;

    int result = num1 + num2;
    print(result);
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
    FUNCTION_NAMES = []
    BRACKET_STACK = []
    i = 0
    for cLine in filterText:
        i+=1
        if cLine == "":
            continue
        funcBool = False
        varBool = False
        opBool = False
        opVar = None
        compBool = False
        compVal = None
        endLine = False
        cLine = cLine.split(" ")
        for token in cLine:
            token = token.strip()
            if token[-1] == ";":
                token = token[:-1]
                endLine = True

            if token in BRACKETS:
                TOKENS.append(("bracket", token))

            # Current token is func --> Next token is a function name
            elif token == "func":
                funcBool = True
                TOKENS.append(("func_def", token))
                BRACKET_STACK.append("{")
            
            # Current token is a datatype --> Next token is a variable name
            elif token in ["int", "float", "str"]:
                TOKENS.append(("dataType",token))
                varBool = True
 
            # Previous token toggled Function flag --> Current token is function name (reset flag)
            elif funcBool == True:
                TOKENS.append(("id", token))
                FUNCTION_NAMES.append(token)
                TOKENS.append(("bracket", "{"))
                funcBool = False
 
            # Previous token toggled variable flag --> Current token is variable name (reset flag)
            elif varBool == True:
                TOKENS.append(("id", token))
                VARIABLE_NAMES.append(token)
                opVar = token
                varBool = False
 
            # Token is an operator
            elif token in OPERATORS:
                TOKENS.append(("op", token))
                opBool = True
                
            # Token is a comparator
            elif token in COMPARISON:
                TOKENS.append("comp", token)
                compBool = True

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
 
            # If token is a singular bracket
            elif token in BRACKETS and (chr(ord(token) - 1) in BRACKET_STACK[-1] or chr(ord(token) - 2) in BRACKET_STACK[-1]):
                BRACKET_STACK.pop()
                pass #TODO - WILL HANDLE LATER...
 
            else:
                pass # THROW ERROR MESSAGE
                print(chr(ord(token)))
                print(token)
                print("ERROR")

            if endLine == True:
                TOKENS.append(("END", ";"))
                endLine = False
 
    return TOKENS


print(scan(temp))
