# Zakaria Kortam - 2/15/2023
# Professor Estrada - COMSC 78
# 1. Asks the user for the price and quantity of an item.
# 2. Calculate the discount percent based on qty.
# 3. Calculate the final price using the discount, qty, and unit price.
# 4. Print the results.

import math
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def main():
    price = float(input("What is the price of each item? --> "))
    quantity = int(input("How many items are there? --> "))
    discount = 0

    if quantity > 10.0:
        discount = 0.10
    elif quantity >= 20.0:
        discount = 0.20
    elif quantity >= 50.0:
        disocunt = 0.30
    else: 
        discount = 0
        
    price = round((price*(1-discount)),2)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>> Final Price >>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")
    print("Unit price: " + str(price))
    print("Quantity: " + str(quantity))
    print("Discount: " + str(discount*100))
    print("Total: " + str(price*quantity))
main()