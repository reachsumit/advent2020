def count_adjacent(_seats, i, j, q1=True):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for direction in directions:
        new_i, new_j = i, j
        while True:
            new_i += direction[0]
            new_j += direction[1]
            if 0 <= new_i < len(_seats) and 0 <= new_j < len(_seats[0]):
                if _seats[new_i][new_j] != '.':
                    if _seats[new_i][new_j] == '#':
                        count += 1
                    break
                if q1:
                    break
            else:
                break
    return count


def count_occupied(_seats):
    count = 0
    for i in range(len(_seats)):
        for j in range(len(_seats[0])):
            if _seats[i][j] == '#':
                count += 1
    return count


def day11q1(seats, q1=True):
    seats_copy = [row[:] for row in seats]
    max_occupied = 4 if q1 else 5
    something_changed = True
    while something_changed:
        something_changed = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == 'L'and count_adjacent(seats, i, j, q1) == 0:
                    something_changed = True
                    seats_copy[i][j] = '#'
                elif seats[i][j] == '#' and count_adjacent(seats, i, j, q1) >= max_occupied:
                    something_changed = True
                    seats_copy[i][j] = 'L'
        seats = [row[:] for row in seats_copy]
    return count_occupied(seats)


all_seats = [[char for char in line.strip('\n')] for line in open('input.txt')]
# Q1
print(day11q1(all_seats))
# Q2
print(day11q1(all_seats, q1=False))
