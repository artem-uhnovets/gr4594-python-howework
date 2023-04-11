# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 0 1 1
# 2

number = int(input('How many coins? '))
count_0 = 0
count_1 = 0
for i in range(number):
    coin = int(input(f'{i + 1}. Enter 1 or 0 - '))
    if coin == 0:
        count_0 += 1
    else:
        count_1 += 1
countMin = count_1 if count_1 < count_0 else count_0
print('{} min coins need to flip'.format(countMin))