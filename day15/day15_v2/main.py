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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
'''
1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

 - Use a infinite while loop to accomplish  i.e. while True
'''


def is_resources_sufficient(ingredients):
    '''
    :param drink_choice: ingredients
    :return: True or False if the resources are sufficient by comparing with the required ingredients
    '''
    is_sufficient = True
    for item in ingredients:
        if resources[item] < (ingredients[item]):
            print(f"Sorry there is not enough {item}.")
            is_sufficient = False
    else:
        return is_sufficient


def process_coins():
    """
    :return: Total amount of money entered by the user up to 2 decimal places.
    """
    total = 0
    print(f"Please insert coins.")
    total = total + int(input("how many quaters?: ")) * 0.25
    total = total + int(input("how many dimes?: ")) * 0.10
    total = total + int(input("how many nickles?: ")) * 0.05
    total = total + int(input("how many pennies?: ")) * 0.01
    return round(total, 2)


def is_transaction_successful(user_payment, cost):
    """

    :param user_payment: The amount of money inputted by the user
    :param cost: Cost of the coffee as in the Menu
    :return: True if the payment is accepted otherwise it returns false when the funds are insufficient.
    """

    change = 0
    global money
    if (user_payment >= cost):
        money = money + cost
        change = round(user_payment - cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(ingredients):
    for items in ingredients:
        resources[items] = resources[items] - ingredients[items]
    print(f"Here is your {user_input}☕️. Enjoy!")


is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if (user_input == 'off'):
        is_on = False
    elif (user_input == 'report'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    else:
        drink = MENU[user_input]
        ingredients = drink['ingredients']
        cost = drink['cost']
        '''
        for making the coffee we should sufficient ingredients and sufficient amount of funds  
        '''
        if is_resources_sufficient(ingredients):
            user_payment = process_coins()
            if is_transaction_successful(user_payment, cost):
               make_coffee(ingredients)
