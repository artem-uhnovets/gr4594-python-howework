# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4
def summ_digits(num_1, num_2):
    if num_2 == 0:
        return num_1
    return summ_digits(num_1 + 1, num_2 - 1)


num_1 = int(input('Enter a number 1. '))
num_2 = int(input('Enter a number 2. '))
print(summ_digits(num_1, num_2))