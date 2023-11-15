currennt_year = int(input())

while True:
    currennt_year += 1
    currennt_year_as_string = str(currennt_year)
    if len(currennt_year_as_string) == len(set(currennt_year_as_string)):
        print(currennt_year_as_string)
        break