import re
from itertools import product


def get_masked_value(mask, val, q2=False):
    if q2:
        return val | int(mask.replace('X', '0'), 2)
    one_ops = int(mask.replace('X', '0'), 2)
    zero_ops = int(mask.replace('X', '1'), 2)
    return (val | one_ops) & zero_ops


def day14q1(all_lines):
    mask = None
    memory = {}
    for line in all_lines:
        if line.startswith('mask'):
            mask = re.match('mask = (.*)', line)[1]
        else:
            group = re.match('mem\[([0-9]+)\] = ([0-9]+)', line)
            idx, val = int(group[1]), int(group[2])
            memory[idx] = get_masked_value(mask, val)
    return(sum(memory.values()))


def day14q2(all_lines):
    mask = None
    memory = {}
    for line in all_lines:
        if line.startswith('mask'):
            mask = re.match('mask = (.*)', line)[1]
        else:
            group = re.match('mem\[([0-9]+)\] = ([0-9]+)', line)
            idx, val = int(group[1]), int(group[2])
            base_val = get_masked_value(mask, idx, q2=True)
            zero_idxs = [idx for idx, v in enumerate(mask) if v == 'X']
            base_mask = list(format(base_val, '036b'))
            for filler in [x for x in product([0, 1], repeat=len(zero_idxs))]:
                for idx, fill in zip(zero_idxs, filler):
                    base_mask[idx] = str(fill)
                memory[int("".join(base_mask), 2)] = val
    return(sum(memory.values()))


print(day14q1(open('input.txt').readlines()))
print(day14q2(open('input.txt').readlines()))
