import re


def apply_op(op, a, b):
    # print(op, a, b)
    if op == '+':
        return int(a) + int(b)
    if op == '*':
        return int(a) * int(b)


def solve_q1(eq):
    eq = eq[::-1]
    operator = []
    value = []
    for char in eq:
        if char == ' ':
            continue
        elif char in '0123456789':
            value.append(char)
        elif char in '+*)':
            operator.append(char)
        elif char == '(':
            while(operator[-1] != ')'):
                value.append(
                    apply_op(operator.pop(), value.pop(), value.pop()))
            operator.pop()
    while operator:
        value.append(apply_op(operator.pop(), value.pop(), value.pop()))
    return value.pop()


class Q2(int):
    def __mul__(self, operand):
        return Q2(int(self) + operand)

    def __add__(self, operand):
        return Q2(int(self) * operand)


def solve_q2(eq):
    eq = re.sub(r"(\d+)", r"fun(\1)", eq)
    eq = eq.replace('*', '-')
    eq = eq.replace('+', '*')
    eq = eq.replace('-', '+')
    return eval(eq, {}, {"fun": Q2})


def day18q1(equations):
    answer = 0
    for equation in equations:
        answer += solve_q1(equation)
    return answer


def day18q2(equations):
    answer = 0
    for equation in equations:
        answer += solve_q2(equation)
    return answer


all_equations = [line.rstrip('\n') for line in open('input.txt')]
print(day18q1(all_equations))
print(day18q2(all_equations))
