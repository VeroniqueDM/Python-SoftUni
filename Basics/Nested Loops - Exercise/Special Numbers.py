n = int(input())

for first in range (1, 10):
    if n%first == 0:
        for second in range (1, 10):
            if n%second == 0:
                for third in range (1, 10):
                    if n%third == 0:
                        for fourth in range (1, 10):
                            if n%fourth == 0:
                                print(f"{first}{second}{third}{fourth}", end=" ")

