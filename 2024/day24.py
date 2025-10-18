import utils
from collections import defaultdict, deque



def calc(r1, r2, op):
    if op == 'OR':
        return r1 | r2
    elif op == 'AND':
        return r1 & r2
    elif op == 'XOR':
        return r1 ^ r2
    else:
        raise f'Unknown operation: {op}'


if __name__ == '__main__':
    data = utils.read_input('inputs/day24.txt')
    inputs = utils.take_while(lambda x: x != '', data)
    instructions = data[len(inputs)+1:]

    reg = defaultdict(None)
    for i in inputs:
        k, v = i.split(': ')
        reg[k] = int(v)
    
    inst = deque()
    for i in instructions:
        r1, op, r2, _, dest = i.split()
        if r1 in reg and r2 in reg:
            reg[dest] = calc(reg[r1], reg[r2], op)
        else: 
            inst.append((r1, op, r2, dest))

    while len(inst) > 0:
        r1, op, r2, dest = inst.popleft()
        if r1 in reg and r2 in reg:
            reg[dest] = calc(reg[r1], reg[r2], op)
        else: 
            inst.append((r1, op, r2, dest))
    

    zzs = {k: v for k, v in reg.items() if k.startswith('z')}
    sorted_keys = sorted(zzs.keys(), key=lambda x: int(x[1:]))
    binary_string = ''.join(str(zzs[key]) for key in sorted_keys)
    ans = int(binary_string[::-1], 2)
    print(ans)
    

    wrong = set()
    for i in instructions:
        r1, op, r2, _, dest = i.split()
        
        # Zn = (Xn ⊕ Yn) ⊕ Cn-1 
        # Cn = (Xn * Yn) + (Cn-1 * (Xn ⊕ Yn))
        if dest.startswith('z') and op != "XOR" and dest != 'z45':
            wrong.add(dest)
        
        elif (
            op == 'XOR' and 
            dest[0] != 'z' and 
            r1[0] not in ['x', 'y'] and
            r2[0] not in ['x', 'y']
            ):
            wrong.add(dest)

        # AND gate can only be input to an OR gate
        elif (op == 'AND' and 
              r1 != 'x00' and 
              r2 != 'x00'):
            for i2 in instructions:
                rr1, subop, rr2, _, _ = i2.split()
                if (dest == rr1 or dest == rr2) and subop != 'OR':
                    wrong.add(dest)

        # XOR gate can only be input to an AND/XOR gate
        elif op == 'XOR' or op == 'OR':
            for i2 in instructions:
                rr1, subop, rr2, _, _ = i2.split()
                if (dest == rr1 or dest == rr2) and subop == "OR":
                    wrong.add(dest)

    print(",".join(sorted(wrong)))
"""
By using the following formula

Zn = (Xn ⊕ Yn) ⊕ Cn-1

Cn = (Xn * Yn) + (Cn-1 * (Xn ⊕ Yn))

with C0 = (Xn * Yn)

We can derive a series of rule.

AND:
AND gate can only be input to an OR gate
AND gate cannot take other AND gate as input

XOR:
XOR gate can only be input to an AND/XOR gate
XOR gate cannot take AND gate as input

OR:
OR gate can only be input of AND/XOR gate
OR gate can only take AND gate as input

(Xn ⊕ Yn) ⊕ (a + b) should always output a Zxx except for the last carry z45
A gate with Zxx as its output cannot directly use Xn or Yn as inputs.
"""