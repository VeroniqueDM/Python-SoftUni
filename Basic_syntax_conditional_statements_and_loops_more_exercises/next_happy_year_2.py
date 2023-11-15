year = input()
year_int = int(year)
length_year = len(year)
length_unique_nums =  len(set(year))
while length_year != length_unique_nums:
    year_int += 1
    year = str(year_int)
    length_year = len(year)
    length_unique_nums = len(set(year))

print(year_int)