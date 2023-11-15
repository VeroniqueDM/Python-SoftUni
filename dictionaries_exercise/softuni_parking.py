number_of_commands = int(input())

cars_in_parking = {}
for a in range (0, number_of_commands):
    command = input().split()
    reg_or_unreg = command[0]
    username = command[1]
    if reg_or_unreg == "register":
        license_plate = command[2]
        if username in cars_in_parking:
            print(f"ERROR: already registered with plate number {cars_in_parking[username]}")
        else:
            cars_in_parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif reg_or_unreg == "unregister":
        if username not in cars_in_parking:
            print(f"ERROR: user {username} not found")
        else:
            del cars_in_parking[username]
            print(f"{username} unregistered successfully")


for i,v in cars_in_parking.items():
    print(f"{i} => {v}")
