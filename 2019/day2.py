
from copy import deepcopy

def runProgram(instructions, noun = 12, verb = 2):
    instructions[1] = noun
    instructions[2] = verb

    for i in range(0, len(instructions), 4):
        op = instructions[i]
        if op == 1: 
            instructions[instructions[i+3]] = instructions[instructions[i+1]] + instructions[instructions[i+2]]
        elif op == 2:
            instructions[instructions[i+3]] = instructions[instructions[i+1]] * instructions[instructions[i+2]]
        elif op == 99:
            break
        else: 
            pass
            # print('unknown op: ', op)
        

    return instructions[0]


if __name__ == "__main__":

    with open('puzzle_input/day2.txt', 'r') as f:
        intList = list(map(lambda x : int(x), f.readline().split(',')))

    instructions = deepcopy(intList)
    print('Part 1: ', runProgram(instructions))


    for noun in range(0,100):
        for verb in range(0,100):
            try:
                instructions = deepcopy(intList)
                answer = runProgram(instructions, noun, verb)
            except: 
                answer = 0
            if answer == 19690720:
                print(noun, verb)
                break
        else:
            continue
        break
    
    print('Part 2: ', 100*noun+verb)
