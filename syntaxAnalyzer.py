import string

def parse(tokens):
    #tokens is a list of tokens, where the elements take the format <identifier,type>
    #Walk through the list given to us
    ind = 0 
    tos = ""
    toi = "" 

    
    while ind < len(tokens):
    
        # Getting the next expected possible values
        # We are also passing the type of token, not the token itself E.g: op, id, etc.
        return_vals = parse_aux(toi)
        
        
        # Checking if the next value from the input is actually the expected value
        tos = tokens[ind][0]
        if (tos == "id" or tos == "fun_decl") and tokens[ind][1][0] not in string.ascii_letters and tokens[ind][1][0] != "_":
            return -1

        print(toi,tos,return_vals)
        print("---> {}".format(tokens[ind]))
        if (return_vals != None and tos not in return_vals and len(return_vals) != 0):
            return -1 
        
        
        # Move onto the next token
        toi = tos 
        ind += 1 
    

    return 1

def parse_aux(toi):
    bracket_list = []
    # We return what the next acceptable tokens
    if toi == "":
        return {"func_def"} 
    
    elif toi ==  "func_def": 
        return {"func_decl"}
          
    
    elif toi ==  "id": 
        return {"op", "bracket","comp","END"}
    
    elif toi == "comp":
        return {"id", "int", "float", "bool"}
    
    elif toi == "int": 
        return {"END", "op", "bracket"}
          
    
    elif toi == "float": 
        return {"END", "op", "bracket"}
          
    
    elif toi == "bool": 
        return {"END", "op", "bracket"}
          
    
    elif toi == "string": 
        return {"END"}

    elif toi == "dataType":
        return {"id"}
          
    
    elif toi == "RTRN_STMT":
        return {"id"}

    elif toi == "func_decl":
        return {"bracket"}
          
    
    # elif toi == "=": 
    #     return {"id","float","int"} 
          
    
    # elif toi == "+": 
    #     return {"id","float","int"} 
          
    
    # elif toi == "-": 
    #     return {"id","float","int"} 
          
    
    # elif toi == "*": 
    #     return {"id","float","int"} 
          
    
    # elif toi == "/": 
    #     return {"id","float","int"} 
          
    
    # elif toi == "%": 
    #     return {"id","float","int"}     

    elif toi == "op":
        return {"id","float","int"}     
          
    
    # elif toi == "^": 
    #     return {"id","float","int"}             
          
    
    # elif toi == "<": 
    #     return {"id","float","int"}             
          
    
    # elif toi == ">": 
    #     return {"id","float","int"}             
          
    
    elif toi == " ": 
        return {"id",}
          
    
    elif toi == "while_loop": 
        return {"bracket"} 
          
    
    elif toi == "for_loop": 
        return {"bracket"} 
          
    
    # elif toi == "if": 
    #     return {"id","float","int","bool", "bracket"} 
          
    
    # elif toi == "elif": 
    #     return {"id","float","int","bool"} 
          
    
    # elif toi == "else": 
    #     return {"id","float","int","bool"} 

    elif toi == "cond":
        return {"id","float","int","bool", "bracket"} 
    
    elif toi == "END":
        return {"id", "dataType", "while", "for", "cond", "bracket", "RTRN_STMT", "while_loop", "for_loop"}
    
    elif toi == "bracket":
        return {"id", "float", "int", "bool", "string", "while", "for", "bracket", "cond", "RTRN_STMT", "dataType"}
    
    else: 
        bracket_list.append(toi) 
    return None
        
    

