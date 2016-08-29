# Author: Nathan Calderon
# File Name: triangle_Calderon.py

# This program produces a pattern using nested loops.

# Define main function.
def main():
    # First loop.
    for r in range(7):
        # Second loop.
        for c in range(7 - r):
            print("*", end="")
        print()
    print()
    input("Press enter to continue...")

# Call main function.
main()

