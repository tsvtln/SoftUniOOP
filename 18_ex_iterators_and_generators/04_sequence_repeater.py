class sequence_repeat:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            idx = self.index % len(self.seq)
            self.index += 1
            return self.seq[idx]
        raise StopIteration


# TEST CODE
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')