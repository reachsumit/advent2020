def count_adjacent(_seats, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if new_i >= 0 and new_j >= 0 and new_i < len(_seats)\
                and new_j < len(_seats[0]) and _seats[new_i][new_j] == '#':
            count += 1
    return count


def count_adjacent_q2(_seats, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for direction in directions:
        new_i, new_j = i, j
        while True:
            new_i += direction[0]
            new_j += direction[1]
            if new_i >= 0 and new_j >= 0 and new_i < len(_seats)\
                    and new_j < len(_seats[0]):
                if _seats[new_i][new_j] != '.':
                    if _seats[new_i][new_j] == '#':
                        count += 1
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


def day11q1(seats):
    seats_copy = [row[:] for row in seats]
    something_changed = True
    while something_changed:
        something_changed = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == 'L'and count_adjacent(seats, i, j) == 0:
                    something_changed = True
                    seats_copy[i][j] = '#'
                elif seats[i][j] == '#' and count_adjacent(seats, i, j) >= 4:
                    something_changed = True
                    seats_copy[i][j] = 'L'
        seats = [row[:] for row in seats_copy]
    return count_occupied(seats)


def day11q2(seats):
    seats_copy = [row[:] for row in seats]
    something_changed = True
    while something_changed:
        something_changed = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == 'L'and count_adjacent_q2(seats, i, j) == 0:
                    something_changed = True
                    seats_copy[i][j] = '#'
                elif seats[i][j] == '#' and count_adjacent_q2(seats, i, j) >= 5:
                    something_changed = True
                    seats_copy[i][j] = 'L'
        seats = [row[:] for row in seats_copy]
    return count_occupied(seats)


all_seats = [[char for char in line.strip('\n')] for line in open('input.txt')]
print(day11q1(all_seats))
print(day11q2(all_seats))
