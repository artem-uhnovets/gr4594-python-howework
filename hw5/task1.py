# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def num_degree(number, degree):
    result = number
    while degree > 0:
        # result = result * num_degree(number, degree - 1)
        return result * num_degree(number, degree - 1)
    return 1

number = int(input('Enter a number: '))
degree = int(input('Enter a degree: '))
print(num_degree(number, degree))
