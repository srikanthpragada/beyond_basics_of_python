

def log(func):
    def decorator_function():
       print('Calling', func.__name__)
       func()
       print('Completed', func.__name__)

    return decorator_function


def hello():
    print('Hello Python')

def wish():
    print("Wishing well!")

dec_func = log(hello)
dec_func()

dec_func = log(wish)
dec_func()
