target = int(input())
daily_income = 0
command = input()

while command != "closed":
    if command == "haircut":
        type_haircut = input()
        if type_haircut == "mens":
            daily_income += 15
        elif type_haircut == "ladies":
            daily_income += 20
        elif type_haircut == "kids":
            daily_income += 10
    elif command == "color":
        type_dye = input()
        if type_dye == "touch up":
            daily_income +=20
        elif type_dye == "full color":
            daily_income +=30
    if daily_income >=target:
        print("You have reached your target for the day!")
        print(f"Earned money: {daily_income}lv.")
        break
    command= input()

if daily_income<target:
    print(f"Target not reached! You need {target -daily_income}lv. more.")
    print(f"Earned money: {daily_income}lv.")

