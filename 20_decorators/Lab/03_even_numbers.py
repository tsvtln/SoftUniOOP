from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(numbers):

        lst = []
        for number in numbers:
            if number % 2 == 0:
                lst.append(number)
        return lst

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
