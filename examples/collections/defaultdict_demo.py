from collections import defaultdict

marks = defaultdict(list)

marks['Steve'].append(80)
marks['Bill'].append(70)
marks['Steve'].append(87)

for name,ml in marks.items():
    print(name, ml)

counts = defaultdict(lambda : 1)
counts["a"] += 2
print(counts['b'])
print(counts)



