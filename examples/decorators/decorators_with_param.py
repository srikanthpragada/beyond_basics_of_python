import time


# Decorator with param
def delay(seconds=10):
    def delay_outer_function(func):
        def delay_inner_function(*args, **kwargs):
            print(f"Waiting for {seconds} seconds!")
            time.sleep(seconds)
            func(*args, **kwargs)

        return delay_inner_function

    return delay_outer_function


@delay(seconds=5)
def printing():
    for n in range(1, 10):
        print(n, end=' ')


@delay()
def printing_reverse():
    for n in range(9, 0, -1):
        print(n, end=' ')


printing()
print("\nReverse")
printing_reverse()
