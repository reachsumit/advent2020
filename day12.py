all_directions = ['east', 'south', 'west', 'north']
q2_switch = [('east', 'north'),
             ('north', 'west'),  # 90
             ('west', 'south'),  # 180
             ('south', 'east')]  # 270
current_direction = 'east'


def get_new_direction(degrees, left=False):
    degrees = 360 - degrees if left else degrees
    return all_directions[(all_directions.index(current_direction) + degrees//90) % len(all_directions)]


def get_new_direction_q2(east, north, degrees, left=False):
    degrees = 360 - degrees if left else degrees
    e, n = q2_switch[(degrees//90) % len(q2_switch)]
    if e == 'south' and n == 'east':
        east, north = (-1 * north), east
    elif e == 'west' and n == 'south':
        east, north = (-1 * east), (-1 * north)
    elif e == 'north' and n == 'west':
        east, north = north, (-1 * east)
    return east, north


def day11q1(steps):
    global current_direction
    north, east = 0, 0
    for step in steps:
        if step[0] == 'N':
            north += int(step[1:])
        elif step[0] == 'S':
            north -= int(step[1:])
        elif step[0] == 'E':
            east += int(step[1:])
        elif step[0] == 'W':
            east -= int(step[1:])
        elif step[0] == 'L':
            current_direction = get_new_direction(int(step[1:]), left=True)
        elif step[0] == 'R':
            current_direction = get_new_direction(int(step[1:]))
        elif step[0] == 'F':
            if current_direction == 'east':
                east += int(step[1:])
            elif current_direction == 'west':
                east -= int(step[1:])
            elif current_direction == 'north':
                north += int(step[1:])
            else:
                north -= int(step[1:])
    return abs(north) + abs(east)


def day11q2(steps):
    s_north, s_east = 0, 0
    w_north, w_east = 1, 10
    for step in steps:
        if step[0] == 'N':
            w_north += int(step[1:])
        elif step[0] == 'S':
            w_north -= int(step[1:])
        elif step[0] == 'E':
            w_east += int(step[1:])
        elif step[0] == 'W':
            w_east -= int(step[1:])
        elif step[0] == 'L':
            w_east, w_north = get_new_direction_q2(
                w_east, w_north, int(step[1:]), left=True)
        elif step[0] == 'R':
            w_east, w_north = get_new_direction_q2(
                w_east, w_north, int(step[1:]))
        elif step[0] == 'F':
            s_east += int(step[1:])*w_east
            s_north += int(step[1:])*w_north
    return abs(s_east) + abs(s_north)


all_steps = [line.rstrip('\n') for line in open('input.txt')]
print(day11q1(all_steps))
print(day11q2(all_steps))
