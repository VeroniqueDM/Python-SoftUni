sequence = [int(x) for x in input().split()]
middle_index = len(sequence) // 2
car_one_time = 0
car_two_time = 0

for step in range (0, middle_index):
    if sequence[step] != 0:
        car_one_time += sequence[step]
    else:
        car_one_time -= car_one_time*0.2


for steps in range (middle_index + 1,len(sequence)):
    if sequence[steps] != 0:
        car_two_time += sequence[steps]
    else:
        car_two_time -= car_two_time * 0.2


if car_one_time < car_two_time:
    winner = "left"
    total_time = car_one_time
else:
    winner = "right"
    total_time = car_two_time

print(f"The winner is {winner} with total time: {total_time:.1f}")