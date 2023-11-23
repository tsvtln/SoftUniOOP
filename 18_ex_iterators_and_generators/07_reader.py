def read_next(*args):
    for col in args:
        for el in col:
            yield el
            