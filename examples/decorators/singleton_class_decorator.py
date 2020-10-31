import functools


def singleton(cls):
    def singleton_function(*args, **kwargs):
        print('Decorator on ' + cls.__name__ + ' called!')
        if not singleton_function.instance:
            # No instance crated so far, so create an instance
            singleton_function.instance = cls(*args, **kwargs)
        return singleton_function.instance

    singleton_function.instance = None  # Initially no instance is created
    return singleton_function


@singleton
class Test:
    def __init__(self, value):
        self.value = value


obj1 = Test(10)
print(id(obj1))
obj2 = Test(20)
print(id(obj2))
