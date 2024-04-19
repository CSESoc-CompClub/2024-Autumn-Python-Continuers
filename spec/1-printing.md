# 🖨 Printing 👋
The code for this exercise can be found in `exercises/exercises.py`.

You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/1-printing
$ python3 hello_world.py
```

## Task 1.1: Hello world!
Welcome to the CompClub Autumn workshops! As is tradition, let us say hello to the world!

Task: fill out `print_hello_world()` so that we print out the phrase

```
Hello world!
```

## Task 1.2: Maths
To prepare us for the future, let's do some basic maths. We can use python as a calculator!

Task: Fill out `print_maths()` to print out the value of the following:
  a) Add the numbers 123 and 456 (Done for you!)
  b) Add the numbers 4373000 and 9221250
  c) Subtract 2165625 from 4375000
  d) Multiply 42537 by 29530
  e) Divide 52305765 by 4237
  f) Integer part of 520537 divided by 500
  g) EXTRA: There is another maths operator '%', see if you can figure out what it does!

HINT: try print(x % 4), for x = 0, 1, ..., 10.

## Task 1.3: Facts
One cool thing we can do is print the value of a variable. Set values of the variables, and the print function will fill out the information for you!

Fill out `print_facts()` to print out some facts about yourself!

## Task 1.4: Printing ascii art!
One more thing. Sometimes, we need to print a lot of things over many lines. One example is ascii art! We can do this by using three quotation marks at the beginning and end of what we want to print.

Here is an example:
```
def print_multiple():
    print(
        """
              |\\
              | \\
              |  \\
              |   )
              |  /  
             _|.'
           .' |
          /   |_.
         |  .'|  '.
          \ * |   /
           '._|_.'
              |
            * |
            '.'
        """
    )
```
Head on over to https://www.asciiart.eu/ and try this for yourself in `print_multiple()`!

## Testing:
You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/1-printing
$ python3 exercises.py
```
Your output should look like this:
```
-==Printing 1==-
Hello world!


-==Printing 2==-
a) 579
b) 13594250
c) 2209375
d) 1256117610
e) 12345.0
f) 1041
g) It's the modulo operator!


-==Printing 3==-
Hi! My name is Totoro. I am 3 years old, and I go to school at Satsuki's School House. I often enjoy interacting with humans.
2 times 6 equals 12


-==Printing 4==-

              |\
              | \
              |  \
              |   )
              |  /  
             _|.'
           .' |
          /   |_.
         |  .'|  '.
          \ * |   /
           '._|_.'
              |
            * |
            '.'
        
-|My ASCII art|-
{your ascii art}
```
