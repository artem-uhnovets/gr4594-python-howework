# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# диапазон задается пользователем
# Вывод: [1, 9, 13, 14, 19]

def list_create_random(begin_num, end_num, length):
    import random
    return [random.randint(begin_num, end_num) for _ in range(length)]

def find_ind_rng_list(rng_start, rng_end, source_list):
    print(f'Range from {rng_start} to {rng_end}')
    list = []
    for i in range(len(source_list)):
        if source_list[i] in range(rng_start, rng_end + 1):
            list.append(i)
    return list

my_list = list_create_random(-10, 10, list_len := int(input('Enter a length for list: ')))
print(my_list)
print(*find_ind_rng_list(2, 5, my_list))
