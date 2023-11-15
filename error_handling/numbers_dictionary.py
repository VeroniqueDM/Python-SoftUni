numbers_dictionary = {}
line = input()
while line != "Search":

    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

while True:
    searched = input()
    if searched == "End":
        break
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
        continue


print(numbers_dictionary)
