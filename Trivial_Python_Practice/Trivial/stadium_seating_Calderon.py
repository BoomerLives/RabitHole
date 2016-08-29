# Author: Nathan Calderon
# File Name: stadium_seating_Calderon.py

# This program asks how many tickets for each class of seats
# were sold and displays the amount of income generated from
# the ticket sales.

# Create global constants.
CLASS_A = 0
CLASS_B = 0
CLASS_C = 0

# Define the main function.
def main():
    # Display the intro screen.
    intro()
    # User enters the number of each class tickets sold.

    # Global Constants
    global CLASS_A
    CLASS_A = int(input("Enter the number of class A tickets sold: "))

    global CLASS_B
    CLASS_B = int(input("Enter the number of class B tickets sold: "))

    global CLASS_C
    CLASS_C = int(input("Enter the number of class C tickets sold: "))
    print()
    # show_income function
    show_income(CLASS_A, CLASS_B, CLASS_C)

    print()
    input("Press enter to continue")

# The intro function displays an introductory screen.
def intro():
    print("This program calculates the amount of income generated")
    print("from the total sales of Class A, Class B, and Class C")
    print("tickets entered by a user.")
    print()

# Define income_generated function.
def show_income(A, B, C):
    income = (A*15.00) + (B*12.00) + (C*9.00)
    print("The amount of income generated from total ticket sales is: ")
    print("$", format(income, ",.2f"))

# Call main function.
main()

# Inputs:
# 1. 5, 3, 456
# 2. 654, 5, 150
# 3. 15, 26, 3

# Outputs:
# 1. $4,215.00
# 2. $11,220.00
# 3. 564.00
   
                
