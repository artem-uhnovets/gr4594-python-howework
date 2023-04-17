# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 5, 6 -> 2, 3

# s = a + b
# p = a * b

# a = s - b
# a = p / b
# s = p / b + b
# b = s - (p / b)
# p / b + b - s = 0
# p + b*b - s*b = 0
# b * b - s * b + p = 0
# D = b^2 - 4*a*c
# d = s * s - 4 * 1 * p
# b_1 = (s + d ** 0.5) / 2
# b_2 = (s - d ** 0.5) / 2
# a_1 = s - b_1
# a_2 = s - b_2

s = int(input('Enter S number: '))
p = int(input('Enter P number: '))
d = s * s - 4 * 1 * p
b_1 = (s + d ** 0.5) / 2
b_2 = (s - d ** 0.5) / 2
a_1 = s - b_1
a_2 = s - b_2
if a_1 + b_1 == s and a_1 * b_1 == p:
    print(f'{s}, {p} -> {a_1}, {b_1}')
elif a_2 + b_2 == s and a_2 * b_2 == p:
    print(f'{s}, {p} -> {a_2}, {b_2}')
else:
    print('s and p are incompatible')

""" 
еще примеры решения
print ('Введите сумму чисел S: ')
s = int(input())
print ('Введите произведение чисел P: ')
p = int(input()) 
for x in range (s):
    for y in range (p):
        if s == x + y  and p == x*y:
            print (x, y)
        # else:
        #     print ('Введены не верные S и P')

summa = int(input(f"Введите сумму чисел S = "))
mult = int(input(f"Введите произведение чисел P = "))
flag_break = False


for x in range(summa):
    if(flag_break == False):
        for y in range(summa):
            if (x + y == summa) and (x * y == mult):
                print("загаданные числа:")
                print(x, y)
                flag_break = True
                break
            elif (x == summa -1) and (y == summa -1):
                print("нет соответствующих чисел")

                
S = int(input("Input a sum of numbers: "))
P = int(input("Input a multiple of numbers: "))
x = 1
while S - x != P/x:
    x += 1
print(f"First num is {x}, second num is {S - x}")
"""