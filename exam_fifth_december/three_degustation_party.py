guests_results = {}

command = input().split("-")
disliked_meals = 0
while command[0] != "Stop":
    attitude = command[0]
    guest = command[1]
    meal = command[2]
    if attitude == "Like":
        if guest not in guests_results:
            guests_results[guest] = [meal]
        else:
            if meal not in guests_results[guest]:
                guests_results[guest].append(meal)
    elif attitude == "Dislike":
        if guest not in guests_results:
            print(f"{guest} is not at the party.")
        else:
            if meal in guests_results[guest]:
                guests_results[guest].remove(meal)
                disliked_meals +=1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

    command = input().split("-")

sorted_list = sorted(guests_results.items(),key=lambda kvp: (-len(kvp[1]), kvp[0]))

for items in sorted_list:
    print(f"{items[0]}: {', '.join(items[1])}")

print(f"Unliked meals: {disliked_meals}")