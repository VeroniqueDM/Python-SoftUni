class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.number:
            res = self.i
            self.i += 1
            if self.i == len(self.sequence):
                self.i = 0
            self.counter +=1
            return self.sequence[res]
        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

