# Author: Nathan Calderon
# File Name: number_analysis_Calderon.py

# This program asks a user to enter a series of 20 numbers.
# The program then stores the series of numbers in a list and displays
# the lowest and highest numbers. The program will also total the
# numbers as well show the average the numbers.

# Constant used for the size of the list.
USER_NUMBERS = 20

# Define Main function
def main():
    # Call get_values function.
    number_list = get_values()
    print()
    # Call do_analysis function.
    do_analysis(number_list)

# Define get_values function.
def get_values():
    numbers = [0] * USER_NUMBERS
    index = 0
    print("Enter twenty numbers.")
    print()
    for index in range(USER_NUMBERS):
        print("Value# ", index + 1, ": ", sep="", end="")
        numbers[index] = float(input())
        index += 1
    return numbers

# Define do_analysis function.
def do_analysis(number_list):
    total = 0.0
    for value in number_list:
        total += value
    average = total / len(number_list)
    print("The lowest value is", min(number_list))
    print("The highest value is", max(number_list))
    print("The total value of the numbers is: ", total)
    print("The average value of the numbers is: ", average)
    print()
    input('press enter to continue')

main()


    
