# Author: Nathan Calderon
# File Name: primary_colors.py

# This program askes a user to enter one of thee primary colors to mix
# together. If the user enters anything other the three primary color,
# an error message is displayed. If primary color's are chosen correctly
# the program will diplay the secondary color that result between their
# mixing.

#Global Constants
global constant
R='Red'
global constant
B='Blue'
global constant
Y='Yellow'
global constant
P='Purple'
global constant
O='Orange'
global constant
G='Green'

# Define main function.
def main():
    # Call intro() function.
    intro()
    print()
    # User entered data.
    color_1 = str(input("Enter the first primary color to mix: "))
    color_2 = str(input("Enter the second primary color to mix:"))
    # Call chose_primary_color() function.
    chose_primary_color(color_1, color_2)
    print()
    # Call primary_color_mix() function.
    primary_color_mix(color_1, color_2)
    input("Press enter to continue.")

# Define intro() function.
def intro():
    print("This program allows a user to enter two of the three primary\
 colors and displays the secondary color produced from the mixing of\
 the chosen primary colors.")
   

# Define chose_primary_color(color_1, color_2)
def chose_primary_color(color_1, color_2):
    if color_1 == R or B or Y:
        print("The first color chosen is", color_1)
    else:
        print("The first color chosen is not one of the primary colors.")
    if color_2 == R or B or Y:
                print("The second color chosen is", color_2)
    else:
        print("The second color chosen is not one of the primary colors.")
# Define primary_color_mix
def primary_color_mix(color_1, color_2):
    if color_1==R and color_2==B:
        print("The resulting secondary color between",color_1,"and",color_2,"is",P)
    elif color_1==R and color_2==Y:
            print("The resulting secondary color between",color_1,"and",color_2,"is",O)
    elif color_1==B and color_2==Y:
                print("The resulting secondary color between",color_1,"and",color_2,"is",G)
    else:
        print("The colors chosen are not primary colors.")
        
# Call main function.
main()








