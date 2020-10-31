from typing import Dict, List, Tuple


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


nums: List[Time] = []  # Uses user-defined type
nums.append(Time(10, 20, 30))
nums.append(10)
