def day13q1(target, departures):
    min_dist, answer = float('inf'), -1
    for departure in departures:
        if departure - (target % departure) < min_dist:
            min_dist = departure - (target % departure)
            answer = departure
    return answer * min_dist


def day13q2(departures):
    candidate, step = 0, departures[0][0]
    for val, offset in departures[1:]:
        while True:
            candidate += step
            if not (candidate+offset) % val:
                break
        step *= val
    return candidate


with open('input.txt') as inp_file:
    target, schedule = inp_file.read().splitlines()
    departures = [int(item) for item in schedule.split(',') if item.isdigit()]

print(day13q1(int(target), departures))

departures = [[int(item), idx] for idx, item in enumerate(
    schedule.split(',')) if item.isdigit()]

print(day13q2(departures))
