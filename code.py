from math import *

number = int(input())
action = input()
number2 = int(input())


def root(x, y):
    return x ** (1 / y)


if action == '+':
    print('Result:', number + number2)
elif action == '-':
    print('Result:', number - number2)
elif action == '*':
    print('Result:', number * number2)
elif action == '/':
    print('Result:', number / number2)
elif action == '/' and number2 == 0:
    print('ERROR! DIVISION BY ZERO!')
elif action == '^':
    print('Result:', number**number2)
elif action == 'root':
    print('Result:', ceil(root(number, number2)) if root(number, number2) * 100 % 100 > 98 else root(number, number2))

# by R0Master
