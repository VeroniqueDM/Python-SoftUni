target = 10000

total_steps = 0

while True:
    command = input()

    if command == "Going home":

        steps = int(input())
        total_steps = total_steps + steps
        if target <= total_steps:
            print("Goal reached! Good job!")
            print(f"{total_steps - target} steps over the goal!")
            break
        else:
            print(f"{target - total_steps} more steps to reach goal.")
            break
    else:
        steps = int(command)
        total_steps = total_steps + steps
        if target <= total_steps:
            print("Goal reached! Good job!")
            print(f"{total_steps - target} steps over the goal!")
            break


