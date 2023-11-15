number_of_pages=int(input())
pages_per_hour=int(input())
days_count=int(input())
hours_per_day=(number_of_pages/pages_per_hour)/days_count
print(hours_per_day)