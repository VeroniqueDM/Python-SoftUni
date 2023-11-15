width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height

number_of_boxes = input()
volume_boxes = 0
while number_of_boxes != "Done":
    volume_boxes = volume_boxes + int(number_of_boxes)
    if volume_boxes > total_volume:
        print(f"No more free space! You need {volume_boxes-total_volume} Cubic meters more.")
        break
    number_of_boxes = input()
if number_of_boxes == "Done":
    print(f"{total_volume-volume_boxes} Cubic meters left.")

