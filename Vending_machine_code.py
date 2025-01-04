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
                print("\nInvalid code. Please try again")
# DISPLAY
def display(): #to display the items
    print("\n-----Available items-----")
    for category, items in VMmenu.items():
       print(f"\n{category}:")
       for code, details in items.items():
           print(f" {code}: {details['Item']} - ${details['Price']} (Quantity: {details['quantity']})") 
    print()