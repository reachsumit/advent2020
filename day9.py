def day9q1(numbers, plen=25):
    store = set(numbers[:plen])
    to_delete = 0

    for i in numbers[plen:]:
        found = False
        for num in store:
            if (i - num) in store:
                found = True
                break
        if not found:
            return i
        store.remove(numbers[to_delete])
        store.add(i)
        to_delete += 1


def day9q2(numbers, target):
    temp = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if sum(numbers[i:j]) == target:
                return min(numbers[i:j]) + max(numbers[i:j])
            elif sum(numbers[i:j]) > target:
                break


all_numbers = [int(line.rstrip('\n')) for line in open('input.txt')]
invalid_number = day9q1(all_numbers, plen=25)
print(invalid_number)
print(day9q2(all_numbers, invalid_number))
