def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        func()  
    return wrapper


def apply_decorator(func):
    return decorator_func(func)

def say_hello():
    print("hello")

say_hello()
