present_passes = []


def find_seat_id(boarding_pass, finding_rows=False):
    start = 0
    end = 127 if finding_rows else 7
    for c in boarding_pass:
        mid = (start + end) // 2
        if c in ('F', 'L'):
            end = mid
        elif c in ('B', 'R'):
            start = mid + 1
    return start if boarding_pass[-1] in ('L', 'F') else end


def day5q1(boarding_passes):
    answer = 0
    for boarding_pass in boarding_passes:
        temp = (find_seat_id(
            boarding_pass[: 7], finding_rows=True)*8) + find_seat_id(boarding_pass[7:])
        present_passes.append(temp)
        if temp > answer:
            answer = temp
    return answer


def day5q2():
    for id in range(8, 1016):
        if id not in present_passes and id-1 in present_passes and id+1 in present_passes:
            return id


passes = [line.rstrip('\n') for line in open('input.txt')]
print(day5q1(passes))
print(day5q2())
