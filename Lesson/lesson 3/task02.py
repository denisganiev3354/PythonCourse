# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# вариант 1
# k = 3
# list_nums = [1, 2, 3, 4, 5]
# for i in range(k):
#
#     list_nums.insert(0, list_nums.pop())
# print(list_nums)

# вариант 2
lst = list(map(int, input().split()))
k = int(input()) % len(lst) + 1
lst = [lst[i - k] for i in range(len(lst))]
print(lst)