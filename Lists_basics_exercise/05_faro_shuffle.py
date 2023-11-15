cards_original_deck = input().split()

faro_shuffles = int(input())

final_deck = []

for shuffle in range (faro_shuffles):
    final_deck = []
    middle_of_the_deck = len(cards_original_deck)//2
    left_half = cards_original_deck[0:middle_of_the_deck]
    right_half = cards_original_deck[middle_of_the_deck:]


    for index_a in range(len(left_half)):
        final_deck.append(left_half[index_a])
        final_deck.append(right_half[index_a])


    cards_original_deck = final_deck

print(final_deck)


  #  for card in range (list_two):