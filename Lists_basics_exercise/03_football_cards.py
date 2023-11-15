referees_cards = input().split(" ")

team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]



game_was_terminated = False

for player in referees_cards:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a)<7 or len(team_b) <7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")














#
# team_a = [1,2,3,4,5,6,7,8,9,10,11]
# team_b = [1,2,3,4,5,6,7,8,9,10,11]
#
# count_a = 11
# count_b = 11
#
# for a in range(len(referees_cards)):
#     if a[0] == "A":
#         team_a.remove(a[2])
#     elif a[0] == "B":
#         team_b.remove(a[2])
#     if len(team_a)<7 or len(team_b)<7:
#         break
#
# if len(team_a)<7 or len(team_b)<7:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#     print("Game was terminated")
# else:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
#
