import utils


def parse_data(data):
    machines = []
    for d in data:
        a, b, p = d.split('\n')

        _, _, x, y = a.split()
        x = int(x[2:-1])
        y = int(y[2:])
        a = (x, y)

        _, _, x, y = b.split()
        x = int(x[2:-1])
        y = int(y[2:])
        b = (x, y)
        
        _, x, y = p.split()
        x = int(x[2:-1])
        y = int(y[2:])
        p = (x, y)
        
        machines.append([a, b, p])
        
    return machines

def play(a, b, p):
    r = solve_diophantine(a, b, p)
    return 3 * r[0] + r[1]


def solve_diophantine(a, b, p):
    a1, a2 = a
    b1, b2 = b
    p1, p2 = p

    # Calculate the determinant of the coefficient matrix
    D = a1 * b2 - a2 * b1
    
    # Calculate the values of n1 and n2 using Cramer's Rule
    numerator_n1 = p1 * b2 - p2 * b1
    numerator_n2 = a1 * p2 - a2 * p1
    
    # Check if both numerators are divisible by the determinant
    if numerator_n1 % D != 0 or numerator_n2 % D != 0:
        return 0, 0
    
    # Calculate the solutions for n1 and n2
    n1 = numerator_n1 // D
    n2 = numerator_n2 // D

    return n1, n2



if __name__ == '__main__':
    data = utils.read_input_as_doc('inputs/day13.txt')
    data = data.split('\n\n')
    machines = parse_data(data)
    
    part_1, part_2 = 0, 0
    for a, b, p in machines:
        part_1 += play(a, b, p)
        part_2 += play(a, b, list(map(lambda x: x+10000000000000, p)))
   
    print(part_1)
    print(part_2)
    