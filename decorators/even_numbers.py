def even_numbers(function):

    def wrapper(numbers):
        res = function(numbers)
        new_res = []
        for num in res:
            if num % 2 == 0 :
                new_res.append(num)
        return new_res

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
