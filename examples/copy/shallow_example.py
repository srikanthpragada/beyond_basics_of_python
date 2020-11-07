import copy

l1 = [1,2,3]
l2 = l1

first = [[1, 2, 3], [10, 20, 30]]
# Make another reference
second = first

print(id(first), id(second))

second.append([100, 200])
second[0].append(4)

# Shallow copy
third = copy.copy(first)
print(id(third))

third[0].append(5)
third.append([1000, 2000])

print(first)
print(third)
