'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Пример:
m n k
3 2 4 -> yes
3 2 1 -> no
'''

# * * * *
# * * * *
# * * * *
# * * * *
# * * * *

m = int(input('Enter rows of chocolate - '))
n = int(input('Enter columns of chocolate - '))
k = int(input('How many pieces you want? - '))
if (k < m * n) and (k >= m or k >= n) and (k % m == 0 or k % n == 0):
    print('yes')
else:
    print('no')
# print('yes' if (k < m * n) and (k >= m or k >= n) and (k % m == 0 or k % n == 0) else 'no')