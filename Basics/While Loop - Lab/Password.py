name = input()
password = input()
attempt = input()
while attempt != password:
    attempt = input()
if attempt == password:
    print(f"Welcome {name}!")