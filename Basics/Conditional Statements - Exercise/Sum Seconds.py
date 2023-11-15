time_first = int(input())
time_second = int(input())
time_third = int(input())
time_total_sec = time_third + time_second + time_first
total_minutes = time_total_sec // 60
remaining_seconds = time_total_sec % 60
if remaining_seconds < 10:
    print(f'{total_minutes}:0{remaining_seconds}')
else:
    print(f'{total_minutes}:{remaining_seconds}')