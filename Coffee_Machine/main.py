machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

machine_money = 0

money_is_ok = True


def verify_money():
    global machine_money, money_is_ok
    price = 0
    if customer_choice.lower() == 'espresso':
        price = 1.5
    elif customer_choice.lower() == 'latte':
        price = 2.5
    elif customer_choice.lower() == 'cappuccino':
        price = 3.0
    print(f"The cost of {customer_choice} is ${price} \nPlease insert coins")

    quarters_inserted = int(input("How many quarters? "))
    dimes_inserted = int(input("How many dimes? "))
    nickles_inserted = int(input("How many nickles? "))
    pennies_inserted = int(input("How many pennies? "))

    total_money = quarters * quarters_inserted + dimes * dimes_inserted + nickles * nickles_inserted + pennies * pennies_inserted
    print(f"The total money you gave is ${total_money}")

    if customer_choice.lower() == 'espresso':
        if total_money > 1.5:
            print(f"Here is your exchange: ${(total_money - 1.5)}")
            machine_money += 1.5
            print("Enjoy your espresso! ☕")
        elif total_money < 1.5:
            print(f"Sorry, you dont have enough money.")
            money_is_ok = False
        else:
            print("You offered the exact amount")
            machine_money += 1.5
            print("Enjoy your espresso! ☕")

    elif customer_choice.lower() == 'latte':
        if total_money > 2.5:
            print(f"Here is your exchange: ${(total_money - 2.5)}")
            machine_money += 2.5
            print("Enjoy your latte! ☕")
        elif total_money < 2.5:
            print(f"Sorry, you dont have enough money.")
            money_is_ok = False
        else:
            print("You offered the exact amount")
            machine_money += 2.5
            print("Enjoy your latte! ☕")

    elif customer_choice.lower() == 'cappuccino':
        if total_money > 3.0:
            print(f"Here is your exchange: ${(total_money - 3.0)}")
            machine_money += 3.0
            print("Enjoy your cappuccino! ☕")
        elif total_money < 3.0:
            print(f"Sorry, you dont have enough money.")
            money_is_ok = False
        else:
            print("You offered the exact amount")
            machine_money += 3.0
            print("Enjoy your cappuccino! ☕")


def verify_espresso():
    global money_is_ok
    if machine_resources['water'] >= 50 and machine_resources['coffee'] >= 18:
        print("Okay, there are enough resources in the machine for this.")
        verify_money()
        machine_resources['water'] -= 50
        machine_resources['coffee'] -= 18
    else:
        print("Sorry, we don´t have enough resources for this")


def verify_latte():
    if machine_resources['water'] >= 200 and machine_resources['milk'] >= 150 and machine_resources['coffee'] >= 24:
        print("Okay, there are enough resources in the machine for this.")
        verify_money()
        machine_resources['water'] -= 200
        machine_resources['milk'] -= 150
        machine_resources['coffee'] -= 24
    else:
        print("Sorry, we don´t have enough resources for this")


def verify_cappuccino():
    if machine_resources['water'] >= 250 and machine_resources['milk'] >= 100 and machine_resources['coffee'] >= 24:
        print("Okay, there are enough resources in the machine for this.")
        verify_money()
        machine_resources['water'] -= 250
        machine_resources['milk'] -= 100
        machine_resources['coffee'] -= 24
    else:
        print("Sorry, we don´t have enough resources for this")


coffee_machine = True
while coffee_machine:
    from art import logo

    print(logo)
    customer_choice = input("Hello, dear customer!\n"
                            "What would you like: an espresso, a latte or a cappuccino? \n"
                            "(You can also ask for a machine report, if you wish) \n")
    if customer_choice.lower() == 'report':
        print(f"Water: {machine_resources['water']}\n"
              f"Milk: {machine_resources['milk']}\n"
              f"Coffee: {machine_resources['coffee']}\n"
              f"Money: ${machine_money}")

    elif customer_choice.lower() == 'espresso':
        verify_espresso()
    elif customer_choice.lower() == 'latte':
        verify_latte()
    elif customer_choice.lower() == 'cappuccino':
        verify_cappuccino()
    else:
        print("\nWrong input")

    want_another = input("Do you wish for another hot beverage?\n")
    if want_another.lower() == "no":
        print("\nThank you, have a good day!")
        coffee_machine = False
