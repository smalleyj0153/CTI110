#Jacob Smalley
#21 Sep 2024
#P1HW2
#Very basic travel expense budgeter.

print('This is a very basic travel budget calculator')
budget = int(input('What is your starting budget: '))
location = input('Where are you traveling too: ')
gas = int(input('How much in fuel will it cost: '))
room = int(input('How much does your lodging cost: '))
food = int(input('How much for food have you saved: '))
print('\t')
print('---------Trip Budget---------')
print('\t')
print('Location:',location)
print('How much you have saved:',budget)
print('\t')
print('Fuel:',gas)
print('Lodging:',room)
print('Food:',food)
print('\t')
print('Amount left over:',budget-gas-room-food)
print('\t')
print('If you have a negative number you will need to alter your plans')
while True:
    pass
