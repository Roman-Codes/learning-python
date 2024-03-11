from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
# menu_item = MenuItem()
coffee_maker: CoffeeMaker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    options = menu.get_items()
    order = input(f'What would you like? {options}: ')
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
