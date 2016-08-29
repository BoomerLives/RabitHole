# Author: Nathan Calderon
# File Name: read_random_Calderon.py

# This program will read a set of random numbers from a file. The program
# will then display the numbers, the total of the numbers, and the
# number of random numbers read from said file.

# Define main function.
def main():
    # Open the random.txt file.
    random_file = open("random.txt", "r")
    # Initialize an accumulator to 0.
    total = 0
    # Initialize a variable to keep count of random numbers.
    count = 0
    print("Here is the data for the random numbers from the random.txt\
file:")
    # Get the numbers from the file and total them.
    for line in random_file:
        # Convert line to float.
        random_number = float(line)
        # Add 1 to the count variable for each line.
        count += 1
        # Display the number.
        print("Random Number #", count, ": ", random_number, sep="")
        # Add the random number to total.
        total += random_number
    # Close the file.
    random_file.close()
    print()
    # Display the total of the random numbers.
    print("The total of the random numbers is", total)
    print()
    input("Press enter to continue...")

# Call main function.
main()
