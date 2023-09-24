# TODO1: The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

import main
#TODO Prompt user by asking what coffee would you like. The prompt should show every time action has completed
def user_input_prompt():
    """

    :return: string - type of coffee or report
    """
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    return user_input

# TODO Turn off the coffee machine by entering "off" to the prompt.
def turn_off():
    exit()

def money_input_prompt():
    print(f"Please insert coins.")
    quaters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (quaters, dimes, nickles, pennies)

def user_input_amount(quaters, dimes, nickles, pennies):
    quarter_value = float(quaters * 0.25)
    dime_value = float(dimes * 0.10)
    nickle_value = float(nickles * 0.05)
    pennie_value = float(pennies * 0.01)
    user_money = quarter_value + dime_value + nickle_value + pennie_value
    return user_money


def sufficient_resources (user_input, water, milk, coffee):

    if(user_input == "latte"):
        if (water < 200):
            print(f"Sorry there is not enough water.")
            return False
        elif(milk < 150):
            print(f"Sorry there is not enough milk.")
            return False
        elif(coffee < 24):
            print(f"Sorry there is not enough coffee.")
            return False
    if (user_input == "espresso"):
        if (water < 50):
            print(f"Sorry there is not enough water.")
            return False
        elif (coffee < 18):
            print(f"Sorry there is not enough coffee.")
            return False
    if (user_input == "cappuccino"):
        if (water < 250):
            print(f"Sorry there is not enough water.")
            return False
        elif (milk < 100):
            print(f"Sorry there is not enough milk.")
            return False
        elif (coffee < 24):
            print(f"Sorry there is not enough coffee.")
            return False
    else:
        return True

def coffee_maker():
    money = 0
    water = 300
    milk = 250
    coffee = 100


    while True:
        coffee_choice = user_input_prompt()
        print(f"Your choice is: {coffee_choice}")
        if (coffee_choice == "off"):
            turn_off()
        if coffee_choice == "report":
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
            print(f"Money: {money}")

        elif coffee_choice in main.MENU:
            if (sufficient_resources (coffee_choice, water, milk, coffee)):
                quaters, dimes, nickles, pennies = money_input_prompt()
                user_money = user_input_amount(quaters, dimes, nickles, pennies)
                item_dict = main.MENU
                for coffee_type, data in item_dict.items():
                    if(coffee_type == coffee_choice):
                        if (user_money < data['cost']):
                            print(f"Sorry that's not enough money. Money refunded.")
                        else:
                            money = money + data['cost']
                            if(coffee_choice == "espresso"):
                                water = water - data['ingredients']['water']
                                coffee = coffee - data['ingredients']['coffee']
                            else:
                                water = water - data['ingredients']['water']
                                coffee = coffee - data['ingredients']['coffee']
                                milk = milk - data['ingredients']['milk']
                            change = round(user_money - data['cost'], 2)
                            print(f"Here is ${change} in change.")
                            print(f"Here is your {coffee_choice} ☕️. Enjoy!")
            else:
                print(f"Sorry! There are not enough resources to make {coffee_choice}")
        else:
            print(f"Invalid Choice. Please from espresso, latte, cappuccino or enter 'off' to turn off the mechine.")


coffee_maker()