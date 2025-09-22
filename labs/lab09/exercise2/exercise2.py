employee_name = input()
base_salary  = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
overtime_pay = overtime_hours * 35
total_income = base_salary  + overtime_pay

if (tax_status == Single):
    if ( total_income >= 5000):
       tax_rate = 0.22
       tax = "22%"
    else :
       tax_rate = 0.18
       tax = "18%"
elif (tax_status == Married):
    if (total_income  >= 6000):
       tax_rate = 0.20
       tax = "20%"
    else :
       tax_rate = 0.25
       tax = "15%"
else:
    if (total_income  >= 5500):
       tax_rate = 0.25
       tax = "25%"
    else :
       tax_rate = 0.19
       tax = "19%"

tax_amount = total_income * tax_rate
epf = total_income * 0.11
socso = total_income * 0.005

net_salary = total_income - tax_amount - epf - socso

net_salary = total_income  * (tax/100)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")