import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
is_on = True


# 1. Print Report
coffee_maker.report()
money_machine.report()

# 2. Check resources sufficient?
while is_on:
    options = menu.get_items()
    choice = input(f"Which menu item would you like to make? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





