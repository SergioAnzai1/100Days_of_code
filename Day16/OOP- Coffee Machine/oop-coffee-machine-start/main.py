from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

continue_buying = True
while continue_buying:
    user = input(f"What would you like? {menu.get_items()}: ")
    if user == "report":
        coffe_maker.report()
        money_machine.report()
    elif user == "off":
        continue_buying = False
        break
    else:
        choice = menu.find_drink(user)
        if coffe_maker.is_resource_sufficient(choice) == True:
            if money_machine.make_payment(choice.cost) == True:
                coffe_maker.make_coffee(choice)

