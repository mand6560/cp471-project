def generate(inter_code):
    pre_inter_code_arr = inter_code.strip("\n").split("\n")
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

    # print('\n'.join(inter_code_arr))

    register_count = 0
    final_string = "L1:\n"
    
    i = 1
    register_map = {}

    while i < len(inter_code_arr):
        curr_instr = inter_code_arr[i].split(" ")
        if (len(curr_instr) == 1):
            final_string += curr_instr[0]+"\n"
        elif (len(curr_instr) == 3):
            # We only look at arithmetic ops here because any instruction with comparisons
            # is going to have length of more than 3
            if (curr_instr[1] == "="):
                if (not(curr_instr[0] in register_map)):
                    # print(curr_instr)
                    register_map[curr_instr[0]] = "R{}".format(register_count)
                    register_count += 1
                final_string += "LD " + register_map[curr_instr[0]] + "," + curr_instr[2] + "\n"
            elif(curr_instr[1] == "+="):
                pass
            elif(curr_instr[1] == "-="):
                pass
            elif(curr_instr[1] == "*="):
                pass
            elif(curr_instr[1] == "/="):
                pass
        # elif (len(curr_instr) == 4):
            

        i += 1
    
    print(get_basic_blocks(inter_code_arr))
    return None

# Used to identify leaders and generate the basic blocks
def get_basic_blocks(inter_code_arr):
    basic_blocks = []
    curr_block = []
    leaders= []

    # Holds the positions of the labels in the code
    label_positions = {}

    # We dont want label, we just want the first 3AC instr
    leaders.append(1)

    # Now we find the leaders using the other definitions for leaders
    prev = None
    curr = None

    # print(inter_code_arr)
    for i in range(2,len(inter_code_arr)):
        # Any instruction that is the target of a jump
        curr = inter_code_arr[i].strip(" ").split(" ")
        # print("curr: ",curr)
        if (":" in curr[0]):
            leaders.append(i)
            
            # print("leaders2: ",leaders)
        
            # leaders.append()    
        # Any instruction that follows a jump/ goto
        if (prev != None and len(prev) == 2 and "goto" in (prev)):
            if (i not in leaders):
                leaders.append(i)
        
        prev = curr
    # Getting rid of the return statement
    # leaders = leaders[:-1]
    print("leaders: ",leaders)

    # basic_blocks = []
    temp = []
    curr = 1
    for i in range(0, len(inter_code_arr)):

        if curr == len(leaders):
            temp.append(inter_code_arr[i])

        elif i == leaders[curr]:
            basic_blocks.append(temp)
            temp = []
            temp.append(inter_code_arr[i])
            curr += 1

        else :
            temp.append(inter_code_arr[i])
            # temp = []

    basic_blocks.append(temp)

    print(basic_blocks)
    return basic_blocks