#Jacob Smalley
#7 Nov 2024
#P4HW1
#Extended grade point calculator.


num_scores = int(input('How many scores do you want to enter? '))
scores = []

def get_valid_score():
    while True:
        score = int(input('Enter a score between 0 and 100: '))
        if 0 <= score <= 100:
            return score
        else:
            print('INVALID score entered. Score should be between 0 and 100.')

for _ in range(num_scores):
    score = get_valid_score()
    scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)

average_score = sum(scores) / len(scores)

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Lowest score: ', lowest_score)
print('Scores after dropping lowest: ', scores)
print('Average score: ', average_score)
print('Letter grade: ', grade)

#Pseudocode
#Ask user to enter for number of scores they would like to enter.
#Create a loop to collect the number of scores the user wants to enter.
#Note every time a score is entered, the following should be done
    #Evaluate if the score is valid, it should be between 0 and 100 . 
    #If it is not, notify the user and ask for a VALID score to be entered.
#If score is valid, add the score to a list. Make sure the score list is given an informative name.
#After collecting all the scores. The program is to display the following: (15 points)
#Lowest score entered
#Score List after dropping lowest score
#The average of scores in modified list
#Determine the letter grade for the calculated average and display it to user. (20 points)
