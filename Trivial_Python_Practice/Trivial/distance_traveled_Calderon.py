# Author: Nathan Calderon
# File Name: distance_traveled_Calderon.py

# This program displays the distance a vehicle has traveled
# for each hour it has traveled.

# Global Constants
START = 1
INCREMENT = 1

# Define main function.
def main():
    # User enters data.
    speed_of_vehicle = int(input("Enter the speed of the vehicle in mph: "))
    hours_traveled = int(input("Enter the number of hours traveled: "))
    print()
    # Print table headings.
    print("Hour\tDistance Traveled")
    print("-----------------------")
    show_travel(speed_of_vehicle, hours_traveled)
    print()
    input("Press enter to continue.")

def show_travel(speed_of_vehicle, hours_traveled):
    for hours_traveled in range(START, hours_traveled +1, INCREMENT):
        distance_traveled = hours_traveled * speed_of_vehicle
        print(hours_traveled, "\t", format(distance_traveled, ",.2f"))

# Call main function.
main()


# Inputs:40, 3
# Outputs:
# Hour	Distance Traveled
# -----------------------
# 1  	  40.00
# 2  	  80.00
# 3  	  120.00

