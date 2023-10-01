from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    drinks_on_menu = menu.get_items()
    # print(f"What would you like? ({drinks_on_menu}): ")
    user_input = input(f"What would you like? ({drinks_on_menu}): ")

    # Turn off the Coffee Machine by entering "off" to the prompt.
    if (user_input == 'off'):
        is_on = False
    # Print a report
    elif(user_input =='report'):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        # ingredients = drink.ingredients
        cost = drink.cost
        # check the resources to make the drink and  check the money required to make the drink
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
            coffee_maker.make_coffee(drink)
