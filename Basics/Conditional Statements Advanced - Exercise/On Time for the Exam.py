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



# My first solution:
# hour_of_exam = int(input())
# minute_of_exam = int(input())
# hour_of_arrival = int(input())
# minute_of_arrival = int(input())
# exam_time = hour_of_exam * 60 + minute_of_exam
# arrival_time = hour_of_arrival * 60 + minute_of_arrival
# if exam_time < arrival_time:
#     print("Late")
#     hour = (arrival_time - exam_time) // 60
#     minute = (arrival_time - exam_time) % 60
#     if minute < 10:
#         minute = (f"0{minute}")
#     if arrival_time - exam_time >= 60:
#         print(f"{hour}:{minute} hours after the start")
#     elif arrival_time - exam_time < 60:
#         print(f"{minute} minutes after the start")
# if arrival_time == exam_time:
#     print("On time")
# if arrival_time < exam_time and exam_time - arrival_time <= 30:
#     print("On time")
#     minute = (exam_time - arrival_time) % 60
#     print(f"{minute} minutes before the start")
# elif arrival_time < exam_time and exam_time - arrival_time > 30:
#     print("Early")
#     hour = (exam_time - arrival_time) // 60
#     minute = (exam_time - arrival_time) % 60
#     if minute < 10:
#         minute = (f"0{minute}")
#     if exam_time - arrival_time >= 60:
#         print(f"{hour}:{minute} hours before the start")
#     elif exam_time - arrival_time < 60:
#         print(f"{minute} minutes before the start")
