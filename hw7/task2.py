# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y) 

# Вывод:
# 1 2  3  4  5  6
# 2 4  6  8  10 12
# 3 6  9  12 15 18
# 4 8  12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

    # for i in range(1, num_rows + 1):
    #     my_list = [i * j for j in range(1, num_columns + 1)]
    #     print(my_list)

    # for i in range(1, num_rows + 1):
    #     my_list = list(map(lambda value: value * i, range(1, num_columns + 1)))
    #     print(my_list)
    
    # my_list = [list(map(lambda value: value * i, range(1, num_columns + 1))) for i in range(1, num_rows +1)]
    # for i in my_list:
    #     print(i)

    # my_list = list(map(operation, list(map(lambda value: value, range(1, num_rows + 1))), list(map(lambda value: value, range(1, num_columns + 1)))))
    # print(my_list)

def print_operation_table(operation, num_rows, num_columns):
    for i in range(num_rows):
        for j in range(num_columns):
            print(((operation)(i + 1, j + 1)), end=" ")
        print("\n")

print_operation_table(lambda x, y: x * y, 6, 6)

# num_rows = 6
# num_cols = 6
# for i in range(num_rows):
#     print(list(map(lambda a: (a + 1) * (i + 1), range(num_cols))))
# print(*[f'{list(map(lambda a: (a + 1) * (i + 1), range(num_cols)))}\n' for i in range(num_rows)])
# print(list(map(lambda x, y: (x + 1) * (y + 1), range(num_cols), range(num_rows)))) 

# for i in range(num_rows):
#     print(' '.join(list(map(lambda a: str((a + 1) * (i + 1)), range(num_cols)))))

# print((lambda x, y: x * y)(list(map(lambda a: (a + 1), range(num_cols))), 2), end=' ')