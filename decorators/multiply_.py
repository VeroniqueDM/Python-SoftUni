def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            new_res = res * times
            return new_res
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
