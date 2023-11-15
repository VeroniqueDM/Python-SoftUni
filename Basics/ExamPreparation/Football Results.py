first_result = input()
second_result = input()
third_result = input()

our_score_1 = first_result[0]
their_score_1 = first_result[2]
our_score_2 = second_result[0]
their_score_2 = second_result[2]
our_score_3 = third_result[0]
their_score_3 = third_result[2]

win_count = 0
draw_count = 0
loss_count = 0

if our_score_1 > their_score_1:
    win_count += 1
elif our_score_1 < their_score_1:
    loss_count += 1
else:
    draw_count += 1

if our_score_2 > their_score_2:
    win_count += 1
elif our_score_2 < their_score_2:
    loss_count += 1
else:
    draw_count += 1

if our_score_3 > their_score_3:
    win_count += 1
elif our_score_3 < their_score_3:
    loss_count += 1
else:
    draw_count += 1

print(f"Team won {win_count} games.")
print(f"Team lost {loss_count} games.")
print(f"Drawn games: {draw_count}")
