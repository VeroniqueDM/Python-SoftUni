events_string = input().split("|")

coins = 100
energy = 100

all_events_done = True

for event in range(len(events_string)):
    current_event = events_string[event].split("-")
    if "rest" in current_event:

        if energy + int(current_event[1]) > 100:
            energy = 100
            print("You gained 0 energy.")

        else:
            energy += int(current_event[1])
            print(f"You gained {int(current_event[1])} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in current_event:

        if energy-30 >= 0:
            energy -= 30
            coins += int(current_event[1])
            print(f"You earned {int(current_event[1])} coins.")
        else:
            #energy -= 30
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:

        if coins - int(current_event[1]) > 0:
            coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")
        else:
            all_events_done = False
            print(f"Closed! Cannot afford {current_event[0]}." )
            break

if all_events_done == True:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")