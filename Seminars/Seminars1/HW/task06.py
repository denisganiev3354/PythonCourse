# ДЗ
# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# мой вариант   

# a = int(input())
# if (99999 < a < 1000000):
#     b = a // 1000
#     b1 = b // 100
#     b2 = b // 10 % 10
#     b3 = b % 10
#     b4 = b1 + b2 + b3
#     c = int(a % 1000)
#     c1 = c // 100
#     c2 = c // 10 % 10
#     c3 = c % 10
#     c4 = c1 + c2 + c3
#     if b4 == c4:
#         print('yes')
#     else:
#         print('no')
# else:
#     print("Invalid result")

# вариант преподавателя с моими корректировками

ticket_number = int(input())
if 100000 < ticket_number < 999999:
    sum_first = 0
    sum_last = 0

    while ticket_number:
        digit = ticket_number % 10
        if ticket_number > 999:
            sum_last += digit
        else:
            sum_first += digit
        ticket_number //= 10
    print(f"The ticket is lucky: {sum_first == sum_last}")
else:
    print("No such ticket exists") 
