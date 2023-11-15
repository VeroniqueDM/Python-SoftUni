numbers = [int(s) for s in input().split(", ")]
# negatives_list = ", ".join([str(s) for s in numbers if s < 0])
# # positives_list =  ", ".join([str(s) for s in numbers if s >= 0])
# even_list =  ", ".join([str(s) for s in numbers if s % 2 == 0])
# odd_list =  ", ".join([str(s) for s in numbers if s %2 != 0])
print(f"Positive: {', '.join([str(s) for s in numbers if s >= 0])}")
print(f"Negative: {', '.join([str(s) for s in numbers if s < 0])}")
print(f"Even: { ', '.join([str(s) for s in numbers if s % 2 == 0])}")
print(f"Odd: { ', '.join([str(s) for s in numbers if s %2 != 0])}")
