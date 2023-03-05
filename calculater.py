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
num1 = int(input("Enter first number?: "))

for symbol in math_operation:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Enter second number?: "))
calculation_function = math_operation[operation_symbol]
# This concatnate simple text (add/subtract) with (n1,n2) in the line below
answer = calculation_function(num1, num2) 
print(f"{num1} {operation_symbol} {num2} = {answer}")