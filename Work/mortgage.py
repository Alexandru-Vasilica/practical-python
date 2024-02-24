# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input("No. of month the extra payments begin:"))
extra_payment_end_month = int(input("No. of month the extra payments end:"))
extra_payment = int(input("Amount paid extra:"))

while principal > 0:
    monthly_payment = payment
    month += 1
    
    if extra_payment_start_month <= month <= extra_payment_end_month:
        monthly_payment += extra_payment
    principal = principal * (1 + rate / 12)
    if principal < monthly_payment:
        monthly_payment = principal
    principal -= monthly_payment
    total_paid = total_paid + monthly_payment
    print(f'{month} {total_paid} {principal}')

print('Total paid', total_paid)
print('No. months', month)
