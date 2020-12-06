def day6q1(groups):
    answer = 0
    for group in groups:
        seen = set()
        for char in group:
            if char != '\n':
                seen.add(char)
        answer += len(seen)
    return answer


def day6q2(groups):
    answer = 0
    for group in groups:
        seen = dict()
        all_lines = group.split('\n')
        for line in all_lines:
            for char in line:
                seen[char] = seen.get(char, 0) + 1
        for k, v in seen.items():
            if v == len(all_lines):
                answer += 1
    return answer


with open('input.txt') as input_file:
    all_groups = input_file.read().split("\n\n")

print(day6q1(all_groups))
print(day6q2(all_groups))
