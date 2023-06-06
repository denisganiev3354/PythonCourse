# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.
import copy
# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

# from random import randint
#
# n1 = int(input())
# n2 = int(input())
# list_1 = list()
# list_2 = list()
# for i in range(n1):
#     list_1.append(randint(1, 10))
# print(list_2)
#
# for i in range(n2):
#     list_2.append(randint(1, 10))
# print(list_1)
#
# for i in list_1:
#     if i not in list_2:
#         copy.append(i)
mas1, mas2 = list(map(int, input().split())), list(map(int, input().split()))
print([i for i in mas1 if i not in mas2])