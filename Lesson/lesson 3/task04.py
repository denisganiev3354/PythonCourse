# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)

lst = list(map(int, input().split()))
print(sum(lst[i] > lst[i - 1] for i in range(1, len(lst))))


n = list(map(int, input().split()))
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i+1]:
        count += 1
print(count)


list = [0, -1, 5, 2, 3]
count = 0
for i in range (len(list)):
    if list[i] > list[i - 1]:
        count += 1
print(count)