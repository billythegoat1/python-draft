

def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator
def greet():
    print("Hello World!")

greet()