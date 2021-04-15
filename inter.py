COMPARISON = ["==", "<", ">", ">=", "<=", "!="]
ANTI_COMPARISON = ["!=", ">=", "<=", "<", ">", "=="]

def generate(tokens,symbol_table):
    # print(tokens[24])
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
    eq_flag = False
    logic_Flag = False
    end_count = 1
    op = ""
    i = 0
    while i < (len(tokens)-1):

        curr_token = tokens[i]

        if (curr_token[0] == "func_decl"):
            final_string += curr_token[1]+":\n"

        elif (curr_token[0] == "while_loop"):
            quadruples.append(("while","","","label{}:".format(label_count)))
            quadruples.append( (tokens[i+3][1], var_maps[tokens[i+2][1]], tokens[i+4][1],"END{}".format(end_count) ) )
            i += 3
            while_insert_flag = True
        elif (curr_token[0] == "cond" and curr_token[1] != "else"):
            # quadruples.append((curr_token[1],"","","label{}:".format(label_count)))
            quadruples.append( (tokens[i+3][1], var_maps[tokens[i+2][1]], var_maps[tokens[i+4][1]],"END{}".format(end_count) ) )
            i += 3
        elif (curr_token[1] == "}" and while_insert_flag):
            # quadruples.append((curr_token[1],"","","label{}:".format(label_count)))
            quadruples.append( ("goto", "","","label{}".format(label_count) ) )
            label_count += 1
            while_insert_flag = False
            logic_Flag = True

        elif (op == "ret" and curr_token[0] == "id"):
            if logic_Flag == False:
                quadruples.append((op,var_maps[curr_token[1]],"",""))
                quadruples.append(("label","","","END{}:".format(end_count)))
            else:
                quadruples.append(("label","","","END{}:".format(end_count)))
                quadruples.append((op,var_maps[curr_token[1]],"",""))
            logic_Flag == False
            end_count += 1
            op = ""
        # elif (curr_token[0])
        elif (curr_token[0] == "id" and tokens[i-1][0] != "comp"):
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
                # if (curr_token[1] in value_dic ):
                #     value_dic[curr_token[1]] += 1
                #     print(value_dic[curr_token[1]],curr_token)
                #     eq_flag = False
                #     # print("increasing value_dic")
                # else:
                #     # print("setting value_dic")
                #     value_dic[curr_token[1]] = 1

                if (not(curr_token[1] in value_dic )):
                    value_dic[curr_token[1]] = 1
                    

                curr_val = symbol_table[curr_token[1]]
                # print(curr_token[1],curr_val,"@",value_dic[curr_token[1]],i)
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
                # print(curr_token[1], " " ,value_dic[curr_token[1]])
                if (len(curr_val[value_dic[curr_token[1]]].strip("").split(" ")) == 1):
                    arg1 = curr_val[value_dic[curr_token[1]]]
                    arg2 = ""
                    if(value_dic[curr_token[1]] == 1) and (value_dic[curr_token[1]] + 1 < (len(curr_val))):
                        value_dic[curr_token[1]] += 1
                    
                else:
                    # What we got from the symbol table
                    val_list = curr_val[value_dic[curr_token[1]]].strip("").split(" ")
                    arg1 = var_maps[val_list[0]]
                    arg2 = val_list[-1]

                    # Making sure that we don't cross the max threshold
                    if(value_dic[curr_token[1]] + 1 < (len(curr_val))):
                        value_dic[curr_token[1]] += 1
                
                    # print(curr_token[1],value_dic[curr_token[1]])
                quadruples.append((op,arg1,arg2,inter_var))
                # print(quadruples)
                var_count += 1
                # print(var_maps,curr_token)
                op = ""
                # print(quadruples)
        elif(curr_token[0] == "RTRN_STMT"):
            op = "ret"
        i += 1
        # print(i)
    for entry in quadruples:
        if (entry[0] == "="):
            final_string += entry[3] + " " + entry[0] + " "+entry[1]+"\n"
        elif (entry[0] == "ret"):
            final_string += "return " + entry[1] + "\n"
        elif (entry[0] == "while"):
            final_string += entry[3] + "\n"
        elif (entry[0] == "label"):
            final_string += entry[3] + "\n"
        elif(entry[0] in COMPARISON):
            final_string += "if " + entry[1] + " " + ANTI_COMPARISON[COMPARISON.index(entry[0])] + " " + entry[2] + " goto " + entry[3] + "\n"
        elif(entry[0] == "goto"):
            final_string += entry[0] + " " + entry[3] +" \n"
        # elif(entry[0] in)
        else:
            final_string += entry[3] +  " = " + entry[1]+" " + entry[0] + " " + entry[2]+"\n"
    
    # print("final_string: ",final_string.split("\n")[-2])
    if ("END" in final_string.split("\n")[-2] ):
        final_string = "\n".join(final_string.split("\n")[:-2])
    # print(quadruples)
    # print(final_string)

    pre_inter_code_arr = final_string.strip("\n").split("\n")
    inter_code_arr = []

    i = 0
    while i < len(pre_inter_code_arr):
        if pre_inter_code_arr[i][-1] == ':':
            new_line = pre_inter_code_arr[i] + ' ' + pre_inter_code_arr[i + 1]
            inter_code_arr.append(new_line)
            i += 1
        else:
            inter_code_arr.append(pre_inter_code_arr[i])
        i += 1
    return '\n'.join(inter_code_arr)