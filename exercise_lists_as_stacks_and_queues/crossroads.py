from collections import deque
green_light_duration = int(input())
free_window = int(input())
total_passed_cars = 0
command = input()
carline = deque()
while not command == "END":
    crash_happened = False
    if command != "green":
        carline.append(command)

    else:
        time_available = green_light_duration + free_window
        while carline and time_available>free_window:
            current_car = carline.popleft()
            time_needed = len(current_car)
            if time_needed <= time_available:
                time_available -= time_needed
                total_passed_cars += 1
            else:
                crash_index = time_needed - time_available
                crash_letter = current_car[len(current_car)-crash_index]

                crash_happened = True
                break
    if crash_happened:
        print("A crash happened!")
        print(f'{current_car} was hit at {crash_letter}.')
        break
    command = input()

if crash_happened == False:
    print("Everyone is safe.")
    print(f'{total_passed_cars} total cars passed the crossroads.')