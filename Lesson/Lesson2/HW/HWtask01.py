# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# n = int(input())
# eagle_count = tails_count = 0
# for n in range(n):
#     x = int(input())
#     if x:
#         eagle_count += 1
#     else:
#         tails_count += 1
#
# if eagle_count < tails_count:
#     print(eagle_count)
# elif eagle_count == tails_count:
#     print(eagle_count)
# else:
#     print(tails_count)
#############################
# option 2

n = int(input())
count = 0
for i in range(n):
    eagle_coin = int(input())
    if eagle_coin:
        count += 1
if count > n //2:
    count = n - count
print(count)