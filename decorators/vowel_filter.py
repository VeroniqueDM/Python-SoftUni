def vowel_filter(function):

    def wrapper():
        res = function()
        vowels = "AOUYIEaouyie"
        new_res = []
        for let in res:
            if let in vowels:
                new_res.append(let)
        return new_res
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
