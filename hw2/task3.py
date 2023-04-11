# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Enter number: '))
level = 0
result = 0
while result < number:
    result = 2 ** level
    level += 1
    if result > number:
        break
    else:
        print(result, sep='', end=' ')