# def f(x):
#     return x*x
# a = f
# print(type(f))
#######################################
# def f(x):
#     return x*x
# a = f
# print(a(5))
# print(f(5))
##################################################
# def calk1(a):
#     return a + a
#
# def calk2(a):
#     return a * a
#
# def math(op, x):
#     print(op(x))
#
# math(calk2, 5)
########################################################
# def calk1(a, b):
#     return a + b
#
# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk1, 5, 45)

#########################################################
# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# # calk1 = lambda a,b: a + b
#
# math(lambda a,b: a + b, 5, 45)
############################################################
# мой вариант

# from random import randint
#
#
# num = int(input())
# list1 = []
# for i in range(num):
#     list1.append(randint(0, 100))
# print(*list1)
# for i in list1:
#     if i % 2 == 0:
#         n = i *i
#         print('(', i,',',  n, ')')

# Вариант лектора
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# def select(f, col):
#     return [f(x)for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
#
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 ==0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)
#################################################################

list1 = [x for x in range(1, 20)]
print(list1)