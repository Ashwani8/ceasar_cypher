#This program checks if the given year is leap year or not
# a leap year is divisible by 4, if divisible by 100 it must also be divisble by 400 otherise its not a leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap Year.")       
else :
    print("Not leap year.")
