from functools import reduce
from utils import read_input_as_doc

data = read_input_as_doc('inputs/input06.txt')
groups = list(map(lambda x: x.split(), data.split('\n\n')))


sum_answers_any = 0
sum_answers_all = 0

for group in groups:
    answers_any = set(''.join(group))
    sum_answers_any += len(answers_any)

    answers_all = reduce(lambda x, y: set(x).intersection(set(y)), group)
    sum_answers_all += len(answers_all)

print(sum_answers_any)
print(sum_answers_all)