#Jacob Smalley
#20 Oct 2024
#P1HW2
#Basic change calculator.

amount = float(input('Enter the amount of money as a float: $'))
    
change = int(round(amount * 100))

usc = {
        'Dollars': 0,
        'Quarters': 0,
        'Dimes': 0,
        'Nickels': 0,
        'Pennies': 0
    }
if amount == 0:
    print('No Change')    
else:
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
        result.append(f'{count} {coin}')

print("\n".join(result))

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
