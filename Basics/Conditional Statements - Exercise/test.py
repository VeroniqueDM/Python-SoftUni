# import math
current_record = float(input())
meters_total = float(input())
seconds_per_meter = float(input())

delay = (meters_total//15)*12.5
ivan_record = seconds_per_meter * meters_total + delay

# delay_times = (math.floor(meters_total / 15))
# ivan_record = ivan_record - delay_times * 12.5

if ivan_record < current_record:
    print(f"Yes, he succeeded! The new world record is {ivan_record:.2f} seconds.")
else:
    insufficient = ivan_record - current_record
    print(f"No, he failed! He was {insufficient:.2f} seconds slower.")
