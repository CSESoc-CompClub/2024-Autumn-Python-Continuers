# 👻 Ghost market shopping spree!!🛍️

## Getting Started
- All the ghost market files are in the `ghost_market/` folder
- To run ghost market, use `python ghost_market/ghost_market.py`

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

### 2.3 Challenge: show_items()
We need to see what our cart looks like!

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
