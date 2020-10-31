def add(v1, v2):
    if isinstance(v1, int):
        return v1 + v2
    else:
        raise ValueError('Only integers are allowed!')


print(add(10, 20))
print(add('abc', 'xyz'))
print(add([1, 2, 3], [6, 7, 8]))
print(add('abc', 10))
