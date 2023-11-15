number = float(input())
input_metric = input()
output_metric = input()
number_in_meters = 0
if input_metric == "mm":
    number_in_meters = number / 1000
elif input_metric == "cm":
    number_in_meters = number / 100

elif input_metric == "m":
    number_in_meters = number

result = 0

if output_metric == "mm":
    result = number_in_meters * 1000
elif output_metric == "cm":
    result = number_in_meters * 100
elif output_metric == "m":
    result = number_in_meters * 1

print (f"{result:.3f}")