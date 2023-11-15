number = int(input())


for row in range (0, number):
    for col in range (0, row+1):
        print("*", end="")
    print()


for row in range (number-1, 0, -1):
    for col in range (1, row+1):
        print("*", end="")
    print()
