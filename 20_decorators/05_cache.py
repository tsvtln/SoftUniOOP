def cache(function):
    def wrapper(n):
        if not hasattr(fibonacci, 'log'):
            fibonacci.log = {}

        if n not in fibonacci.log:
            fibonacci.log[n] = function(n)
        return fibonacci.log[n]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
