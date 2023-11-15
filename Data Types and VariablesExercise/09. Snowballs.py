number_snowballs = int(input())
highest_value = 0
for snowball in range (1, number_snowballs +1):
    weight = int(input())
    speed = int(input())
    quality = int(input())
    current_value = (weight/speed) ** quality
    if current_value > highest_value:
        highest_value = int(current_value)
        best_weight = weight
        best_speed = speed
        best_quality = quality

print(f"{best_weight} : {best_speed} = {highest_value} ({best_quality})")