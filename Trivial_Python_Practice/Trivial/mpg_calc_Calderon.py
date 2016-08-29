# Author: Nathan Calderon
# File Name: mpg_calc.py

# This program calculates MPG for a given number of miles driven 
# and gallons of gas used.

# User enters consumption data.
miles_driven = float(input("Enter how many miles that\
have been driven and press enter: "))
gallons_of_gas = float(input("Enter how many gallons of\
gas that have been used and press enter: "))

# MPG calculation.
mpg = miles_driven / gallons_of_gas

# Display the results.
# Results displayed with two significant digits.
print("The miles per gallon for the data entered is: ", \
      format(mpg, ",.2f"))

input("Press enter to continue")
    
# Notes:
# Negative numbers can be entered and calculated but render the results 
# to be invaled for MPG values.

# Imputs used: Mile_driven:5, 0.5, -1; Gallons_of_gas: 3, 20, 4.
# Outputs respectively: 1.67, 0.03, -0.25.
