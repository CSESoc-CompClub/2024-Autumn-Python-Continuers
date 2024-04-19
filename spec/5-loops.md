# 💫 Looooops 😵‍💫
The code for this exercise can be found in `exercises/5-loops/`.

You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/5-loops
$ python3 {FILE_NAME}.py
```

## Task 5.1: Counter
**Task file:** `counter.py`

Given a number, print all the numbers from 0 to your number.
For example:
-> if 'num' is 5, then we print 0, 1, 2, 3, 4, 5
-> if 'num' is -5, then we print 0, -1, -2, -3, -4, -5

**Expected output:**
```
$ python3 counter.py
Enter your number: -5
0
-1
-2
-3
-4
-5

$ python3 counter.py
Enter your number: 5
0
1
2
3
4
5

$ python3 counter.py
Enter your number: 0
0
```

## Task 5.2: Guess the Number
**Task file:** `guess_num.py`

Write a program that asks the user to input a guess, UNTIL their guess matches the 'number' variable. You should also tell the user if their input was too high or too low.

Hint: Check how the value of 'number' compares to their input 'n'

**Expected output:**
```
$ python3 guess_num.py
Your guess: 1
Too low!
Your guess: 20
Too high!
Your guess: 5
Too high!
Your guess: 3
Too high!
Your guess: 2
You got it! The number was 2
```
