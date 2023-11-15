hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time = hour_of_exam * 60 + minute_of_exam
arrival_time = hour_of_arrival * 60 + minute_of_arrival

difference = arrival_time - exam_time

text = ""
if difference < -30:
    text = "Early"
elif difference <= 0:
    text = "On time"
else:
    text = "Late"
print(text)


if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    if hours > 0:
        if difference < 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{hours}:{minutes:02d} hours after the start")
    else:
        if difference < 0:
            print(f"{minutes} minutes before the start")
        else:
            print(f"{minutes} minutes after the start")
