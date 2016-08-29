# Author: Nathan Calderon
# File Name: bmi_Calderon.py

# This program allows a user to enter weight and height data,
# which is then calculated to give the user's Body Mass Index, BMI.

# Create global constants.
WEIGHT = 0
HEIGHT = 0

# Define the main function.
def main():
    # Display the intro screen.
    intro()
    # User enters the weight and height data.

    # Global Constants.
    global WEIGHT
    WEIGHT = float(input("Enter a value of weight in pounds: "))

    global HEIGHT
    HEIGHT = float(input("Enter a value of height in inches: "))
    # BMI calculation. 
    show_bmi(WEIGHT, HEIGHT)
    input("Press enter to continue")

# The intro function displays an introductory screen.
def intro():
    print("This program calculates a user's Body Mass Index know as BMI.")
    print()
    print("For your reference, the equation used is: ")
    print("\tBMI = Weight X 703 / Height^2")
    print()
    print("Where weight is measured in pounds and height is measured in inches.")
    print()

# The show_bmi function calculates the BMI for the weight and height
# data entered by the user in bounds and inches respectively.
# The calculated data is presented with two significant digits.
def show_bmi(weight, height):
    BMI = weight*(703/height**2)
    print()
    print("The BMI for the given data entered is: ", \
          format(BMI, ",.2f"))

# Call main function.
main()

# Inputs:
# 180lbs, 71in
# 225lbs, 45in
# 90lbs, 80in

# Outputs:
# 25.1
# 8.11
# 9.89 respectively.
