# def make_bold(function):
#     def wrapper(*args, **kwargs):
#         values = function(*args, **kwargs)
#         return f"<b>{values}</b>"
#
#     return wrapper
#
#
# def make_italic(function):
#     def wrapper(*args, **kwargs):
#         values = function(*args, **kwargs)
#         return f"<i>{values}</i>"
#
#     return wrapper
#
#
# def make_underline(function):
#     def wrapper(*args, **kwargs):
#         values = function(*args, **kwargs)
#         return f"<u>{values}</u>"
#
#     return wrapper
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))


def make_format(format_symbol):
    def decorator(function):
        def wrapper(*args, **kwargs):
            values = function(*args, **kwargs)
            return f"<{format_symbol}>{values}</{format_symbol}>"
        return wrapper
    return decorator


make_bold = make_format('b')
make_italic = make_format('i')
make_underline = make_format('u')


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
