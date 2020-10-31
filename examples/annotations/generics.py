from typing import Dict, List, Tuple

nums: List[int] = [1, 3, 3]
nums.append('abc')

t: Tuple[int, float, int] = (1, 20.2, 3)

d: Dict[str, int] = {}
d['k1'] = 20
d['k2'] = 'Xyz'

print(t)
print(type(t))
print(nums)
print(type(nums))
print(d)
print(type(d))
