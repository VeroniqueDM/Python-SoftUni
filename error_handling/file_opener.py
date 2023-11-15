import os
# try:
#     file = open("custom_files/text.txt") # automatically changed the path when refactoring
#     print("File found.")
# except FileNotFoundError:
#     print("File not found")
#

if os.path.exists("text.txt"):
    print("File found.")
else:
    print("File not found")