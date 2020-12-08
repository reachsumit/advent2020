def day8q1(instructions, starting_index=0):
    n = len(instructions)
    visited = [0] * n
    index, accumulator = starting_index, 0

    while True:
        if index > n-1 or visited[index]:
            break
        inst = instructions[index]
        visited[index] = 1
        if inst[:3] == 'nop':
            index += 1
            continue
        elif inst[:3] == 'acc':
            accumulator += int(inst[4:])
            index += 1
            continue
        else:
            index += int(inst[4:])
            continue

    retflag = True if index == n else False
    return accumulator, retflag


def day8q2(instructions):
    for idx, inst in enumerate(instructions):
        done = False
        if inst[:3] == 'nop':
            instructions[idx] = 'jmp'+inst[3:]
            acc, done = day8q1(instructions)
            instructions[idx] = inst
        elif inst[:3] == 'jmp':
            instructions[idx] = 'nop'+inst[3:]
            acc, done = day8q1(instructions)
            instructions[idx] = inst
        if done:
            return acc


all_instructions = [line.rstrip('\n') for line in open('input.txt')]
print(day8q1(all_instructions)[0])
print(day8q2(all_instructions))
