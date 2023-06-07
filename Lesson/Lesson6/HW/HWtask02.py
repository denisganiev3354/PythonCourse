# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
# 5 - 15
print(list_1 := [randint(0, 20) for i in range((int(input())))])

for index, i in enumerate(list_1):
    if 5 < i < 15:
        print(index)
