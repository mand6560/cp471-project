def generate(tokens,symbol_table):
    final_string = ""
    triples = {}
    for curr_token in tokens:
        if (curr_token[0] == "func_decl"):
            final_string += curr_token[1]+":\n"
        elif (curr_token[0] == "id"):  
            curr_ind = len(triples)+1
            # print(curr_token[1])
            if (not(curr_token[1] in triples)):
                inter_var = "t"+ str(curr_ind)
            else:
                print("else")
                inter_var = triples[curr_token[1]][0]
                print(inter_var)
            curr_val = symbol_table[curr_token[1]]
            final_string += inter_var + " = " + curr_val[0] + "\n"
            triples[curr_token[1]] = (inter_var,curr_val[0])

    print(final_string)
    # print(triples)
    return final_string