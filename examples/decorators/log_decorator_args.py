def log(func):
    def decorator_function(*args, **kwargs):
        print('Calling ', func.__name__)
        print('Arguments :', args, kwargs)
        rv = func(*args, **kwargs)  # Invoke target function
        print('Completed and returned ', func.__name__, rv)
        return rv

    return decorator_function


@log
def hello(name):
    print('Hello', name)


@log
def add(n1, n2):
    return n1 + n2


hello('Decorators')  # Call function that is decorated
print(add(10, 20))
print(add(n1=20, n2=50))
