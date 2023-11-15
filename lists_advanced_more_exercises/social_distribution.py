population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
is_possible = True
for i in range (0, len(population)):
    person = int(population[i])
    max_value = max(population)
    index_max_value = population.index(max_value)
    if person < minimum_wealth:
        difference = minimum_wealth - person
        if population[index_max_value] - difference >= minimum_wealth:
            population[i] += difference
            population[index_max_value] -= difference
        else:
            is_possible = False
            print("No equal distribution possible")
            break


if is_possible == True:
    print(population)


