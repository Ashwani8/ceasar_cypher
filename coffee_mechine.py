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
    "water": 1000,
    "milk": 400,
    "coffee": 200,
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
def is_transition_successful(money_received, drink_cost):
    """Return True when payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        # money is outside the scope
        global money 
        money+=drink_cost
        change =  round(money_received - drink_cost, 2)
        print(f" Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredient from the resources"""
    for item in drink_ingredients:
        # reduce the amount used in preparing drink from the resources
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} 😊")
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
            if is_transition_successful(payment,drink["cost"] ):
                # deduct resources
                make_coffee(choice, drink['ingredients'])
                
           