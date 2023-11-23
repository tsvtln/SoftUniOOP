class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.values[self.index]
            rez = (key, value)
            self.index += 1
            return rez
        raise StopIteration


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)