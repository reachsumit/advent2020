def day15q1(nums, q1=True):
    memory = {}
    for turn, num in enumerate(nums):
        if num in memory:
            t, l1, l2 = memory[num]
            memory[num] = (t+1, turn+1, l1)
        else:
            memory[num] = (1, turn+1, 0)
    last = num
    target = 2021 if q1 else 30000001
    for turn in range(len(nums)+1, target):
        if memory[last][0] == 1:
            last = 0
        else:
            last = memory[last][1] - memory[last][2]
        if last in memory:
            t, l1, l2 = memory[last]
            memory[last] = (t + 1, turn, l1)
        else:
            memory[last] = (1, turn, 0)
    return last


all_nums = [int(num) for num in open('input.txt').read().split(',')]
print(day15q1(all_nums))
print(day15q1(all_nums, q1=False))
