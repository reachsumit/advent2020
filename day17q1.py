import copy
# for 6 turns make a 22x22x15 matrix
# input flat matrix will start at (7,7,7) and end at (14,14,7)
matrix = [[['.' for _ in range(22)] for _ in range(22)] for _ in range(15)]
# access memebers as: matrix[z][y][x] for e.g. print(matrix[14][21][21])


def get_active_count(tz, ty, tx):
    all = list()
    count = 0
    for _z in [0, -1, 1]:
        for _y in [0, -1, 1]:
            for _x in [0, -1, 1]:
                if tz+_z == tz and ty+_y == ty and tx+_x == tx:
                    continue
                if matrix[tz+_z][ty+_y][tx+_x] == '#':
                    count += 1
    return count


def total_active_count():
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if matrix[i][j][k] == '#':
                    count += 1
    return count


def day17q1():
    global matrix
    x_lower, x_upper, y_lower, y_upper, z_lower, z_upper = 6, 15, 6, 15, 6, 8
    matrix_copy = copy.deepcopy(matrix)
    for cycle in range(6):
        for z in range(z_lower, z_upper+1):
            for y in range(y_lower, y_upper+1):
                for x in range(x_lower, x_upper+1):
                    active_count = get_active_count(z, y, x)
                    if matrix[z][y][x] == '#' and active_count not in [2, 3]:
                        matrix_copy[z][y][x] = '.'
                    if matrix[z][y][x] == '.' and active_count == 3:
                        matrix_copy[z][y][x] = '#'
        matrix = copy.deepcopy(matrix_copy)
        x_lower -= 1
        x_upper += 1
        y_lower -= 1
        y_upper += 1
        z_lower -= 1
        z_upper += 1

    return total_active_count()


x, y, z = 7, 7, 7
for line in open('input.txt'):
    y = 7
    for val in line.strip('\n'):
        matrix[z][y][x] = val
        y += 1
    x += 1

print(day17q1())
