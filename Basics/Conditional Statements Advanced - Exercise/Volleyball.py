type_of_year = input()
holidays_count = int(input())
weekends_in_ht_count = int(input())
weekends_in_sofia = 48 - weekends_in_ht_count
weekends_to_play_in_sofia = weekends_in_sofia*0.75
holidays_to_play = holidays_count *2/3
result = weekends_in_ht_count + holidays_to_play + weekends_to_play_in_sofia
if type_of_year == "leap":
    result = result*1.15
import math
result = math.floor(result)
print(result)