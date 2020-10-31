import math

print(math.lcm(10, 15))
print(math.gcd(30, 21, 15))

# Do not support lists
# print(math.lcm([10,15,20]))
print(math.lcm(*[10, 15, 20]))  # Unpack list
