""" Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

# 1ый способ
a = input('Enter 3-digit number - ')
print('{} {} {} {}'.format(a, '->', (int(a[0])+int(a[1])+int(a[2])), f'({a[0]} + {a[1]} + {a[2]})'))

# 2ой способ
a = int(input('Enter 3-digit number - '))
result = 0
print(a, sep='', end='')
while a > 0:
    result += a % 10
    a //= 10
print('{} {}'.format(' ->', result))