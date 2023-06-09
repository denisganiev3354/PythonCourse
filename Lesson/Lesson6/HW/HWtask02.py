# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
# 5 - 15
min_num = 5
max_num = 15
print(list_1 := [randint(0, 20) for i in range((int(input())))])

for index, i in enumerate(list_1):
    if min_num <= i <= max_num:
        print(index)
