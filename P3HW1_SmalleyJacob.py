#Jacob Smalley
#20 Oct 2024
#P1HW2
#Basic grade point calculator.

mod_1 = float(input('Enter grade for module 1: '))
mod_2 = float(input('Enter grade for module 2: '))
mod_3 = float(input('Enter grade for module 3: '))
mod_4 = float(input('Enter grade for module 4: '))
mod_5 = float(input('Enter grade for module 5: '))
mod_6 = float(input('Enter grade for module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print('\t')
print('---------------Results-------------')
lowest_grade = min(grades)
highest_grade = max(grades)
print('Lowest Grade:' .ljust(20), f'{lowest_grade:.2f}')
print('Highest Grade:' .ljust(20), f'{highest_grade:.2f}')
print('Sum of Grades:' .ljust(20), f'{mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6:.2f}')
print('Average:' .ljust(20), f'{(mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6) / 6:.2f}')
print('-----------------------------------')
print('\t')

Average = sum(grades) / 6

if Average >= 90:
    print('Your grade is: A')
elif Average >= 80:
    print('Your grade is: B')
elif Average >= 70:
    print('Your grade is: C')
elif Average >= 60:
    print('Your grade is: D')
elif Average >= 50:
    print('Your grade is: E')
else:
    print('Your grade is: F')

while True:
    pass



#Pseudocode:
#Get grades for module 1, 2, 3, 4, 5, and 6 from the user.
#Store the grades in a list.
#Find the lowest and highest grades from the list.
#Calculate the sum of all grades.
#Calculate the average of all grades.
#Print the results:
    #- Lowest Grade
    #- Highest Grade
    #- Sum of Grades
    #- Average
#Print the results in a letter format.
