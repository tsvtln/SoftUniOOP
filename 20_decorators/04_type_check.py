from functools import wraps


def type_check(type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            rez = function(*args, **kwargs)
            if all(isinstance(arg, type) for arg in args):
                return rez
            return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
