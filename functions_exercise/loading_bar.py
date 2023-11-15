number_for_bar = int(input())


def loading_bar(number):
    if number == 100:
        print("100% Complete!\n[%%%%%%%%%%]")

    else:
        c = number // 10
        loaded = c * "%"
        remaining = (10 - c) * "."

        print(f"{number}% [{loaded}{remaining}]\nStill loading...")


loading_bar(number_for_bar)
