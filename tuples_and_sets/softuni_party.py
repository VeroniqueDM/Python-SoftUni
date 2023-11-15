n = int(input())
guests = set()
for _ in range(n):
    res_code = input()
    guests.add(res_code)

guest_code = input()

while not guest_code == "END":
    guests.remove(guest_code)
    guest_code = input()
print(len(guests))
print("\n".join(sorted(guests)))