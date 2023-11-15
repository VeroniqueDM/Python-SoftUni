def create_sequence(num):
    seq = [0, 1]
    for a in range(num - 2):
        new_num = seq[-1] + seq[-2]
        seq.append(new_num)
    return seq


def locate(sequence, number):
    if number in sequence:
        print(f"The number - {number} is at index {sequence.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")
