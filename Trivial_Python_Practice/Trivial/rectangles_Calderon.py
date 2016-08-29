# Author: Nathan Calderon
# File Name: rectangles_Calderon.py

# This program gets the width and length for two rectangles from
# the user and determines which rectangle's area is larger or if
# they're the same.

# Main funcion.
def main():
    # User enters width and length for two rectangles.
    rec1_width=float(input("Enter the width for the first \
rectangle: "))
    rec1_length=float(input("Enter the length for the first \
rectangle: "))
    print()
    rec2_width=float(input("Enter the width for the second \
rectangle: "))
    rec2_length=float(input("Enter the length for the second \
rectangle: "))
    print()
    # Call function
    compare_rectangles(rec1_width, rec1_length, rec2_width,\
                        rec2_length)

    input("Press enter to continue.")

def compare_rectangles(rec1_width, rec1_length, rec2_width,\
                        rec2_length):
    # Caclculate the area for rectangle 1 and 2.
    rec1_area = rec1_width * rec1_length
    rec2_area = rec2_width * rec2_length

    if rec1_area > rec2_area:
        print("Rectangle 1's area is larger than Rectangle 2's area.")
        print(format(rec1_area, ",.2f"), ">", format(rec2_area, ",.2f"))
    else:
        if rec2_area > rec1_area:
            print("Rectangle 2's area is larger than Rectangle \
1's area.")
            print(format(rec2_area, ",.2f"), ">",\
                  format(rec1_area, ",.2f"))
        else:
            if rec1_area == rec2_area:
                print("Rectangle 1's area is equal to Rectangle \
2's area.")
                print(format(rec1_area, ",.2f"), "=", \
                      format(rec2_area, ",.2f"))
                
# Call main function.
main()

# Inputs:
# 1.[75,56;23,98]
# 2.[65,85;85,65] 


# Outputs:
# 1. Rectangle 1's area is larger than Rectangle 2's area.
# 4200.0 > 2254.0

# 2. Rectangle 1's area is equal to Rectangle 2's area.
# 5525.0 = 5525.0        






       
