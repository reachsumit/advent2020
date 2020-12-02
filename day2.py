def day2q1(data):
    answer = 0
    for password in data:
        parts = password.split()
        min_len, max_len = parts[0].split("-")

        count = 0
        target = parts[1][0]
        for c in parts[2]:
            if c == target:
                count += 1

        if count >= int(min_len) and count <= int(max_len):
            answer += 1
    return answer


def day2q2(data):
    answer = 0
    for password in data:
        parts = password.split()
        min_len, max_len = parts[0].split("-")

        found = 0
        target = parts[1][0]
        if parts[2][int(min_len)-1] == target:
            found += 1
        if parts[2][int(max_len)-1] == target:
            found += 1
        if found == 1:
            answer += 1

    return answer


inputs = [line.rstrip('\n') for line in open('input.txt')]

print(day2q1(inputs))
print(day2q2(inputs))
