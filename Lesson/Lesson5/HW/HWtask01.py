# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def ExponentiationRec(num1, num2):
    if num2 == 1:
        return num1
    elif num2 == 0:
        return 1
    elif num2 != 1:
        return (num1 * ExponentiationRec(num1, num2 - 1))


print(ExponentiationRec(int(input()), int(input())))

