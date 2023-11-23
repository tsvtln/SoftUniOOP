def number_increment(numbers):

    def increase():
        tr = []

        for number in numbers:
            tr.append(number + 1)
        return tr

    return increase()

print(number_increment([1, 2, 3]))
