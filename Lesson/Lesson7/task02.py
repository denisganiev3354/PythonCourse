# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.


def find_farthest_orbit(nums_list):
    max_sq = [(i[0] * i[1], i) for i in nums_list if i[0] != i[1]]
    return max(max_sq)[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))