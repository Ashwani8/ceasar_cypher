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
    if user_guess == 'b' and b_counts > a_counts:
        return True
    else:
        return False

print(high_low_logo)
account_a = random.choice(data)
answer = True 
while answer:
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    a_follower_count =int(account_a['follower_count'])
    b_follower_count = int(account_b['follower_count'])

    print(f"Compare A, {format_data(account_a)}")
# display score only after first attempt

# define a function to randomly select from data 
# for item in data:
#     print (item)
# number_of_followers = 0
# option_a_dic = data_list[randint(0,3)]
# a_option = f" {option_a_dic['name']}, {option_a_dic['description']}, {option_a_dic['country']}"
# a_followers = int(option_a_dic['follower_count'])
# def new_account():
    
#     account_dic = data_list[randint(0,3)]
#     account = f" {account_dic['name']}, {account_dic['description']}, {account_dic['country']}"
#     account_follower = int(account_dic['follower_count'])
#     return account, account_follower
# a_followers = int(option_a_dic['follower_count'])
# b_option = "option"
# b_followers = 5
# print(f"Compare A, {a_option}")
# display option A, ask for input A or B, but accept both lower and upper case 
#print(f" ")
# any other answer is treated as incorrect

    print(vs)
    print(f"Compare B, {format_data(account_b)}")
    # Display option B
    # print(f"Compare B,{a_followers} ")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = check_answer(guess= user_guess, a_counts= a_follower_count, b_counts= b_follower_count)
    if answer:
        score +=1
        print(f" You're right! Current score {score}")
        account_a = account_b
        a_follower_count = b_follower_count
    else:
        print(f"Sorry, that's wrong, Final score {score}")

# print(user_choice)
# # if user choice is correct, increase current score, print the corresponding message, 
# # and replace choice A with B, and fetch a new data account for choice a , game continue
# a_option = b_option
# b_option = new_account()


# # if incorrect, print score, and game ends

