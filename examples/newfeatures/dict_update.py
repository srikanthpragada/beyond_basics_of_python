from collections import defaultdict

d1 = {'k1': 10, 'k2': 20}
d2 = {'k2': 200, 'k3': 300}
d3 = defaultdict(lambda: 0)
d3['k1'] = 100
d3['k3'] = 3

print({**d1, **d3})  # Creates a normal dict
print(d1 | d2)
print(d1 | d3)       # Returns defaultdict
d1 |= d2
print(d1)

d2 |= [('k4', 40)]  # Any dict like object will do
print(d2)
