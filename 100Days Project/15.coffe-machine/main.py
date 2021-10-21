from data import resources, MENU


# Show report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# check if there are enough resources to make that drink
def check_ingredients(choose):
    for key in resources:
        if resources[key] < MENU[choose]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
        return True


# Let user input and sum the coins
def insert_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return value


# Check that the user has inserted enough money to purchase.If has inserted too much money, offer change.
def check_money(value, choose):
    cost = MENU[choose]["cost"]
    if value >= cost:
        print(f"Here is ${round(value - cost, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# deducted the ingredients to make the drink, add profit, give coffee
def make_coffee(choose, total_money):
    for key in MENU[choose]["ingredients"]:
        resources[key] -= MENU[choose]["ingredients"][key]
    total_money += MENU[choose]["cost"]
    print(f"Here is your {choose} ☕. Enjoy!")
    return total_money


coffee_machine_working = True
money = 0

while coffee_machine_working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        coffee_machine_working = False
    elif user_input == "report":
        report()
    else:
        if check_ingredients(user_input):
            user_coins = insert_coins()
            if check_money(user_coins, user_input):
                money = make_coffee(user_input, money)
