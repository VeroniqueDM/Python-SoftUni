number_of_rooms = int(input())



room_num = 1
free_chairs = 0
good_rooms_counter = 0

for i in range (0, number_of_rooms):
    info = input().split()
    chairs = len(info[0])
    people = int(info[1])
    if chairs >= people:
        free_chairs += chairs - people
        good_rooms_counter += 1
    else:
        needed_chairs = people - chairs
        print(f"{needed_chairs} more chairs needed in room {room_num}")

    room_num += 1

if good_rooms_counter == number_of_rooms:
    print(f"Game On, {free_chairs} free chairs left")