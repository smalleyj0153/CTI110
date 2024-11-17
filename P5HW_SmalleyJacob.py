#Jacob Smalley
#17 Nov 2024
#P5HW
#Math Quiz

import random

def add_quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    correct_answer = num1 + num2
    guess_count = 0

    while True:
        guess = int(input(f'What is {num1} + {num2}? '))
        guess_count += 1

        if guess == correct_answer:
            print('Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses: {guess_count}\n\n')
            break
        elif guess < correct_answer:
            print('Sorry guess is too low.')
        else:
            print('Sorry guess is too high.')

def subtract_quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, num1)
    correct_answer = num1 - num2
    guess_count = 0

    while True:
        guess = int(input(f"What is {num1} - {num2}? "))
        guess_count += 1

        if guess == correct_answer:
            print('Congratulations!!!! Your answer is correct.')
            print(f'Number of guesses: {guess_count}\n')
            break
        elif guess < correct_answer:
            print('Sorry guess is too low.')
        else:
            print('Sorry guess is too high.')


while True:
    print('\nWelcome to Math Quiz!\n')
    print('Main Menu:')
    print('------------------------------')
    print('1. Adding random numbers')
    print('2. Subtracting random numbers')
    print('3. Exit\n')

    choice = input("Please choose one of the menu options: ")

    if choice == '1':
        add_quiz()
    elif choice == '2':
        subtract_quiz()
    elif choice == '3':
        print("Thank you for playing...")
        print('Bye!!')
        break
    else:
        print('You must choose between options 1, 2 or 3.\n')

    play_again = input('Do you want to play again? (yes/no): \n')
    if play_again != "yes":
        print("\nThank you for playing...")
        print('Bye!!')
        break

#Pseudocode
#Write a program that gives simple math quizzes.
#The program should display two random numbers.
#The program should allow the student to enter the answer.
#If the answer is correct, a message of congratulations should be displayed.
#If the answer is incorrect, the program should notify the user if their answer was too low or too high and ask them to guess again. The user will have to continue to guess until they get the right answer.
#The program is to keep track of the number of guesses. Once the user has made a correct guess, the program is to tell them the number of guesses it took to get the right answer
