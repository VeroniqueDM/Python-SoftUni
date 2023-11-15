days_tournament = int(input())
winner_days_count = 0
loser_days_count = 0
money_earned_total = 0
for days in range(1, days_tournament + 1):
    daily_win_count = 0
    daily_loss_count = 0
    money_earned_daily = 0
    command = input()
    while command != "Finish":
        result = input()
        if result == "win":
            daily_win_count += 1
            money_earned_daily += 20
        else:
            daily_loss_count += 1
        command = input()
    if daily_win_count > daily_loss_count:
        winner_days_count += 1
        money_earned_daily += money_earned_daily * 0.1
        money_earned_total += money_earned_daily
    else:
        loser_days_count += 1
        money_earned_total += money_earned_daily
if winner_days_count > loser_days_count:
    money_earned_total += money_earned_total * 0.20
    print(f"You won the tournament! Total raised money: {money_earned_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_earned_total:.2f}")
