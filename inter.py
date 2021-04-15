COMPARISON = ["==", "<", ">", ">=", "<=", "!="]

def generate(tokens,symbol_table):
    
    final_string = ""
    # triples = {}

    #   OP | arg1 | arg2 | res
    #   =  |  2   |  -   | t1
    #   +  |  t1  |  1   | t2
    #  ret |  t2  |  -   |    
    var_count = 1
    label_count = 1

    # To get from symbol value
    value_dic = {}
    var_maps = {}
    quadruples = []
    while_insert_flag = False
    op = ""
    i = 0
    while i < (len(tokens)):
        # print(i)
    # for curr_token in tokens:
        curr_token = tokens[i]

        if (curr_token[0] == "func_decl"):
            final_string += curr_token[1]+":\n"

        elif (curr_token[0] == "while_loop"):
            quadruples.append(("while","","","label{}:".format(label_count)))
            quadruples.append( (tokens[i+3][1], var_maps[tokens[i+2][1]], tokens[i+4][1],"END" ) )
            i += 3
            label_count += 1
            while_insert_flag = True
        # elif while_insert_flag == True:
        #     if curr_token[0] == "bracket" and curr_token[1] == "}":
                

        elif (op == "ret" and curr_token[0] == "id"):
            quadruples.append(("while","","","END:"))
            quadruples.append((op,var_maps[curr_token[1]],"",""))
        # elif (curr_token[0])
        elif (curr_token[0] == "id"):
            op = "="
            # print(curr_token[1])

            if (tokens[i - 1][1] != "=" and tokens[i - 1][1] != "("):

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
                
                var_maps[curr_token[1]] = inter_var
                # print(curr_token, value_dic, quadruples)
                if (curr_token[1] in value_dic):
                    value_dic[curr_token[1]] += 1
                    # print("increasing value_dic")
                else:
                    # print("setting value_dic")
                    value_dic[curr_token[1]] = 1
                    

                curr_val = symbol_table[curr_token[1]]

                if ("+" in curr_val[value_dic[curr_token[1]]]):
                    op = "+"
                elif ("-" in curr_val[value_dic[curr_token[1]]]):
                    op = "-"
                elif ("*" in curr_val[value_dic[curr_token[1]]]):
                    op = "*"
                elif ("/" in curr_val[value_dic[curr_token[1]]]):
                    op = "/"
                
                # print("curr_val: ",curr_val[value_dic[curr_token[1]]])
                # print("len: ",len(curr_val[value_dic[curr_token[1]]].strip("")))
                
                # We must split
                if (len(curr_val[value_dic[curr_token[1]]].strip("").split(" ")) == 1):
                    arg1 = curr_val[value_dic[curr_token[1]]]
                    arg2 = ""
                else:
                    # What we got from the symbol table
                    val_list = curr_val[value_dic[curr_token[1]]].strip("").split(" ")
                    # print("curr_val: ",curr_val)
                    # print("value_dic: ",value_dic)
                    # print("curr_token[1]: ", curr_token[1])
                    # print("curr_val[value_dic[curr_token[1]]]: ",curr_val[value_dic[curr_token[1]]])
                    arg1 = var_maps[val_list[0]]
                    arg2 = val_list[-1]
                
                
                quadruples.append((op,arg1,arg2,inter_var))
                # print(quadruples)
                var_count += 1
                # print(var_maps,curr_token)
                op = ""
                print(quadruples)
        elif(curr_token[0] == "RTRN_STMT"):
            op = "ret"
        i += 1
    for entry in quadruples:
        if (entry[0] == "="):
            final_string += entry[3] + " " + entry[0] + " "+entry[1]+"\n"
        elif (entry[0] == "ret"):
            final_string += "return " + entry[1] + "\n"
        elif (entry[0] == "while"):
            final_string += entry[3] + "\n"
        elif(entry[0] in COMPARISON):
            final_string += "if " + entry[1] + " " + entry[0] + " " + entry[2] + " goto " + entry[3] + "\n"
        else:
            final_string += entry[3] +  " = " + entry[1]+" " + entry[0] + " " + entry[2]+"\n"
    
    
    print(quadruples)
    print(final_string)
    return final_string