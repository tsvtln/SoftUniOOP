def multiply(times):

    def decorator(function):

        def wrapper(*args, **kwargs):
            value = function(*args, **kwargs)
            result = value * times
            return result

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))