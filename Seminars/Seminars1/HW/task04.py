# ДЗ
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
S = int(input())

if(S % 6):
    print("Invalid result")

else: 
    petya = S // 6
    sergey = petya
    katya = S // 6 * 2
    print('petya =' , int(petya), 'sergey =', int(sergey), 'katya =', int(katya))
   

