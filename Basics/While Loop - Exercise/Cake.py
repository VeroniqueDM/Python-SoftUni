cake_length = int(input())
cake_width = int(input())
cake_area = cake_width*cake_length
# pieces_taken_count = 0

while cake_area>0:
    command = input()
    if command != "STOP":
        pieces = int(command)
        cake_area = cake_area - pieces
    else:
        print(f"{cake_area} pieces are left.")
        break
if cake_area<0:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")


# while True:
#     command = input()
#     if command != "STOP" and pieces_taken_count<=cake_area:
#         pieces = int(command)
#         pieces_taken_count = pieces_taken_count + pieces
#     elif command == "STOP" and pieces_taken_count <= cake_area:
#         print(f"{cake_area - pieces_taken_count} pieces are left.")
#         break
#     else:
#         print(f"No more cake left! You need {pieces_taken_count - cake_area} pieces more.")
#         break
