width_ship = float(input())
length_ship = float(input())
height_ship = float(input())
average_austronaut_height = float(input())

volume = length_ship*width_ship*height_ship

room_volume = 2*2* (average_austronaut_height + 0.40)
number_of_rooms = volume // room_volume

if 3<=number_of_rooms<=10:
    print(f"The spacecraft holds {number_of_rooms:.0f} astronauts.")
elif number_of_rooms<3:
    print(f"The spacecraft is too small.")
elif number_of_rooms >10:
    print(f"The spacecraft is too big.")