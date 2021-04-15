def generate(inter_code):
    inter_code_arr = inter_code.split("\n")

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
    # print(final_string)
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
        if (len(curr) == 2 and "goto" in (curr)):
            leaders.append(inter_code_arr.index(curr[-1]+":"))    
        # Any instruction that follows a jump/ goto
        if (prev != None and len(prev) == 2 and "goto" in (prev)):
            leaders.append(i)
        prev = curr
    print("leaders: ",leaders)
    return basic_blocks