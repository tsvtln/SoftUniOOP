def get_primes(numbers: list):
    for i in numbers:
        if i < 2:
            continue
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            yield i

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
