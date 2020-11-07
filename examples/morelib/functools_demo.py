# functools.reduce(function, iterable[, initializer])
from functools import reduce
from operator import mul


def multiply(x, y):
    print(x,y)
    return x * y


values = [1, 5, 8, 10]

print(reduce(multiply, values))
print(reduce(multiply, values, 1))
print(reduce(lambda x,y : x * y, values))
print(reduce(mul, values))
