# Author: Nathan Calderon
# File Name: paint_job_estimator_Calderon.py

# This program is a paint job estimator.
# This program asks the user to enter the square feet of wall space
# to be painted and the price of the paint per gallon.
# After calculating the data entered, a job estimate is displayed.

# Create a global constant.
SQUARE_FEET = 0
PRICE_PER_GALLON = 0

# Define the main function.
def main():
    # Display the intro screen.
    intro()
    # The user enters the square feet of wall space to be painted and
    # the price of paint per gallon.

    #Global Constants.
    global SQUARE_FEET
    SQUARE_FEET = float(input("Enter the square feet of wall space to be painted: "))

    global PRICE_PER_GALLON

    PRICE_PER_GALLON = float(input("Enter the price per gallon of paint: $"))
    print()
    # show_cost_estimate function.
    show_cost_estimate(SQUARE_FEET, PRICE_PER_GALLON)

    print()
    input("Press enter to continue:")

# The intro function displays an introductory screen.
def intro():
    print("This program calculates data pertaining to a paint job estimate.")
    print()
    print("The following estamates will be displayed:")
    print("1. The number of gallons of paint required.")
    print("2. The hours of labor required.")
    print("3. The cost of the paint.")
    print("4. The labor charges.")
    print("5. The total cost of the paint job.")
    print()
    print("Enter the following and press enter:")

# Define show_cost_estimate function.
def show_cost_estimate(sqfeet, pricepergallon):
    number_of_gallons = sqfeet/115
    hours_of_labor = (sqfeet/115)*8
    cost_of_paint = number_of_gallons * pricepergallon
    labor_charges = hours_of_labor * 20.00
    total_cost = cost_of_paint + labor_charges
# Display the number of gallons required, two signidicant digits.
    print("The number of gallons of paint required is:",\
          format(number_of_gallons, ",.2f"))
# Display the hours of labor required, two significant digits.
    print("The hours of labor required is:",\
          format(hours_of_labor, ",.2f"), "hr(s)")
# Display the cost of paint, two dignificant digits.                                
    print("The cost of the paint is: $",  format(cost_of_paint, ",.2f"))
# Display the labor charges, two significant digits.
    print("The labor charges are:", "$", format(labor_charges, ",.2f"))
# Display the total cost of the paint job, two significant digits.
    print("The total cost of the paint job is: $", \
          format(total_cost, ",.2f"))        

# Call main function    
main()

# Input 1: 230, 5.65 
# Input 2: 172.5, 9.36
# Input 3: 86.25, 3.26

# Output 1:
# The number of gallons of paint required is: 2.00
# The hours of labor required is: 16.00 hr(s)
# The cost of the paint is: $ 11.30
# The labor charges are: $ 320.00
# The total cost of the paint job is: $ 331.30

# Output 2:
# The number of gallons of paint required is: 1.50
# The hours of labor required is: 12.00 hr(s)
# The cost of the paint is: $ 14.04
# The labor charges are: $ 240.00
# The total cost of the paint job is: $ 254.04

# Output 3:
# The number of gallons of paint required is: 0.75
# The hours of labor required is: 6.00 hr(s)
# The cost of the paint is: $ 2.44
# The labor charges are: $ 120.00
# The total cost of the paint job is: $ 122.44





