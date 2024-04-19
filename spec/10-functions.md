# 📕 FUNctions 🌟
The code for this exercise can be found in `exercises/10-functions/`.

You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/10-functions
$ python3 {FILE_NAME}.py
```

## Task 10.1: Fruit Stock
**Task file:** `fruit_stock.py`
Welcome to your new job as an (unpaid) fruit stocker!
This program contains 5 functions, 1 of which has already been completed for you.
Follow the tasks in order and follow the comments to see what to do.
Remove "pass" from the functions and if statements when they are implemented.


**Expected output:**
```
$ python3 fruit_stock.py

Welcome to the Fruit Stock Manager!
There are 10 apples, 10 bananas and 10 oranges in stock.

--------------------------------------------------------
Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: add
How many do you want to add? 4
Which fruit do you want to add? apples


Successfully added 4 apples to the stock.
There are 14 apples, 10 bananas and 10 oranges in stock.

--------------------------------------------------------
Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: add
How many do you want to add? 5
Which fruit do you want to add? pears


Invalid fruit type. Please try again.
--------------------------------------------------------
Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: remove
How many do you want to remove? 4
Which fruit do you want to remove? oranges


Successfully removed 4 oranges from the stock.
There are 14 apples, 10 bananas and 6 oranges in stock.

--------------------------------------------------------
Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: remove
How many do you want to remove? 20
Which fruit do you want to remove? oranges


Not enough oranges in stock. Please try again.
There are 14 apples, 10 bananas and 6 oranges in stock.

--------------------------------------------------------
Enter 'add' to add fruit to the stock, 'remove' to remove fruit from the stock, or 'stop' to exit: 
```