# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
monthly_payment = monthly_payment = base_payment + extra_payment_start_month + extra_payment_end_month
total_paid = 0.0
quota = 0 # this is the actual monthly payment after its modified by special payment conditions 

total_time = 0 # total number of months for payment
time_year = 12 # one year 

print('Time(Months) Total_paid quota Principal(remaining)')
while principal > 0:
    if total_time < (time_year*5):
        quota = monthly_payment
    elif total_time < (time_year*9):
        quota = monthly_payment + extra_payment

    principal = principal * (1+rate/12) - quota

    if(principal<0):
        adjustment = 0-principal
        quota -= adjustment
        principal += adjustment

    total_paid = total_paid + quota
    total_time += 1
    print(f'{total_time}(months) ${total_paid:0.2f} ${quota:0.2f} ${principal:0.2f}')
total_paid = round(total_paid,2)    
print('Total paid', total_paid, '\nTime (Months):', total_time)