import timeit
import re


def day16q1(groups):
    data = set()
    error = 0
    invalid_indices = []
    for line in groups[0].split('\n'):
        l, r = re.findall(r'([0-9]+)-([0-9]+)', line)
        data.update(range(int(l[0]), int(l[1])+1))
        data.update(range(int(r[0]), int(r[1])+1))
    for idx, line in enumerate(groups[2].split('\n')[1:]):
        for num in line.split(','):
            if int(num) not in data:
                invalid_indices.append(idx)
                error += int(num)
    return error, invalid_indices


def day16q2(groups, invalids):
    all_fields = {}
    for line in groups[0].split('\n'):
        match = re.match(
            r'([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line)
        all_fields[match[1]] = set()
        all_fields[match[1]].update(range(int(match[2]), int(match[3])+1))
        all_fields[match[1]].update(range(int(match[4]), int(match[5])+1))

    list_of_list = [[int(y) for y in x.split(',')]
                    for idx, x in enumerate(groups[2].split('\n')[1:]) if idx not in invalids]
    list_of_list = [x for x in zip(*list_of_list)]
    matched = {}
    for idx, item in enumerate(list_of_list):
        for name in all_fields.keys():
            if all([i in all_fields[name] for i in item]):
                if name not in matched:
                    matched[name] = set()
                matched[name].add(idx)
    claimed = set()
    for k, v in sorted(matched.items(), key=lambda item: len(item[1])):
        for val in v:
            if val not in claimed:
                matched[k] = val
                claimed.add(val)
    my_tickets = groups[1].split('\n')[1].split(',')
    answer = 1
    for idx, name in enumerate(all_fields.keys()):
        if name.startswith('departure '):
            answer *= int(my_tickets[matched[name]])
    return answer


all_groups = open('input.txt').read().split('\n\n')
error_rate, invalid_indices = day16q1(all_groups)
# Q1
print(error_rate)
# Q2
print(day16q2(all_groups, invalid_indices))
