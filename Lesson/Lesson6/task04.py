# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110



# def sum1(num):
#     n = int(num ** 0.5)
#     m = 1 + (0 if n **2 != num else n)
#    return sum([i + num // i for i in range(2, n) if num % i == 0]) + m
#
# k = int(input())
#
# for i in range(10, k):
#     s1 = sum1(i)
#     s2 = sum1(s1)
#     if s2 == i and s1 < s2:
#         print(i, s1)


def sum1(num):
    n = int(num ** 0.5)
    m = 1 + (0 if n ** 2 != num else n)
    return sum([i + num // i for i in range(2, n) if num % i == 0]) + m
    # return sum([i for i in range(2, num // 2) if num % i == 0])

k = int(input())

for i in range(10, k):
    s1 = sum1(i)
    s2 = sum1(s1)
    if s2 == i and s1 < s2:
        print(i, s1)