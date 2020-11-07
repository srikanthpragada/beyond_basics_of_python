from collections import ChainMap

d1 = {1: 10, 2: 20, 3: 30}
d2 = {4: 100, 5: 200, 1 : 100}
cm = ChainMap(d1, d2)

print(cm[1])
cm[4] = 999  # Changes are made to first dict
print(cm.maps)
print(d2)
d2[5] = 1000
for t in cm.items():
    print(t)
