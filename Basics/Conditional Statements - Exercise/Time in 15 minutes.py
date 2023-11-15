hour_now = int(input())
minutes_now = int(input())
minutes_now += 15
if minutes_now > 59:
    hour_now += 1
    minutes_now = minutes_now % 60
    if hour_now == 24:
        hour_now = 0
if minutes_now < 10:
    print(f"{hour_now}:0{minutes_now}")
else:
    print(f"{hour_now}:{minutes_now}")