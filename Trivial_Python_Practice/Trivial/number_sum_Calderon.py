# Author: Nathan Calderon
# File Name: numbers_sum_Calderon.py

# This program displays a series of positive numbers and
# their sum.

# Define main function.
def main():
    # Initialize an accumulator varaiable.
    total = 0.0
    # Explanation of program.
    print("This program calculates the sum of positive numbers you enter.")
    print()
    # User enters a series of positive numbers.
    print("Enter a positve number to continue or a negative number to quit.")
    x = float(input("Enter a number: "))
    # Continue the processing as long as the user does not enter a
    # negative number. 
    while x >= 0:
        total = total + x
        x = float(input("Enter a number: "))
    # Display sum of series.
    print()
    print("The sum of the positive numbers entered is:", format(total, ",.2f"))
    input("Press enter to continue.")
    
# Call main function.
main()

# Inputs:12.23, 26.5, 5, -1
# Outputs: 43.73
