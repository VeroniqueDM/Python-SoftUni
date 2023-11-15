class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.i = 0
        self.end = len(self.dict_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.end:
            current = list(self.dict_obj.items())[self.i]
            self.i +=1
            return current
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
