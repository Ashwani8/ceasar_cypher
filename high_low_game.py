import random 
from art import high_low_logo, vs
# import high_low_game_data as data # not a good choice as i have to use data.data

from high_low_game_data import data
score = 0
def format_data(account):
   """Format the account data and convert it into printable format"""
   account_name = account['name']
   account_discr = account['description']
   account_country = account['country']
   account_summary = f" {account_name}, {account_discr}, {account_country} "
   return account_summary
def check_answer(guess, a_counts, b_counts):
    """ Takes the user_guess and follower's count and return if they got it right"""
    if user_guess == 'a' and a_counts > b_counts:
        return True
    elif user_guess == 'b' and b_counts > a_counts:
        return True
    else:
        return False

print(high_low_logo)
account_a = random.choice(data)
game_should_continue = True # to have game continue
while game_should_continue:
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    a_follower_count =int(account_a['follower_count'])
    b_follower_count = int(account_b['follower_count'])

    print(f"Compare A, {format_data(account_a)}")
    # output vs logo 
    print(vs)
    print(f"Compare B, {format_data(account_b)}")
    # user makes a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # clean screen
    print("\033c", end='')
    #print logo again 
    print(high_low_logo)
    # check user's guess! if the guess is correct, game continue, otherwise it ends
    answer = check_answer(guess= user_guess, a_counts= a_follower_count, b_counts= b_follower_count)
    
    if answer:
        score +=1
        print(f" You're right! Current score {score}")
        account_a = account_b
        a_follower_count = b_follower_count
        game_should_continue = True
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final score {score}")

