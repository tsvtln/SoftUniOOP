class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter_step = 0
        self.counter_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter_count < self.count:
            current_value = self.counter_step
            self.counter_step += self.step
            self.counter_count += 1
            return current_value
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
