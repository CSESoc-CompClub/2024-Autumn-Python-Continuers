"""
Checkout our order!

This is your third task of the project. A useful function from constants.py has been imported for you, if you
want to use other functions you can import them in a similar manner.
An example cart and customer have been given to you to test the functions. Scroll to the bottom to see expected output.
"""

from constants import get_price

example_cart = {"Konpeito": 3, "Aji Fry": 2}
example_customer = "Bob"


def checkout(name, cart):
    """
    Prompt the customer to enter their payment amount
        -> If they have enough money, we print a reciept containing details on our purchase
        -> If they don't have enough money, let the customer know :'(
    Hint: You are expected to use print_reciept() in this function (maybe look at that first!)
    """
    # TODO: IMPLEMENT THIS FUNCTION
    pass

    # Solution
    print("== Checkout ==")
    payment = input("Enter payment amount: ")

    cost = 0
    for item in cart:
        cost += get_price(item)

    if float(payment) < float(cost):
        print(
            "Sorry, you don't have enough money to buy all the items in your cart! :("
        )
    else:
        print_reciept(name, cart, payment)


def print_reciept(name, cart, paid_amount):
    """
    Given a cart, and how much money the customer paid,
    print a reciept of the purchase to console.
    Hint: To print in columns, we use '{0:20}  ${1}'.format(variable1, variable2)
      - 0:20 means 20 spaces between 1st column and 2nd column

    Optional task: At the same time, create a file named customer_name.txt which contains the receipt.
    Example receipt - Jack.txt
    """
    # TODO: IMPLEMENT THIS FUNCTION
    pass

    # Solution
    total_cost = 0
    print("Thank you " + name + " for shopping with us! ^.^!")
    print("Reciept:")

    f = open(f"{name}.txt", "a")
    f.write("")
    for item in cart:
        item_details = item + " x" + str(cart[item])
        cost = get_price(item)
        line = "{0:20}  ${1}".format(item_details, cost)
        f.write(line + "\n")
        print(line)
        total_cost += float(cost)

    f.write("\n{0:20}  ${1}\n".format("TOTAL", total_cost))
    f.write("{0:20}  ${1}\n".format("PAID", paid_amount))
    print("\n{0:20}  ${1}".format("TOTAL", total_cost))
    print("{0:20}  ${1}".format("PAID", paid_amount))

    change = float(paid_amount) - float(total_cost)
    f.write("{0:20}  ${1}".format("CHANGE", change))
    print("{0:20}  ${1}".format("CHANGE", change))


""" Expected output (have enough money):
== Checkout ==
Enter payment amount: 20
Thank you Bob for shopping with us! ^.^!
Reciept:
Konpeito x3           $0.5
Aji Fry x2            $8.5

TOTAL                 $9.0
PAID                  $20
CHANGE                $11.0
"""

""" Expected output (not enough money):
== Checkout ==
Enter payment amount: 2
Sorry, you don't have enough money to buy all the items in your cart! :(
"""

# To test your functions, uncomment below:
# checkout(example_customer, example_cart)