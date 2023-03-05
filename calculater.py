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
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}
num1 = int(input("Enter first number: "))
num1 = int(input("Enter second number: "))
