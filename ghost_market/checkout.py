"""
Checkout our order!

This is your third task of the project. A useful function from constants.py has been imported for you, if you
want to use other functions you can import them in a similar manner.
An example cart and customer have been given to you to test the functions. Scroll to the bottom to see expected output.
"""

from constants import get_price

example_cart = {"Konpeito": 3, "Aji Fry": 2}
example_customer = "Bob"


def print_reciept(name, cart, paid_amount):
    # TODO: Write your code here
    pass


def checkout(name, cart):
    # TODO: Write your code here
    pass


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
