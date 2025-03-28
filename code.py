# by R0Master

number = int(input())
operation = input()
number2 = int(input())

sdasdsad
def root(x, y):
    return x ** (1 / y)


def rounder(number):
    if str(number)[2:-10].count('9') >= 4:
        number = str(a//1+1)[:-2]
    return number


if operation == '+':
    print(f'Result: {number + number2}')
elif operation == '-':
    print(f'Result: {number - number2}')
elif operation == '*':
    print(f'Result: {number * number2}')
elif operation == '/':
    print(f'Result: {number / number2}')
elif operation == '/' and number2 == 0:
    print('ERROR! DIVISION BY ZERO!')
elif operation == '^':
    print(f'Result: {number**number2}')
elif operation == 'root':
    print(f'Result: {rounder(root(number, number2))}')
