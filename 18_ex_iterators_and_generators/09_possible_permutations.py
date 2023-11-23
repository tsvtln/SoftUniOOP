import itertools


def possible_permutations(ls):
    for perm in itertools.permutations(ls):
        yield list(perm)
