paper = int(input())
fabric = int(input())
glue = float(input())
discount_percentage = int(input())
percentage = discount_percentage/100

bill = paper*5.8 + fabric*7.20 + glue*1.20
discounted_bill = bill - bill*percentage

print(f"{discounted_bill:.3f}")