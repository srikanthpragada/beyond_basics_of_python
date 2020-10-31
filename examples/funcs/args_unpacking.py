def outer_function(func, *args, **kwargs):
    # call passed function with given parameters
    print("Args   : ", args)
    print("Kwargs : ", kwargs)
    func(*args, **kwargs)  # Arguments unpacking


def fun1():
    print("Function 1")


outer_function(fun1)


def fun2(name):
    print("Function 2 using", name)


def fun3(*, x, y):
    print(x, y)


outer_function(fun1)
outer_function(fun2, "Guido")
outer_function(fun3, x=10, y=20)

outer_function(fun1, 10)
