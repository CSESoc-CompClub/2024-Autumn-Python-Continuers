# [Ghibli adventure]
# Write a program that selects which  Ghibli movie character they'd like to 
# accompany on an adventure, and based on their choice.
# How would we handle cases where the number inputted is not within 1-3?

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

    # CHANGE THE CODE BELOW
    if choice == 13:
        print("You chose ...poco?")

#####################################################################
main()