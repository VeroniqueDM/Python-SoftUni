
class reverse_iter:
    def __init__(self, element):
        self.element = element


    def __iter__(self):
        return self

    def __next__(self):
        if len(self.element)>0:
            return self.element.pop()
        else:
            raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

