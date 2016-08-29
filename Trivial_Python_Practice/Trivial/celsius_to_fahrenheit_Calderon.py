# Author: Nathan Calderon
# File Name: celsius_to_fahrenheit_Calderon.py

# This program converts a temperature entered in Celsius 
# to Fahrenheit.

# User enters a temperature in Celsius.
celsius_temp = float(input("Enter the temperature in \
Celsius and press enter: "))

# Celsius temperature converted to Fahrenheit calculation.
fahrenheit_temp = (9/5)*celsius_temp+32

# Display the results entered and calculated.
# Results displayed with one significant digits.
print("The Celsius temperature of", celsius_temp, "is", \
format(fahrenheit_temp, ",.1f"), "Fahrenheit")

input("Press enter to continue...")

# Imputs used: 21, 0, -12
# Outputs respectively: 69.8, 32, 10.4
