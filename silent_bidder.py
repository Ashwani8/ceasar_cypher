from art import auctionlogo
print(auctionlogo)
bidder_dictionary = {}   
more_bidder =  True
while more_bidder:
  name = input("What is your name?\n")
  amount = int(input("What is your bid? $"))
  bidder_dictionary[name] = amount
  user = input("Are there any more users? please type 'yes' or 'no'.\n ")
  if user == 'yes' :
    print("\033c", end='')

  elif user == "no" :
    more_bidder = False
    #print(bidder_dictionary)
    max_bid = 0
    winner = ""
    for name in bidder_dictionary:
      
      bid = bidder_dictionary[name]
      if bid > max_bid:
        max_bid = bid
        winner = name
    print("\033c", end='')
    print(f"{winner} wins the bid with ${max_bid}.")
  