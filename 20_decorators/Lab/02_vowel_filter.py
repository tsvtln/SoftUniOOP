def vowel_filter(function):
    def wrapper():

        letters = function()
        tr = []
        for letter in letters:
            if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
                tr.append(letter)
        return tr

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


