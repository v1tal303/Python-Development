from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
run = True

while run:
    print(menu.get_items())
    choice = input("What would you like? (espresso/latte/cappuccino) or off or report: ")
    if choice == "off":
        print("Thank you for using the coffee machine")
        run = False
    elif choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            print(f"The drink costs {drink.cost}")
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
