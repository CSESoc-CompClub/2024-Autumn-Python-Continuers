# This program is supposed to print the first 10 even numbers.
# Use ctrl + C to exit the infinite loop

# Function to print the first 10 even numbers
def print_even_numbers():
    count = 1
    even_numbers = []
    while len(even_numbers) < 10:
        if count % 2 == 0:
            even_numbers.append(count)
        count += 1  # This line should not be inside the if statement
    return even_numbers

# Main program
def main():
    # Call the function to print even numbers
    even_numbers = print_even_numbers()
    
    # Print the even numbers
    print("The first 10 even numbers are:", even_numbers)

# Call the main function to start the program
main()