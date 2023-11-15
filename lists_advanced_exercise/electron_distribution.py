electrons = int(input())
list_shells = []

def electron_distribution(electrons_list, electrons_amount):
    index = 1

    while electrons_amount > 0:
        volume = 2 * (index ** 2)
        if electrons_amount >= volume:
            electrons_amount -= volume
            electrons_list.append(volume)
            index += 1
        else:
            electrons_amount -= volume
            final = volume + electrons_amount
            electrons_list.append(final)


    return electrons_list

res = electron_distribution(list_shells,electrons)

print(res)


