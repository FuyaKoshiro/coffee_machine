from menu import resources, MENU, profit
from art import logo, title

loop = True

welcome = """
    Welcome to the Fuya's Coffee!!

    What would like to order??
    espresso ($1.5) : 0
    latte ($2.5) : 1
    cappuccino ($3.0) : 2
    
    #display resources : 3
    """

r_water = resources["water"]
r_milk = resources["milk"]
r_coffee = resources["coffee"]


def turn_off():
    print("turn off.")
    return False

def report(resources_input):
    print(f"The resources are : \n{resources_input}")
    print(f"The profit is now {profit}.")

    #if sufficiency = True:
        #coin(command_input, menu_input)
        #deduction(command_input, resources_input)
        #enjoy

def check_sufficiency(user_oder_input, m_water, m_milk, m_coffee):
    if m_water > r_water or m_milk > r_milk or m_coffee > r_coffee:
        print("Sorry, we do not have enough resource.")
        return False
    else:
        return True
 
def coin():
    inserted_coin = int(input("How much coin did you insert? : "))
    if inserted_coin < m_cost:
        print("Oops, it is not enough. Refunded.")
        coin()
    elif inserted_coin == m_cost:
        print("Thank you!")
    else:
        refund = inserted_coin - m_cost
        print(f"Here is your change : {refund}.")

def calculate(user_order_input, m_water, m_milk, m_coffee, m_cost, profit, resources):
    water = int(m_water)
    milk = int(m_milk)
    coffee = int(m_coffee)
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    profit += m_cost

def enjoy(logo):
    print(f"Remember to grab your recipet! Thanks! See you soon! \n{logo}")

while loop:
    print(title)
    #input
    command = input(welcome)

    if command == "turn off":
        loop = turn_off()
    elif command == "3":
        report(resources)
    elif command == "0" or command == "1" or command == "2":
        if command == "0":
            user_order = "espresso"
        elif command == "1":
            user_order = "latte"
        else:
            user_order = "cappuccino"

        m_water = MENU[user_order]["ingredients"]["water"]
        m_milk = MENU[user_order]["ingredients"]["milk"]
        m_coffee = MENU[user_order]["ingredients"]["coffee"]
        m_cost = MENU[user_order]["cost"]

        order = check_sufficiency(user_order, m_water, m_milk, m_coffee)

        if order == False:
            loop = False
        else:
            coin()
            calculate(user_order, m_water, m_milk, m_coffee, m_cost, profit, resources)
            enjoy(logo)



    #if command, boolean: off, report, order
        #report()
        #turn_off()
        #order()
            #check_sufficiency(), boolean: sufficiency
                #coin()
                #deduction()
                #enjoy()
