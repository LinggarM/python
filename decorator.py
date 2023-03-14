def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Running function {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def add_numbers(x, y):
    return x + y

print(add_numbers(2,3))