def parse(tokens):
    #tokens is a list of tokens, where the elements take the format <identifier,type>
    #Walk through the list given to us
    ind = 0 
    tos = ""
    toi = "" 
    bracket_list = []
    
    while ind < tokens.length:
    
        # Getting the next expected possible values
        # We are also passing the type of token, not the token itself E.g: op, id, etc.
        return_vals = parse(toi)
        
        
        # Checking if the next value from the input is actually the expected value
        tos = tokens[ind][0]
        if (tos not in return_vals and return_vals.length != 0):
            return -1 
        
        
        # Move onto the next token
        toi = tos 
        ind += 1 
    

    return 1

def parse(toi):

    # We return what the next acceptable tokens
    if toi == "":
        return {"func"} 
    
    if toi ==  "func": 
        return {"id"}
          
    
    if toi ==  "id": 
        return {"op"}
          
    
    if toi == "int": 
        return {"id"}
          
    
    if toi == "float": 
        return {"id"}
          
    
    if toi == "bool": 
        return {"id"}
          
    
    if toi == "string": 
        return {"id"}
          
    
    if toi == "return":
        return {" "}
          
    
    if toi == "=": 
        return {"id","float","int"} 
          
    
    if toi == "+": 
        return {"id","float","int"} 
          
    
    if toi == "-": 
        return {"id","float","int"} 
          
    
    if toi == "*": 
        return {"id","float","int"} 
          
    
    if toi == "/": 
        return {"id","float","int"} 
          
    
    if toi == "%": 
        return {"id","float","int"}             
          
    
    if toi == "^": 
        return {"id","float","int"}             
          
    
    if toi == "<": 
        return {"id","float","int"}             
          
    
    if toi == ">": 
        return {"id","float","int"}             
          
    
    if toi == " ": 
        return {"id",}
          
    
    if toi == "while": 
        return {"id","float","int"} 
          
    
    if toi == "for": 
        return {"id","int"} 
          
    
    if toi == "if": 
        return {"id","float","int","bool"} 
          
    
    if toi == "elif": 
        return {"id","float","int","bool"} 
          
    
    if toi == "else": 
        return {"id","float","int","bool"} 
          
    
    else: 
        bracket_list.insert(toi) 
    return None
        
    

