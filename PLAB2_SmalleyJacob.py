#Jacob Smalley
#27 Oct 2024
#P3HW2_Salary
#Basic calculator.

while True:
    num = int(input("Enter a number between 0 and 12: "))
    if num < 0:
        print("Negative numbers are not accepted.")
    else:
        for i in range(0, 13):
            print(f"{num} x {i} = {num * i}")

    play_again = input("Do you want to try again? (y/n): ")
    if play_again.lower() != 'y':
        print('Thank you for playing!')
        break

#Pseudocode
#Make statement while true.
#Ask for a user entered number between 1 and 12.
#Multiply the number throughout the number range of 1 - 12.
#Ask user if they want to try again.
#If yes they start over.
#If no they are given a goodbye message and the program ends.
