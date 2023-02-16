# Zakaria Kortam - 2/15/2023
# Professor Estrada - COMSC 78
# 1. Asks the user for the number of units through the get_units() function. No negatives.
# 2. Calculate the cost of plan A and plan B.
# 3. Compare them and declare which is a better price.
# 4. Print the results.

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def get_units():
    return int(input("Please state the number of units: "))

def calculate_cost(units,baseCost,baseLimit,costPerUnit):
    a = 0
    if units < baseLimit:
        a = baseCost
    else:
        a = baseCost + costPerUnit*(units - baseLimit)
    return round(a,2)

def main():
    units = -1
    while(units < 0):
        if(units < 0):
            units = get_units()
            if(units < 0):
                print("units must be 0 or greater.")
    a = calculate_cost(units,9.38,65,0.045)
    b = calculate_cost(units,8.57,50,0.052)
    
    cheaper = "A"
    if(a>b):
        cheaper = "B"
    else:
        cheaper = "A"
        
    print("Plan A: $" + str(a))
    print("Plan B: $" + str(b))
    print("Plan "+cheaper+" is cheaper.")
    # If format were to be used. I used round. --> print("Plan A:{:.2f}".format(a))
    
main()
    