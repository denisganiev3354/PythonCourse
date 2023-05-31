# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
###########################################
# мой вариант

import random

num = int(input())
result = 0
list_nums = []
x = int(input())
for i in range(num):
    list_nums.append(random.randint(1, 5))
    if list_nums[i] == x:
        result += 1
print(list_nums)
print(result)

#######################################
# варианты преподавателя
# вариант 1

# list_nums = [int(input()) for _ in range(int(input()))]
# print(list_nums.count(int(input())))

# вариант 2

# from random import choices
#
# num = int(input())
# list_nums = choices(range(num * 2), k=num)
# print(list_nums)
#
# result = list_nums.count(int(input()))
# print(result)