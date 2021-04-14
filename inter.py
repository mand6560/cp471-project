def generate(tokens,symbol_table):
    final_string = ""
    triples = {}

    #   OP | arg1 | arg2 | res
    #   =  |  2   |  -   | t1
    #   +  |  t1  |  1   | t2
    #  ret |  t2  |  -   |    
    var_count = 1
    var_maps = {}
    quadruples = []
    insert_flag = False
    op = ""
    for curr_token in tokens:
        
        if (curr_token[0] == "func_decl"):
            final_string += curr_token[1]+":\n"
        elif (curr_token[0] == "dataType"):
            insert_flag = True
        elif (op == "ret" and curr_token[0] == "id"):
            quadruples.append((op,var_maps[curr_token[1]],"",""))
        elif (curr_token[0] == "id" and insert_flag):
            op = "="
            # print(curr_token[1])
            token_exists = 0
            for each in quadruples:
                if (curr_token[-1] in var_maps):
                    if (each[-1] == var_maps[curr_token[1]]):
                        token_exists = 1
                        break

            if (token_exists == 0):
                inter_var = "t"+ str(var_count)
                # print("D:")
            else:
                inter_var = var_maps[curr_token[1]]
            curr_val = symbol_table[curr_token[1]]

            if ("+" in curr_val[1]):
                op = "+"
            elif ("-" in curr_val[1]):
                op = "-"
            elif ("*" in curr_val[1]):
                op = "*"
            elif ("/" in curr_val[1]):
                op = "/"
            
            if (len(curr_val[1].strip("")) == 1):
                arg1 = curr_val[1]
                arg2 = ""
            else:
                val_list = curr_val[1].strip("").split(" ")
                arg1 = var_maps[val_list[0]]
                arg2 = val_list[-1]
            
            var_maps[curr_token[1]] = inter_var
            quadruples.append((op,arg1,arg2,inter_var))
            var_count += 1
            # print(var_maps,curr_token)
            insert_flag = False
        elif(curr_token[0] == "RTRN_STMT"):
            op = "ret"
    for entry in quadruples:
        if (entry[0] == "="):
            final_string += entry[3] + " " + entry[0] + " "+entry[1]+"\n"
        elif (entry[0] == "ret"):
            final_string += "return " + entry[1] 
        else:
            final_string += entry[3] +  " = " + entry[1]+" " + entry[0] + " " + entry[2]+"\n"
        

    print(final_string)
    print(quadruples)
    return final_string