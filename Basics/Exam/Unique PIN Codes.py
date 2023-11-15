limit_1 = int(input())
limit_2 = int(input())
limit_3 = int(input())

for first in range(1, limit_1 + 1):
    if first % 2 == 0:
        for second in range(1, limit_2 + 1):
            denom_count = 0
            for i in range(2, second+1):
                if second % i == 0:
                    denom_count += 1
            if denom_count == 1:
                for third in range(1, limit_3 + 1):
                    if third % 2 == 0:
                        print(f"{first}{second}{third}")
