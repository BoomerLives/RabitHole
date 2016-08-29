# Author: Nathan Calderon
# File Name: increase_amt_Calderon.py

# This program adds a user defined whole number to a defined set of numbers
# main function

def main():
    values = [[10,0], [13, 0], [36, 0], [74,0], [22,0]]

    index = 0    
    user_number = int(input("Enter an amount: "))
    print()
    for i in values:
        value = values[index]
        number = int(value[0])
        new_value = number + user_number
        print(number, new_value)
        print()
        index += 1
        
    input('press enter to continue')


# Call the main function
main()

# Inputs: 2 and 5

# Outputs:
#   10 12 and 10 15
#   13 15 and 13 18
#   36 38 and 36 41
#   74 76 and 74 79
#   22 24 and 22 27
