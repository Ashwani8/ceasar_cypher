import random 
from art import high_low_logo
from art import vs
import high_low_game_data as data # not a good choice as i have to use data.data

from high_low_game_data import data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
 
# data_list = [{
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },]
# 
print(high_low_logo)
print(f"Compare A, {account_a}")
# display score only after first attempt
# initial_score = 0
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
print(f"Compare B, {account_b}")
# Display option B
# print(f"Compare B,{a_followers} ")
# user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
# print(user_choice)
# # if user choice is correct, increase current score, print the corresponding message, 
# # and replace choice A with B, and fetch a new data account for choice a , game continue
# a_option = b_option
# b_option = new_account()
# current_score = 0
# print(f" You're right! Current score {current_score}")
# # if incorrect, print score, and game ends

# print(f"Sorry, that's wrong, Final score {current_score}")