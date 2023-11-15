import os
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "custom_files", "inner.txt")
file3 = open(file_path)
file = open("example.txt")
file_2 = open("example.txt", "r")
file_1 = open("custom_files/inner.txt")

print(file_2.readlines())
print(file_path)
print(file3.readlines())

file_path = os.path.join(absolute_path, "custom_files", "test.txt")
file4= open(file_path, "w")

print(file4.writelines("test sth"))
file5= open(file_path, "a")

print(file4.writelines( " \nappend"))
