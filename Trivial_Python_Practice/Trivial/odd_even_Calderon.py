# Author: Nathan Calderon
# File Name: odd_even_Calderon.py

# This program will generate 1000 random numbers and keep count of how
# many numbers are even and how many are odd.

# Import random module.
import random

# Define main function.
def main():
    # Initialize an accumulator variable.
    total_even = 0
    total_odd = 0
    # Intro
    print("This will generate 1000 random numbers and keep count of\
 how many numbers are even and how many are odd.")
    print()
    # Create a variable to control the loop.
    again = "y"
    # Start loop.
    while again == "y" or again == "Y":
        for count in range(100):
            number = random.randrange(100)
            # Call is_even number function.
            is_even(number)
            print()
            again = input("Would you like to start the program again? \
 (y = 'yes'): ")
            input("Press enter to continue...")

def is_even(number):
    print(number)
    if (number % 2) == 0:
        total_even += number
        print("The number of even numbers out of a random 100 numbers\
is: ", total_even)
    else:
        total_odd =+number
        print("The number of odd numbers out of a random 100 numbers\
is: ", total_odd)

# Call the main function.
main()


        
        
        
