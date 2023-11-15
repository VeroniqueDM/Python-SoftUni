line_one = [int(x) for x in input().split()]
line_two = [int(x) for x in input().split()]
line_three = [int(x) for x in input().split()]
a = 0
b = 1
c = 2
row_one = [line_one[a], line_two[a], line_three[a]]
row_two = [line_one[b], line_two[b], line_three[b]]
row_three = [line_one[c], line_two[c], line_three[c]]
diagonal_one = [line_one[a], line_two[b], line_three[c]]
diagonal_two = [line_one[c], line_two[b], line_three[a]]


def win(list):
    unique = set(list)
    if unique == {1}:
        winner = "First player won"
    elif unique == {2}:
        winner = "Second player won"
    else:
        winner = "Draw!"

    return winner


if win(line_one) == "Draw!":
    if win(line_two) == "Draw!":
        if win(line_three) == "Draw!":
            if win(row_one) == "Draw!":
                if win(row_two) == "Draw!":
                    if win(row_three) == "Draw!":
                        if win(diagonal_one) == "Draw!":
                            print(win(diagonal_two))
                        else:
                            print(win(diagonal_one))
                    else:
                        print(win(row_three))
                else:
                    print(win(row_two))
            else:
                print(win(row_one))
        else:
            print(win(line_three))
    else:
        print(win(line_two))
else:
    print(win(line_one))
