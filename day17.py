import utils
from functools import reduce

std = ''

def combo(operand):
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return register[operand-4]
    else:
        raise f'Invalid combo operand, {operand}'

def program(opcode, operand, p):
    if opcode == 0:
        """performs division. 
        The numerator is the value in the A register. 
        The denominator is found by raising 2 to the power of the instruction's combo operand. 
        (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        The result of the division operation is truncated to an integer and then written to the A register."""
        num = register[0]
        denom = pow(2, combo(operand))
        register[0] = int(num/denom)
        p += 2
    
    elif opcode == 1:
        """ bitwise XOR of register B and the instruction's literal operand, 
        then stores the result in register B."""
        register[1] = register[1] ^ operand
        p += 2
    
    elif opcode == 2:
        """combo operand modulo 8 (thereby keeping only its lowest 3 bits), 
        then writes that value to the B register."""
        register[1] = combo(operand) % 8
        p += 2
    
    elif opcode == 3:
        """does nothing if the A register is 0. 
        However, if the A register is not zero, 
        it jumps by setting the instruction pointer to the value of its literal operand; 
        if this instruction jumps, the instruction pointer is not increased by 2 after this instruction."""
        if register[0] != 0:
            p = operand
        else:
            p += 2
    
    elif opcode == 4:
        """bitwise XOR of register B and register C, 
        then stores the result in register B.
          (For legacy reasons, this instruction reads an operand but ignores it.)"""
        register[1] = register[1] ^ register[2]
        p += 2
    
    elif opcode == 5:
        """calculates the value of its combo operand modulo 8, 
        then outputs that value. (If a program outputs multiple values, they are separated by commas.)"""
        std.append(str(combo(operand) % 8))
        p += 2
    
    elif opcode == 6: 
        """exactly like the op = 0 instruction except that the result is stored in the B register. 
        (The numerator is still read from the A register.)"""
        num = register[0]
        denom = pow(2, combo(operand))
        register[1] = int(num/denom)
        p += 2
    
    elif opcode == 7:
        """works exactly like the adv instruction except that the result is stored in the C register. 
        (The numerator is still read from the A register.)"""
        num = register[0]
        denom = pow(2, combo(operand))
        register[2] = int(num/denom)
        p += 2
    
    return p


if __name__ == '__main__':
    register = ['A', 'B', 'C']
    std = []
    p = 0

    lines = utils.read_input('inputs/day17.txt')
    for i, line in enumerate(lines):
        if line.startswith('Register'):
            v = line.split()[-1]
            register[i] = int(v)
        elif line.startswith('Program'):
            inst = line.split()[-1]
            inst = [int(x) for x in inst.split(',')]

    while p < len(inst):
        p = program(inst[p], inst[p+1], p)

    print('part 1: ', ','.join(std))

    a1, a2 = pow(8, 15), pow(8, 16)
    for i in range(15,-1,-1):
        for a in range(a1, a2)[::pow(8, i)]:
            p = 0
            std = []
            register = [a, 0, 0]
            while p < len(inst):
                p = program(inst[p], inst[p+1], p)
            if [int(x) for x in std[i:]] == inst[i:]:
                a1 = a
                break
    print('part 2: ', a)
