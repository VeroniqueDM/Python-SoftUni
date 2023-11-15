numbers = [int(x) for x in input().split()]
pos_num = sum([x for x in numbers if x > 0 ])
neg_num = sum([x for x in numbers if x < 0 ])
print(neg_num)
print(pos_num)
if abs(pos_num) > abs(neg_num):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
