# Author: Nathan Calderon
# File Name: grade_exam_Calderon.py

# This program compares two parallel lists to grade
# a multiple choice exam. One list has the exam solution
# and the second list has a student's answers.
#
# The question number of each missed question is stored
# in a third list.

# main function
def main():
   
    # do not modify this statement or contents of list
    exam_solution = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C',\
               'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

    # do not modify this statement or contents of list
    student_answers = ['B', 'D', 'B', 'A', 'C', 'A', 'A', 'A', 'C', 'D', 'B', 'C',\
               'D', 'B', 'D', 'C', 'C', 'B', 'D', 'A']
    
    # do not modify this statement, you must begin with an empty list
    questions_missed = []

    # Accumulators
    index = 0
    correct = 0

    # for loop using zip
    for exam_letter, student_letter in zip(exam_solution, student_answers):
        exam_key = exam_letter.split()
        stud_answers = student_letter.split()
        if exam_key != stud_answers:
            questions_missed.append(index + 1)
            index += 1
        else:
            correct += 1
            index += 1
    grade = (correct / 20) * 100
    print("The number of correctly answered questions: ", correct)
    print("The number of incorrectly answered questions: ", 20 - correct)
    print("Your grade is: ", grade)
    if grade <= 74:
        print("You did not pass.")
    else:
        print("You passed!")
    print()
    print("You missed questions:")
    for q in questions_missed:
        print("#", q)
    print()
    input('press enter to continue')    # required at end of main function


# Call the main function
main()

