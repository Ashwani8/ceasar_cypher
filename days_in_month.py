#This program checks if the given year is leap year or not
# a leap year is divisible by 4, if divisible by 100 it must also be divisble by 400 otherise its not a leap year
def is_leap(year):
    """This function return True if the year is a leap year"""
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                #print("Leap Year.")
                return True
            else:
                #print("Not leap year.")
                return False
        else:
            #print("Leap Year.")       
            return True
    else :
        #print("Not leap year.")
        return False

def days_in_month(year, month):
    """ This function return days in a given month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "invalid month"
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
        
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)