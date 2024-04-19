# 👻 Ghost market shopping spree!!🛍️

## Getting Started
All the files you need to edit are in the `ghost_market` directory.

## Task 1: Come one, come all!
### 1.1 welcome()
Welcome our new customer to the ghost market. Print a welcoming welcome message!

**fill the `welcome` function in `welcome.py`**

### 1.2 get_next_customer()
Lets ask the name of our customer!

**fill the `get_next_customer` function in `welcome.py`**

> HINT
> -
> - Use the `input` function

### 1.3 display_catalogue()
Lets show the customer what we have on sale. Display our catalogue to our customer however you'd like! Make it pretty!

**fill the `display_catalogue` function in `welcome.py`**

> HINT
> -
> - use the `CATALOGUE` dictionary from `constants.py`
> - use a `for in` loop (e.g. `for category in CATALOGUE`)
> - for some nice printing, use tabs in your print statements (e.g. `print("\t" + ...)`)

## Task 2: I have great self control (and other lies I tell myself)
### 2.1 add_to_cart()
Lets get buying!

Prompt the customer for an item to buy:
- if it exists in our catalogue, add it to the customer's cart
- otherwise, let the customer know this item does not exist

**fill the `add_to_card` function in `welcome.py`**

> HINT
> -
> - You can use the `is_valid_item()` function from `constants.py` to check if the item exists in the catalogue

### 2.2 remove_from_cart()
Sometimes we realise that we really didn't need that fancy purchase :(

Prompt the customer for an item to remove:
- if it exists in our cart, remove 1 of it
- otherwise, let the customer know this item does not exist

**fill the `remove_from_cart` function in `welcome.py`**

> HINT
> -
> - You can use the Dictionaries `.pop()` method to remove an item from the cart

### 2.3 show_items()
We need to see what our card looks like!

Display the names and quantities of items that the customer
has added to their cart. Also sum up the current total and print it.

Try get this format:

```
Your Cart:
QUANTITY    ITEM
1           Konpeito
2           Herring and Pumpkin Pie
1           Nabeyaki Udon
1           Haku's Onigiri
1           Howl's Bacon and Eggs

Total: $ 67.5
```

> HINT
> -
> - Try use "\t" in your print statements to make it look nice
> - You can use the get_price() function from constants.py to get the price of an item

## Task 3: Wise financial decisions

Expected output (have enough money):
```
== Checkout ==
Enter payment amount: 20
Thank you Bob for shopping with us! ^.^!
Reciept:
Konpeito x3           $0.5
Aji Fry x2            $8.5

TOTAL                 $9.0
PAID                  $20
CHANGE                $11.0
```

Expected output (not enough money):
```
== Checkout ==
Enter payment amount: 2
Sorry, you don't have enough money to buy all the items in your cart! :(
```

### 3.1 print_reciept()
Lets print a reciept to show us how much money we've spent 😲

Given a cart, and how much money the customer paid,
print a reciept of the purchase to console.
Hint: To print in columns, we use '{0:20}  ${1}'.format(variable1, variable2)
    - 0:20 means 20 spaces between 1st column and 2nd column

Optional task: At the same time, create a file named customer_name.txt which contains the receipt.
Example receipt - Jack.txt

### 3.2 checkout()
Lets finally go and spend that precious money of ours!

Prompt the customer to enter their payment amount
- If they have enough money, we print a reciept containing details on our purchase
- If they don't have enough money, let the customer know :'(

> HINT
> -
> Hint: You are expected to use print_reciept() in this function (maybe look at that first!)
