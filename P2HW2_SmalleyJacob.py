#Jacob Smalley
#21 Sep 2024
#P1HW2
#Basic grade point calculator.

module1 = float(input('Enter grade for module 1: '))
module2 = float(input('Enter grade for module 2: '))
module3 = float(input('Enter grade for module 3: '))
module4 = float(input('Enter grade for module 4: '))
module5 = float(input('Enter grade for module 5: '))
module6 = float(input('Enter grade for module 6: '))

grades = [module1, module2, module3, module4, module5, module6]

print('\t')
print('---------------Results-------------')
lowest_grade = min(grades)
highest_grade = max(grades)
print('Lowest Grade:' .ljust(20), f'{lowest_grade:.2f}')
print('Highest Grade:' .ljust(20), f'{highest_grade:.2f}')
print('Sum of Grades:' .ljust(20), f'{module1 + module2 + module3 + module4 + module5 + module6:.2f}')
print('Average:' .ljust(20), f'{(module1 + module2 + module3 + module4 + module5 + module6) / 6:.2f}')
print('-----------------------------------')
print('\t')
while True:
    pass
