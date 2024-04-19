# 🌷 If-Else ⛄
The code for this exercise can be found in `exercises/4-ifelse/`.

You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/4-ifelse
$ python3 {FILE_NAME}.py
```

## Task 4.1: Divisible
**Task file:** `divisible.py`

Write a program that checks the divisibility of different numbers. 

If num is divisible by 4 and 6, print CompClub.
If num is divisible by 4 and not 6, print Comp.
If num is divisible by 6 and not 4, print Club.
If num is not divisible by 6 or 4, print the number.
If num is negative, print “INVALID NUMBER”

Hint: How many if/elif statements do you need?
Hint: How do we ensure our input is an integer?
Hint: Should we use % or / when testing for divisibility?

**Expected output:**
```
$ python3 divisible.py
Please enter a positive number: 12
Compclub 

$ python3 divisible.py
Please enter a positive number: 20
Comp

$ python3 divisible.py
Please enter a positive number: -10
INVALID INTEGER


```
## Task 4.1: Ghibli adventure!
**Task file:** `adventure.py`

Write a program that selects which Ghibli movie character the user would like to accompany on an adventure, and based on their choice.

Your output should look something like this:
```
$ python3 adventure.py

Choose a character for your adventure:

[1] Totoro from My Neighbor Totoro
[2] Chihiro from Spirited Away
[3] Howl from Howl's Moving Castle

Enter the number of your chosen character: 1
"You chose Totoro!”
```

How would we handle cases where the number inputted is not within 1-3?