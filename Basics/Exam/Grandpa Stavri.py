n = int(input())
liters_total = 0
degrees_daily = 0
degrees_total = 0
for i in range (1, n +1):
    liters_rakia = float(input())
    alcohol = float(input())
    liters_total += liters_rakia
    degrees_daily = liters_rakia*alcohol
    degrees_total += degrees_daily

degrees_average = degrees_total/liters_total

print(f"Liter: {liters_total:.2f}")
print(f"Degrees: {degrees_average:.2f}")
if degrees_average<38:
    print("Not good, you should baking!")
elif 38<=degrees_average<=42:
    print("Super!")
elif degrees_average> 42:
    print("Dilution with distilled water!")