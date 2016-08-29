# Author: Nathan Calderon
# File Name: mass_weight_Calderon.py

# This program asks the user to enter an objects mass in kilograms, and
# then calculates its weight in newtons. If the objects is more than
# 1,000 newtons the program displays a message indicating it is too
# heavy. If the object is less then 10 newtons the program displays a
# message indicating it is too light.

# Global Constants
global x
x = 10
global y
y = 1000

# Main Function.
def main():
    # User enters an objects mass in kilograms.
    object_mass = float(input("Enter an object's mass in kilograms: "))
    print()
    # Call show_mass_weight Function.
    eval_weight(object_mass)
    print()
    input("Press enter to continue.")

def eval_weight(object_mass):
    # Calculate the object's weight.
    # Results diplayed with two significant digits.
    object_weight = object_mass * 9.8

    if object_weight > y:
        print("The object's weight in newtons is:", \
              format(object_weight, ",.2f"))
        print("The object is too heavy.")
    else:
        if object_weight < x:
            print("The object's weight in newtons:",\
                  format(object_weight, ",.2f"))
            print("The object is too light.")
        else:
            if object_weight > x and object_weight < y:
                print("The object's weight in newtons is:",\
                      format(object_weight, ",.2f"))
            
# Call main function
main()

# Inputs:
#1. 2.3
#2. 0.2
#3. 105

#Outputs: 
#1. 22.54 
#2. 1.96 - Object is too light.
#3. 1,029.00 - Object is too heavy.

        
            

        
    
        






        
    
