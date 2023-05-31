# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint

A = [randint(1, 21) for i in range(int(input()))]
print(A)

x = int(input())
next_num = A[0]
for i in A:
    if abs(x - i) < abs(x - next_num):
        next_num = i

print(next_num)