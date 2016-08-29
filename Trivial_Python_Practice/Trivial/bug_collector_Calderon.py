# Author: Nathan Calderon
# File Name: bug_collector_Calderon.py

# This program keeps a running tally of bugs collected
# through the course of seven days.

# Constant for the maximum number of days of collection.
MAX = 7

# Define main function.
def main():
    # Initialize an accumulator variable.
    total = 0.0
    # Introduction statement.
    print("This program keeps a running tally of bugs collected during\
 seven days.")
    print("Please enter the daily tally below.")
    print()
    # User entered data enters a For Loop.
    for tally in range(MAX):
        number = int(input("Enter the number of bugs collected for the\
 day: "))
        total += number
        print()
        print("The bugs collected for the day is:", number)
        print()
    # The total data is displayed.
    print("The total bugs collected over the course of seven days is\
:",total)
    print()
    input("Press enter to continue.")   

# Call main function.
main()

# Inputs:1, 2, 3, 4, 5, 6, 7
# Outputs: 28






    
