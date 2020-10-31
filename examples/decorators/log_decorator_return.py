import functools


def log(func):
    @functools.wraps(func)   # Preserve original function info
    def decorator_function(*args, **kwargs):
        print('Calling ', func.__name__)
        print('Arguments :', *args, **kwargs)
        rv = func(*args, **kwargs)
        print('Completed', func.__name__)
        return rv

    return decorator_function


@log
def hello(name):
    return "Hello " + name


print(hello('Decorators'))  # Call function that is decorated
print(hello.__name__)
