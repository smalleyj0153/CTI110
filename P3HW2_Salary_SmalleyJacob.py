#Jacob Smalley
#27 Oct 2024
#P3HW2_Salary
#Basic pay calculator.

name = input('Enter employee\'s name: ')
hours = float(input('Enter number of hours worked: '))
rate = float(input('Enter employee\'s pay rate: $'))
print('-----------------------------------')
print(f'Emplyee  name: {name}')
print('\t')

overtime_hours = (hours - 40 if hours > 40 else 0)
regular_hours = (hours - overtime_hours)

overtime_pay = overtime_hours * rate * 1.5
regular_pay = regular_hours * rate
gross_pay = (overtime_pay + regular_pay)

print(f'Hours Worked:\t\tPay Rate\t\tOverTime\t\tOvertime Pay\t\tRegHour Pay\t\tGross Pay:')
print('-----------------------------------------------------------------------------------------------------------------------------------')
print(f'{hours}\t\t\t${rate:.2f}\t\t\t{overtime_hours:.2f}\t\t\t${overtime_pay:.2f}\t\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}')

#Pseudocode
#Prompt user to enter name, hours worked, and hourly pay.
#Calculate overtime hours.
#Calculate regular hours.
#Calculate overtime pay.
#Calculate regular pay.
#Calculate total pay.
#Print hours worked, pay rate, overtime, overtime pay, regular hour pay, and total pay.
#Output so the the hours and pay are above a dashed line and the amounts are directly below their corresponding part below the dashed line.
