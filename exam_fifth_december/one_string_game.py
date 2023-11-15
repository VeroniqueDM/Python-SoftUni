text = input()
command = input().split()

while command[0] != "Done":
    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        text = text.replace(char,replacement)
        print(text)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif command[0] == "End":
        substring = command[1]
        length_sub = len(substring)
        string_to_check = text[len(text)-length_sub:]
        if substring == string_to_check:
            print(True)
        else:
            print(False)
    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        for chars in range(0, len(text)):
            current_char = text[chars]
            if current_char == char:
                print(chars)
                break
    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        result = text[start_index: start_index +count]
        print(result)
    command = input().split()