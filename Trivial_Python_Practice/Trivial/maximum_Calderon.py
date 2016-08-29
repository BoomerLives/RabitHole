# Author: Nathan Calderon
# File Name: maximum_Calderon.py

# This program determines and displays the greater of two integers
# given by a user.

# Define main function.
def main():
    # Create variable to control loop.
    again = "y"
    # Start loop.
    while again == "Y" or again == "y":
        # The user enters the two integers of choice.
        num1 = int(input("Enter the first integer: "))
        print()
        num2 = int(input("Enter the second integer: "))
        print()
        # Get the greater of the two integers.
        greater_integer = maximum(num1, num2)
        # Display the greater of the two integers
        print("The greater integer is: ", greater_integer)
        print()
        again = input("Would you like to enter more integers? \
(y = 'yes'): ")
        
        input("Press enter to continue...")

# Define maximum function.
def maximum(num1, num2):
    if num1 > num2:
        x = num1
        return x
    else:
        x = num2
        return x
    
# Call main function.
main()

# Inputs:
# Outputs:
