#Sample solution to the Fruit Stock exercise

def addToStock(fruitStock, fruitType, quantity):
    fruitStock[fruitType] += quantity
    print("Successfully added " + str(quantity) + " " + fruitType + " to the stock.")

def removeFromStock(fruitStock, fruitType, quantity):
    if fruitStock[fruitType] < quantity:
        print("Not enough " + fruitType + " in stock. Please try again.")
        return
    fruitStock[fruitType] -= quantity
    print("Successfully removed " + str(quantity) + " " + fruitType + " from the stock.")

def checkValidInput(fruitStock, fruitType, quantity):
    if not quantity.isdigit():
        print("Quantity has to be a integer. Please try again.")
        return False
    quantity = int(quantity)
    if quantity <= 0:
        print("Quantity cannot be less than or equal to 0. Please try again.")
        return False
    if fruitType not in fruitStock:
        print("Invalid fruit type. Please try again.")
        return False
    return True

def printStock(fruitStock):
    print("There are " + str(fruitStock['apples']) + " apples, " + 
          str(fruitStock['bananas']) + " bananas and " + str(fruitStock['oranges']) + " oranges in stock.\n")

def main():
    fruitStock = {'apples': 10, 'bananas': 10, 'oranges': 10}
    print("Welcome to the Fruit Stock Manager!")
    printStock(fruitStock)

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

        if not checkValidInput(fruitStock, fruitType, quantity):
            continue

        quantity = int(quantity)

        if action == 'add':
            addToStock(fruitStock, fruitType, quantity)
        elif action == 'remove':
            removeFromStock(fruitStock, fruitType, quantity)

        printStock(fruitStock)
        
    print("Exiting Fruit Stock Manager...")
        
main()