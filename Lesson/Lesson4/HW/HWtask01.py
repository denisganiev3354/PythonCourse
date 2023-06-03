# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

# n = int(input())
# list_num1 = []

# for i in range(n):
#     list_num1.append(randint(1, 10))
# print(list_num1)

# print(list_num1[int(input())], list_num1.append(randint(1, 10)))

# m = int(input())
# list_num2 = []
#
# for i in range(m):
#     list_num2.append(randint(1, 10))
# print(list_num2)
#
# # print(list_num1[int(input())], list_num1.append(randint(1, 10)))

print(list_1 := [randint(1, 10) for i in range((int(input())))])
print(list_2 := [randint(1, 10) for i in range((int(input())))])
l_n1 = set(list_1)
u = l_n1.union(list_2)
print(*u)