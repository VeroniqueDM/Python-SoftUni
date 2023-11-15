import os
file = open("inner.txt")
file_3 = open("../example.txt")

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "venv", "example.txt")
file_2 = open(file_path)
print(file_2.readlines())
print(file.readlines())
print(file_3.readlines())