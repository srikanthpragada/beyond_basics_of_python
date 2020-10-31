

def log(func):
    def decorator_function():
       print('Calling', func.__name__)  # Pre-process
       func()
       print('Completed', func.__name__) # Post-process

    return decorator_function

@log
def hello():
    print('Hello Python')


hello()  # Call function that is decorated