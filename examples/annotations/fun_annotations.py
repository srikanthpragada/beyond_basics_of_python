def add(n1: int, n2: int) -> int:
    print(n1 + n2)


print(add(10, 20))
print(add('abc', 'xyz'))

print(add.__annotations__)
# a  = 10
# reveal_type(a)   # used by mypy and shows the type it understood
