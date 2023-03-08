MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_resources(order_ingredients):
    """Return True/False, Check if we have enough ingredient to make a selected drink"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"“Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

money = 0
is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml ")
        print(f"Coffee: {resources['coffee']} g ")
        print(f"Money:$ {money} ")
    else:
        drink = MENU[choice]
        if enough_resources(drink['ingredients']):
            payment = process_coin()
            print(f"{choice} will be ready")
            # proceed! 