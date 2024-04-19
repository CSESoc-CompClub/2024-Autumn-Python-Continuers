'''
[Ghibli adventure]
Write a program that selects which  Ghibli movie character they'd like to 
accompany on an adventure, and based on their choice.

Your output should look something like this:

Choose a character for your adventure:
Totoro from My Neighbor Totoro
Chihiro from Spirited Away
Howl from Howl's Moving Castle


Enter the number of your chosen character: 1
"You chose Totoro!”

How would we handle cases where the number inputted is not within 1-3?
'''

characters = '''
Choose a character for your adventure:
    
[1] Totoro from My Neighbor Totoro
[2] Chihiro from Spirited Away
[3] Howl from Howl's Moving Castle
'''
#####################################################################

def main():
    print(characters)

    choice = int(input("Enter the number of your chosen character: "))

    if choice == 1:
        print('You chose Totoro!')
    elif choice == 2:
        print('You chose Chihiro!')
    elif choice == 3:
        print('You chose Howl!')
    else:
        print('Invalid choice. Please select a number from 1 to 3')

#####################################################################
main()