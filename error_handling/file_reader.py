num_list = []
try:
    with open("custom_files/numbers.txt") as file:
        for line in file.readlines():
            num_list.append(int(line))
except FileNotFoundError:
    print("File was not found")
print(sum(num_list))
