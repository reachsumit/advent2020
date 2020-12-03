def day3q1(data, rows, cols, down=0, right=0):
    x, y = 0, 0
    answer = 0

    while True:
        x += down
        y += right

        if y > cols - 1:
            y -= cols
        if x <= rows-1:
            if data[x][y] == '#':
                answer += 1
        else:
            break

    return answer


inputs = [line.rstrip('\n') for line in open('input.txt')]
r, c = len(inputs), len(inputs[0])

# Q1:
print(day3q1(data=inputs, rows=r, cols=c, right=3, down=1))

# Q2:
print(day3q1(data=inputs, rows=r, cols=c, right=1, down=1) *
      day3q1(data=inputs, rows=r, cols=c, right=3, down=1) *
      day3q1(data=inputs, rows=r, cols=c, right=5, down=1) *
      day3q1(data=inputs, rows=r, cols=c, right=7, down=1) *
      day3q1(data=inputs, rows=r, cols=c, right=1, down=2))
