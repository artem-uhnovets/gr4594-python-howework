'''
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1
'''
import random
number = int(input('Enter a number - length of list: '))
list = [0] * number
for i in range(number):
    list[i] = random.randint(0, 9)
print(*list)    # запись *list пзволяет выводить список без [ ] и ,
numberX = int(input('Enter a number to count in list: '))
print('Number {} in list are {} time(s)'.format(numberX, list.count(numberX)))