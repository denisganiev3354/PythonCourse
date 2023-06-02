# СПИСКИ


# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
#
# print(list_1)#  вывод списка в квадратных скобках
# print(*list_1)#  вывод списка без квадратных скобок
# ########################
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
#
# for i in list_1:
#     print(i) # поочередно выводит значения из списка
# #########################
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
#
# print(len(list_1)) # выводит колличество элементов с списке
# # ##########################
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(list_1[2]) # обращение к элементу от начала
##############################
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(list_1[-1]) # обращение к элементу с конца
# ##################################
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавляет элемент в конец списка
# print(list_1)
# ##############################################
# list_1 = []
# for i in range(5):
#     list_1.append(i) # при каждой итерации цикла будет добавляться значение i (от 0 до 4)
#     print(list_1) # для отслеживания итераций
#################################################
# Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1)# [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

#################################################
# Удаление конкретного элемента из списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]
###################################################
# # Добавление элемента на нужную позицию.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]
###################################################
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('1:',list_1[0])                # 1
# print('2:',list_1[1])                # 2
# print('3:',list_1[len(list_1)-1])    #10  # or print('3',list_1[-1])
# print('4:',list_1[-5])               #6
# print('5:',list_1[:])                #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('6:',list_1[:2])               #[1, 2]
# print('7:',list_1[len(list_1)-2:])   #[9, 10]
# print('8:',list_1[2:9])              #[3, 4, 5, 6, 7, 8, 9]
# print('9:',list_1[6:-18])            #[]
# print('10:',list_1[0:len(list_1):6])  #[1, 7]
# print('11:',list_1[::6])              #[1, 7]

###############################################################
# КОРТЕЖИ


# t = ()
#
# print(type(t))      # покажет тип данных
#
# t = (1)             # в таком виде покажет тип  данных int
# t = (1, )           # чтобы показал tuplе нужно поставить " , "
# print(type(t))

# v = [1, 8, 9]           # список
# print(v)                # вывод списка
# print(type(v))          # вывод типа данных
#
# v = tuple (v)           # преобразование списка в кортеж(tuple)
# print(v)                # вывод кортежа
# print(type(v))          # вывод типа данных
#
# # a = 1     or     a,b = 1,2
# # b = 2
#
# # a = 1     or      a = b = 1
# # b = 1
#
#
# a,b,c = v               # разделение кортежа на отдельные переменные
# print(a,b,c)            # вывод отдельных чисел 1, 8, 9.

###############################################################
# Кортежи

# t = (1, 2, 3, 5,)
#
# print(t[1])                # вывод значения с определённым индексом
#
#
# for i in (t):              # поочерёдный вывод значений
#     print(i)
#
# # or
#
# for i in range(len(t)):    # вывод значений по индексу через  цикл
#     print(t[i])

########################################################

# t = (1, 2, 3, 5,)
# print(t)
# t = list(t)                 # преобразование кортежа в список
# t[0] = 2                    # изменяем элемент.кортеж не изменяем для того чтобы изменить значение нужно кортеж преобразовать в список.
# print(t)                    # вывод списка
#

#############################################################
# СЛОВАРИ


# d = {}                      # пустой словарь
# d = dict()                  # пустой словарь
#
# d['q'] = 'qwerty'
# print(d)
#
# d['w'] = 'werty'
# print(d)
# print(d['q'])


#######################################################################

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)                                               #{'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])                                       # ←
# # типы ключей могут отличаться
# dictionary['left'] = '⟸'
# print(dictionary['left'])                                       # ⟸
# print(dictionary['type'])                                       # KeyError: 'type'
# del dictionary['left']                                          # удаление элемента
# for item in dictionary:                                         # вывод словаря в виде ключ и значение
#     print('{}: {}'.format(item, dictionary[item]))              # up: ↑
                                                                  # left: ←
                                                                  # down: ↓
                                                                  # right: →
# print(dictionary.items())                                       # выводиться список, где каждый элемент будет являтся
                                                                  # кортежом из двух значений, ключ и значение из словаря.

# for (k,v) in dictionary.items():                                # цикл который проходит по k и v, где "к" это ключ, a "v" это значение.
#     print(k,v)
                                                                  # up ↑
                                                                  # left ←
                                                                  # down ↓
                                                                  # right →


# dictionary[895] = 98989                                          # добавляем ключ 895 со значением 98989
# print(dictionary)                                                # вывод словаря с добавлением нового значения.

##############################################################
# МНОЖЕСТВА


# colors = {'red', 'green', 'blue'}
# print(colors)                   # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)                   # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)                   # {'red', 'gray', 'green', 'blue'}
# colors.remove('red')
# print(colors)                   # {'gray', 'green', 'blue'}
# colors.remove('red')            # KeyError: 'red'
# colors.discard('red')           # ok
# print(colors)                   # {'gray', 'green', 'blue'}
# colors.clear()                  # { }
# print(colors)                   # set()
#
# q = set()                       # создание пустого множества

#########################################################################
# Операции со множествами в Python
#
# a = {1, 2, 3, 5, 8}
# print('a:', a)
# b = {2, 5, 8, 13, 21}
# print('b:', b)
# c = a.copy()                                    # c = {1, 2, 3, 5, 8}   копия множества "а"
# print('c:', c)
# u = a.union(b)                                  # u = {1, 2, 3, 8, 13, 21}   объеденение множеств "а" и "b" содержит уникальные значения из двух множеств
# print('u:', u)
# i = a.intersection(b)                           # i = {8, 2, 5}     пересечение множеств(только повторяющиеся значения)
# print('i:', i)
# dl = a.difference(b)                            # dl = {1, 3}   разность двух множеств. вычетаем из множества "а" повторяющиеся значения со множеством "b"
# print('dl:', dl)
# dr = b.difference(a)                            # dr = {13, 21}     разность двух множеств. вычетаем из множества "b" повторяющиеся значения со множеством "а"
# print('dr:', dr)
# q = a.union(b).difference(a.intersection(b))    # {1, 21, 3, 13}    сначала находиться пересечение "а" и "b"(получается первое множество),
# print('q:', q)                                  # после этого "а" объеденяем с "b"(получается второе множество) затем находим разность между первым и вторым множеством.

###############################################################
# Замороженное множество
#
# a = {1, 8, 6}
# b = frozenset(a)
#
# print(b)



# Коллекции данных
# _________________________________________________________________________________________
# |    тип     | изменяемость  | индексированность  | уникальность  | как создаём          |
# | коллекции  |               |                    |               |                      |
# |------------|---------------|--------------------|---------------|----------------------|
# |   список   |      +        |          +         |       -       | [], list()           |
# -------------|---------------|--------------------|---------------|----------------------|
# |   кортеж   |      -        |          +         |       -       | (), tuple()          |
# -------------|---------------|--------------------|---------------|----------------------|
# |   строка   |      -        |          +         |       -       | '', ""               |
# -------------|---------------|--------------------|---------------|----------------------|
# |  множество |      +        |          -         |       +       | {elem1, elem2}, set()|
# -------------|---------------|--------------------|---------------|----------------------|
# | неизменное |               |                    |               |  frozenset()         |
# | множество  |      -        |          -         |       +       |                      |
# -------------|---------------|--------------------|---------------|----------------------|
# |            |   + элементы  |                    |    +элементы  |   {}                 |
# |  словарь   |   - ключи     |          -         |    +ключи     |  {key:value,}        |
# |            |   + значения  |                    |    -значения  |   dict()             |
# |____________|_______________|____________________|_______________|______________________|
