"""
Jacob Smalley
6 Oct 2024
P2LAB2
Python dictionary assignment.
"""

mpgdict = {
    'Camaro': '18.21',
    'Prius': '52.36',
    'Model S': '110',
    'Silverado': '26'
}
for key in mpgdict.keys():
    print(key)

car_model = input('Enter a vehicle to see its mpg: ')

print(f'The {car_model} gets {mpgdict[car_model]} mpg.')

drive = float(input(f'How many miles will you drive the {car_model}? '))

estimated_gallons = drive / float(mpgdict[car_model])

print(f'{estimated_gallons:.2f} gallon(s) of gas are needed to drive the {car_model} {drive} miles.')

while True:
    pass
