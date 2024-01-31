def display_available_items(dct):
    print("{:<10}{:<15}{:<15}{:<15}".format('S.No.', 'Item', 'Quanity', 'Cost/Item'))
    for key, value in dct.items():
        print("{:<10}{:<15}{:<15}{:<15}".format(key, value['Item'], value['Quantity'], value['Cost/Item']))

availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)
#create a user define dictionary
my_dict = {}
items = int(input("Enter the number of items:"))

for i in range(items):
    keys = input("Enter the item name: ")
    values = int(input("Enter the quantity: "))
    my_dict[keys] = values
print(my_dict)

for i in my_dict:
    if not availableItems.get(i):
        print("The Item is Not Available")
    else:
        qty = availableItems[i]['Quantity']
        orderQty = my_dict[i]
        if qty < orderQty :
            print("We are out of stock for this item.")
        else:
            availableItems[i]['Quantity'] -= orderQty
            print("Your Order has been placed successfully!")
            
user_cart={}

    

    
