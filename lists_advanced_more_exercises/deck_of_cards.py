list_of_cards = input().split(", ")
n = int(input())

for i in range(0, n):
    command = input().split(", ")
    activity = command[0]
    if activity == "Add":
        card = command[1]
        if card in list_of_cards:
            print("Card is already in the deck")

        else:
            list_of_cards.append(card)
            print("Card successfully added")

    elif activity == "Remove":
        card = command[1]
        if card in list_of_cards:
            list_of_cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif activity == "Remove At":
        index = int(command[1])

        if -(len(list_of_cards) - 1) <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif activity == "Insert":
        index = int(command[1])
        card = command[2]
        if 0 <= index < len(list_of_cards):
            if card in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index, card)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))