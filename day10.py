def day10q1(volts):
    volts.add(max(volts)+3)
    start, last_found = 0, 0
    result = {1: [], 3: []}

    while start <= max(volts):
        if start + 1 in volts:
            result[1].append(start+1)
            last_found = start
            start += 1
        elif start + 2 in volts:
            start += 2
        elif start + 3 in volts:
            result[3].append(start+3)
            last_found = start
            start += 3
        else:
            break
    return len(result[1]) * len(result[3])


def day10q2(volts):
    dp = {0: 1}
    volts.add(0)
    volts.add(max(volts)+3)

    for volt in volts:
        to_add = 0
        if volt - 1 in volts:
            to_add += dp[volt-1]
        if volt - 2 in volts:
            to_add += dp[volt-2]
        if volt - 3 in volts:
            to_add += dp[volt-3]
        dp[volt] = to_add
        dp[0] = 1
    return dp[max(volts)]


all_volts = {int(line.rstrip('\n')) for line in open('input.txt')}
print(day10q1(all_volts))
print(day10q2(all_volts))
