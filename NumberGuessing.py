import random

def difficulty(choice):
    if choice == 'easy':
        lives = 10
    else:
        lives = 5

    computer = random.randint(1,100)

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while lives > 0:
        print(f"You have {lives} attempts remaing to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == computer:
            print(f"You got it! The answer was {computer}.")
            return 
        elif guess > computer:
            print("Too high.")
        elif guess < computer:
            print("Too low.")
        lives -= 1
        if lives == 0:
            print("You've run out of guesses, you lose.")
        
    
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty(choice=choice)