import utils
from collections import defaultdict
from functools import cmp_to_key

def parse_rules(rules):
    r = defaultdict(set)
    for rule in rules:
        x, y = rule.split('|')
        r[int(x)].add(int(y))
    return r


def compare_func(a, b):
    if b in rules[a]:
         return -1 # all good
    elif a in rules[b]:
         return 1 # wrong order
    else:
         return 0


def check_page(page):
    i = (len(page)-1)//2 
    return page[i] if sorted(page, key=cmp_to_key(compare_func)) == page else 0


def fix_ordering(page):
    i = (len(page)-1)//2
    return sorted(page, key=cmp_to_key(compare_func))[i]


if __name__ == '__main__':
    data = utils.read_input('inputs/day5.txt')
    rules = utils.take_while(lambda x: x != '', data)
    pages = data[len(rules)+1:]
    rules = parse_rules(rules)
    
    part_1 = 0
    part_2 = 0
    for page in pages:
        page = [int(x) for x in page.split(',')]
        res = check_page(page)
        if res > 0:
             part_1 += res
        else:
             part_2 += fix_ordering(page)
    print(part_1)
    print(part_2)
