def operation(func, a, b):
    return func(a, b)


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


print(operation(add, 10, 20))
print(operation(mul, 10, 20))
