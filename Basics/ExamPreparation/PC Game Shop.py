n = int(input())
heartstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
for i in range (1, n +1):
    game_name = input()
    if game_name == "Hearthstone":
        heartstone_counter += 1
    elif game_name == "Fornite":
        fornite_counter +=1
    elif game_name == "Overwatch":
        overwatch_counter +=1
    else:
        others_counter +=1


total_counter = overwatch_counter+heartstone_counter+fornite_counter+others_counter
p_heartstone = heartstone_counter/total_counter*100
p_fornite = fornite_counter/total_counter*100
p_overwatch = overwatch_counter/total_counter*100
p_others = others_counter/total_counter*100


print(f"Hearthstone - {p_heartstone:.2f}%")

print(f"Fornite - {p_fornite:.2f}%")
print(f"Overwatch - {p_overwatch:.2f}%")
print(f"Others - {p_others:.2f}%")
