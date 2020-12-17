import copy
matrix = [[[['.' for _ in range(22)] for _ in range(22)]
           for _ in range(15)] for _ in range(15)]


def get_active_count_q2(tw, tz, ty, tx):
    all = list()
    count = 0
    for _w in [0, -1, 1]:
        for _z in [0, -1, 1]:
            for _y in [0, -1, 1]:
                for _x in [0, -1, 1]:
                    if tw+_w == tw and tz+_z == tz and ty+_y == ty and tx+_x == tx:
                        continue
                    if matrix[tw+_w][tz+_z][ty+_y][tx+_x] == '#':
                        count += 1
    return count


def total_active_count_q2():
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                for l in range(len(matrix[0][0][0])):
                    if matrix[i][j][k][l] == '#':
                        count += 1
    return count


def day17q2():
    global matrix
    x_lower, x_upper, y_lower, y_upper, z_lower, z_upper, w_lower, w_upper = 6, 15, 6, 15, 6, 8, 6, 8
    matrix_copy = copy.deepcopy(matrix)
    for cycle in range(6):
        for w in range(w_lower, w_upper+1):
            for z in range(z_lower, z_upper+1):
                for y in range(y_lower, y_upper+1):
                    for x in range(x_lower, x_upper+1):
                        active_count = get_active_count_q2(w, z, y, x)
                        if matrix[w][z][y][x] == '#' and active_count not in [2, 3]:
                            matrix_copy[w][z][y][x] = '.'
                        if matrix[w][z][y][x] == '.' and active_count == 3:
                            matrix_copy[w][z][y][x] = '#'
        matrix = copy.deepcopy(matrix_copy)
        x_lower -= 1
        x_upper += 1
        y_lower -= 1
        y_upper += 1
        z_lower -= 1
        z_upper += 1
        w_lower -= 1
        w_upper += 1

    return total_active_count_q2()


x, y, z, w = 7, 7, 7, 7
for line in open('input.txt'):
    y = 7
    for val in line.strip('\n'):
        matrix[w][z][y][x] = val
        y += 1
    x += 1

print(day17q2())
