def fill_the_box(height, width, length, *args):
    size = height * length * width
    cubes = []
    for ind in range(len(args)):
        if args[ind] != "Finish":
            cubes.append(args[ind])
        else:

            break
    total_cubes = sum(cubes)
    for cube in cubes:
        if size>cube:
            size -= cube
            total_cubes -=cube
        if size < cube:
            total_cubes -= size
            return f"No more free space! You have {total_cubes} more cubes."

    return f"There is free space in the box. You could put {size} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))