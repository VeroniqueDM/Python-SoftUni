file_path = input()
# raw_filepath = r + file_path
elements_list = file_path.split("\\")

file = elements_list[len(elements_list)-1]
file_list = file.split(".")
file_name = file_list[0]
file_extension = file_list[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
