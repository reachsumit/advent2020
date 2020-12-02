def day1q1(numbers, target=2020):
    seen = set()

    for num in numbers:
        if (target - num) in seen:
            return num * (target - num)
        seen.add(num)

    return False


def day1q2(numbers, target=2020):
    for item in numbers:
        retval = day1q1(numbers, target - item)
        if retval:
            return retval * item


inputs = [int(line.rstrip('\n')) for line in open('input.txt')]

print(day1q1(inputs))
print(day1q2(inputs))
