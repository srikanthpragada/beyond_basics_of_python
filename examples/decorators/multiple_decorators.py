import time


def log(func):
    def decorator_function():
        print('Calling', func.__name__)
        func()
        print('Completed', func.__name__)

    return decorator_function


def delay(func):
    seconds = 10

    def delay_function(*args, **kwargs):
        print(f"Waiting for {seconds} seconds!")
        time.sleep(seconds)
        func(*args, **kwargs)

    return delay_function


@delay
@log
def printing():
    print("Hello!")


printing()
