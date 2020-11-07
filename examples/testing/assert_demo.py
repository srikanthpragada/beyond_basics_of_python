
def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


assert iseven(10), 'Should return True but returns False'
assert iseven(11) == False, 'Should return False but returns True'

