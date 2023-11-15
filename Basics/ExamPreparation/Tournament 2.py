total_days = int(input())
total_money = 0
days_won = 0
days_lost = 0
for day in range(1, total_days+1):
    daily_won_games = 0
    daily_lost_games = 0
    daily_money = 0
    command = input()
    while command != "Finish":
        win_or_lose = input()
        if win_or_lose == "win":
            daily_won_games += 1
            daily_money += 20
        elif win_or_lose == "lose":
            daily_lost_games += 1
        command = input()
    if daily_won_games > daily_lost_games:
        days_won += 1
        daily_money *= 1.10
        total_money += daily_money
    else:
        days_lost += 1
        total_money += daily_money
if days_won > days_lost:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")