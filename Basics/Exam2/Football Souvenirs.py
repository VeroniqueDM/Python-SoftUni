team = input()
type_of_souvenier = input()
number_of_souveniers = int(input())

if team == "Argentina":
    if type_of_souvenier == "flags":
        bill = number_of_souveniers * 3.25
    elif type_of_souvenier == "caps":
        bill = number_of_souveniers * 7.20
    elif type_of_souvenier == "posters":
        bill = number_of_souveniers * 5.10
    elif type_of_souvenier == "stickers":
        bill = number_of_souveniers * 1.25
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if type_of_souvenier == "flags":
        bill = number_of_souveniers * 4.20
    elif type_of_souvenier == "caps":
        bill = number_of_souveniers * 8.50
    elif type_of_souvenier == "posters":
        bill = number_of_souveniers * 5.35
    elif type_of_souvenier == "stickers":
        bill = number_of_souveniers * 1.20
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if type_of_souvenier == "flags":
        bill = number_of_souveniers * 2.75
    elif type_of_souvenier == "caps":
        bill = number_of_souveniers * 6.90
    elif type_of_souvenier == "posters":
        bill = number_of_souveniers * 4.95
    elif type_of_souvenier == "stickers":
        bill = number_of_souveniers * 1.10
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if type_of_souvenier == "flags":
        bill = number_of_souveniers * 3.10
    elif type_of_souvenier == "caps":
        bill = number_of_souveniers * 6.50
    elif type_of_souvenier == "posters":
        bill = number_of_souveniers * 4.80
    elif type_of_souvenier == "stickers":
        bill = number_of_souveniers * 0.90
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

if (team == "Argentina" or team == "Croatia" or team == "Denmark" or team == "Brazil") and (type_of_souvenier == "flags" or type_of_souvenier == "caps" or type_of_souvenier == "posters" or type_of_souvenier == "stickers"):
    print(f'Pepi bought {number_of_souveniers} {type_of_souvenier} of {team} for {bill:.2f} lv.')