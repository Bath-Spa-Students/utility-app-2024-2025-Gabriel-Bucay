#Main menu of Vending machine
VMmenu = {
    "Snacks":{
        "S1": {"Item": "Lays", "Price": 3.00, "quantity": 10},
        "S2": {"Item": "Cheetos", "Price": 3.50, "quantity": 10},
        "S3": {"Item": "Doritos", "Price": 4.00, "quantity": 10},
        "S4": {"Item": "Pringles", "Price": 5.00, "quantity": 10},
        "S5": {"Item": "Ruffles", "Price": 2.50, "quantity": 10},
        "S6": {"Item": "Nuts", "Price": 5.50, "quantity": 10},
    },
    "Drinks":{
        "D1": {"Item": "Water", "Price": 1.00, "quantity": 10},
        "D2": {"Item": "Pepsi", "Price": 4.50, "quantity": 10},
        "D3": {"Item": "Coke", "Price": 5.00, "quantity": 10},
        "D4": {"Item": "Mogu-mogu", "Price": 6.00, "quantity": 10},
        "D5": {"Item": "Red bull", "Price": 6.00, "quantity": 10},
        "D6": {"Item": "Orange juice", "Price": 2.00, "quantity": 10},
    },
    "Sweets":{
        "SW1": {"Item": "Kit-kat", "Price": 2.50, "quantity": 10},
        "SW2": {"Item": "Snickers", "Price": 3.00, "quantity": 10},
        "SW3": {"Item": "Hersheys", "Price": 4.00, "quantity": 10},
        "SW4": {"Item": "Mars", "Price": 2.00, "quantity": 10},
        "SW5": {"Item": "Reeches", "Price": 5.00, "quantity": 10},
        "SW6": {"Item": "M&Ms", "Price": 4.50, "quantity": 10},
    },
}   

 # DISPLAY
def display(): #to display the items
    print("\n-----Available items-----")
    for category, items in VMmenu.items():
       print(f"\n{category}:")
       for code, details in items.items():
           print(f" {code}: {details['Item']} - ${details['Price']} (Quantity: {details['quantity']})") 
    print()
#ITEM HANDLING
def IH(): #item handler
    query = input("Please enter the ITEM CODE of the item you want to purchase").upper()
    ifind = False
    for category, items in VMmenu.items():
        if query in items:
            item = items[query]
            ifind = True
            if item["quantity"] > 0:
                print(f"\nGetting your item{item['item']}")
                item['quantity'] -= 1
            else:
                print("\nApologies, this item is no longer available.")
                break
            if not ifind:
                print("\nInvalide code. Please try again")

#MONEY MANAGER
def money_manager(price): 
    """Manage money input and return change.""" 
    sufficient_amount = False 
    while not sufficient_amount: # loop to make sure proper price is given
        user_input = input(f"Please insert ${price}: ") 
        try:
            money_in = float(user_input)
            if money_in >= price:
                change = round(money_in - price, 2)
                print(f"Your change amount is ${change}")
                sufficient_amount = True
            else:
                print("Insufficient amount payed. Please pay full.")
        except ValueError:
            print("Invalid input. Please insert money in numerical forms.")
    
#main program
def VM_main_program():
    while True:
        print("\n------- My Vending Machine -------")
        print("1. Items")
        print("2. Picked Items")
        print("3. Exit")
        picked = input("Please select an option (1-3):")
#if else statements to manage the interface and "buttons"
        if picked == '1': # 1st option
            display()
        elif picked == '2': # 2nd option 
            display()
            num = input("Please enter the number of the item you want: ").upper()
            ifind = False

            for category, items in VMmenu.items(): #item counter for product in stock
                if num in items:
                    items = items[num]
                    ifind = True
                    if items["quantity"] > 0:
                        money_manager(items["Price"])
                        print(f"\nDispensing your {items['Item']}")
                        items["quantity"] -= 1
                    else:
                        print("\nSorry, this item is out of stock unfortunately.")
                    break
            if not ifind:
                    print("\nInvalid code. Please try again")
        elif picked == '3': #3rd option 
            print("THANK YOUR FOR USING THIS VENDING MACHINE. HAVE A NICE LIFE")
            break
        else:
            print("Please select valid option.")
#run the whole program 
VM_main_program()