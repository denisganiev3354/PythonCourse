# print ('Введите первую строку: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print (a, '+' , b , '= ', a + b)
#########################################
# a = 5.897
# b = 6.786
# print (round(a*b,3))
##########################################
# iter = 2
# iter += 3 #iter = iter + 3
# iter -= 4 #iter = iter - 4
# iter *= 2 #iter = iter * 2
# iter /= 2 #iter = iter / 2
# iter //= 2 #iter = iter // 2
# iter %= 2 #iter = iter % 2
# iter **= 2 #iter = iter ** 2
##########################################
# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a='qwe'
# b= 'qwe'
# print(a==b)
# a=1<3<5<10
# print(a)
##########################################
# username =input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас Марина')
# elif username == 'Ильнар':
#     print ('Ильнар - топ :)')
# else:
#     print('Привет,', username)
####################################
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa += x
#     n //= 10
# print(summa) #9
############################
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i += 1
# else:
#     print('Пожалуй')
#     print('хватит ')
# print(i)
###################################
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введённое число, деленное на 2
#         print(n)
#         flag = False
#     i += 1
#############################################
# a = 'qwerty'

# for i in a:
#     print(i)
###############################################

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
#####################################

text = 'Съешь ещё этих Мягких Францусских булок'
print(len(text))
print('еще' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё','ЕЩЁ'))