def cache(func):
    log= {}
    def wrapper(num):
        if num in log:
            return log[num]
        log[num]=func(num)
        return func(num)
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)




fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
