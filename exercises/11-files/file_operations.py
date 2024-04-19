# Exercise 1: Character Reader 

# Jack, an anime enthusiast, wrote down all the characters from Spirited Away in a text file called 'spirited_away.txt' and decided to create a program 
# that would help him quickly retrieve information about a character without needing to read through the whole file, and quickly add new
# characters to his text file. Within the text file, each line stores character details seperated by commas. Jack stores the name,
# age, species, hobby, and fun fact of each character.

# Can you help him make this program by completing the following functions?

# Hint: look at spirited_away.txt to see what the text file looks like
# Hint 2: if you mess up the text file, there is a 'spirited_awayFRESHCOPY.txt' for you to copy and paste


"""
Function add_character(): Add a character to the text file!
"""
def add_character(): 
  # TODO: IMPLEMENT THIS FUNCTION
  pass


"""
Function get_character(): Given the name of character, return the line containing its character details if found.
If there is no such character, return 'Character not found!'

Optional task: Sometimes we forget to capitalise a name wrong, can you make this function work when there are no capitals, 
or when the capitals are in the wrong place? For example, when name = 'chihiro', or name = 'chiHiRo'? 
"""
def get_character(name):
  # TODO: IMPLEMENT THIS FUNCTION
  pass


# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
  print('=== Spirited Away Archive ===')

  func = None
  while func == None:
    input_val = input('What action do you want to carry out? (add | get | read)\n')
    if input_val == 'add':
      func = input_val
      print('== Adding Character ==')
      add_character()
      print("Character has been added to file!")
    elif input_val == 'get':
      func = input_val
      print('== Retrieving Character ==')
      name = input('What is the character\'s name? ')
      result = get_character(name)
      if result == 'Character not found!':
        print('Character not found!')
      else:
        data = result.strip('\n').split(',')
        print('== Character Details ==')
        print('Name:', data[0])
        print('Age:', data[1])
        print('Species:', data[2])
        print('Hobby:', data[3])
        print('Fun fact:', data[4])
    elif input_val == 'read':
      f = open('spirited_away.txt', 'r')
      print(f.read() + '\n')
      f.close()
    else:
      print('== Valid Commands ==')
      print('add: adds a character to file')
      print('get: gets character details from file')
      print('read: reads file data\n')