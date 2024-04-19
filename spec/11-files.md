# 📕 File IO 🌟
The code for this exercise can be found in `exercises/11-files/`.

You can manually run your code by clicking the play button, or:
```
$ cd ~/Desktop/2024-autumn-python-intro/exercises/11-files
$ python3 {FILE_NAME}.py
```

## Task 11.1: Character Reader
**Task file:** `file_operations.py`
Jack, an anime enthusiast, wrote down all the characters from Spirited Away in a text file called 'spirited_away.txt' and decided to create a program that would help him quickly retrieve information about a character without needing to read through the whole file, and quickly add new characters to his text file. Within the text file, each line stores character details seperated by commas. Jack stores the name, age, species, hobby, and fun fact of each character.

Can you help him make this program by completing the following functions?

Hint: look at spirited_away.txt to see what the text file looks like
Hint 2: if you mess up the text file, there is a 'spirited_awayFRESHCOPY.txt' for you to copy and paste

### Part 1: Add Character
Function add_character(): Add a character to the text file!

**Expected output:**
```
$ python3 file_operations.py

=== Spirited Away Archive ===
What action do you want to carry out? (add | get)
add
== Adding Character ==
Name: Bob
Age: 57
Species: human
Hobby: drinking red wine
Fun fact: has a long beard
Character has been added to file!
```

### Part 2: Get Character
Function get_character(): Given the name of character, return the line containing its character details if found.
If there is no such character, return 'Character not found!'

Optional task: Sometimes we forget to capitalise a name wrong, can you make this function work when there are no capitals, or when the capitals are in the wrong place? For example, when name = 'chihiro', or name = 'chiHiRo'? 

```
$ python3 file_operations.py

=== Spirited Away Archive ===
What action do you want to carry out? (add | get | read)
get
== Retrieving Character ==
What is the character's name? Chihiro
== Character Details ==
Name: Chihiro
Age: 10
Species: human
Hobby: swimming
Fun fact: spirits like her very much

=== Spirited Away Archive ===
What action do you want to carry out? (add | get | read)
get
== Retrieving Character ==
What is the character's name? jack
Character not found!
```