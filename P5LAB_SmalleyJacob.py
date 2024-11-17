#Jacob Smalley
#16 Nov 2024
#P5LAB
#Self-checkout simulation.

import random

def disperse_change(amount):
    change = int(round(amount * 100))
    usc = {
        'Dollars': 0,
        'Quarters': 0,
        'Dimes': 0,
        'Nickels': 0,
        'Pennies': 0
    }
    if change == 0:
        print("No Change")
        return []
    while change > 0:
        if change >= 100:
            usc['Dollars'] += 1
            change -= 100
        elif change >= 25:
            usc['Quarters'] += 1
            change -= 25
        elif change >= 10:
            usc['Dimes'] += 1
            change -= 10
        elif change >= 5:
            usc['Nickels'] += 1
            change -= 5
        else:
            usc['Pennies'] += 1
            change -= 1
    result = []
    for coin, count in usc.items():
        if count > 0:
            result.append(f"{count} {coin}")

    return result


total_purchase = float(input('You owe $'))
amount_paid = float(input('How much cash will you put in the self-checkout? $'))

change_owed = round(amount_paid - total_purchase, 2)

if change_owed < 0:
    print('Error: The amount paid is less than the total purchase.')
else:
    print(f'Change is: ${change_owed:.2f}\n')
    result = disperse_change(change_owed)
    if result:
        print('\n'.join(result))

while True:
    pass

#usc means US currency

#Pseudocode
#Ask user for a monetary amount to be broken down into its change.
#Convert the input amount to pennies by calculating * 100.
#Make a dictionary to store the coin count of each coin amount.
#Make a no change statement.
#Calculate the change into dollars, quarters, dimes, nickles, and pennies.
#Print the output.
