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
    final_string = ""

    
    register_map = {}

    # Registor desc = {"R0":("t71","t43",...),..."RN":("t8","t32",...)}
    registor_descriptor = {}

    # Address dec = {"t1":"R0",...,"tn":"x"}
    address_descriptor = {}

    basic_blocks = get_basic_blocks(inter_code_arr)
    print(basic_blocks)
    i = 1


    return None

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
