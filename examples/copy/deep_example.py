import copy

first = [[1, 2, 3], [10, 20, 30]]

second = copy.deepcopy(first)
second[0].append(5)
second.append([1000, 2000])

print(first)
print(second)
