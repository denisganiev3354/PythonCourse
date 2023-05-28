# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())

degree_digit = 1

while degree_digit <= n:
    print(degree_digit, end=" ")
    degree_digit *= 2
