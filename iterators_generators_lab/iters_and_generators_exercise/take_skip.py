class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0
        self.end = self.step * (self.count - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            res = self.i
            self.i += self.step
            return res
        else:
            raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)


