elements = input().split()

integers = input().split()
counter_moves = 0

while integers[0] != "end":
    counter_moves +=1
    index_one = int(integers[0])
    index_two = int(integers[1])
    if index_two == index_one or index_two< 0 or index_one < 0 or index_one>= len(elements) or index_two>= len(elements):
        first_pos = len(elements)//2
        second_pos = first_pos + 1
        elements.insert(first_pos, f"-{counter_moves}a")
        elements.insert(second_pos, f"-{counter_moves}a")
        print("Invalid input! Adding additional elements to the board")
        integers = input().split()
        continue
    element_one = elements[index_one]
    element_two = elements[index_two]
    if element_one == element_two:

        print(f"Congrats! You have found matching elements - {elements[index_two]}!")
        indices_list = sorted([index_one, index_two], reverse=True)

        for index in indices_list:
            del elements[index]


    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {counter_moves} turns!")
        break
    integers = input().split()

if len(elements)>0:
    elements_as_str = " ".join(elements)
    print(f"Sorry you lose :( \n{elements_as_str}")

