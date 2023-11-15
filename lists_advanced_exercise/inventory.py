current_items = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":
    activity = command[0]
    item = command[1]
    if activity == "Collect":
        if item not in current_items:
            current_items.append(item)
    elif activity == "Drop":
        if item in current_items:
            current_items.remove(item)
    elif activity == "Combine Items":
        items_group = item.split(":")
        if items_group[0] in current_items:
            index = current_items.index(items_group[0])
            current_items.insert(index +1, items_group[1])
    elif activity == "Renew":
        if item in current_items:
            index = current_items.index(item)
            current_items.insert(len(current_items)-1, current_items.pop(index))
    command = input().split(" - ")

print(", ".join(current_items))
