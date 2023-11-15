def nested_loops(index, array):
    if index>= len(array):
        print(*array, sep=' ')
        return
    for num in range(1, len(array) +1):
        array[index] = num
        nested_loops(index + 1, array)

n = int(input())
array = [None] * n

nested_loops(0, array)