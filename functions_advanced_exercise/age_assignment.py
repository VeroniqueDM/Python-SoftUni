def age_assignment(*args, **kwargs):

    return {x: kwargs[x[0]] for x in args}
    # result = {}
    # for name in args:
    #     first_letter = name[0]
    #     age = kwargs[first_letter]
    #     result[name] = age
    #
    # return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	
