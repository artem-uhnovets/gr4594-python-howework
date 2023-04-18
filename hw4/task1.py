"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
import random
# n = int(input('Enter a number - length of list: '))
list_n = [0] * int(input('Enter a number - amount of numbers: 1. '))
for i in range(len(list_n)):
    list_n[i] = random.randint(0, 9)
list_m = [0] * int(input('Enter a number - amount of numbers: 2. '))
for i in range(len(list_m)):
    list_m[i] = random.randint(0, 9)
print('{}\n{}\n{}'.format(list_n, list_m, sorted(set(list_n).intersection(set(list_m)))))


