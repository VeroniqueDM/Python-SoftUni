
# ark = int(input())
#
# aa = text*ark
# print(aa)

while True:
    try:
        text = input()
        times = int(input())
        break
    except ValueError:
        print("Variable times must be an integer")

print(text*times)