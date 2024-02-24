bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    num_bills = num_bills * 2
    day += 1

print("No. days: ", day)
