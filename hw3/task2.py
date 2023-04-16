'''
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X.

5
1 2 3 4 5
6
-> 5
'''
import random
import sys
number = int(input('Enter a number - length of list: '))
numberX = int(input('Enter a number to compare: '))
diff = int(sys.maxsize) # максимальное число в Python
diffIndex = 0
list = [0] * number
for i in range(number):
    list[i] = random.randint(0, 9)
    if abs(numberX - list[i]) < diff:
        diff = abs(numberX - list[i])
        diffIndex = i
print(*list)    # запись *list пзволяет выводить список без [ ] и ,
print('Number {} with index {} in list as close as possible to the number {}.'.format(list[diffIndex], diffIndex, numberX))