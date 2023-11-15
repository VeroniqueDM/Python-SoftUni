def resolver(bool_values, results):
    for ind in range(len(bool_values)):
        if bool_values[ind] == 't':
            if ind == len(bool_values) - 1:
                result = results[0]
                return result
            else:
                resolver(bool_values[ind + 1:], results[:len(results) - 1 - ind])
        elif bool_values[ind] == 'f':
            if ind == 0:
                return results[-1]
            if ind == len(bool_values) - 1:
                result = results[-1]
                return result
            else:
                resolver(bool_values[ind + 1:], results[:len(results) - 1 - ind])


expression = input()
bool_values = [x.strip() for x in expression.split('?')]
results = [y.strip() for y in bool_values.pop().split(':')]

print(resolver(bool_values, results))
