"""
В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

"""
import random
max_summ = 0
max_index = 0
list = [0] * int(input('Enter a number of blueberry bushes: '))
for i in range(len(list)):
    list[i] = random.randint(0, 9)
print(*list)
for i in range(len(list)):
    if (list[i-1] + list[i] + list[1 - len(list) + i]) > max_summ:
        max_summ = list[i-1] + list[i] + list[1 - len(list) + i]
        max_index = i
print(f'Max number of berries is {max_summ} and located in the bushes {len(list) if max_index == 0 else max_index}-{max_index + 1}-{max_index + 2 if (max_index + 2) <= len(list) else 1}')

# for i in range(len(list := [0] * int(input('Enter a number of blueberry bushes: ')))):
#     list[i] = random.randint(0, 9)
# print(*list)

# list = [random.randint(0, 99) for i in range(int(input('Enter a number of blueberry bushes: ')))]
# print(list)