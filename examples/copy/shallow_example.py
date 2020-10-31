import copy

first = [[1, 2, 3], [10, 20, 30]]
second = first
second.append([100, 200])
second[0].append(4)

third = copy.copy(first)
third[0].append(5)
third.append([1000, 2000])

print(first)
print(third)
