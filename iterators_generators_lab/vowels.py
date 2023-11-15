class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0
        self.end = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        vowels = "AEIOUYaeiouy"
        while self.i < self.end:
            res = self.string[self.i]
            self.i += 1
            if res in vowels:
                return res
        else:
            raise StopIteration()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
