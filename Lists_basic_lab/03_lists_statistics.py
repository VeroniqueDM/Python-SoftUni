n = int(input())

list_positives = []
list_negatives = []
sum_negatives = 0
count_positives = 0

for a in range (1, n+1):
    number = int(input())
    if number > 0:
        list_positives.append(number)
        count_positives += 1
        #count_positives = len(list_positives)

    if number < 0:
        list_negatives.append(number)
        sum_negatives += number
        #sum = sum(list_negatives)

print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")