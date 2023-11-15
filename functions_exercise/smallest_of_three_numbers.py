def smallest_number(a, b, c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < b and c < a:
        return c


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(smallest_number(number_one, number_two, number_three))