n = int(input())
collection_of_pieces = {}
for a in range(n):
    piece, composer, key = input().split("|")
    if piece not in collection_of_pieces:
        collection_of_pieces[piece] = {"Composer":composer, "Key":key}

command = input().split("|")
while command[0] != "Stop":
    action = command[0]
    if action == "Add":
        current_piece, current_composer, current_key = command[1:4]
        if current_piece not in collection_of_pieces:
            collection_of_pieces[current_piece] = {"Composer":current_composer, "Key":current_key}
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")
    elif action == "Remove":
        current_piece = command[1]
        if current_piece in collection_of_pieces:
            del collection_of_pieces[current_piece]
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    elif action == "ChangeKey":
        current_piece,current_key = command[1:3]
        if current_piece in collection_of_pieces:
            collection_of_pieces[current_piece]["Key"] = current_key
            print(f"Changed the key of {current_piece} to {current_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    command = input().split("|")

sorted_collection = sorted(collection_of_pieces.items(), key=lambda kvp:(kvp[0], kvp[1]["Composer"]))


for items in sorted_collection:
    print(f"{items[0]} -> Composer: {items[1]['Composer']}, Key: {items[1]['Key']}")