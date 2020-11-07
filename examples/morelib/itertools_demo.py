from itertools import accumulate, product, takewhile,dropwhile

values = [1, 2, 3, 4]

print(list(accumulate(values, lambda a, b: a * b)))

print(list(product(['a', 'b'], [1, 2, 3])))

print(list(takewhile(lambda v: v > 10, [30, 50, 4, 5, 6])))
print(list(dropwhile(lambda v: v > 10, [30, 50, 4, 5, 6])))
