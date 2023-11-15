command = input()
force_catalogue = {}

# def add_user(forces_as_dicts, to_side, user_to_be_added):
#     for side, users in forces_as_dicts.items():
#         if user_to_be_added in users:
#             return  forces_as_dicts
#     if to_side not in forces_as_dicts:
#         forces_as_dicts[to_side]=user_to_be_added
#     else:
#         forces_as_dicts[to_side].append(user_to_be_added)
#     return forces_as_dicts
#
# def change_side(forces_as_dict, to_side, user_to_be_changed):
#     for side, users in forces_as_dict.items:
#         if user_to_be_changed in users:
#             forces_as_dict[side].remove(user_to_be_changed)
#             return add_user(forces_as_dict,to_side,user_to_be_changed)
#     return add_user(forces_as_dict,to_side,user_to_be_changed)


while command != "Lumpawaroo":
    if " | " in command:
        current_action = command.split(" | ")
        force_user = current_action[1]
        force_side = current_action[0]
        exists = False
        for v in force_catalogue.values():
            if force_user in v:
                exists = True
        if exists == False:
            if force_side not in force_catalogue:
                force_catalogue[force_side] = []
            force_catalogue[force_side].append(force_user)
            force_catalogue[force_side].sort()

    else:
        current_action = command.split(" -> ")
        force_user = current_action[0]
        force_side = current_action[1]

        if force_side not in force_catalogue:
            force_catalogue[force_side] = []
        for v in force_catalogue.values():
            if force_user in v:
                v.remove(force_user)
                break
        force_catalogue[force_side].append(force_user)
        force_catalogue[force_side].sort()
        print(f"{force_user} joins the {force_side} side!")
    command = input()


sorted_catalogue = sorted(force_catalogue.items(), key=lambda kv:(-len(kv[1]), kv[0]))

for forces in sorted_catalogue:
    if len(forces[1])>0:
        print(f"Side: {forces[0]}, Members: {len(forces[1])}")
        for a in forces[1]:
            print(f"! {a}")