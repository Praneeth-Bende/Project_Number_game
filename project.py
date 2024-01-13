import random
actual_no = random.randint(1,100)
no_of_attempts=0
print("\"\"\" WELCOME TO THE NUMBER GAME \"\"\"")
print("In this game you have to guess the number with as less number of attempts as possible")
print("Guess the Number? \nHint: Number lies between 1 and 100 - ")
while (no_of_attempts < 10):
    no_of_attempts+=1
    guess=int(input())
    if(guess < actual_no):
        print("Enter a greater number....!")
    elif(guess > actual_no):
        print("Enter a lower number....!")
    else:
        print("KUDOS! YOU GUESSED IT RIGHT IN",no_of_attempts,"ATTEMPTS")
        print("YOU ARE IN TOP",no_of_attempts,"% PEOPLE WHO GUESSED IT RIGHT")
if(no_of_attempts >= 10):
    print("YOU REACHED THE MAXIMUM LIMIT")
    print("The number you missed is",actual_no)