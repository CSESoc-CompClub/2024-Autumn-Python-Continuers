"""
Welcome to your new job as an (unpaid) fruit stocker!
This program contains 5 functions, 1 of which has already been completed for you.
Follow the tasks in order and follow the comments to see what to do.
Remove "pass" from the functions and if statements when they are implemented.
"""

def printStock(fruitStock):
    # TODO - TASK 1: Complete this function!
    # When called, this function should print the number of each fruit in the dictionary
    pass

def checkValidInput(fruitStock, fruitType, quantity):
    # TODO - TASK 2: Complete this function!
    # Returns True if an input is valid, and False if it is invalid
    # An input is invalid if:
    # - The quantity is not an integer
    # - The quantity is less than or equal to 0
    # - The fruit type is not in the dictionary
    pass

# This function has already been completed for you :)
def addToStock(fruitStock, fruitType, quantity):
    fruitStock[fruitType] += quantity
    print("Successfully added " + str(quantity) + " " + fruitType + " to the stock.")

#TODO - Task 4: Create the removeFromStock function 
# If there is not enough stock, then the function should print that there is not enough stock
# Otherwise, remove that quantity of fruit from its stock
# Hint: it's similar to the addToStock function


def main():
    fruitStock = {'apples': 10, 'bananas': 10, 'oranges': 10}
    print("Welcome to the Fruit Stock Manager!")
    
    # TODO - TASK 1: Complete the printStock function and call it here
    
    while True:
        print("--------------------------------------------------------")
        action = input("Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: ")
        if action == 'stop':
            break

        # if action not in ['add', 'remove']:
        if action != 'add' and action != 'remove':
            print("Invalid action. Please try again.")
            continue
            
        quantity = input("How many do you want to " + action + "? ")
        fruitType = input("Which fruit do you want to " + action + "? ")
        print("\n")
        
        # TODO - TASK 2: Complete the checkValidInput function
        if not checkValidInput(fruitStock, fruitType, quantity):
            continue
        
        quantity = int(quantity)
        
        if action == 'add':
            #TODO - TASK 3: Call the appropriate function here
            pass
        elif action == 'remove':
            #TODO - TASK 4: Create the removeFromStock function and call it here
            pass
        
        #TODO - Task 5: Print out the stock of each fruit again :D
        
    print("Exiting Fruit Stock Manager...")
        
main()