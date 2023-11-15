neighbours = [int(x) for x in input().split("@")]
cupid_position = 0
command = input().split()


def give_hearts(house, index):
    house[index]-=2
    if house[index]<0:
        print(f"Place {index} already had Valentine's day.")
    elif house[index] == 0:
        print(f"Place {index} has Valentine's day." )
    return house

while command[0] != "Love!":
    value = int(command[1])
    cupid_position += value
    if cupid_position >= len(neighbours):
        cupid_position = 0
        neighbours = give_hearts(neighbours,cupid_position)
    else:
        neighbours = give_hearts(neighbours,cupid_position)

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_list = [int(l) for l in neighbours if int(l) > 0]
if failed_list:
    print(f"Cupid has failed {len(failed_list)} places.")
else:
    print("Mission was successful.")