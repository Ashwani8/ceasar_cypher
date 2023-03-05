# let us make a simple calculator
from art import calculator_logo
print(calculator_logo)
# Add
def add(n1,n2):
    return n1 + n2
# Substract
def subtract(n1, n2):
    return n1- n2
# multiplication 
def multiply(n1, n2):
    return n1 * n2
# divide
def divide(n1, n2):
    if n2 == 0:
        return 
    return n1/n2

# create a dictionary with math symbole as key and corresponsing operations as values
math_operation = {
    # This is clever, we are not using operation(n1,n2), but just a string, (num1,num2) is concocnated later
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}
def calculator():
    """Perform basic math operation +, -, * and /"""
    num1 = int(input("Enter first number?: "))

    for symbol in math_operation:
        print(symbol)
    should_contunue = True
    while should_contunue:
        operation_symbol = input("Pick an operation: ")
        new_number = int(input("What's the next number?: "))
        calculation_function = math_operation[operation_symbol]
        answer = calculation_function(num1, new_number) 
        print(f"{num1} {operation_symbol} {new_number} = {answer}")

        user_decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if user_decision == "y":
            num1 = answer
        elif user_decision == "n" :
            should_contunue = False
            # continue with calculating with new values
            calculator() # recursive operation 
        else:
            print("invalid choice")
            num1 = answer
            

calculator()