# Author: Nathan Calderon
# File Name: test_average_Calderon.py

# This program determines the letter grades of five test scores and
# produces the average test score.

# Define main function.
def main():
    # Create a variable to control the loop.
    again = "y"
    # Define loop.
    while again == "y" or again == "Y":
        # Display intro.
        print("This program will assign a letter grade to each of five\
 test scores entered by a user and then given an average test score.")
        print("Enter the five test scores below: ")
        # User entered data.
        print()
        # Test Score 1
        grade = int(input("Enter the first test score: "))
        t_score1 = determine_grade(grade)
        grade1 = grade
        # Test Score 2
        grade = int(input("Enter the second test score: ")) 
        t_score2 = determine_grade(grade)
        grade2 = grade
        # Test Score 3
        grade = int(input("Enter the third test score: ")) 
        t_score3 = determine_grade(grade)
        grade3 = grade
        # Test Score 4
        grade = int(input("Enter the fourth test score: "))
        t_score4 = determine_grade(grade)
        grade4 = grade
        # Test Score 5
        grade = int(input("Enter the fifth test score: "))
        t_score5 = determine_grade(grade)
        grade5 = grade
        # Average Test Score function.
        avg = calc_average(grade1, grade2, grade3, grade4, grade5)
        ave_letter_grade = determine_grade(avg)
        # Display results.
        print()
        print("The first test score of", grade1, "has a letter grade \
of", t_score1)
        print("The second test score of", grade2, "has a letter grade \
of", t_score2)
        print("The third test score of", grade3, "has a letter grade \
of", t_score3)
        print("The fourth test score of", grade4, "has a letter grade \
of", t_score4)
        print("The fifth test score of", grade5, "has a letter grade \
of", t_score5)
        print()
        print("The average test score of", avg, "has a letter grade \
of", ave_letter_grade)
        print()
        # End loop.
        again = input("Would you like to enter more test scores? \
 (y = 'yes'): ")
        print()

# Define determine_grade function.
def determine_grade(grade):
    if grade >= 90:
        grade = "A"
    elif grade >= 80 and grade < 90:
        grade = "B"
    elif grade >= 70 and grade < 80:
        grade = "C"
    elif grade >= 60 and grade < 70:
        grade = "D"
    else:
        grade = "F"
    return grade

# Define calc_average.
def calc_average(grade1, grade2, grade3, grade4, grade5):
    x = (grade1 + grade2 + grade3 + grade4 + grade5)/5
    return x

# Call main function.
main()
                        
#Inputs:90, 80, 70, 60, 50
#Outputs: A, B, C, D, F, 70, C
        
        
        
