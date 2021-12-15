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
    "money": 0,
}


def update_resources(drink):
    resources_remaining = {}
    resources_remaining["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources_remaining["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    else:
        resources_remaining["milk"] = resources["milk"]
    resources_remaining["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    resources_remaining["money"] = 0
    resources_remaining["money"] = resources["money"] + MENU[drink]["cost"]
    return resources_remaining


def resource_check(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print(f"There's not enough water, remaining water: {resources['water']}ml")
        if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print(f"There's not enough coffee, remaining coffee: {resources['coffee']}g")
        if "milk" in MENU[drink]["ingredients"]:
            if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
                print(f"There's not enough milk, remaining milk: {resources['milk']}g")
        make_drink = False
    else:
        make_drink = True
        return make_drink


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {resources['money']}$")


quarters = 0
dimes = 0
nickles = 0
pennies = 0
can_make = True
turn_off = False


while not turn_off:
    input_check = input("What would you like? (espresso/latte/cappuccino, type report or turn off): ")
    if input_check == "report":
        report()
    elif input_check == "turn off":
        turn_off = True
        print("Thank you for using this coffee machine")
    else:
        can_make = resource_check(input_check)
        total_coins = 0
        if can_make:
            while total_coins < MENU[input_check]["cost"]:
                print("Please insert coins")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes ?"))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))
                total_coins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
                if total_coins < MENU[input_check]["cost"]:
                    print("Sorry not enough coins, please add more coins")
            resources = update_resources(input_check)
            print("The machine contains:")
            report()
            print(f"Here is ${round(total_coins - MENU[input_check]['cost'], 2)} change.")
            print(f"Here is your {input_check}. Enjoy!")

