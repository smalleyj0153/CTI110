"""
Jacob Smalley
21 Sep 2024
P1HW2
Basic travel expense budgeter.
"""

print('This program calculates and displays travel expenses')
print('\t')
budget = float(input('Enter budget: '))
print('\t')
location = input('Enter your travel destination: ')
print('\t')
gas = float(input('How much do you think you will spend on gas: '))
print('\t')
room = float(input('Approximately, how much will you need for accomodation/hotel? '))
print('\t')
food = float(input('Last, how much do you need for food? '))
print('\t')
print('-----------Trip Expenses-----------')
print('Location:'.ljust(20),location)
print('Initial Budget:' .ljust(20), f'${budget:.2f}')
print(f'Fuel:' .ljust(20), f'${gas:.2f}')
print(f'Lodging:' .ljust(20), f'${room:.2f}')
print(f'Food:' .ljust(20), f'${food:.2f}')
print('-----------------------------------')
print('\t')
print(f'Remaining Balance: ${budget-gas-room-food:.2f}')
print('\t')
while True:
    pass
