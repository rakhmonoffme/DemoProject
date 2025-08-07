def my_decorator(func):
    def wrapper():
        print("Hello from the decorator!")
        func()  # Call the original function
        print("Goodbye from the decorator!")
    return wrapper

@my_decorator
def my_function():
    print("This is the original function.")

my_function()