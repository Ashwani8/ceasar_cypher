import random
from art import guessing_number_logo
print(guessing_number_logo)
print("Welcome to the number Guessing Game!")
# genrate a random number
is_game_over = False
attempt_remained = 10 
level = input("I'm thinking of a number between 1 and 100. \n Choose a Difficulty level. Type 'easy' or 'hard': ")
if level == 'hard':
    attempt_remained = 5
random_number = random.randint(1,101)

while attempt_remained > 0 and is_game_over ==False :
    
    user_guess = int(input(f"You have {attempt_remained} attempts remaining to guess the number. \nMake a Guess: "))
    attempt_remained += -1
# compare user's guess with the random number
    if user_guess < random_number:
        if attempt_remained  == 0:
            print(" You have run out of guesses, you lose!")
        else:
            print(f"Too Low, Guess Again")
    
    elif user_guess > random_number:
        if attempt_remained  == 0:
            print(" You have run out of guesses, you lose!")
        else:
            print("Too High, Guess Again")
    elif user_guess == random_number:
        is_game_over = True
        print(f"You got it, the answer was {random_number}.")
    
