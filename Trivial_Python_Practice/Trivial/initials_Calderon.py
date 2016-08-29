# Author: Nathan Calderon
# File Name: initials_Calderon.py

# This program asks a user's first, middle, and last name. The program
# then displays their first, middle, and last initials.

# Define main function.
def main():
    # User enters full name.
    full_n = input("Enter your full name: ")
    # List is split into indices.
    full_list = full_n.split()
    # Combining and uppercasing the initials.
    initials = (full_list[0].upper()[0] + ".") + (full_list[1].upper()[0] + ".") + (full_list[2].upper()[0] + ".")
    print()
    # Displaying the output.
    print("Your initials are:", initials)
    print()
    print("Press enter to continue...")

main()


# Inputs: Nathan Reuben Calderon and John William Smith.
# Outputs: N.R.C and J.W.S.
