"""
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero

OP-Codes:
01 - adds
02 - multiplies
03 - save input
04 - output
05 - jump-if-true
06 - jump-if-false
07 - less than
08 - equals
99 - halt
"""
outputs = []

def decodeIntruction(pointer, program, input):
    instruction = str(program[pointer])
    instruction = (5 - len(instruction)) * '0' + instruction
    
    mode3 = instruction[0]
    if mode3 == '1':
        raise Exception('mode3 is 1')
    mode2 = instruction[1]
    mode1 = instruction[2]
    op = int(instruction[3:])

    isHalt = False

    if op == 1: 
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        program[program[pointer+3]] = v1 + v2
        pointer += 4

    elif op == 2:
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        program[program[pointer+3]] = v1 * v2
        pointer +=  4
    
    elif op == 3:
        program[program[pointer+1]] = input
        pointer += 2

    elif op == 4:
        if mode1 == '1': v = program[pointer+1] 
        else: v = program[program[pointer+1]]
        outputs.append(v)
        pointer += 2

    elif op == 5:
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        if v1 != 0:
           pointer = v2 
        else:
            pointer += 3

    elif op == 6:
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        if v1 == 0:
           pointer = v2 
        else:
            pointer += 3
    
    elif op == 7:
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        program[program[pointer+3]] = int(v1 < v2)
        pointer +=  4
    
    elif op == 8:
        if mode1 == '1': v1 = program[pointer+1] 
        else: v1 = program[program[pointer+1]]
        if mode2 == '1': v2 = program[pointer+2] 
        else: v2 = program[program[pointer+2]]
        program[program[pointer+3]] = int(v1 == v2)
        pointer +=  4
    
    elif op == 99:
        isHalt = True
    
    else:
        raise Exception('Op code error: ', op)

    return pointer, program, isHalt

        

if __name__ == "__main__":

    with open('puzzle_input/day5.txt', 'r') as f:
        program = list(map(lambda x : int(x), f.readline().split(',')))
    
    isHalt = False
    pointer = 0

    while not isHalt:
        pointer, program, isHalt = decodeIntruction(pointer, program, 2)

    print('Part one: ',  outputs[-1])

    # Part 2
    with open('puzzle_input/day5.txt', 'r') as f:
        program = list(map(lambda x : int(x), f.readline().split(',')))
    
    isHalt = False
    pointer = 0

    while not isHalt:
        pointer, program, isHalt = decodeIntruction(pointer, program, 5)

    print('Part two: ',  outputs[-1])