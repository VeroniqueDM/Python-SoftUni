
def start_spring(**kwargs):
    spring_types = {}
    for name, category in kwargs.items():
        if category not  in spring_types:
            spring_types[category] = []
        spring_types[category].append(name)
    for cat, names in spring_types.items():
        spring_types[cat] = sorted(spring_types[cat])

    result = sorted(spring_types.items(), key=lambda kvpt:(-len(kvpt[1]), kvpt[0]))
    def printing_res(a_list):
        res = []
        for index in range(len(a_list)):
            res.append(f"{a_list[index][0]}:")
            for ind in range(len(a_list[index][1])):
                res.append(f"-{a_list[index][1][ind]}")
        return "\n".join(res)


    return printing_res(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
