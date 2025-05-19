#program to check if the user's guessed number and the computer generated number is the same. 
#constraint: number is between 1 and 10. 

import random  #library for random number in python

computer_number = random.randint(1,10)  #computer generates a random number between 1-10

while True:          #keeps running until the correct answer is guessed
    user_guess = int(input("Guess a number between 1-10"))   #user guesses a number between 1-10
    
    def guess_the_number(user_guess, computer_number):  #defining the function
        if user_guess == computer_number:
            print(f"You got it right! The number was {computer_number}")
            return True  #same number is guessed by user #break is only used for 'for/while' loops!!!!
        elif user_guess > computer_number:
            print("Guess Lower!")   #number guessed by user is higher than the computer generated number
        else:
            print("Guess Higher!")   #number guessed by user is lower than computer generated number
    result = guess_the_number(user_guess, computer_number)  #calling the function

    if result:  #stops the loop once the correct value is entered!
        break

     






