# Author: Nathan Calderon
# File Name: magic_dates_Calderon.py

# This program determines if the data entered by a user is a magic date.
# The user enters the numerical values for a given day, month, and two
# digit year, the program determines if the day times the month equals
# the year.

# Define main function.
def main():
    # Call intro function.
    intro()
    print()
    # User enters date data.

    # Globale Constants
    global D
    D = int(input("Enter any numerical day between 1 and 31: "))

    global M
    M = int(input("Enter any numerical month between 1 and 12: "))

    global Y
    Y = int(input("Enter any two digit year between 00 and 99: "))
    print()

    # Call show_magic_dates function.
    check_magic(D, M, Y)

    print()
    input("Press enter to continue.")

# Define intro function.
def intro():
    print("Determine if a given date is a magic date!")

# Define show_magic_dates funciont.
def check_magic(D, M, Y):
    y = D*M
    if y==Y:
        print("The date of:",D,"/",M, "/",Y, "is magic!")
    else:
        print("The date of:",D,"/",M, "/",Y, "is not magic.")


# Call main function.
main()
          
# Inputs:
# 1. 06, 10 ,60
# 2. 02, 09, 32

# Outputs:
# 1.The date of: 6 / 10 / 60 is magic!
# 2.The date of: 2 / 9 / 32 is not magic.













          
