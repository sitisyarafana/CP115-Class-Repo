employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if (tax_status == Single):
    if (base_salary >= 5000):
       tax = 22
       tax_rate = "22%"
    else :
       tax = 18
       tax_rate = "18%"
elif (tax_status == Married):
    if (base_salary >= 6000):
       tax = 20
       tax_rate = "20%"
    else :
       tax = 25
       tax_rate = "15%"
else:
    if (base_salary >= 5500):
       tax = 25
       tax_rate = "25%"
    else :
       tax = 19
       tax_rate = "19%"

net_salary = base_salary * (tax/100)


print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")