def day15q1(nums, target=True):
    memory = {}
    for turn, num in enumerate(nums):
        memory[num] = (1, turn+1, 0)
    for turn in range(len(nums)+1, target):
        t, l1, l2 = memory[num]
        if t == 1:
            num = 0
        else:
            num = l1 - l2
        if num in memory:
            t, l1, l2 = memory[num]
            memory[num] = (t + 1, turn, l1)
        else:
            memory[num] = (1, turn, 0)
    return num


all_nums = [int(num) for num in open('input.txt').read().split(',')]
print(day15q1(all_nums, target=2021))
print(day15q1(all_nums, target=30000001))
