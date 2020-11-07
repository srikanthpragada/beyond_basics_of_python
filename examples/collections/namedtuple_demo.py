from collections import namedtuple

Time = namedtuple('Time', 'hours, minutes, seconds', defaults=[0, 0, 0])

t1 = Time(10, 20, 30)
print(t1, type(t1))
print(t1.hours)
# t1.hours = 10

t2 = Time(minutes=10, seconds=30)
print(t2)
t = (1, 2, 3)
t3 = Time(*t)
print(t3)
