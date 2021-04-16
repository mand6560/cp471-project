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

    final_string = ""
    space_str = ""
    register_count = 1
    register_map = {}
    # Registor desc = {"R0":("t71","t43",...),..."RN":("t8","t32",...)}
    registor_descriptor = {}

    # Address dec = {"t1":"R0",...,"tn":"x"}
    address_descriptor = {}

    basic_blocks = get_basic_blocks(inter_code_arr)
    # print(basic_blocks)

    temp_b_b = basic_blocks
    basic_blocks = []
    for block in temp_b_b:
        temp = []
        for line in block:
            if(":" in line):
                line = line.split(":")
                temp += ['{}:'.format(line[0]), line[1].strip()]
            else:
                temp.append(line)
        basic_blocks.append(temp)

        #  temp = basic_blocks[k].pop(l)
        #   temp = temp.split(" ", 1)
        #    for element in temp:
        #         basic_blocks[k].insert(element)
        #     print("temp: ", temp)

    # print(basic_blocks)

    for i in range(len(basic_blocks)):
        for j in range(len(basic_blocks[i])):
            curr_instr = basic_blocks[i][j].split(" ")
            if (":" in curr_instr[0]):
                final_string += curr_instr[0].strip() + "\n"

                # # print(curr_instr)
                # if (curr_instr[2] == "="):
                #     # space_str += " "
                #     if (not(curr_instr[1] in register_map)):
                #         register_map[curr_instr[1]] = "R{}".format(
                #             register_count)
                #         register_count += 1

                #     final_string += "LD " + register_map[curr_instr[1]]
                #     if (curr_instr[3].isdigit()):
                #         final_string += ",#" + curr_instr[3] + "\n"
                #     else:
                #         final_string += "," + curr_instr[3] + "\n"
                #     space_str += " "
                # elif (curr_instr[1] == "if"):
                #     pass
                # elif (curr_instr[1] == "return"):
                #     pass
            elif ("return" in curr_instr[0]):
                final_string += "ST {},{}".format("RESULT",
                                                  register_map[curr_instr[1]]) + "\n"
            elif ("goto" in curr_instr[0]):
                final_string += "B "+curr_instr[1] +"\n"
            elif("if" in curr_instr[0]):
                # t3 = t2-t1
                arg1 = curr_instr[1]

                arg2 = curr_instr[3]
                if not(arg2.isdigit()):
                    arg2 = register_map[arg2]
                else:
                    arg2 = "#"+arg2
                final_string += "LD " + \
                    "R{},{}".format(len(register_map)+1,
                                    register_map[arg1])+"\n"
                final_string += "LD " + \
                    "R{},{}".format(len(register_map)+2,
                                    arg2)+"\n"
                final_string += "SUB " + \
                    "R{},R{},R{}".format(
                        len(register_map)+1, len(register_map)+1, len(register_map)+2) + "\n"

                # IF R1 = 0 means they are eq
                # IF R1 > 0 means R1 is bigger
                # Else R2 is bigger
                if (curr_instr[2] == ">="):
                    final_string += "BGE R{},R{},{}".format(
                        len(register_map)+1, len(register_map)+2, curr_instr[-1] + "\n")
                if (curr_instr[2] == "<="):
                    final_string += "BLE R{},R{},{}".format(
                        len(register_map)+1, len(register_map)+2, curr_instr[-1] + "\n")
                if (curr_instr[2] == "<"):
                    final_string += "BLT R{},R{},{}".format(
                        len(register_map)+1, len(register_map)+2, curr_instr[-1] + "\n")
                if (curr_instr[2] == ">"):
                    final_string += "BGT R{},R{},{}".format(
                        len(register_map)+1, len(register_map)+2, curr_instr[-1] + "\n")
                
                
                # elif ("")

            elif(curr_instr[1] == "="):

                if (len(curr_instr) == 3):
                    # print("strict eq", curr_instr)

                    if (not(curr_instr[0] in register_map)):
                        register_map[curr_instr[0]] = "R{}".format(
                            register_count)
                        register_count += 1

                    space_str += " "
                    final_string += "LD " + register_map[curr_instr[0]]
                    if (curr_instr[2].isdigit()):
                        final_string += ",#" + curr_instr[2] + "\n"
                    else:
                        final_string += "," + curr_instr[2] + "\n"
                else:
                    # print("strict eq", curr_instr)
                    if (not(curr_instr[0] in register_map)):
                        register_map[curr_instr[0]] = "R{}".format(
                            register_count)
                        register_count += 1
                    if (not(curr_instr[2] in register_map)):
                        register_map[curr_instr[2]] = "R{}".format(
                            register_count)
                        register_count += 1
                    space_str += " "
                    op = "LD"
                    if (curr_instr[3] == "+"):
                        op = "ADD"
                    elif (curr_instr[3] == "-"):
                        op = "SUB"
                    elif (curr_instr[3] == "*"):
                        op = "MUL"
                    elif (curr_instr[3] == "/"):
                        op = "DIV"
                    final_string += "{} {},{}".format(
                        op, register_map[curr_instr[0]], register_map[curr_instr[2]])
                    if (curr_instr[-1].isdigit()):
                        final_string += ",#" + curr_instr[-1] + "\n"
                    else:
                        final_string += "," + curr_instr[-1] + "\n"

        space_str = ""
    # print("final_string:\n"+final_string)

    return final_string

# Used to identify leaders and generate the basic blocks


def get_basic_blocks(inter_code_arr):
    basic_blocks = []
    curr_block = []
    leaders = []

    # Holds the positions of the labels in the code
    label_positions = {}

    # We dont want label, we just want the first 3AC instr
    leaders.append(0)

    # Now we find the leaders using the other definitions for leaders
    prev = None
    curr = None

    # print(inter_code_arr)
    for i in range(1, len(inter_code_arr)):
        # Any instruction that is the target of a jump
        curr = inter_code_arr[i].strip(" ").split(" ")
        # print("curr: ",curr)

        if (":" in curr[0]):
            leaders.append(i)

            # print("leaders2: ",leaders)

            # leaders.append()
        # Any instruction that follows a jump/ goto
        if (prev != None and "goto" in (prev)):
            # if (i not in leaders):
            leaders.append(i)

        prev = curr
    # Getting rid of the return statement
    # leaders = leaders[:-1]
    # print("leaders: ", leaders)

    # basic_blocks = []
    temp = []
    curr = 0
    for i in range(0, len(inter_code_arr)):

        if curr == len(leaders):
            temp.append(inter_code_arr[i])

        elif i == leaders[curr]:
            basic_blocks.append(temp)
            temp = []
            temp.append(inter_code_arr[i])
            curr += 1

        else:
            temp.append(inter_code_arr[i])
            # temp = []

    basic_blocks.append(temp)
    basic_blocks = basic_blocks[1:]
    # print(basic_blocks)
    return basic_blocks
