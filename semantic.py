# def checker(tokens, symbol_table):
#     BRACKETS = ["{", "}", "(", ")","[", "]"]
#     OPERATORS = ["+", "-", "/", "*", "="]
#     COMPARISON = ["==", "<", ">", ">=", "<=", "!="]

#     SEMANTIC_ERROR = "Semantic Eror"

#     for tok in tokens:
#         classify = tok[0]
#         value = tok[1]

#         if classify == "bracket" and value not in BRACKETS:
#             return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
        
#         value = "hello"
#         elif classify == "dataType":
            
#             try:
#                 int(value)
#             except ValueError:
#                 return "Error: {}, token not a bracket".format(SEMANTIC_ERROR)
