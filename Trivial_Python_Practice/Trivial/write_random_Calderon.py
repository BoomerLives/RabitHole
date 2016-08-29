# Author: Nathan Calderon
# File Name: write_random_Calderon.py

# This program will write a series of 100 random numbers in the range
# of 1 through 100 to a file. The user will specify how many random
# numbers the file will hold.

# Import random module.
import random

# Define main function.
def main():
    # Open the file to hold the random numbers.
    ran_number_file = open("random.txt", "w")
    
    # User inputs how many random numbers the file will hold.
    num_hold = int(input("How many random numbers do you want the file \
to hold? "))
    # Write the random numbers to file.
    for count in range(num_hold):
        ran_number = random.randrange(101)
        ran_number_file.write(str(ran_number) + "\n")

    # Close the file.
    ran_number_file.close()
    print("The random numbers have been saved to random.txt")

# Call main function.
main()
        
# Input: 25
