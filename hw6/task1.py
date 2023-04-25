# Задача 30
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии:
# a(n) = a(1) + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# 7 первый элемент
# 2 разность между элементами
# 5 количество элементов

def list_create_arithmetic(num_first, num_diff, num_len):
    return [value := num_first + i * num_diff for i in range(num_len)]

num_first = int(input('Enter a 1st-number: '))
num_diff = int(input('Enter a dif-number: '))
num_len = int(input('Enter a length-number: '))
print(*list_create_arithmetic(num_first, num_diff, num_len))