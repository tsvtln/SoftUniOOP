def solution():
    def integers():
        starting = 1
        while True:
            yield starting
            starting += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for num in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


# test code
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
