#Jacob Smalley
#7 Nov 2024
#P3HW2_Salary
#Multiple employee pay calculator.

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    name = input('Enter employee\'s name or \"Done\" to quit: ')
    if name.lower() == 'done':
        break

    hours = float(input(f'How many hours did {name} work? '))
    rate = float(input(f'What is {name}\'s pay rate: $'))
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
    print('\t')
    print('\t')
  
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

print('Total number of employees entered: ', total_employees)
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')


#Pseudocode
#Prompt user to enter name, hours worked, and hourly pay.
#Calculate for individual overtime hours.
#Calculate for individual regular hours.
#Calculate for individual overtime pay.
#Calculate for individual regular pay.
#Calculate for individual total pay.
#Print hours worked, pay rate, overtime, overtime pay, regular hour pay, and total pay.
#Output so the the hours and pay are above a dashed line and the amounts are directly below their corresponding part below the dashed line.
#Give user option to add more employees or be done.
#If more user keep calculating.
#If done then tally up total number of Total number of employees entered, Total amount paid for overtime, Total amount paid for regular hours, and Total amount paid in gross.
