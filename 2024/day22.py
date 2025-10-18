import utils 
from functools import reduce
from collections import defaultdict

def mix(n1, n2):
    return n1 ^ n2

def prune(n):
    return n % 16777216

def evolve(n):
    n = prune(mix(n, n*64))
    n = prune(mix(n, int(n/32)))
    n = prune(mix(n, n*2048))
    return n


if __name__ == '__main__':
    numbers = utils.read_input_as_int('inputs/day22.txt')
    print('part 1: ', sum(reduce(lambda v, _: evolve(v), range(2000), x) for x in numbers))

    seqs = defaultdict(int)
    for n in numbers:
        seen = set()
        seq = []
        prev_price = n % 10
        for i in range(2000):
            n = evolve(n)
            price = n % 10
            
            seq.append(price - prev_price)
            
            if i >= 3:
                k = ','.join(map(str, seq))
                if k not in seen:
                    seqs[k] += price
                    seen.add(k)
                
                seq.pop(0)
            
            prev_price = price

    max_key, max_value = max(seqs.items(), key=lambda item: item[1])
    print('part 2: ', max_value)
